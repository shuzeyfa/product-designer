# Product Designer Skill

A design skill for building client-facing SaaS apps, consumer web products, marketing and landing pages, onboarding flows, pricing pages, auth surfaces, and dashboards for non-technical users.

This skill is the companion to [`design-engineer`](https://github.com/farming-labs/design-eng-skills). Where `design-engineer` builds for developers, dashboards, and OSS tools, `product-designer` builds for clients, customers, and people who just need something to work beautifully.

## Install

```bash
npx skills add farming-labs/product-designer --skill product-designer
```

Codex-targeted install:

```bash
npx skills add farming-labs/product-designer --skill product-designer --agent codex --yes
```

For local testing:

```bash
mkdir -p ~/.codex/skills
cp -R product-designer ~/.codex/skills/product-designer
```

Restart your agent after installing so the skill is discovered.

---

## When to Use Which Skill

| Situation | Use |
|-----------|-----|
| Building a landing page, marketing site, or product website for a client | `$product-designer` |
| Building a SaaS app for non-technical end users | `$product-designer` |
| Building an onboarding flow, pricing page, or auth surface | `$product-designer` |
| Building a dashboard a non-technical manager or client will use daily | `$product-designer` |
| Building a developer tool, OSS docs site, or technical dashboard | `$design-engineer` |
| Building a studio app, command palette interface, or dense admin tool | `$design-engineer` |
| Polishing a component library or design system for developers | `$design-engineer` |

If you are unsure — ask who the end user is. If they are not a developer, use `$product-designer`.

---

## Skills

- **`product-designer`**: Design and build polished client-facing web products for SaaS apps, consumer products, marketing sites, onboarding flows, pricing pages, auth surfaces, and dashboards for non-technical users. Covers human-centered visual language, background image system, trust signals, warm motion and illustration guidance, form best practices, mobile-first interaction patterns, and an AI-slop risk scanner to prevent generic output.

---

## What This Skill Guards Against

The biggest risk when using an AI to build client-facing UIs is that it defaults to a generic "AI-generated" aesthetic:

- Purple/indigo gradients as the brand color
- Glassmorphism panels stacked on gradients
- Sparkle icons on every AI feature
- "Seamless, powerful, next-generation" copy
- Three floating metric cards with made-up numbers
- Generic stock photography
- Forms using placeholder text as labels
- Empty states that just say "No data found"

There is a second, subtler failure mode: the **"tech vibe."** An AI that has read a thousand developer-tool landing pages will reach for their vocabulary even when the audience is a clinic's front desk or a small business owner:

- `uppercase tracking-widest` eyebrows above every section — the single most reliable AI-dev-tool tell
- `font-mono` used as chrome rather than for actual code
- Dark mode as the default canvas
- A command palette (⌘K) as primary navigation
- Version numbers, changelogs, or "v2.0 is here" in the hero
- Terminal windows or code blocks as hero imagery
- Inter chosen by reflex rather than on purpose

Every reference file in this skill is written to actively prevent both sets of patterns and push toward specific, human, brand-grounded design decisions instead. The developer-tool tells are catalogued in "Developer-Tool Tells — The 'Tech Vibe' Trap" in `references/design-language.md`.

---

## Bundled Resources

| File | Purpose |
|------|---------|
| `SKILL.md` | Entry point — workflow, quick start, and example requests |
| `references/design-language.md` | Visual language: color, typography, radius, spacing, shadow, background image system, AI-trap anti-patterns, page archetypes, component style contract |
| `references/implementation-patterns.md` | Code patterns for hero sections, pricing tables, auth surfaces, onboarding flows, testimonials, and non-technical dashboards |
| `references/interaction-language.md` | Behavior rules for forms, CTAs, multi-step flows, loading/empty/error/success states, trust interactions, mobile touch, and accessibility |
| `references/motion-and-icons.md` | Motion timing, scroll reveals, celebration animations, icon policy, and illustration guidance |
| `scripts/product_audit.py` | Python scanner — detects background images, trust signals, auth/pricing/onboarding surfaces, and 12 categories of AI-slop risk |

---

## Running the Audit Script

Before starting a design pass on a client project:

```bash
python /path/to/product-designer/scripts/product_audit.py <project-path>
```

Output includes:

- Detected stack and scripts
- **AI-slop risk warnings** — 12 signals in total: sparkle icons, generic copy, purple/indigo as primary, glassmorphism, excessive radius, decorative orbs and blobs, lorem ipsum, placeholder CTAs, fake round metrics, neon glow, developer-tool signals (`uppercase tracking-widest` eyebrows, command palettes, version badges), and `font-mono` used as chrome. The mono signal is suppressed in files that render real code (`<code>`, `<pre>`, syntax highlighters), where monospace is correct
- **Form label risks** — files with `placeholder=` but no visible `<label>`. Design-system primitives under `components/ui/` are skipped, since the label belongs at the call site, not in the primitive.
- Product signals (hero, trust, onboarding, pricing, auth, CTA, forms, empty/loading/success states, accessibility) and conversion surfaces (social login, billing toggle, trust copy near CTA, confirmation dialogs, mobile nav, progress indicators)
- Background image files (verify overlay contrast)
- Trust signal files (verify real content)
- Auth, pricing, onboarding, and illustration files with specific audit reminders
- Radius usage with flags for `rounded-3xl`, `rounded-4xl`, and arbitrary values large enough to read as a pill
- Most common raw colors (flag for semantic token use)
- Files ranked by design attention needed, with AI-slop hits weighted 3x so the worst offenders sort first

JSON output for programmatic use:

```bash
python /path/to/product-designer/scripts/product_audit.py <project-path> --json
```

---

## Example Requests

```text
Use $product-designer to make this landing page feel premium and trustworthy.
```

```text
Polish this onboarding flow so new users feel guided and confident.
```

```text
Redesign this pricing page so it is clear, scannable, and converts.
```

```text
Make this client dashboard feel clean and approachable for non-technical users.
```

```text
Add a full-bleed hero with a background image that still reads well on mobile.
```

```text
Improve the empty and error states so they feel encouraging, not broken.
```

```text
Build the auth page as a split-screen with a brand image and a focused sign-in form.
```
