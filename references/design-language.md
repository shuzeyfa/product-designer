# Product Design Language

Load this reference when the task is a client-facing SaaS app, consumer web product, marketing or landing page, onboarding flow, pricing surface, auth page, or any interface where the end user is a non-technical person — a client, customer, buyer, or employee who just needs something to work.

This reference is intentionally portable. It does not depend on private local paths. When the user provides inspiration repos, screenshots, URLs, or brand assets, inspect those sources directly and translate their patterns into the current project.

---

## The Core Rule: Design for a Specific Product, Not for "Modern UI"

Every visual decision must be answerable with: **"why does this choice serve this product and this user?"**

If the answer is "because it looks modern" or "because AI apps look like this" — it is the wrong choice.

Good product design is specific. It has a point of view. It reflects the brand, the audience, and the job the product does. Generic looks unfinished, even when it is technically polished.

---

## The AI-Generated App Trap — What to Never Do

These are the patterns that make an app look like it was designed by an AI averaging the internet. Avoid all of them unless the existing codebase already uses them deliberately with restraint and they are working.

### Visual Anti-Patterns

- **Purple/indigo gradient as the brand color.** This is the default "AI product" color. Use it only if the brand explicitly calls for it, never as a shortcut to look modern.
- **Glassmorphism panels everywhere.** `backdrop-blur` with semi-transparent white/dark backgrounds stacked on top of a gradient hero is overused. Use it in one focused place if the brand warrants it, not as the default card style.
- **Competing gradient blobs and orbs.** Multiple radial gradients, animated blobs, or decorative orbs scattered around the page add noise without meaning. If a background effect exists, one is enough — behind a hero, behind a CTA band, not floating throughout the layout.
- **`rounded-3xl` or `rounded-full` on rectangular content containers.** Soft radius is good. Excessive radius on cards, inputs, and panels makes the UI look toy-like. Use `rounded-lg` or `rounded-xl` as the default; reserve `rounded-2xl` for image containers, and `rounded-full` for pills and avatars only.
- **Dark mode with neon purple, cyan, or green accents.** Neon colors on dark backgrounds look like a developer portfolio. Client apps in dark mode should use muted, desaturated accents with appropriate luminosity — not glow effects.
- **Dark mode as the default canvas.** A client-facing product should ship light by default. Dark-first is a developer-tool convention: it signals "this is for engineers" to exactly the audience this skill is not for. Build the light theme first and make it excellent; add dark mode only if the product already has it or the brand demands it.
- **Decorative grid lines or dot patterns as the only texture.** Grid/dot overlays as a background treatment are acceptable only when they reinforce a structured, technical feel that fits the brand. They are not a substitute for a real design decision.
- **Fake 3D mockups floating in space.** A browser window or phone frame with a screenshot of the product, floating on a gradient with a soft shadow, is overused. When showing the product, use real screenshots in a natural, grounded composition — or don't show a screenshot at all.
- **Too many animated elements competing for attention.** Motion should serve one purpose per viewport. When every section has staggered fade-ins, floating icons, rotating gradients, and hover shimmer effects, nothing has emphasis.

### Developer-Tool Tells — The "Tech Vibe" Trap

These are subtler than purple gradients, and they are the reason a design can pass every other rule in this file and still feel like a developer tool. They come from the vocabulary of docs sites, changelogs, and OSS landing pages. A client, a clinic manager, or a shopper reads them as "this is not for me."

- **`uppercase tracking-widest` eyebrows above every heading.** The all-caps micro-label (`text-xs font-medium tracking-widest uppercase text-primary`) is the single most reliable tell of an AI-generated developer-tool page. It appears above the hero, above every section, above every card. Use it at most once per page, or not at all. A normal sentence-case subheading, or no eyebrow, reads warmer and more human.
- **Monospace type as chrome.** `font-mono` belongs on code, IDs, timestamps, and technical values. Using it for nav items, labels, badges, or section headers makes the product look like a terminal.
- **Dense, hairline-bordered, square-cornered UI.** 1px borders on every surface, `rounded-none` or `rounded-sm`, tight `p-3` padding, and 12px body text is the developer-dashboard aesthetic. Client surfaces want fewer borders, softer corners, and more air.
- **Command palettes, keyboard-shortcut hints, and `⌘K` affordances as primary navigation.** These are power-user features. A non-technical user needs a visible, labeled button.
- **Version numbers, changelog links, and "v2.0" badges in the hero.** Ship notes belong in a footer link, not the first viewport.
- **Terminal or code-block imagery as the hero visual.** A client does not want to see a shell. Show the product's actual output — the report, the booking, the invoice, the result.
- **Inter as an unconsidered default.** Inter is a fine typeface, but it is also the default of every AI-generated page. Reach for it only after considering the brand. A distinctive-but-legible face (see Typography) does more for perceived quality than any other single choice.

### Copy and Content Anti-Patterns

- **"Seamless", "powerful", "intuitive", "AI-powered", "next-generation".** These words say nothing. Every hero on the internet uses them. Write copy that names the specific problem the user has and the specific result they get.
- **Sparkle or magic wand icons for AI features.** The ✨ metaphor is exhausted. If the product has AI features, describe what they do — do not decorate them with sparkles.
- **"Get Started Free" + "Learn More" as the only CTA pair.** These are placeholders. CTAs should name the action and its outcome: "Start your free 14-day trial", "See how it works for teams", "Book a demo for your clinic".
- **Three floating metric cards with made-up numbers in the hero.** "10,000+ users", "99.9% uptime", "4.9 stars" placed in hero sections without context look like decoration, not proof. Use real numbers and name the source, or use a real product screenshot instead.
- **Generic testimonials with initials-only avatars.** A quote from "Sarah M., Founder" with a gray circle initial is indistinguishable from placeholder content. Use real photos, real names, real companies, and quotes that name a specific result.
- **Lorem ipsum anywhere in a shipped design pass.** Always write real copy or clearly marked placeholder copy that reflects the product's actual voice.

### Layout and Structure Anti-Patterns

- **A page made entirely of full-width gradient bands stacked vertically.** Product pages need rhythm: some full-width sections, some contained, some asymmetric. All-full-width stacking creates a monotonous scroll.
- **Every section centered with equal top and bottom padding.** Real editorial layout alternates density, alignment, and emphasis. Not every section should look like every other section.
- **Forms that use placeholder text as the label.** When the user starts typing, the label disappears. This is an accessibility failure and a trust failure on a form a client will use every day.
- **Mobile layout that is just the desktop layout squished.** Mobile needs layout decisions: stacked vs. scrollable, hidden vs. collapsed, touch target size, bottom bar vs. hamburger menu.
- **Empty state that just says "No data found".** Every empty state needs to name what is missing, explain why it might be empty, and offer one clear next action.

---

## Design Language Brief

The target design language for client and consumer products is warm, specific, and trustworthy:

- **Clarity first**: the user's eye should land on one thing — the most important thing — before anything else. Layout, hierarchy, and contrast all serve this.
- **Brand-specific color**: one primary brand color drives CTAs, links, and active states. Supporting neutrals carry the rest of the page. No rainbow palettes, no neon.
- **Soft geometry**: rounded corners read as approachable. `rounded-lg` through `rounded-xl` is the default. Reserve `rounded-2xl` for image containers, and `rounded-full` for pills and avatars.
- **Generous space**: whitespace is not emptiness — it is structure. Sections breathe. Cards have padding. Type has line-height. Tight spacing reads as cheap.
- **Real content proof**: the actual product, a screenshot, a workflow result, a customer outcome. Not a mockup of a mockup. Not a floating card with icons.
- **Human copy**: short sentences. Active voice. The user's problem named directly. The benefit stated, not implied.
- **Trust through specificity**: real customer names, real logos, real numbers with context, real security language when needed.
- **Motion with restraint**: transitions should feel like the product breathing — not a show. One entrance per section, calm duration, never blocking the user.

---

## Foundations

### Color

- Build the palette around **one brand color** and a neutral scale. The brand color should be specific to the product — not "looks modern".
- Use the brand color for: primary buttons, active nav states, focus rings, links, selected states, and progress indicators.
- Keep the neutral scale in warm or cool grays depending on the brand personality. Warm grays (stone, zinc) feel approachable. Cool grays (slate, gray) feel professional.
- Use color to encode meaning — success, warning, error, info — not decoration. Semantic colors should be consistent across every screen.
- Background: white or warm near-white (`#FAFAF9`, `#F9FAFB`) for light mode. For dark mode, use deep neutrals — not pure black (`#09090B`, `#111113`).
- Avoid: more than one accent color competing on the same viewport. Avoid neon or oversaturated tones unless the brand explicitly requires them.

### Typography

- Pair one display/heading face with one body face. Add a mono face only when the product has code, IDs, or technical content.
- Start from the brand's chosen typeface. If there is none, pick a face with some character that still reads cleanly at body size — Plus Jakarta Sans, DM Sans, Manrope, Figtree, Sora, or Fraunces for a warmer editorial feel. Inter is acceptable but is the default of every AI-generated page; choose it deliberately, not by reflex.
- Load fonts through `next/font` (or the framework's equivalent) with `display: "swap"` and explicit subsets. Do not add a `<link>` to Google Fonts in the document head.
- Scale: establish a clear type scale — display (48-72px), H1 (36-48px), H2 (24-32px), H3 (18-22px), body (15-16px), small (13-14px), label (11-12px). Stick to it.
- Line height: `leading-relaxed` (1.625) or `leading-loose` (2) for body copy. Tight line height is for headings only.
- Weight: use two or three weights — regular for body, medium for labels and UI, semibold or bold for headings and CTAs. Do not use thin or ultra-bold weights unless the brand has a strong editorial voice.
- Letter spacing: minimal. Avoid tracking on body text. Light tracking (`tracking-tight`) is acceptable on large headings. Uppercase small caps for labels only when the brand uses that rhythm — and never as a default eyebrow above every section.
- Avoid: mixing three or more typefaces on one page. Avoid decorative or script fonts unless the brand's visual identity calls for them.

### Radius

One radius contract, used everywhere in this skill. Do not invent a second one per page.

- **Controls** — buttons, inputs, selects, textareas: `rounded-lg` (8px).
- **Cards and panels** — feature cards, pricing tiers, testimonial cards, metric cards, modals, drawers: `rounded-xl` (12px).
- **Image containers** — product screenshots, thumbnails, media blocks: `rounded-2xl` (16px).
- **Pills** — tags, chips, status badges, avatars: `rounded-full`. Nothing else.
- The two-tier control/card split is deliberate: it reads as hierarchy. A button at `rounded-lg` inside a `rounded-xl` card looks intentional; a button at `rounded-xl` inside a `rounded-xl` card looks like everything is the same object.
- Avoid: `rounded-3xl` and above on rectangular content. Avoid `rounded-none` unless the brand has a deliberate editorial square geometry.

### Spacing

- Use a consistent spacing scale: 4, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80, 96, 128px.
- Section padding: `py-16 md:py-24 lg:py-32` as the default. Marketing sections can go higher — `py-24 md:py-32 lg:py-40`.
- Card padding: `p-6` for compact cards, `p-8` for standard, `p-10` or `p-12` for featured or hero cards.
- Form gaps: `gap-4` between fields, `gap-6` between field groups.
- Do not use arbitrary spacing values scattered through the codebase. Encode spacing in tokens or Tailwind classes consistently.

### Shadow

- Use layered, soft shadows — not harsh hard-offset shadows (those belong in the technical/developer skill).
- Default card: `shadow-sm` or `shadow` for light elevation. `shadow-md` for modals and floating elements. `shadow-lg` for key CTAs and feature highlights. Promoted cards are marked by border and badge, not by extra elevation — see the promoted-card rule under Component and Token Guidance.
- Avoid: `shadow-2xl` as the default for every card. Avoid hard `drop-shadow` without an intentional reason. Avoid inset shadows for flat-design surfaces.
- In dark mode: reduce shadow opacity; use `shadow-black/20` or border-based separation instead of heavy drop shadows.

---

## Background Image System

Background images are a first-class design tool in this skill. Use them when they serve the brand and the user's emotional experience.

### When to Use Background Images

- **Hero sections**: when the product, service, lifestyle, or brand has a strong visual identity that an image reinforces better than any illustration or gradient.
- **Feature callout bands**: a full-width section that breaks the visual rhythm and creates emphasis.
- **CTA sections**: an image behind a final conversion section adds urgency and brand presence.
- **Auth pages**: a split-screen layout with a brand image on one half and the form on the other is a proven, clean pattern for client apps.
- **Pricing bands**: a subtle image or texture background differentiates the pricing section from adjacent content sections.

### How to Use Background Images

- Always pair a background image with a **color overlay** to protect text readability. Use `bg-black/40`, `bg-black/50`, or a gradient from `from-black/60 to-black/20` depending on the image darkness and text position.
- Keep the overlay color consistent with the brand. For warm brands, use warm dark overlays (`bg-[#1a0a00]/50`). For neutral brands, use `bg-black/40` or `bg-slate-900/50`.
- Ensure text contrast ratio passes WCAG AA (4.5:1 for body, 3:1 for large text) even on top of the overlay. Test this.
- Use `object-cover` and `object-position` to control how the image crops on different screen sizes. Test at mobile width specifically — a beautiful hero image often needs `object-position: center top` or a separate mobile image.
- For subtle section backgrounds, use very low-opacity images (`opacity-10` to `opacity-20`) combined with a solid background color — this gives texture without competing with the content.
- Prefer images that feel authentic to the brand: real environments, real people doing real things, real product contexts. Avoid generic stock — smiling people pointing at laptops, anonymous hands on keyboards, abstract blue technology.
- Use `priority` (or `loading="eager"`) for above-the-fold hero images. Use `loading="lazy"` for below-the-fold background sections.
- Alt text: if the image carries meaning the user would otherwise miss, describe it. If it is purely decorative — a texture, a mood shot behind a headline — use `alt=""` so screen readers skip it. Never write `alt="image"`, `alt="background"`, or a keyword-stuffed description.

### Background Image vs. Gradient — When to Choose Which

| Use background image when... | Use gradient when... |
|---|---|
| The brand has strong visual identity | The brand is abstract or digital-native |
| A lifestyle or context can be shown | No authentic image is available |
| Emotion is the primary goal | Structure and clarity are the primary goal |
| The auth or landing page is a brand moment | The app interior needs a subtle background treatment |

### What Makes a Background Image Look Cheap

- Low-resolution images stretched to fill. Always use images at least 1920px wide for full-bleed sections.
- Generic stock photography with no connection to the actual product or brand.
- Too dark an overlay that makes the image invisible — if you cannot see the image, remove it and use a solid color.
- Text placed on the lightest or most complex part of the image without protection.
- Background images that move or parallax with no `prefers-reduced-motion` fallback.

---

## Product and Page Archetypes

Use these archetypes to choose the right visual and interaction posture before designing:

- **SaaS landing page**: strong first-viewport identity, real product screenshot or demo, one primary CTA, trust signals (logos, review count, testimonials) early, pricing accessible from nav, responsive across all widths.
- **Client-delivered web app**: operational shell with clear navigation, non-technical labels on every metric and control, friendly loading and empty states, mobile-first layout for field or remote users.
- **Onboarding flow**: one task per step, progress indicator, friendly copy at each gate, celebration on completion, never a dead end. The user should always know where they are and what comes next.
- **Pricing page**: three tiers maximum, one clearly recommended, plain-language feature comparison, visible CTA per tier, trust signals near the payment step, FAQ section below.
- **Auth surface**: focused form with minimal surrounding noise, brand presence without clutter, clear error recovery in plain language, link to sign-up or sign-in, optional SSO when the product supports it.
- **Dashboard for non-technical users**: calm hierarchy, every metric labeled with context (not just the number), friendly empty states, charts explained with a caption, mobile layout that prioritizes the most-used controls.
- **Settings and profile pages**: predictable form layout, clear section headings, success confirmation near the saved control, destructive actions behind confirmation, mobile-safe form inputs.

---

## House Style

The shared visual language is warm, specific, and trustworthy:

- **Soft structure**: rounded corners, layered shadows, generous padding, section bands, and clear visual hierarchy — not hard rails and dividers.
- **Breathing room**: whitespace is structure. Every section should have enough vertical padding that the user's eye can settle before moving on.
- **One accent**: a single brand color drives the page. Supporting colors are neutrals. Semantic colors (success, warning, error) have dedicated tokens.
- **Typography with purpose**: display type is for the headline. Body type is for reading. Labels are for navigation and metadata. Do not use display type for everything.
- **Real content**: actual product screenshots, real customer names, real outcomes, real copy. The UI should look like it is about something specific.
- **Background images as a design tool**: used in hero sections, auth splits, CTA bands, and feature callouts when they reinforce the brand story.
- **Trust signals near friction**: logos, security language, testimonials, and guarantees placed near CTAs and payment steps — not only at the bottom of the page.

---

## Inspiration Sites

Use these as live design references when the network is available. Inspect them for component behavior, copy rhythm, background treatment, layout rhythm, and trust signal placement. Do not clone them blindly — translate the patterns into the current repo's stack and tokens.

**Read the split below carefully.** Several of these are developer tools. They are excellent at craft, and they are the wrong reference for a client-facing product. Study them for *execution* — spacing discipline, type scale, screenshot composition — and never for *tone*. If you copy a developer tool's tone onto a clinic booking page, you have produced exactly the "tech vibe" this skill exists to prevent.

**Consumer and business products — study tone and structure here:**

- `https://stripe.com`: benchmark for trust-first financial product design. Study CTA placement, trust signal use, section rhythm, and typography.
- `https://lemonsqueezy.com`: warm, approachable SaaS billing product. Study the color use, card style, pricing layout, and CTA copy.
- `https://notion.so`: clean, flexible product identity. Study the homepage hierarchy, feature section structure, and testimonial placement.
- `https://cron.com`: premium, minimal calendar SaaS. Study whitespace use, product screenshot composition, and section transitions.
- `https://airbnb.com`: consumer marketplace benchmark. Study how a non-technical audience is guided, how trust is built, and how imagery carries the page.
- `https://wise.com`: plain-language financial product. Study how a complex product is explained without jargon.

**Developer tools — study execution only, not tone:**

- `https://linear.app`: benchmark for calm, minimal, high-quality SaaS product design. Study the layout rhythm, typography scale, and product screenshot integration.
- `https://clerk.com`: polished auth product. Study the auth surface design and the split between brand moment and form.
- `https://resend.com`: clean technical product with warm brand. Study the hero layout and product proof sections.
- `https://vercel.com`: polished developer platform. Study the dashboard design and feature section structure.

**Component and block libraries:**

- `https://efferd.com`: section/block library for clean, ready-to-use shadcn blocks and responsive page composition.
- `https://21st.dev`: community React component reference for high-quality, remixable UI components.

---

## Component and Token Guidance

- Use the existing `components/ui/*` primitives first. Do not build a new button when one already exists.
- Route repeated visual decisions through semantic tokens: `bg-background`, `text-foreground`, `text-muted-foreground`, `border`, `ring`, `primary`, `secondary`, `destructive`. Avoid raw hex values or hardcoded Tailwind colors scattered through components.
- For soft-geometry products, use `rounded-lg` for controls and `rounded-xl` for cards and dialogs. Apply the same two-tier contract everywhere — see Radius above.
- Prefer `cn(...)`, `class-variance-authority`, `tailwind-merge`, and existing `components/ui/*` variants over one-off inline Tailwind strings.
- If the project uses shadcn/ui, extend its theme tokens — do not create a parallel color system alongside it.
- Keep component APIs small. A button should have `variant`, `size`, and `loading` — not 15 props.

---

## Primitive Style Contract

Use this contract as the default house style when the current repo has no stronger design system. Align to the repo's existing tokens and component APIs first if they exist.

### Foundations

- Radius: `rounded-lg` for controls (buttons, inputs), `rounded-xl` for cards and panels, `rounded-2xl` for image containers, `rounded-full` for pills and avatars only.
- Border: subtle — `border border-border` or `border border-gray-200/60`. Not structural dividers — use spacing and background color to separate sections instead.
- Shadow: soft layered elevation — `shadow-sm` for resting state, `shadow-md` for hover or floating state.
- Type: body in a clean sans-serif. Use mono only for code, IDs, or technical content. Labels in medium weight, body in regular, headings in semibold or bold.
- Density: client and consumer surfaces should feel spacious and approachable, not compact. Reserve compact density for settings forms and data-heavy pages.
- Focus: every interactive element needs a visible `focus-visible` ring that uses the brand accent color — not the browser default.

### Buttons

- Primary: solid brand color background, white text, `rounded-lg`, clear hover darkening, stable width during loading.
- Secondary: bordered or low-contrast fill, same height and radius as primary, secondary text color.
- Ghost: no border at rest, subtle background on hover, used for less important actions in toolbars or inline contexts.
- Destructive: red-toned background, explicit destructive label ("Delete account", not just "Delete"), requires confirmation when the action is irreversible.
- Loading: preserve button width, disable on click, show a compact spinner with the action label ("Saving...", "Sending...").
- CTA: the primary conversion button should be larger than a standard button — `h-12` or `h-14`, wider padding, and the brand accent color at full saturation.

### Forms

- Always use visible labels above the input — never placeholder-only.
- Input style: `rounded-lg`, `border border-input`, `bg-background`, clear `focus-visible:ring-2 focus-visible:ring-primary` state.
- Error state: red border, error message directly below the field in plain language, never just an icon.
- Success confirmation: green check or inline success text near the submitted control, not just a toast.
- Keep forms short. If more than five fields are needed on one screen, group them into logical steps or sections with clear headings.

### Cards

- Use cards for: repeated content items, feature grids, pricing tiers, testimonials, and contained tool surfaces.
- Anatomy: `Card`, `CardHeader`, `CardTitle`, `CardDescription`, `CardContent`, `CardFooter`.
- Do not nest cards. Use a separator, section band, or increased padding to create internal sections.
- Hoverable cards need a clear hover state: `shadow-md`, subtle background shift, or border color change — not just cursor change.
- Featured or promoted cards (e.g., the pricing recommended tier) get exactly one treatment: a persistent brand-color border plus a "Most popular" badge. The border marks it, the badge names it — that pair is the whole signal. Do not stack a scale, a glow, a tinted background, or a second shadow on top. A card that is bigger, glowing, tinted, *and* badged reads as a sales tactic rather than a recommendation.

### Images and Media

- Product screenshots: use `rounded-2xl` containers, `shadow-lg`, and a subtle border (`border border-gray-200/50`) to ground them on the page.
- Background images: always with a color overlay, `object-cover`, tested at mobile width.
- Illustrations: use sparingly and consistently. One illustration style per product — do not mix flat vector, 3D render, and line art on the same surface.
- Avatars: `rounded-full`, consistent size within a component, with a fallback initial or generic user icon.

### Trust and Social Proof Components

- Logo grid: grayscale logos at consistent height (28-40px), generous horizontal spacing, at least 6 logos before using this pattern. Do not show a logo grid with 2-3 logos.
- Testimonial cards: real photo, full name, real company and role, a quote that names a specific result — never generic praise.
- Rating display: star rating with the numeric score and review count. Link to the source when possible.
- Security badge: simple text or icon treatment — "256-bit encryption", "SOC 2 compliant", "GDPR ready" — placed near the payment or sign-up step.
- Stats: use real, verifiable numbers. Format them readably ("10,000+ teams", not "10000"). Always explain what the number measures.

---

## Visual System Checklist

Before editing any screen, identify:

- **Audience**: who is the user and what should they feel on this screen?
- **Canvas**: white, warm near-white, dark, or image-backed.
- **Hierarchy**: what is the first thing the user should see? What is second?
- **CTA**: is there one clear primary action? Is it visible without scrolling?
- **Trust signals**: does the screen address the user's likely hesitation near the point of action?
- **States**: are loading, empty, error, and success states handled?
- **Mobile**: does the layout reflow correctly? Are touch targets large enough?
- **Copy**: is every label, heading, and CTA in real, specific, human language?
- **Tone check**: would this screen look out of place on a developer-tool marketing site? If yes, that is the wrong instinct — reread "Developer-Tool Tells" above.

Encode visual decisions in tokens and classes before adding one-off styles.

---

## Quality Bar

A finished product design pass should:

- make the main user action clearer and more confident to take
- feel warmer and more trustworthy than it did before
- use brand-specific color, type, and layout — not generic "SaaS defaults"
- cover loading, empty, error, and success states for every surface touched
- pass WCAG AA contrast for all text, including text over background images
- maintain responsive layout from 320px mobile to 1440px desktop
- contain no AI-generated copy placeholder patterns ("Discover the power of...", "Seamlessly integrate...", "Next-generation...")
- contain no developer-tool tells: no `uppercase tracking-widest` eyebrow, no `font-mono` chrome, no dark-first canvas, no command palette as primary navigation, no version badge in the hero
- be visually verified in a browser as if seeing it for the first time as a client
