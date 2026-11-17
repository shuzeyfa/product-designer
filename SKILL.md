---
name: product-designer
description: "End-to-end product design workflow for client-facing SaaS apps, consumer web products, marketing sites, onboarding flows, pricing pages, dashboards for non-technical users, and client-delivered web applications. Use when the user asks to make UI/UX/design/frontend feel premium, warm, trustworthy, approachable, clean, or client-ready; when editing TSX/JSX/CSS/Tailwind/shadcn/Radix interfaces for non-developer audiences; or when adding background images, soft layouts, onboarding flows, pricing sections, hero sections, auth surfaces, or any surface where the end user is a client, customer, or non-technical person."
---

# Product Designer

## Overview

Use this skill to turn functional frontend work into a polished, human-centered product that clients trust and customers enjoy using. The goal is not technical credibility — it is clarity, warmth, and confidence. Read the product and its audience first, then improve the actual experience rather than decorating the surface.

This skill is the companion to `design-engineer`. Where `design-engineer` builds for developers, dashboards, and OSS tools, `product-designer` builds for clients, customers, and people who just need something to work beautifully.

## Quick Start

1. Inspect the project before proposing any visual direction:

```bash
python /path/to/product-designer/scripts/product_audit.py <app-or-package-path>
```

2. Read `references/design-language.md` before touching color, typography, layout, background images, spacing, or component style.
3. Read `references/implementation-patterns.md` when building reusable sections, landing pages, auth surfaces, pricing tables, onboarding flows, or dashboard layouts for non-technical users.
4. Read `references/interaction-language.md` before changing forms, onboarding steps, CTAs, navigation, error states, success feedback, or any flow a non-technical user will walk through.
5. Read `references/motion-and-icons.md` before adding transitions, page animations, hover effects, loaders, or choosing an icon style.
6. Implement the smallest complete design pass that meaningfully improves the real user experience.
7. Run the app's typecheck/build/tests when available, then verify the edited screens in a browser across desktop and mobile — paying particular attention to how a non-technical user would perceive the result.

## Workflow

### 1. Understand the Audience and Surface

Before touching a single class, answer these questions:

- Who is the primary user? A client, a customer, a non-technical employee, a buyer?
- What is the job of this screen? Sell, onboard, retain, inform, collect, or reassure?
- What emotion should the user feel? Trust, confidence, delight, calm, curiosity, urgency?
- Is this a marketing surface, a product surface, or a hybrid?
- What does the user see first, and does it immediately answer "what is this, and why should I care?"

Identify the surface type before choosing any visual direction:

- **Marketing / landing page**: sell the product, establish trust, guide to CTA
- **Onboarding flow**: reduce anxiety, celebrate progress, make the first step obvious
- **Client-facing SaaS dashboard**: useful immediately, non-intimidating, data with context
- **Pricing page**: clear value, easy comparison, confident CTA, trust signals
- **Auth surface**: minimal friction, clear error recovery, brand moment
- **Settings / profile**: predictable, calm, no surprises
- **Empty / first-use states**: encouraging, never cold or broken-feeling

### 2. Set a Human-Centered Design Direction

Choose the visual direction from the user's job, not from trends:

- For marketing and landing pages: strong first-viewport identity, real product proof, one clear CTA, background imagery when it reinforces the brand story, breathing room between sections.
- For SaaS dashboards: calm hierarchy, non-technical labels, context near every metric, friendly empty states, soft loading behavior, mobile-aware layout.
- For onboarding: step indicators, one task per screen, celebration on completion, never dead ends.
- For pricing: clear tier names, plain-language feature lists, trust badges, prominent recommended plan, one-click CTA.
- For auth: focused form, helpful error copy, brand presence without clutter.

Define the visual grammar in tokens before writing components:

- Background: white, near-white, warm neutral, or a full-bleed image with overlay. Light by default — dark-first is a developer-tool convention.
- Surface: card white, soft gray, or translucent panel over image
- Text: near-black primary, medium-gray secondary, muted hint text
- Brand accent: one primary color for CTAs, links, and selected states
- Radius: soft by default — `rounded-lg` for cards and inputs, `rounded-xl` for elevated panels, `rounded-2xl` for image containers, `rounded-full` for pills and avatars only
- Spacing: generous — sections breathe, cards have room, type has line-height
- Shadow: soft and layered, not hard or flat
- Motion: smooth, purposeful, never distracting

### 3. Use Background Images and Visual Texture With Intention

Background images are a first-class tool in this skill when they serve the product story:

- Use full-bleed background images in hero sections when the product, lifestyle, or brand has a strong visual identity.
- Always pair image backgrounds with a gradient or color overlay that keeps text readable. Never place text directly on a busy image without protection.
- Prefer images that feel authentic, not stocky: real product screenshots, real environments, editorial photography.
- For SaaS and client apps, abstract or gradient backgrounds work well when they establish brand tone without distracting from the UI.
- Use subtle texture, grain, or noise overlays to add warmth to flat color backgrounds — keep them barely visible, not decorative wallpaper.
- Background sections should feel intentional: use them for heroes, feature callouts, pricing bands, or CTA sections — not randomly throughout the page.
- Always test image backgrounds at mobile widths; reposition, darken, or replace them when text becomes unreadable on small screens.
- Respect `prefers-reduced-motion` for any animated or parallax background behavior.

### 4. Design the Whole State, Not Just the Happy Path

Cover expected states before calling the UI done:

- Loading and skeleton states that feel calm, not broken
- Empty states with a friendly message and a clear next action — never a blank white box
- Error states that explain what happened in plain language and offer recovery
- Success and confirmation states that celebrate the user's action
- Hover, focus-visible, pressed, and disabled states that feel polished
- Mobile layouts that reflow rather than shrink — primary actions always reachable
- Long content, overflow text, narrow viewports, and touch targets

### 5. Apply Product Craft Rules

- Make the primary action obvious. There should be one dominant CTA per viewport.
- Use real copy. Avoid lorem ipsum. Write as if speaking directly to the user.
- Keep forms short. Ask only what is needed. Group related fields.
- Trust signals matter: logos, testimonials, review counts, security badges, and money-back guarantees belong near friction points.
- Use images and illustrations purposefully — they should explain or reassure, not decorate.
- Soft radius is the default. Use `rounded-lg` for cards and inputs, `rounded-xl` for elevated panels, `rounded-2xl` for image containers, `rounded-full` for pills and avatars only.
- Generous whitespace reads as premium. Tight spacing reads as cheap.
- One brand color does more than five. Keep the accent palette constrained.
- Avoid hero sections that only show marketing text. Show the actual product, a screenshot, a preview, or a result.
- Keep navigation simple. Clients and consumers do not read nav bars — they scan for one familiar label.
- Do not import developer-tool vocabulary. No `uppercase tracking-widest` eyebrow above every section, no `font-mono` chrome, no command palette as primary navigation, no version badges in the hero. These are the tells that make a client app feel like a dev tool. See "Developer-Tool Tells" in `references/design-language.md`.

### 6. Verify Like a Product Designer

Before finishing:

- Run formatter/linter/typecheck/build/test commands that are standard in the repo.
- Start the dev server and walk through the flow as if you were the client seeing it for the first time.
- Check desktop and mobile widths for broken layouts, clipped text, unreadable contrast over backgrounds, lost CTAs, and broken form states.
- Ask: does this feel trustworthy? Does it feel finished? Would a non-technical client be proud to show this to their users?
- Summarize changed files and the verification performed.

## Bundled Resources

- `scripts/product_audit.py`: quick project scan for stack, UI files, background/image usage, radius scale, color tokens, and surface-level design signals.
- `references/design-language.md`: warm, accessible, client-ready visual language for SaaS apps, consumer products, and client-delivered web applications.
- `references/implementation-patterns.md`: component and section patterns for building polished client-facing products — heroes, pricing tables, onboarding flows, auth surfaces, and dashboards.
- `references/interaction-language.md`: interaction grammar for non-technical users — forms, onboarding, navigation, feedback, trust flows, and mobile behavior.
- `references/motion-and-icons.md`: motion vocabulary, icon choices, and animation rules for warm, approachable product surfaces.

## Example Requests

- "Use `$product-designer` to make this landing page feel premium and trustworthy."
- "Polish this onboarding flow so new users feel guided and confident."
- "Redesign this pricing page so it is clear, scannable, and converts."
- "Make this client dashboard feel clean and approachable for non-technical users."
- "Add a full-bleed hero with a background image that still reads well on mobile."
- "Improve the empty and error states so they feel encouraging, not broken."
