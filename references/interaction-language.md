# Interaction Language

Use this reference before changing how a client-facing or consumer-facing UI behaves. The goal is to make every interaction feel clear, safe, and human — so a non-technical user never feels lost, never feels tricked, and always knows what will happen before they click.

---

## Interaction Principles

These principles govern every decision in this skill:

- **The next action must always be obvious.** A non-technical user should never have to look for what to do. The primary action is visually dominant. Everything else is secondary.
- **Tell the user what will happen before they click.** CTA copy must name both the action and the outcome. "Save and continue" is better than "Next". "Start your free 14-day trial" is better than "Get started".
- **Never make the user feel they made a mistake.** Errors, empty states, and loading states should feel like the product communicating — not like failures. The language is calm, specific, and solution-oriented.
- **Confirm before anything that cannot be undone.** Destructive or costly actions must require a second step. Never trigger an irreversible action on a single click.
- **Feedback must happen near where the action happened.** A success message at the top of the page when the user just submitted a form at the bottom is easy to miss. Confirm near the action.
- **Keep controls stable while content loads.** Do not move the primary CTA because a loading state shifted the layout. Do not hide the navigation while content is fetching.
- **Mobile is not a reduced experience — it is a different one.** Primary actions on mobile must be reachable with a thumb. Navigation must not bury the most-used routes. Forms must be one column.
- **Consistency builds trust.** The same interaction must look and behave the same way everywhere in the product. Buttons with the same appearance must do the same type of thing.

---

## Navigation

Navigation tells the user where they are and where they can go. For non-technical users, it must be instantly readable with no learning curve.

### Marketing Navigation

- Keep the primary nav to 4-6 items maximum. Every item should be a noun a non-technical user would search for: "Pricing", "Features", "About", "Blog", "Sign in".
- The sign-in and primary CTA button must always be visible in the nav — never hidden behind a hamburger on desktop.
- Active route: use a visual marker beyond color — an underline, background, or font weight change that communicates "you are here" to a user who does not read URL bars.
- Sticky header: use a sticky nav on marketing pages. As the user scrolls, the CTA in the nav becomes more valuable — do not hide it.
- Mobile: use a full-screen drawer or a simple stacked list — not a mega menu. Show only the 4-5 most important items. The CTA button must be large and near the top of the mobile menu.
- Scroll behavior: when the user scrolls down on a marketing page, the nav can reduce in height (`py-3` instead of `py-5`) but must not disappear completely.

### App Navigation (SaaS Shell)

- Left sidebar: 5-7 primary navigation items. Labels must use plain language — the words the user themselves would use, not system architecture terms.
- Group secondary items: settings, billing, help, and profile belong at the bottom of the sidebar or in a separate profile menu — not mixed with primary navigation.
- Active route: bold font weight + brand accent left border or background. The user must instantly see where they are.
- Sidebar on mobile: use a bottom tab bar for the 4-5 most used items. Reserve the hamburger/drawer for secondary items. Never put the primary workflow behind a hamburger on mobile.
- Breadcrumbs: use breadcrumbs for apps with nested views — especially when the user can navigate several levels deep. Keep them small and de-emphasized (muted text, small size).
- Help and support: always accessible from the sidebar or top bar. A non-technical user must be able to find help without leaving their current context.

---

## CTAs and Primary Actions

The CTA is where the user's decision becomes an action. Every CTA must be treated with care.

### CTA Copy Rules

- Name the action and the outcome, not just the action: "Start free trial" not "Submit". "Book a demo" not "Contact us". "Download the report" not "Download".
- Use the user's language, not the system's language. The button that creates a new project should say "Create project" — not "Initialize entity" or "New record".
- Avoid vague verbs: "Get started", "Learn more", "Click here", "Continue" with no context are placeholders. Replace them with specific language about what happens next.
- Urgency is fine when it is real. "Offer ends Friday" is fine if it is true. "Limited time only" with no end date is a trust violation.

### CTA Hierarchy

- One primary CTA per viewport. If two equally weighted CTAs compete, the user does nothing.
- The primary CTA is the largest, most contrast-rich button on the section. It uses the brand accent color at full saturation.
- The secondary CTA is visually quieter: `variant="outline"` or `variant="ghost"`. It should not compete with the primary.
- Tertiary actions (e.g., "Learn more", "See all features") are text links or ghost buttons — never the same size as the primary.
- Do not place two primary (solid accent) buttons next to each other. One of them is secondary — style it accordingly.

### Micro-Copy Near CTAs

- Trust lines directly below a CTA reduce hesitation: "No credit card required", "Cancel anytime", "14-day free trial, then $29/month", "Free forever for small teams".
- Security language near payment CTAs: "Secured by Stripe", "256-bit encryption", "SOC 2 certified". Place it immediately below the payment button, not at the bottom of the page.
- These lines should be small (`text-xs`), muted (`text-muted-foreground`), and not compete with the CTA itself.

### Button Loading States

- When a form submits or an action is in progress, disable the button immediately and show a loading state. This prevents duplicate submission — a critical issue on payment and account creation forms.
- Preserve the button width during loading. Do not collapse the button to fit a spinner. Keep the original dimensions and replace the label with a spinner + action-in-progress text ("Saving...", "Creating your account...", "Processing payment...").
- Never just show a spinner with no text on a CTA. The user needs to know what is happening.

---

## Forms and Input

Forms are where non-technical users most often feel confused, judged, or stuck. Every form decision must reduce that friction.

### Form Structure

- Always use a visible label above every input. Placeholder text disappears when the user starts typing — it cannot be the label.
- Group related fields with a visual section heading or increased gap. Separate optional and advanced fields with an accordion or a secondary section.
- One column on mobile, always. Two-column form layouts break on mobile and create scanning confusion on desktop for most non-technical users.
- Keep forms short. If more than five fields are needed, split them into steps. The user should never feel like they are filling out a tax form to sign up for a product.
- Required fields: mark optional fields as "(optional)" rather than marking required fields with an asterisk — most non-technical users do not know what the asterisk means.

### Input States

- Default: `border border-input bg-background` — neutral, not calling attention.
- Focus: `focus-visible:ring-2 focus-visible:ring-primary` — clear, brand-colored focus ring. Never rely on the browser default blue outline. Add `ring-offset-2` when the input sits on a tinted or image background, so the ring does not merge into it.
- Error: `border-destructive` with an error message directly below the field. The message must be in plain language and tell the user exactly what to fix: "Please enter a valid email address" not "Invalid format". "Password must be at least 8 characters" not "Weak password".
- Success/valid: a subtle green indicator or checkmark when the field is correctly filled — optional, but useful for password strength and email validation.
- Disabled: visually muted, with a tooltip or nearby explanation of why it is disabled and what the user can do to enable it.

### Validation Timing

- Validate on blur (when the user leaves a field), not on every keystroke. Showing "Invalid email" while the user is still typing is aggressive and discourages them.
- Exception: password strength can show progressive feedback on input — but frame it as help ("Your password needs a number") not as an error.
- On submit: validate all fields, scroll to the first error, focus the first errored field, and show a summary if there are multiple errors.
- Prevent duplicate form submission. Disable the submit button immediately on the first click.

### Select, Combobox, and Date Inputs

- Use native `<select>` only for very short, closed lists (fewer than 6 options). For longer lists, use a searchable combobox.
- Date inputs: use a calendar popover with quick presets ("Today", "Last 7 days", "This month") for filter contexts. Use a simple date input field for single date entry.
- Phone number inputs: format automatically and show the country code selector when international numbers are possible.

---

## Multi-Step Flows and Onboarding

Multi-step flows are where non-technical users are most likely to abandon if they feel lost or overwhelmed.

### Progress Communication

- Always show where the user is: a step counter ("Step 2 of 4"), a progress bar, or a visual step indicator at the top of the flow.
- Show what comes next: the step counter tells the user how much is left. Consider showing upcoming step names ("Next: Connect your calendar").
- Never show more steps than expected. If a flow was advertised as "3 steps" and the user reaches step 4, it feels like a betrayal.

### Step Design

- One decision or task per step. If a step has two unrelated questions, split it.
- The step headline must state clearly what this step is for: "Tell us about your team" not "Step 2".
- The description should explain why the information is needed when it is not obvious: "We'll use this to personalize your dashboard" or "This helps us set up your billing correctly".
- Skip: allow skipping optional steps. Label them as optional before the user reaches them, not only on the step itself.
- Back: always allow going back. Never lock a step once the user has moved forward — they may need to correct something.

### Completion State

- The final step or completion screen must feel like an arrival, not an end.
- Show a summary of what was set up: "Your account is ready. Here's what we've configured for you."
- Offer one clear CTA into the actual product: "Go to your dashboard", "Start your first project", "Invite your team".
- A small, appropriate celebration (a checkmark animation, a friendly illustration, a congratulations message) is welcome here — this is the right place for warmth and delight, not in the middle of a form.

---

## Loading, Empty, Error, and Success States

These states reveal the quality of the product to a non-technical user. Generic states feel like bugs. Specific states feel like the product is alive and communicating.

### Loading States

- Preserve layout during loading. Show skeletons that match the shape of the loaded content — not a spinner floating in a blank white space.
- Skeletons: use `animate-pulse` on placeholder shapes that match the width and height of the actual content, with the radius of the thing they stand in for — `rounded-md` for a text line, `rounded-lg` for a control, `rounded-xl` for a card or media block — and `bg-muted` as the fill.
- Loading buttons: preserve button dimensions, disable the button, show spinner + in-progress label.
- Page-level loading: use a thin progress bar at the top of the page (like NProgress) for route transitions. Full-page spinner for initial app load only.
- Never show a loading state for longer than 10 seconds without explaining what is happening and offering a retry or a way out.

### Empty States

Every empty state must answer three questions: what is missing, why it is empty, and what the user can do next.

- **Bad**: "No data found." (What data? Why? What do I do?)
- **Good**: "You have no active projects yet. Create your first project to start tracking work and collaborating with your team." + "Create a project" button.

Structure:
- Icon or illustration that represents the missing content (not a generic warning icon)
- Heading: name what is missing ("No projects yet", "No invoices sent", "Your inbox is empty")
- Body: one sentence explaining why and what it means
- CTA: one specific action that resolves the emptiness

For search empty states: "No results for '[query]'. Try a different search term or browse all [category]."

### Error States

Error messages must be in the user's language, not the system's.

- **Bad**: "Error 403: Unauthorized access." / "Unhandled exception occurred." / "Invalid credentials."
- **Good**: "You don't have permission to view this page. Contact your team admin to request access." / "The email or password you entered is incorrect. Try again or reset your password."

Structure:
- What failed: name the specific thing that did not work, not just "An error occurred."
- Why it failed: explain the reason when it is known and user-actionable.
- What to do next: a specific recovery action — "Try again", "Reset your password", "Contact support", "Go back to [page]".

Error placement:
- Form field errors: directly below the field, `text-destructive text-sm`.
- Form-level errors (server errors): above the submit button in a visible callout, not a toast.
- Page-level errors: a full empty-state treatment with a retry button.
- Toast: use for non-critical errors only ("Failed to save draft — your changes are still here. Try again?").

### Success States

- Confirm near the action, not at the top of the page.
- For form submission: replace the form with a success message, or show a success state inline below the button.
- For completed tasks: use a toast for minor confirmations ("Invoice sent"), an inline state for form submissions, and a full celebration screen for significant milestones (account created, subscription started, project completed).
- Never just disappear — the user must know that the action worked.
- Avoid success toasts for critical actions like payment. Use a dedicated confirmation page or screen.

---

## Trust-Building Interactions

These interactions exist specifically to reduce the anxiety a non-technical user feels before committing to a product.

### Pre-Click Reassurance

- Show trust lines near CTAs before the user clicks: "No credit card required", "Cancel anytime", "14-day free trial".
- On payment forms: show the total, billing period, and cancellation policy before asking for card details.
- Security indicators near sensitive inputs: a lock icon or "Secured by Stripe" text near the card number field.

### Hover States on Pricing and CTAs

- Pricing card hover: `shadow-md` or a border color shift, with `transition-shadow duration-200`. Do not scale or lift cards on hover — it shifts the layout under the cursor and reads as a gimmick, especially while the user is comparing prices. The recommended tier is distinguished by a persistent brand-color border and a "Most popular" badge, not by pulsing, glowing, or extra elevation.
- CTA button hover: darken the background by 8-10%, not a dramatic color change. Keep the text the same.
- Logo grid hover: individual logos can lift to full opacity from a grayscale state — this is a subtle trust signal that the brands are real.

### Confirmation Dialogs for Destructive Actions

- Never delete, cancel, or remove on a single click. Always show a confirmation dialog.
- The dialog must name the specific thing being deleted and the specific consequences: "Delete 'Q4 Report' project? This will permanently remove all tasks, files, and comments in this project. This cannot be undone."
- The confirm button must use destructive styling and name the action explicitly: "Delete project" not "Yes" or "Confirm".
- The cancel button is the default focus — pressing Enter should cancel, not confirm, a destructive action.
- For high-stakes actions (account deletion, subscription cancellation): require the user to type a confirmation phrase before the button enables.

---

## Dialogs, Drawers, and Toasts

### Dialogs

- Use for: focused tasks (create, edit, delete confirm), payment steps, or critical notices.
- Keep content task-focused. A dialog is not a landing page. If the dialog needs more than a form or a paragraph of text, consider a drawer or a dedicated page.
- Trap focus inside the dialog when it is open. Restore focus to the trigger when it closes.
- Close on escape. Close on overlay click for informational dialogs. For forms with unsaved changes, confirm before closing.
- Footer: "Cancel" (secondary) on the left, primary action on the right. Destructive actions use `variant="destructive"`.
- Do not make dialogs too wide or too tall. `max-w-md` or `max-w-lg` for most dialogs. `max-h-[80vh]` with internal scroll for long content.

### Drawers

- Use for: detail panels, inspector views, side-by-side context, or multi-field forms that are too heavy for a dialog.
- Drawers open from the right on desktop, from the bottom on mobile.
- Always include a visible close button (X in the top corner) in addition to escape/overlay close.
- For forms in drawers: show the save and cancel actions in a sticky footer at the bottom of the drawer, not at the top.

### Toasts

- Use for: brief, nonblocking confirmations and low-priority errors.
- Never use a toast as the only feedback for a critical action (payment, account creation, file deletion). These need inline or page-level confirmation.
- Keep toast messages to one sentence: "Invoice sent to client@company.com" not a paragraph.
- Toast duration: 4-5 seconds for success, 6-8 seconds for errors (the user may need to read and act). Always include a manual dismiss.
- Position: bottom-right on desktop, bottom-center on mobile.

---

## Mobile Touch Behavior

Client-facing apps are frequently used on phones. Mobile is not a fallback — it is a primary surface.

### Touch Targets

- Minimum 44x44px for all interactive elements: buttons, links, checkboxes, radio buttons, switches, icons that are clickable.
- Increase padding, not the visible size, when an element looks right but is too small to tap reliably: `px-4 py-3` on small buttons gives enough touch area without changing the visual appearance.
- Do not place two tappable elements closer than 8px apart. Accidental taps on the wrong element break trust.

### Mobile Layout Rules

- Forms: always one column. Never two-column form layouts on mobile.
- Navigation: bottom tab bar for primary routes. Hamburger drawer for secondary routes. The user's most common action must be one thumb-tap away.
- Tables: on mobile, transform wide tables into card-list views. Never allow horizontal scroll on the page level — only inside a clearly bounded container.
- Modals: use `bottom-sheet` behavior on mobile (a drawer from the bottom) instead of a centered modal. Centered modals with a dark overlay feel heavy on small screens.
- Text inputs: ensure inputs do not zoom the page on focus on iOS. Set `font-size: 16px` minimum on inputs — iOS zooms in when the font size is smaller.
- Touch gestures: swipe to dismiss is a native pattern for bottom sheets and notifications. Implement it when the motion library supports it, with a `prefers-reduced-motion` fallback.

---

## Accessibility for Real Users

Accessibility is not a compliance checklist — it is about making the product work for everyone, including users who use keyboard navigation, screen readers, low-vision settings, or slow internet connections.

- **Contrast**: WCAG AA minimum for all text. 4.5:1 for body text, 3:1 for large text (18px+ or 14px bold+). Test text over background images specifically — do not assume the overlay is enough.
- **Focus visible**: every interactive element must have a clear `focus-visible` ring using the brand accent color. Never `outline: none` without a custom focus style.
- **Color alone**: never use color as the only signal for state. Status badges must include text. Error fields must include an error message, not just a red border. Form validation must not rely solely on red/green color.
- **Alt text**: real, descriptive alt text for all informative images. `alt=""` for genuinely decorative images. Never `alt="image"` or `alt="photo"`.
- **Form labels**: every input has an associated visible label using `<label htmlFor="...">`. Do not use `aria-label` as a substitute for a visible label on user-facing forms.
- **Error announcements**: use `aria-live="polite"` on error message regions so screen readers announce them when they appear.
- **Keyboard flows**: all navigation, forms, dialogs, and dropdowns must be fully operable with keyboard alone. Tab order must follow the visual reading order.
- **Motion**: always implement `prefers-reduced-motion` for any animation that is not essential to understanding state. Static alternatives must be visually complete, not just the animation removed.

---

## Acceptance Checklist

An interaction pass is complete when:

- the primary action is visible and its copy names both the action and the outcome
- trust micro-copy appears near every CTA and payment step
- form labels are visible at all times — not placeholder-only
- validation errors appear near the field in plain, human language
- loading states preserve layout and show what is happening
- empty states name the missing thing and offer a next action
- error states explain what failed and what to do next
- success states confirm near where the action happened
- destructive actions require a confirmation dialog with explicit consequences
- all touch targets are at least 44x44px
- mobile layouts reflow correctly with no horizontal overflow
- focus-visible states are clear on every interactive element
- contrast passes WCAG AA for all text, including text over images
- the flow was walked through in a browser on both desktop and a mobile viewport
