# Motion and Icons Reference

Use this reference before adding animation, transitions, loaders, hover effects, page reveals, celebration states, or choosing an icon and illustration style for a client-facing or consumer product.

---

## Motion Philosophy

The goal of motion in a client product is not to impress — it is to guide, confirm, and occasionally delight. Motion should make the product feel alive and responsive, not like a marketing template playing itself out on every scroll.

Three tests before adding any animation:

1. **Does it help the user understand something?** (a transition that shows where content came from, a skeleton that shows what is loading)
2. **Does it confirm that an action worked?** (a button that pulses on success, a checkmark that appears after saving)
3. **Does it create an appropriate moment of delight?** (onboarding completion, first project created, first payment received)

If the answer to all three is no — the animation is decoration. Remove it.

### What "Warm but Not Noisy" Means

- Warm: transitions that ease out gently, hover states that have soft lift, success states that feel like a small reward.
- Not noisy: not every card fading in on scroll, not every section playing an entrance animation, not hover effects that move things around and shift the layout.
- The rule: **one intentional animation per viewport, not one per element.** When everything moves, nothing has emphasis.

---

## Motion Anti-Patterns — What to Never Do

These are the patterns that make a client app feel like a template, not a product:

- **Stagger reveals that are too slow.** Six cards fading in with 150ms delay each means the last card takes 900ms to appear. The user is waiting for content. Keep stagger delay under 60ms per item.
- **Text that types itself on every page load.** Typewriter effects on headings are overused and slow to read. Use them only for a very specific brand purpose, never as the default hero treatment.
- **Scroll-triggered animations above the fold.** The hero should be fully visible and readable immediately. No fade-in, no slide-up on the headline — the user should not have to wait to read the most important content on the page.
- **Hover effects that shift the layout.** A card that grows on hover and pushes adjacent cards is disorienting. On cards, use shadow and border changes instead of scale — see "Hover and Micro-Interaction States" below. If a scale is genuinely needed on a non-card element, keep it under 1.02 and never let it cause reflow.
- **Background gradients that animate constantly.** A slowly rotating gradient background playing on every page at all times adds visual noise. Reserve animated backgrounds for the hero, one CTA section, or the auth page — not the full app.
- **Loading spinners on every micro-interaction.** Saving a form field should not show a spinner. Use an inline confirmation ("Saved") or a checkmark animation instead. Reserve spinners for operations that take more than 500ms.
- **Animations that replay on every visit.** Onboarding celebration, success screens, and welcome animations should play once. If the user navigates away and back, the animation should not replay.
- **Page entrance animations in the app shell.** The app interior (dashboard, settings, detail pages) should feel instant. Route transitions between app pages should use no animation or a very brief cross-fade (120ms). Save entrance motion for marketing pages.

---

## Timing Defaults

Start with these values and tune by feel. When in doubt, go shorter — users perceive responsive as faster, not slower.

- **Hover states** (button, card, link): 150-200ms ease-out.
- **Button press feedback**: 80-120ms ease-in-out.
- **Tooltip and small popover entrance**: 140-180ms ease-out.
- **Dropdown and select menu**: 150-200ms ease-out.
- **Dialog entrance**: 200-260ms ease-out (scale from 95% + fade).
- **Drawer entrance**: 260-320ms ease-out (slide from edge).
- **Page section scroll reveal** (marketing only): 400-600ms ease-out, with a small Y translate (20-30px), not 100px.
- **Route transitions** (marketing pages): 200-300ms cross-fade or fade-through.
- **Route transitions** (app pages): 0-120ms. App interiors should feel instant.
- **Success checkmark animation**: 400-600ms. It is a moment, not a show.
- **Celebration/confetti** (onboarding completion, first payment): 1.5-3s, then fade out. Never loop.
- **Skeleton pulse**: 1.5s ease-in-out loop, low amplitude. Not a fast flash.
- **Toast entrance/exit**: 200ms ease-out in, 160ms ease-in out.

Always respect `prefers-reduced-motion`. Provide static alternatives for all motion. In CSS:

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

In Framer Motion, use the `useReducedMotion()` hook to disable or simplify animations.

---

## Page and Route Transitions

### Marketing Pages

- Route transitions between marketing pages (home → pricing → about) should feel smooth and confident — a cross-fade or a brief slide works well.
- Use Next.js View Transitions API when available for page-level transitions. Wrap in a `startViewTransition` check for progressive enhancement.
- Keep the transition under 300ms. Longer transitions on navigation feel sluggish and suggest poor performance.
- The page should be readable and interactive before any entrance animations complete. Never block content visibility with an animation.

### App Shell (SaaS Interior)

- App page transitions should feel instant. No entrance animations between `/dashboard` and `/projects/1`.
- Use a very brief cross-fade (120ms, opacity only) if a transition is needed to prevent jarring content swaps.
- Loading new data within the same page: use skeleton placeholders, not page-level spinners.
- Do not animate the sidebar or navigation shell on route changes — keep it stable.

### Modal and Dialog

```tsx
// Scale + fade — the natural attention-drawing pattern for a focused overlay.
// `animate-in` / `zoom-in-95` / `fade-in-0` require tailwindcss-animate (v3) or
// tw-animate-css (v4). Without the plugin these classes do nothing.
<DialogContent className="animate-in fade-in-0 zoom-in-95 duration-200">
```

### Drawer

```tsx
// Slide from the right edge on desktop.
// `animate-in` / `slide-in-from-right` require tailwindcss-animate (v3) or
// tw-animate-css (v4). Without the plugin these classes do nothing.
<SheetContent className="animate-in slide-in-from-right duration-300">
```

---

## Scroll Reveal Animations (Marketing Pages Only)

Scroll reveals tell the story of the product as the user reads down the page. Used well, they create rhythm. Used poorly, they make the page feel like every other marketing site.

### Rules

- Only use scroll reveals on marketing and landing pages — never in the app shell.
- Do not reveal content above the fold. The hero must be immediately readable.
- Keep the Y translate small: 20-24px maximum. The user should not feel like content is flying in from below.
- Stagger delay: 50-60ms per item in a grid. For 6 cards at 60ms: 0, 60, 120, 180, 240, 300ms. With a 500ms duration the last card finishes at 800ms — that is the ceiling. If a grid has more than 6 items, cap the stagger at 6 steps and let the rest share the final delay, or the bottom of the page will still be animating when the user scrolls to it.
- Trigger the animation when the element is 10-15% visible in the viewport — not when the top of the element just enters the screen.
- Use `once: true` — the animation plays when the element first enters view and does not replay on scroll-back.

### Implementation with Framer Motion

```tsx
// Reusable reveal wrapper
const FadeUp = ({ children, delay = 0 }: { children: React.ReactNode; delay?: number }) => {
  const shouldReduceMotion = useReducedMotion()

  return (
    <motion.div
      initial={shouldReduceMotion ? { opacity: 1 } : { opacity: 0, y: 20 }}
      whileInView={{ opacity: 1, y: 0 }}
      viewport={{ once: true, margin: "-10%" }}
      transition={{ duration: 0.5, delay, ease: "easeOut" }}
    >
      {children}
    </motion.div>
  )
}

// Usage in a feature grid
<div className="grid grid-cols-1 md:grid-cols-3 gap-6">
  {features.map((feature, i) => (
    <FadeUp key={feature.title} delay={i * 0.06}>
      <FeatureCard {...feature} />
    </FadeUp>
  ))}
</div>
```

### Implementation with CSS + Intersection Observer (no Framer Motion)

```css
.reveal {
  opacity: 0;
  transform: translateY(20px);
  transition: opacity 0.5s ease-out, transform 0.5s ease-out;
}
.reveal.visible {
  opacity: 1;
  transform: translateY(0);
}
@media (prefers-reduced-motion: reduce) {
  .reveal { opacity: 1; transform: none; transition: none; }
}
```

---

## Hover and Micro-Interaction States

Hover states on a client product should feel premium — a subtle signal that the element is alive and interactive.

### Cards

- Feature cards: `hover:shadow-md transition-shadow duration-200` — quiet lift.
- Pricing cards: `hover:shadow-md transition-shadow duration-200`. No `-translate-y` either — a tier that lifts on hover makes the row feel unstable while the user is comparing prices. The recommended tier is marked persistently (border + badge), not on hover.
- Testimonial cards: same as feature cards. No lift needed — testimonials are static content.
- Clickable cards (linking to a detail): `hover:border-primary/50 transition-colors duration-200` — border tint to signal interactivity.
- Never use `hover:scale` or `hover:-translate-y` on cards — both shift the layout under the cursor and read as a gimmick.

### Buttons

- Primary button: `hover:bg-primary/90` or `hover:brightness-95` — slight darkening. No scale, no shadow, no glow.
- Secondary/outline button: `hover:bg-muted` — subtle fill.
- Ghost button: `hover:bg-muted/60` — softer fill.
- CTA in hero: a subtle `hover:shadow-md` can reinforce the premium feel alongside the color shift.
- Icon inside button: do not animate the icon independently of the button. Keep icon and label moving together.

### Links

- Body links: `hover:text-primary transition-colors duration-150` — color shift.
- Navigation links: underline or background treatment on hover, matching the active state language.
- External links: show the external link icon (`ExternalLink` from lucide) on hover, or always if the link leaves the product.

### Background Image Sections

- Parallax scrolling on background images: use sparingly, only in hero sections, only 15-25% movement speed (not 1:1). Always disable with `prefers-reduced-motion`.
- Gradient animation (marketing hero): a very slow, low-amplitude movement — 8-12s loop, `ease-in-out`. Keep opacity of the animated element low enough that it reads as texture, not a spotlight.

---

## Onboarding and Celebration Motion

These are the moments where warmth and delight are appropriate. They mark progress and reward the user for completing something meaningful.

### Onboarding Step Transitions

- Transition between steps: a brief slide (new step slides in from the right, old step slides out to the left) or a cross-fade. 240-300ms ease-out.
- The progress bar fill: `transition-all duration-500 ease-out` — a smooth fill that feels like forward momentum.
- Do not animate every label or field on a step — only the step container itself transitions.

### Completion Celebration

Use celebration motion when the user completes a meaningful milestone:

- **Onboarding complete**: a confetti burst using `canvas-confetti` (a lightweight, well-maintained library). Burst on mount, do not loop, fade out after 2-3s. Follow with a success illustration and headline.
- **First item created** (first project, first invoice, first client): a subtle checkmark animation on the empty state before it transitions to the first item.
- **Subscription started**: a dedicated success page — not just a toast. The moment a user pays is a trust moment, not a micro-notification.
- **Task or workflow completed**: a brief, inline checkmark animation. `animate-in zoom-in-95 fade-in-0 duration-300` on a green check icon (requires `tailwindcss-animate` on v3 or `tw-animate-css` on v4), then fade to the completion state.

```tsx
// Confetti on onboarding completion
import confetti from "canvas-confetti"
import { useReducedMotion } from "framer-motion"

const shouldReduceMotion = useReducedMotion()

useEffect(() => {
  if (shouldReduceMotion) return
  confetti({
    particleCount: 80,
    spread: 70,
    origin: { y: 0.6 },
    // Pass the brand color in — read it from a token or prop, do not leave a
    // placeholder string here, or the burst fires with no visible color.
    colors: [brandColor, "#ffffff", "#f0f0f0"],
  })
}, [shouldReduceMotion, brandColor])
```

If Framer Motion is not installed, read the preference directly instead of adding a dependency for it:

```tsx
const shouldReduceMotion =
  typeof window !== "undefined" &&
  window.matchMedia("(prefers-reduced-motion: reduce)").matches
```

---

## Loading and Skeleton Animations

### Skeletons

- Use skeletons that match the shape of the loaded content — same width, same height, and the same radius as the element being replaced.
- Skeleton pulse: `animate-pulse bg-muted`, with the radius of the thing it stands in for: `rounded-md` for a text line, `rounded-lg` for a control, `rounded-xl` for a card or media block.
- Do not use a single wide skeleton block for content that will be a grid — make a skeleton grid that matches the loaded layout.
- Skeleton duration: `animate-pulse` defaults are fine. Do not speed them up — a fast pulse looks anxious.

```tsx
// Skeleton that matches a metric card
<Card className="p-6 rounded-xl">
  {/* Bars stand in for text, so they take a small radius — not the card's. */}
  <div className="h-4 w-24 bg-muted rounded-md animate-pulse mb-3" />
  <div className="h-8 w-32 bg-muted rounded-md animate-pulse mb-2" />
  <div className="h-3 w-20 bg-muted rounded-md animate-pulse" />
</Card>
```

### Button Loading

```tsx
<Button disabled={isLoading}>
  {isLoading ? (
    <>
      <Loader2 className="mr-2 h-4 w-4 animate-spin" />
      Saving...
    </>
  ) : (
    "Save changes"
  )}
</Button>
```

### Page Loading

- Use a thin top progress bar (NProgress-style) for route transitions, not a full-page spinner.
- Full-page spinner only for the initial app load before the shell is ready.
- If a data fetch takes more than 2 seconds, show a message: "Still loading... this is taking longer than usual."

---

## Icon Policy

### Default: Lucide React

Use `lucide-react` as the default icon library for all UI actions and objects. It is clean, consistent, and works well for both technical and consumer products.

Best lucide icons for client apps:
- Navigation and UI: `Menu`, `X`, `ChevronDown`, `ChevronRight`, `ArrowRight`, `ArrowLeft`, `ExternalLink`
- Actions: `Plus`, `Trash2`, `Edit`, `Copy`, `Check`, `Save`, `Send`, `Download`, `Upload`
- Status: `CheckCircle`, `AlertCircle`, `Info`, `AlertTriangle`, `XCircle`
- Objects: `User`, `Users`, `Building2`, `Calendar`, `Clock`, `FileText`, `Folder`, `Mail`, `Phone`, `Globe`
- Product: `LayoutDashboard`, `Settings`, `Bell`, `Search`, `Filter`, `BarChart3`, `TrendingUp`, `CreditCard`, `Lock`

Match `size` (16 or 20px) and `strokeWidth` (1.5 or 2) consistently within each section. Do not mix sizes and weights in the same toolbar or nav.

### When to Use Filled or Duotone Icons

For client apps, filled icon variants can feel warmer and more approachable than outline-only. Consider these alternatives when the product needs a softer, more consumer-friendly feel:

- **Phosphor Icons** (`@phosphor-icons/react`): supports thin, light, regular, bold, fill, and duotone variants. Use the `fill` variant for feature section icons, empty states, and onboarding steps. Use the `regular` variant for UI chrome.
- **Heroicons** (`@heroicons/react`): `solid` variant for more weight and warmth when lucide feels too light.
- **Rule**: pick one icon family per surface. Do not mix lucide outline, phosphor fill, and heroicons solid in the same component.

### Icons to Avoid

- ✨ **Sparkle or magic icons for AI or premium features.** This is exhausted. Describe what the feature does in copy — do not decorate it with sparkles.
- 🤖 **Robot or AI icons as the brand identity of an AI feature.** Same reason.
- Generic "star" or "heart" icons for feature highlights when a more specific icon exists.
- Thin icon weights (`strokeWidth={1}`) in small sizes — they disappear and feel low-quality.
- Mixing lucide and emoji as inline icons in the same product.

### Brand and Logo Icons

- Use `simple-icons` for brand logos (Stripe, Google, GitHub, Slack, etc.).
- Never use lucide for brand logos — lucide does not have brand icons and approximating them looks unprofessional.
- Keep brand icons at a consistent size and use their official brand color or grayscale — never recolor them arbitrarily.

---

## Illustration Policy

Illustrations are the right tool for empty states, onboarding steps, 404 pages, success screens, and feature explainers. They communicate warmth and personality in a way that icons cannot.

### When to Use Illustrations

- Empty state screens where the user has not yet created any content.
- Onboarding step introductions — a small illustration sets the context before a form.
- Success and celebration screens — onboarding complete, subscription started, goal reached.
- 404 and error pages — an illustration makes an error page feel brand-consistent rather than broken.
- Feature explainer sections — when a concept needs a visual metaphor, an illustration can carry it better than a screenshot.

### Illustration Style Rules

- **One style per product.** Do not mix flat vector illustrations, 3D render illustrations, and line-art illustrations on the same product.
- **Match the audience.** If the product serves diverse teams, the illustrations should reflect diversity in characters. If the product serves a specific industry, the illustrations should reflect that context.
- **Customizable color.** Prefer illustration libraries that allow you to change the primary and accent colors to match the brand: Undraw (`https://undraw.co`), Storyset (`https://storyset.com`), Humaaans (`https://humaaans.com`).
- **Keep them purposeful.** An illustration on an empty state earns its place. An illustration purely as section decoration is unnecessary unless it is part of a cohesive product story.
- **Size appropriately.** Empty state illustrations: 120-180px. Onboarding illustrations: 200-280px. Full-screen celebration: up to 400px. Do not scale illustrations so large they become the focus of the page instead of the action.
- **Provide `alt` text.** An illustration that carries meaning — an empty-state graphic that explains what the user can create — needs a short description. A purely decorative illustration that repeats the adjacent heading should use `alt=""` so screen readers skip it rather than hear the same idea twice.

### Free Illustration Sources

- `https://undraw.co`: flat style, fully customizable brand color, MIT-like license. The most versatile choice for SaaS products.
- `https://storyset.com`: flat style with animation options, customizable, free with attribution.
- `https://humaaans.com`: mix-and-match people illustrations, customizable, good for people-centric products.
- `https://www.opendoodles.com`: loose, sketchy, friendly style — good for products with a casual or creative brand personality.

---

## Implementation Notes

- **Prefer CSS transitions for simple hover, reveal, and state changes.** `transition-all`, `transition-shadow`, `transition-colors`, `transition-transform` cover the vast majority of micro-interaction needs without a JS animation library.
- **Use Framer Motion when already installed** for scroll reveals, shared element transitions, layout animations, drag-to-reorder, and orchestrated onboarding sequences.
- **Do not add Framer Motion to a project that does not already use it** just for a hover effect. The CSS `transition` utility is sufficient.
- **Use `canvas-confetti` for celebration bursts.** It is lightweight, battle-tested, and straightforward.
- **Use `lucide-react` as a direct import**, not via a dynamic icon map, to avoid bundling the entire icon set.
- **Avoid animating layout-heavy properties** (`width`, `height`, `padding`, `margin`, `top`, `left`). Animate `transform` and `opacity` only — they run on the GPU and do not cause reflow.
- **Keep animated backgrounds behind content.** Set `pointer-events: none` and appropriate `z-index` on any animated background layer. The UI must remain fully usable if the background animation fails or is disabled.
- **Test motion on a mid-range device**, not just a high-performance development machine. Animations that feel smooth on a MacBook Pro can feel janky on an older Android device.

---

## Acceptance Checklist

A motion and icon pass is complete when:

- every animation has a clear purpose — guide, confirm, or celebrate
- no animation replays unnecessarily on subsequent visits
- stagger delays keep the full reveal under ~800ms for any grid, with the stagger capped at 6 steps
- scroll reveal animations are absent above the fold
- hover effects do not cause layout shift
- loading skeletons match the shape of the loaded content
- celebration motion is present on meaningful milestones (onboarding, payment, first item)
- all animations respect `prefers-reduced-motion` with a static fallback
- one icon family is used consistently per surface with matched size and stroke weight
- sparkle, magic, robot, and AI-cliché icons are absent
- illustrations (if used) follow one style with customized brand colors
- motion was verified in a browser at 60fps on desktop and simulated mobile
