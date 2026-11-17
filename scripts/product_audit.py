#!/usr/bin/env python3
"""Scan a client-facing frontend project for product design signals and AI-slop risks."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any

EXCLUDE_DIRS = {
    ".git", ".next", ".nuxt", ".output", ".svelte-kit",
    "build", "coverage", "dist", "node_modules", "out", "target",
}

UI_EXTENSIONS = {
    ".astro", ".css", ".html", ".js", ".jsx", ".mdx",
    ".scss", ".svelte", ".ts", ".tsx", ".vue",
}

STACK_DEPS = {
    "next": "Next.js",
    "vite": "Vite",
    "react": "React",
    "tailwindcss": "Tailwind CSS",
    "@tailwindcss/postcss": "Tailwind CSS v4",
    "@radix-ui/react-dialog": "Radix UI",
    "class-variance-authority": "CVA",
    "lucide-react": "lucide-react",
    "@phosphor-icons/react": "Phosphor Icons",
    "@heroicons/react": "Heroicons",
    "react-hook-form": "React Hook Form",
    "zod": "Zod",
    "framer-motion": "Framer Motion",
    "motion": "Motion",
    "canvas-confetti": "canvas-confetti",
    "sonner": "sonner",
    "next-auth": "NextAuth",
    "@auth/core": "Auth.js",
    "stripe": "Stripe",
    "@stripe/stripe-js": "Stripe.js",
    "recharts": "Recharts",
    "cmdk": "cmdk",
    "resend": "Resend",
    "simple-icons": "simple-icons",
}

# Signals that indicate client-facing product work.
#
# These are deliberately anchored with \b. An unanchored alternation like
# ``star|review`` matches "Get started" and "preview", which floods the trust
# signal list with every marketing file in the repo. Keep every term a word.
SIGNAL_PATTERNS = {
    "background_images": re.compile(
        r'background-image|bg-\[url\(|<Image[^>]+fill|object-cover|object-contain',
        re.IGNORECASE,
    ),
    "image_overlays": re.compile(
        r'bg-black/|bg-white/|from-black|to-black|from-white|to-white',
    ),
    "trust_signals": re.compile(
        r'\btestimonials?\b|\btestified\b|\breviews?\b|\bratings?\b|\bstars?\b|\bstarred\b'
        r'|\blogos?\b|\bsecurity\b|\bencrypt(?:ed|ion)?\b|\bsoc\s?2\b|\bgdpr\b'
        r'|\bbadges?\b|\bguarantees?\b|\bmoney.?back\b',
        re.IGNORECASE,
    ),
    "onboarding": re.compile(
        r'\bonboard(?:ing)?\b|\bwizards?\b|\bgetting.?started\b|\bsetup.?wizard\b'
        r'|\bStepIndicator\b|\bStepper\b|\bcurrentStep\b|\bstep\s*\d+\s*(?:of|/)\s*\d+'
        r'|\bwelcome.?screen\b',
        re.IGNORECASE,
    ),
    # Bare ``plan`` is a variable name far more often than a pricing surface
    # (``const plan = 'free'``), so it only counts next to a pricing verb.
    "pricing": re.compile(
        r'\bpricing\b|\btiers?\b|\bsubscriptions?\b|\bbilling\b|\bcheckout\b'
        r'|\bstripe\b|\bpayment.?intent\b|\bper.?month\b|\bmonthly.?plan\b'
        r'|\b(?:choose|select|pick|your|current)\s+plan\b|\bplans?\s*(?:page|card|tier|grid)\b',
        re.IGNORECASE,
    ),
    "auth": re.compile(
        r'\bsign.?in\b|\bsign.?up\b|\blog.?in\b|\blog.?out\b|\bsignOut\b'
        r'|\bforgot.?password\b|\breset.?password\b|\bauth(?:entication)?\b',
        re.IGNORECASE,
    ),
    "cta_patterns": re.compile(
        r'\bget.?started\b|\bstart.?free\b|\btry.?free\b|\bbook.?demo\b|\bfree.?trial\b',
        re.IGNORECASE,
    ),
    "forms": re.compile(
        r'useForm|FormField|FormLabel|FormMessage|handleSubmit|zodResolver',
    ),
    "empty_states": re.compile(
        r'empty.?state|\bno results\b|\bno data\b|\bnothing here\b|\bcreate (?:your )?first\b',
        re.IGNORECASE,
    ),
    "loading_states": re.compile(
        r'\bskeleton\b|\banimate-pulse\b|\bisLoading\b|\bisFetching\b',
    ),
    "success_states": re.compile(
        r'\bconfetti\b|\bcelebration\b|\bcongratulations\b|\bwell done\b'
        r'|\bCheckCircle\b|\bsuccess(?:Page|Screen|State)\b',
        re.IGNORECASE,
    ),
    "illustrations": re.compile(
        r'\bundraw\b|\bstoryset\b|\bhumaaans\b|\billustration',
        re.IGNORECASE,
    ),
    "mobile_patterns": re.compile(
        r'bottom-nav|tab.?bar|bottom.?sheet|safe.?area',
        re.IGNORECASE,
    ),
    "accessibility": re.compile(
        r'aria-|focus-visible|prefers-reduced-motion|sr-only',
        re.IGNORECASE,
    ),
}

# AI-slop risk patterns — things that make client apps look generic and AI-generated.
#
# The violet/indigo/purple family is the default "AI product" palette. `violet`
# is Tailwind's actual purple and is the one most often generated, so it must be
# in the alternation alongside purple/indigo.
AI_SLOP_PATTERNS = {
    "sparkle_magic_icons": re.compile(
        r'\bSparkles?\b|\bSparkleIcon\b|\bWandIcon\b|\bMagicWand\b|\bwand-2\b|\bsparkle',
        re.IGNORECASE,
    ),
    "generic_copy": re.compile(
        r'\bseamless(?:ly)?\b|\bpowerful solution\b|\bnext.?generation\b|\bAI-powered\b'
        r'|\bgame.?changer\b|\brevolutionary\b|\bcutting.?edge\b|\bsupercharge\b'
        r'|\bunleash\b|\belevate your\b|\bin today\'s fast.?paced world\b',
        re.IGNORECASE,
    ),
    "purple_indigo_as_primary": re.compile(
        r'\b(?:bg|text|from|to|via|border|ring|fill|stroke)-(?:violet|purple|indigo|fuchsia)-'
        r'(?:300|400|500|600|700|800|900|950)\b',
    ),
    "glassmorphism": re.compile(
        r'\bbackdrop-blur-(?:md|lg|xl|2xl|3xl)\b',
    ),
    "excessive_radius": re.compile(
        r'\brounded-(?:3xl|4xl|\[[2-9](?:\.\d+)?rem\]|\[[4-9]\dpx\])\b',
    ),
    "orbs_blobs": re.compile(
        r'\borb\b|\bblob\b|\bbokeh\b|\bblur-3xl\b|\bconic-gradient\b',
        re.IGNORECASE,
    ),
    "lorem_ipsum": re.compile(
        r'lorem ipsum|dolor sit amet',
        re.IGNORECASE,
    ),
    # Case-insensitive: "Learn more" and "Get started" are written in sentence
    # case far more often than title case.
    "placeholder_cta_copy": re.compile(
        r'["\'`>]\s*(?:get started|learn more|click here|read more)\s*[<"\'`]',
        re.IGNORECASE,
    ),
    "fake_round_metrics": re.compile(
        r'\b\d{2,3},000\+\s*(?:users|teams|customers|companies)\b|\b99\.9%\s*uptime\b'
        r'|\b4\.9\s*(?:stars|/5)\b',
        re.IGNORECASE,
    ),
    "neon_glow": re.compile(
        r'\bshadow-\[[^\]]*rgba\([^)]*\b0?\.\d+[^)]*\)\s*\]|\bdrop-shadow-\['
        r'|\bglow-(?:sm|md|lg|xl)\b|\bneon\b',
        re.IGNORECASE,
    ),
    "developer_tool_signals": re.compile(
        # The all-caps tracked eyebrow is the strongest single tell, so it only
        # counts when the two classes appear together — `uppercase` alone is
        # normal on tags and buttons.
        r'\btracking-widest\b.*\buppercase\b|\buppercase\b.*\btracking-widest\b'
        # Command palettes used as primary navigation.
        r'|\bcmdk\b|<\/?Command(?:Dialog|Input|List|Item|Group|Empty|Separator)'
        r'|⌘K'
        # Version badges and changelog chips in the first viewport.
        r'|\bv\d+\.\d+(?:\.\d+)?\b',
    ),
    # Monospace as *chrome* is a tell; monospace on actual code is the style
    # guide. Kept separate so ``ai_slop_hits`` can suppress it in files that
    # render code blocks or technical values.
    "mono_as_chrome": re.compile(r'\bfont-mono\b'),
}

# Files that legitimately render code or technical values: `font-mono` there is
# intentional, so the mono-as-chrome signal is skipped for those files.
CODE_CONTEXT_RE = re.compile(r'<code\b|<pre\b|\bCodeBlock\b|\bSyntaxHighlighter\b|\bhighlight\.js\b')

MONO_SIGNAL = "mono_as_chrome"


def ai_slop_hits(text: str) -> Counter:
    """Count AI-slop signals in *text*, dropping mono hits in code-bearing files."""
    hits: Counter = Counter()
    for name, pattern in AI_SLOP_PATTERNS.items():
        count = len(pattern.findall(text))
        if count:
            hits[name] = count
    if MONO_SIGNAL in hits and CODE_CONTEXT_RE.search(text):
        del hits[MONO_SIGNAL]
    return hits


# Conversion and interaction patterns specific to client apps
CONVERSION_PATTERNS = {
    "social_login": re.compile(r'\bgoogle.?auth\b|\bgithub.?auth\b|\bapple.?auth\b|\boauth\b|\bsso\b', re.IGNORECASE),
    "pricing_toggle": re.compile(r'\bbilling.?toggle\b|\bper.?year\b|\bannually\b|\bmonthly.?annual\b', re.IGNORECASE),
    "trust_near_cta": re.compile(r'\bno.?credit.?card\b|\bcancel.?anytime\b|\bmoney.?back\b|\bfree.?trial\b', re.IGNORECASE),
    "confirmation_dialog": re.compile(r'\bAlertDialog\b|\bConfirmDialog\b|\bare you sure\b', re.IGNORECASE),
    "mobile_nav": re.compile(r'\bBottomNav\b|\bTabBar\b|\bMobileNav\b|\bbottom.?navigation\b', re.IGNORECASE),
    "progress_indicator": re.compile(r'\bStepIndicator\b|\bStepper\b|\bcurrentStep\b|\bstep\s*\d+\s*(?:of|/)\s*\d+', re.IGNORECASE),
    "form_validation": re.compile(r'\bFormMessage\b|\bfieldState\b|\berrorMessage\b'),
    "responsive_images": re.compile(r'\bsizes=|next/image|loading="(?:lazy|eager)"', re.IGNORECASE),
}

HEX_RE = re.compile(r'#[0-9a-fA-F]{3,8}\b')

# Capture the full utility, including arbitrary values and directional forms.
# A trailing \b after ``\]`` never matches (``]`` and the following character
# are both non-word), which previously collapsed ``rounded-[2.5rem]`` and
# ``rounded-t-lg`` into a bare ``rounded``.
RADIUS_RE = re.compile(r'\brounded(?:-(?:[trblse]{1,2}-)?(?:none|sm|md|lg|xl|2xl|3xl|4xl|full|\[[^\]]+\]))?\b')


def iter_files(root: Path, max_files: int) -> list[Path]:
    """Collect UI files under *root*, skipping build and vendor directories.

    Only the path *relative to root* is inspected for excluded directory names.
    Testing absolute parts would skip a perfectly valid project that happens to
    live under ``C:\\Code\\build\\...`` or in a folder called ``out``.
    """
    files: list[Path] = []
    for path in root.rglob("*"):
        if len(files) >= max_files:
            break
        if not path.is_file() or path.suffix not in UI_EXTENSIONS:
            continue
        rel_parts = path.relative_to(root).parts[:-1]
        if any(part in EXCLUDE_DIRS for part in rel_parts):
            continue
        files.append(path)
    return files


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return ""


def read_package(root: Path) -> tuple[dict[str, str], dict[str, str]]:
    package_path = root / "package.json"
    if not package_path.exists():
        return {}, {}
    try:
        data = json.loads(package_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}, {}
    deps = {**(data.get("dependencies") or {}), **(data.get("devDependencies") or {})}
    scripts = data.get("scripts") or {}
    return deps, scripts


def score_file(text: str) -> int:
    """Rank a file by how much design attention it needs.

    AI-slop hits are weighted 3x: a file full of purple gradients and sparkle
    icons is the one worth reading first, even if it has fewer product signals
    than a plain form.
    """
    score = 0
    for pattern in SIGNAL_PATTERNS.values():
        score += len(pattern.findall(text))
    for count in ai_slop_hits(text).values():
        score += 3 * count
    return score


def analyze(root: Path, max_files: int) -> dict[str, Any]:
    root = root.resolve()
    deps, scripts = read_package(root)
    files = iter_files(root, max_files)

    signal_counts: Counter = Counter()
    conversion_counts: Counter = Counter()
    ai_slop_counts: Counter = Counter()
    colors: Counter = Counter()
    radii: Counter = Counter()
    top_files: list[tuple[int, Path]] = []

    background_image_files: set[str] = set()
    trust_files: set[str] = set()
    onboarding_files: set[str] = set()
    auth_files: set[str] = set()
    pricing_files: set[str] = set()
    ai_slop_files: set[str] = set()
    illustration_files: set[str] = set()
    missing_label_risk_files: set[str] = set()

    for file_path in files:
        text = read_text(file_path)
        if not text:
            continue

        rel = str(file_path.relative_to(root))

        for name, pattern in SIGNAL_PATTERNS.items():
            signal_counts[name] += len(pattern.findall(text))

        for name, pattern in CONVERSION_PATTERNS.items():
            conversion_counts[name] += len(pattern.findall(text))

        for name, count in ai_slop_hits(text).items():
            ai_slop_counts[name] += count
            ai_slop_files.add(rel)

        colors.update(HEX_RE.findall(text))
        radii.update(RADIUS_RE.findall(text))

        score = score_file(text)
        if score:
            top_files.append((score, file_path))

        if SIGNAL_PATTERNS["background_images"].search(text):
            background_image_files.add(rel)
        if SIGNAL_PATTERNS["trust_signals"].search(text):
            trust_files.add(rel)
        if SIGNAL_PATTERNS["onboarding"].search(text):
            onboarding_files.add(rel)
        if SIGNAL_PATTERNS["auth"].search(text):
            auth_files.add(rel)
        if SIGNAL_PATTERNS["pricing"].search(text):
            pricing_files.add(rel)
        if SIGNAL_PATTERNS["illustrations"].search(text):
            illustration_files.add(rel)

        # Flag screens whose inputs may be missing visible labels.
        #
        # Skip design-system primitives: `components/ui/input.tsx` forwards
        # `placeholder` by design and is *supposed* to have no label. The label
        # belongs at the call site, so flagging the primitive is pure noise.
        is_primitive = bool({"ui", "primitives"} & set(file_path.relative_to(root).parts[:-1]))
        has_input = re.search(r'<(?:input|textarea|select)\b|placeholder=', text)
        has_label = re.search(r'FormLabel|<label\b|htmlFor=|aria-label(?:ledby)?=|\bLabel\b', text)
        if (
            file_path.suffix in {".tsx", ".jsx"}
            and not is_primitive
            and has_input
            and not has_label
        ):
            missing_label_risk_files.add(rel)

    detected_stack = sorted({label for dep, label in STACK_DEPS.items() if dep in deps})
    top_files.sort(reverse=True, key=lambda item: item[0])

    return {
        "root": str(root),
        "files_scanned": len(files),
        "detected_stack": detected_stack,
        "scripts": {
            k: scripts[k]
            for k in sorted(scripts)
            if k in {"dev", "build", "test", "lint", "typecheck", "check"}
        },
        "signals": dict(signal_counts.most_common()),
        "conversion_surfaces": dict(conversion_counts.most_common()),
        "ai_slop_risks": dict(ai_slop_counts.most_common()),
        "radii": radii.most_common(12),
        "colors": colors.most_common(12),
        "top_ui_files": [
            {"score": s, "path": str(p.relative_to(root))}
            for s, p in top_files[:12]
        ],
        "background_image_files": sorted(background_image_files)[:10],
        "trust_files": sorted(trust_files)[:10],
        "onboarding_files": sorted(onboarding_files)[:8],
        "auth_files": sorted(auth_files)[:8],
        "pricing_files": sorted(pricing_files)[:8],
        "illustration_files": sorted(illustration_files)[:8],
        "ai_slop_risk_files": sorted(ai_slop_files)[:12],
        "missing_label_risk_files": sorted(missing_label_risk_files)[:8],
    }


def print_report(report: dict[str, Any]) -> None:
    sep = "-" * 60

    print(f"\nProduct design audit: {report['root']}")
    print(f"Files scanned:        {report['files_scanned']}")

    stack = ", ".join(report["detected_stack"]) or "No known stack detected from package.json"
    print(f"Stack:                {stack}")

    if report["scripts"]:
        print("\nUseful scripts:")
        for name, cmd in report["scripts"].items():
            print(f"  {name}: {cmd}")

    # AI slop section — printed first because it is the most urgent
    print(f"\n{sep}")
    if report["ai_slop_risks"]:
        print("WARNING: AI-GENERATED DESIGN RISKS -- fix before shipping")
        print(sep)
        for name, count in report["ai_slop_risks"].items():
            print(f"  {name:<32} {count:>4} occurrence(s)")
        if report["ai_slop_risk_files"]:
            print("\n  Files containing these signals:")
            for path in report["ai_slop_risk_files"]:
                print(f"    {path}")
    else:
        print("OK: No AI-slop signals detected.")
        print(sep)

    if report["missing_label_risk_files"]:
        print(f"\n{sep}")
        print("WARNING: FORM LABEL RISKS -- inputs may be missing visible labels")
        print(sep)
        for path in report["missing_label_risk_files"]:
            print(f"  {path}")

    # Only print signals that actually fired. A wall of zeroes trains the reader
    # to skim past the section, which defeats the point of the report.
    present_signals = {k: v for k, v in report["signals"].items() if v}
    print(f"\n{sep}")
    print("PRODUCT SIGNALS")
    print(sep)
    if present_signals:
        for name, count in present_signals.items():
            print(f"  {name:<28} {count:>4}")
    else:
        print("  None detected -- this may not be a client-facing surface.")

    present_conversion = {k: v for k, v in report["conversion_surfaces"].items() if v}
    if present_conversion:
        print(f"\n{sep}")
        print("CONVERSION SURFACES")
        print(sep)
        for name, count in present_conversion.items():
            print(f"  {name:<28} {count:>4}")

    if report["radii"]:
        print(f"\n{sep}")
        print("RADIUS USAGE")
        print(sep)
        for value, count in report["radii"]:
            excessive = re.search(r'rounded-(?:3xl|4xl|\[[2-9](?:\.\d+)?rem\]|\[[4-9]\dpx\])', value)
            flag = "  <- check: excessive for rectangular content" if excessive else ""
            print(f"  {value:<30} {count:>4}{flag}")

    if report["colors"]:
        print(f"\n{sep}")
        print("COMMON RAW COLORS  (prefer semantic tokens)")
        print(sep)
        for value, count in report["colors"]:
            print(f"  {value:<14} {count:>4}")

    if report["top_ui_files"]:
        print(f"\n{sep}")
        print("START BY READING THESE FILES")
        print(sep)
        for item in report["top_ui_files"][:8]:
            print(f"  {item['path']}  (score {item['score']})")

    if report["background_image_files"]:
        print(f"\n{sep}")
        print("BACKGROUND IMAGE FILES  -- verify overlay contrast (WCAG AA)")
        print(sep)
        for path in report["background_image_files"]:
            print(f"  {path}")

    if report["trust_files"]:
        print(f"\n{sep}")
        print("TRUST SIGNAL FILES  -- verify real content, not placeholder logos/quotes")
        print(sep)
        for path in report["trust_files"]:
            print(f"  {path}")

    if report["auth_files"]:
        print(f"\n{sep}")
        print("AUTH FILES  -- check labels, error copy, mobile layout, and SSO")
        print(sep)
        for path in report["auth_files"]:
            print(f"  {path}")

    if report["pricing_files"]:
        print(f"\n{sep}")
        print("PRICING FILES  -- check tier clarity, CTA copy, and trust lines")
        print(sep)
        for path in report["pricing_files"]:
            print(f"  {path}")

    if report["onboarding_files"]:
        print(f"\n{sep}")
        print("ONBOARDING FILES  -- check progress indicator, back/skip, completion")
        print(sep)
        for path in report["onboarding_files"]:
            print(f"  {path}")

    if report["illustration_files"]:
        print(f"\n{sep}")
        print("ILLUSTRATION FILES  -- verify consistent style and brand color")
        print(sep)
        for path in report["illustration_files"]:
            print(f"  {path}")

    print(f"\n{sep}\n")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Scan a client-facing frontend project for product design signals and AI-slop risks.",
    )
    parser.add_argument(
        "path",
        nargs="?",
        default=".",
        help="Project or app directory to scan.",
    )
    parser.add_argument(
        "--max-files",
        type=int,
        default=2500,
        help="Maximum UI files to scan (default: 2500).",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Print JSON output instead of a text report.",
    )
    args = parser.parse_args()

    root = Path(args.path)
    if not root.exists():
        print(f"Error: path '{root}' does not exist.")
        return 1

    report = analyze(root, args.max_files)

    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print_report(report)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
