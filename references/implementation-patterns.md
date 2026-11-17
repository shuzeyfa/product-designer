# Implementation Patterns

Use this reference when building client-facing SaaS apps, landing pages, onboarding flows, pricing pages, auth surfaces, or dashboards for non-technical users. These patterns are grounded in the same stack as `design-engineer` — Next.js, Tailwind, shadcn/Radix, lucide-react — but shaped for warmth, trust, and human-centered product surfaces.

Adapt every pattern to the current repo rather than copying blindly. The structure is the guidance; the tokens, copy, and radius should come from the product.

---

## Package Stack Patterns

The same stack, with different emphasis:

- **App framework**: Next.js App Router for SaaS and marketing sites. Use layouts wisely — marketing shell and app shell are usually separate.
- **Styling**: Tailwind CSS with `clsx`, `tailwind-merge`, and a local `cn(...)` helper. Semantic tokens via CSS variables (`--background`, `--foreground`, `--primary`, etc.).
- **Component base**: shadcn/ui with Radix primitives. Extend the existing `components/ui/*` before creating new files.
- **Icons**: `lucide-react` for UI actions. Use `simple-icons` for brand logos. Avoid mixing icon families on the same surface.
- **Images**: Next.js `<Image />` for all images — `fill` for background images, `width/height` for content images. Never use a raw `<img>` for user-facing content.
- **Forms**: `react-hook-form` with `zod` for validation. Pair with shadcn `Form`, `FormField`, `FormItem`, `FormLabel`, `FormMessage` wrappers for consistent error presentation.
- **Motion**: CSS transitions and Tailwind animation for simple hover and reveal states. Framer Motion only when already installed and the interaction genuinely needs orchestration or layout animation.
- **Toasts**: `sonner` for nonblocking feedback. Inline feedback for critical form errors — never rely on toast alone for field-level validation.
- **Fonts**: load via `next/font` with `display: "swap"` and explicit subsets. Start from the brand's typeface; if there is none, prefer Plus Jakarta Sans, DM Sans, Manrope, or Figtree over Inter. Never load fonts from a CDN link in a head tag.
- **Animation utilities**: `animate-in`, `fade-in`, `zoom-in-95`, and `slide-in-from-*` come from `tailwindcss-animate` (Tailwind v3) or `tw-animate-css` (Tailwind v4). They are not built into Tailwind. Check `package.json` before using them; if the plugin is absent, either add it or use plain CSS transitions instead.

---

## Page and Section Patterns

### Hero Section — Without Background Image

Use when the product is abstract, digital-native, or when no strong brand photography is available.

Structure:
- Centered or split (text left, visual right) layout
- Optional eyebrow: a short sentence-case line that names the category ("For growing teams", "Now in beta"). Use it at most once per page. Do **not** style it `uppercase tracking-widest` — that is the developer-tool tell. If in doubt, drop the eyebrow and let the headline do the work.
- Headline: one specific, benefit-driven sentence. Not a tagline. Not a slogan. The user's problem or outcome named directly.
- Subhead: one or two sentences of supporting context. Keep it under 20 words.
- Primary CTA + optional secondary CTA. CTA copy must name the action and outcome, not just "Get started".
- Product proof: a real screenshot, a short demo video, or a result the product produces. For a client product this is the report, the booking, the invoice, the finished design — not a terminal or code block.
- Trust micro-line below the CTA: "No credit card required · Cancel anytime · 14-day free trial"

```tsx
<section className="py-24 md:py-32 lg:py-40">
  <div className="container mx-auto px-4 max-w-5xl text-center">
    <p className="text-sm font-medium text-primary mb-4">
      For growing teams
    </p>
    <h1 className="text-4xl md:text-5xl lg:text-6xl font-bold tracking-tight text-foreground mb-6">
      {/* Specific benefit, not "The best platform for everything" */}
      Manage client projects without the spreadsheet chaos
    </h1>
    <p className="text-lg text-muted-foreground max-w-2xl mx-auto mb-8">
      {/* One or two sentences. Active voice. User outcome. */}
    </p>
    <div className="flex flex-col sm:flex-row gap-3 justify-center mb-4">
      <Button size="lg" className="h-12 px-8 text-base">
        Start your free trial
      </Button>
      <Button size="lg" variant="outline" className="h-12 px-8 text-base">
        See how it works
      </Button>
    </div>
    <p className="text-xs text-muted-foreground">
      No credit card required · Cancel anytime
    </p>
    {/* Product proof below — real screenshot in a grounded frame */}
    <div className="mt-16 rounded-2xl overflow-hidden border border-border shadow-lg">
      <Image src="/product-screenshot.png" alt="Project dashboard showing three active client projects" width={1200} height={700} className="w-full" />
    </div>
  </div>
</section>
```

---

### Hero Section — With Background Image

Use when the product, service, or brand has strong visual identity — a physical space, a lifestyle, an environment, or a bold brand statement.

Rules:
- Always `position: relative` on the section, `fill` on the Image, `absolute inset-0` on the overlay.
- Overlay opacity: `bg-black/40` minimum. Test actual text contrast — do not guess.
- Text: white on dark overlay. Keep the text block contained and left-aligned or centered — do not spread text across the full image width.
- CTA buttons: use a solid white button with dark text, or the brand accent at full opacity. Semi-transparent buttons are hard to read on images.
- Mobile: set `object-position` explicitly. Test that the image crops sensibly at 375px. Consider a separate mobile-optimized image.
- Performance: use `priority` on above-the-fold hero images. Set `sizes` correctly.

```tsx
<section className="relative min-h-[85vh] flex items-center justify-center overflow-hidden">
  {/* Background image */}
  <Image
    src="/hero-bg.jpg"
    alt=""
    fill
    className="object-cover object-center"
    priority
    sizes="100vw"
  />
  {/* Overlay — adjust opacity to pass contrast check */}
  <div className="absolute inset-0 bg-black/50" />
  {/* Optional gradient at bottom to blend into next section.
      Tailwind v4 renamed bg-gradient-to-* to bg-linear-to-*; v3 uses the old name. */}
  <div className="absolute bottom-0 left-0 right-0 h-32 bg-linear-to-t from-background to-transparent" />

  {/* Content */}
  <div className="relative z-10 container mx-auto px-4 max-w-4xl text-center text-white">
    <p className="text-sm font-medium text-white/80 mb-4">
      For growing teams
    </p>
    <h1 className="text-4xl md:text-6xl font-bold tracking-tight mb-6">
      Specific headline for this product
    </h1>
    <p className="text-lg text-white/80 max-w-xl mx-auto mb-8">
      Supporting subhead in plain language.
    </p>
    <div className="flex flex-col sm:flex-row gap-3 justify-center">
      <Button size="lg" className="h-12 px-8 bg-white text-gray-900 hover:bg-white/90">
        Primary action
      </Button>
      <Button size="lg" variant="ghost" className="h-12 px-8 text-white border-white/40 hover:bg-white/10">
        Secondary action
      </Button>
    </div>
  </div>
</section>
```

---

### Feature Section

Use to explain what the product does in concrete terms — not abstract benefits.

Rules:
- Each feature card must describe a specific capability, not a vague value ("Instant sync" not "Powerful performance").
- Use a real icon from lucide-react that matches the concept — not a generic star or sparkle.
- Feature sections work best with 3 or 6 cards in a grid. Avoid 4 or 5 — the grid breaks unevenly.
- Alternate between icon-led cards (for feature grids) and screenshot-led sections (for deeper feature explanations) to create rhythm.

```tsx
<section className="py-24 bg-muted/30">
  <div className="container mx-auto px-4 max-w-6xl">
    <div className="text-center mb-16">
      <h2 className="text-3xl md:text-4xl font-bold mb-4">Everything your team needs</h2>
      <p className="text-muted-foreground max-w-xl mx-auto">
        {/* One sentence that names who this is for */}
      </p>
    </div>
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      {features.map((feature) => (
        <Card key={feature.title} className="p-6 rounded-xl border-border/60 hover:shadow-md transition-shadow">
          <div className="w-10 h-10 rounded-lg bg-primary/10 flex items-center justify-center mb-4">
            <feature.Icon className="w-5 h-5 text-primary" />
          </div>
          <h3 className="font-semibold text-foreground mb-2">{feature.title}</h3>
          <p className="text-sm text-muted-foreground leading-relaxed">{feature.description}</p>
        </Card>
      ))}
    </div>
  </div>
</section>
```

---

### Pricing Table

Rules:
- Maximum three tiers. If more are needed, use a comparison table below, not more cards.
- One tier should be clearly recommended — mark it with a brand-color border and a small "Most popular" pill. Not a shouting all-caps "BEST VALUE" starburst, and not a scale-up or a glow. Border plus badge, nothing else.
- Feature list: use checkmarks for included features. Use a muted dash or omit for excluded. Never use a red X — it creates anxiety.
- Price: show the number large. Show the billing period small. Show the savings for annual billing.
- CTA per tier must be specific to the tier — not all three saying "Get started".
- Always include a trust line below the table: "All plans include a 14-day free trial. No credit card required."
- FAQ section below the pricing table reduces the most common hesitations before they become reasons to leave.

```tsx
<section className="py-24">
  <div className="container mx-auto px-4 max-w-5xl">
    <div className="text-center mb-16">
      <h2 className="text-3xl md:text-4xl font-bold mb-4">Simple, honest pricing</h2>
      <p className="text-muted-foreground">Start free. Upgrade when you need to.</p>
      {/* Billing toggle: monthly / annual */}
    </div>

    <div className="grid grid-cols-1 md:grid-cols-3 gap-6 items-start">
      {/* Standard tier */}
      <Card className="p-8 rounded-xl">...</Card>

      {/* Recommended tier — brand border + badge, nothing else */}
      <Card className="p-8 rounded-xl border-2 border-primary relative">
        <span className="absolute -top-3 left-1/2 -translate-x-1/2 bg-primary text-primary-foreground text-xs font-medium px-3 py-1 rounded-full">
          Most popular
        </span>
        {/* Same layout as other tiers */}
      </Card>

      {/* Enterprise tier */}
      <Card className="p-8 rounded-xl">...</Card>
    </div>

    <p className="text-center text-sm text-muted-foreground mt-8">
      All plans include a 14-day free trial. No credit card required. Cancel anytime.
    </p>
  </div>
</section>
```

---

### Testimonials and Social Proof

Rules:
- Never use placeholder testimonials. Write real quotes or clearly mark them as placeholder.
- Each testimonial must include: real photo, full name, real company, real role, and a quote that names a specific result — not generic praise.
- Keep quotes short: 2-4 sentences. If the quote is longer, use a pull quote with the most specific sentence.
- Logo grid: grayscale at a consistent height (32-40px), minimum 6 logos, generous spacing. If fewer than 6 logos are available, use a text list instead of a logo grid.
- Review counts and star ratings must link to the source when possible.

```tsx
{/* Testimonial card */}
<Card className="p-6 rounded-xl flex flex-col gap-4">
  <div className="flex gap-1">
    {[1,2,3,4,5].map(i => (
      <Star key={i} className="w-4 h-4 fill-yellow-400 text-yellow-400" />
    ))}
  </div>
  <p className="text-foreground leading-relaxed">
    "{/* Specific result quote — not 'This tool changed our lives' */}"
  </p>
  <div className="flex items-center gap-3 mt-auto pt-4 border-t border-border/50">
    <Image
      src="/testimonials/sarah.jpg"
      alt="Sarah Chen"
      width={40}
      height={40}
      className="rounded-full object-cover"
    />
    <div>
      <p className="text-sm font-medium text-foreground">Sarah Chen</p>
      <p className="text-xs text-muted-foreground">Head of Operations, Acme Corp</p>
    </div>
  </div>
</Card>
```

---

### Auth Surface

Rules:
- Two layouts: centered card (simpler, works for most products) or split-screen (image left, form right — stronger brand moment).
- Keep the form minimal: email + password for sign-in, email + password + name for sign-up. Additional fields belong in onboarding, not auth.
- Error messages must be in plain language and placed directly below the failing field. Never just "Invalid credentials" — say "The email or password you entered is incorrect. Try again or reset your password."
- Brand the page — logo, brand color on the CTA — but do not distract from the form.
- Always include: forgot password link, sign-in/sign-up toggle, and optional SSO when the product supports it.

```tsx
{/* Split-screen auth */}
<div className="min-h-screen grid grid-cols-1 lg:grid-cols-2">
  {/* Brand side — image or gradient */}
  <div className="hidden lg:flex relative bg-muted">
    <Image src="/auth-bg.jpg" alt="" fill className="object-cover object-center" />
    <div className="absolute inset-0 bg-black/40" />
    <div className="relative z-10 p-12 flex flex-col justify-between text-white">
      <Logo className="text-white" />
      {/* Optional brand quote or product highlight */}
      <blockquote className="text-sm text-white/80 leading-relaxed">
        "{/* Real customer quote that reinforces trust */}"
        <footer className="mt-2 text-xs text-white/60">— Name, Company</footer>
      </blockquote>
    </div>
  </div>

  {/* Form side */}
  <div className="flex items-center justify-center p-8">
    <div className="w-full max-w-sm">
      <div className="mb-8">
        <h1 className="text-2xl font-bold">Welcome back</h1>
        <p className="text-muted-foreground mt-1 text-sm">Sign in to your account</p>
      </div>
      {/* Form fields with react-hook-form + shadcn Form */}
    </div>
  </div>
</div>
```

---

### Onboarding Flow

Rules:
- One task per step. Never combine two decisions on one screen.
- Always show a progress indicator — a step counter ("Step 2 of 5") or a progress bar. The user must always know where they are.
- Every step has a "Back" and "Continue" button. Back is secondary; Continue is primary.
- The final step should feel like an arrival — a small celebration, a summary of what was set up, and a clear CTA into the actual product.
- Never dead-end. If a step fails, tell the user what happened and what they can do next.
- Skip links for optional steps — but make it clear the step is optional before the user clicks Skip.

```tsx
<div className="min-h-screen flex flex-col">
  {/* Progress header */}
  <header className="border-b border-border py-4 px-6">
    <div className="flex items-center justify-between max-w-xl mx-auto">
      <Logo />
      <span className="text-sm text-muted-foreground">Step {step} of {total}</span>
    </div>
    <Progress value={(step / total) * 100} className="mt-3 h-1" />
  </header>

  {/* Step content */}
  <main className="flex-1 flex items-center justify-center p-8">
    <div className="w-full max-w-md">
      <h2 className="text-2xl font-bold mb-2">{currentStep.title}</h2>
      <p className="text-muted-foreground mb-8">{currentStep.description}</p>
      {/* Step-specific form or choice UI */}
    </div>
  </main>

  {/* Navigation footer */}
  <footer className="border-t border-border py-4 px-6">
    <div className="flex justify-between items-center max-w-xl mx-auto">
      <Button variant="ghost" onClick={goBack} disabled={step === 1}>Back</Button>
      {currentStep.optional && (
        <Button variant="ghost" onClick={skipStep} className="text-muted-foreground">
          Skip for now
        </Button>
      )}
      <Button onClick={goNext}>
        {step === total ? "Go to dashboard" : "Continue"}
      </Button>
    </div>
  </footer>
</div>
```

---

### Dashboard for Non-Technical Users

Rules:
- Every metric must be labeled with context, not just the number. "Total revenue this month" not "Revenue". "Active clients" not "Users".
- Charts must have a caption or tooltip that explains what the data means.
- Empty states must be specific and encouraging. "You have no active projects yet. Create your first project to get started." with a CTA button.
- Loading states must preserve layout — use skeletons that match the shape of the loaded content.
- Keep the left sidebar simple: 5-7 top-level items maximum. Group secondary items under a collapsible section.
- Mobile layout: consider a bottom tab bar for primary navigation items instead of a hamburger that hides everything.
- Avoid jargon in labels. "Invoices" not "AP/AR". "Team members" not "Users". "Projects" not "Entities". Write for the actual user.

```tsx
{/* Metric card — with context label, not just a number */}
<Card className="p-6 rounded-xl">
  <CardHeader className="flex flex-row items-center justify-between pb-2">
    <CardTitle className="text-sm font-medium text-muted-foreground">
      Revenue this month
    </CardTitle>
    <TrendingUp className="w-4 h-4 text-muted-foreground" />
  </CardHeader>
  <CardContent>
    <div className="text-2xl font-bold">$12,340</div>
    <p className="text-xs text-muted-foreground mt-1">
      <span className="text-green-600 font-medium">+8%</span> from last month
    </p>
  </CardContent>
</Card>

{/* Friendly empty state */}
<div className="flex flex-col items-center justify-center py-20 text-center">
  {/* Icon badge: rounded-lg keeps it in the control tier. A circular
      rounded-full badge is also fine here — this is decorative chrome, not a
      card or a panel, so it should not borrow rounded-xl. */}
  <div className="w-12 h-12 rounded-lg bg-muted flex items-center justify-center mb-4">
    <FolderOpen className="w-6 h-6 text-muted-foreground" />
  </div>
  <h3 className="font-semibold text-foreground mb-1">No projects yet</h3>
  <p className="text-sm text-muted-foreground mb-6 max-w-xs">
    Create your first project to start tracking work and collaborating with your team.
  </p>
  <Button>Create a project</Button>
</div>
```

---

## Visual Patterns That Work

Patterns that consistently produce warm, trustworthy, non-generic output:

- **Headline + subhead + CTA** as the section structure, with an optional sentence-case eyebrow used sparingly. Used consistently, this creates a readable rhythm without monotony.
- **Background color alternation** between sections: `bg-background` → `bg-muted/30` → `bg-background` → `bg-primary` (for a CTA band). This avoids the all-white or all-gradient page.
- **One brand-color CTA section** per page — usually the last conversion point. Full-width band with the brand primary color as background, white text, and one focused action.
- **Split-screen auth** with a real image or brand gradient on the left side. Significantly more trustworthy than a centered card on a plain background.
- **Logo grid in grayscale** placed immediately after the hero — signals that real companies use the product.
- **Feature + screenshot alternating layout** — text on the left, screenshot on the right, then text on the right, screenshot on the left. Creates editorial rhythm and shows the product without feeling like a slideshow.
- **Soft card hover** — `hover:shadow-md transition-shadow duration-200` on feature cards and pricing tiers. Signals interactivity without being loud.
- **Sticky CTA on mobile** — a fixed bottom bar on mobile with the primary action visible at all times on marketing pages.
- **Progress bar in onboarding** — reduces drop-off by showing how close the user is to being done.

---

## Source-Mining Checklist

When reading a client repo before a design pass, inspect:

- `package.json` — which form library, motion library, image handler, and font setup are in use.
- `app/layout.tsx` and `app/globals.css` or `app/global.css` — font loading, CSS variable tokens, baseline styles.
- `components/ui/*` — existing shadcn primitives, their radius, their variant names.
- `app/page.tsx` or `app/(marketing)/page.tsx` — current marketing page structure.
- `app/(auth)/` or `app/login/` — existing auth surface.
- `app/(app)/dashboard/` or `app/(dashboard)/` — app shell and dashboard layout.
- Existing `Button`, `Card`, `Input`, `Form`, `Dialog`, `Skeleton`, and `Toast` implementations — understand their current radius, shadow, and variant style before proposing anything.
- Color tokens in `globals.css` — are there already semantic tokens? Use them. Do not add a parallel system.
- Any existing hero images or brand photography in `public/` — use them before proposing generic alternatives.
- Existing empty states, loading states, and error pages — improve them before creating new ones.

---

## Quality Bar

A component or page pass should leave behind:

- real, specific copy — no placeholder patterns, no "lorem ipsum", no "Powerful and seamless" filler
- semantic color tokens used throughout — no raw hex or hardcoded Tailwind color names
- proper form labels visible at all times — no placeholder-only fields
- loading, empty, error, and success states for every surface touched
- responsive layout from 320px to 1440px with no clipped text or broken controls
- trust signals near friction points — not only at the page bottom
- background images with tested overlay contrast — not assumed readable
- verification through lint/typecheck/build and browser inspection as a first-time user
