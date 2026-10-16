---
name: ai-ui-tells
description: Use when building, reviewing, or polishing any web or app UI (landing page, pricing page, dashboard, settings screen, component) and especially when the request is vague, such as "make it better", "make it look professional", "make it look less AI", or "make it look less generic". Detects the visual tells that make an interface look machine-generated and replaces each one with a specific, measurable design decision.
---

# AI UI tells

A vague request like "make it better" tends to produce more of the same: another gradient, another shadow, another row of icon cards. This skill gives you a senior product designer's review pass instead. Each tell below has a rule you can check in the code, the reason an experienced designer notices it, and a replacement with concrete values.

This is not a ban list. Every pattern here is fine when it is a deliberate choice that serves the content. The problem is the default: the pattern appears because nothing else was decided. When you keep one, you should be able to say why in one sentence.

## How to use this skill

1. Before writing UI, set the system decisions in "Set the system first" below. Most tells disappear when these exist.
2. Build the screen.
3. Run the detection rules against your own output (read the CSS, classes, and markup, or computed styles if you can render).
4. Apply the replacements for any tell that fires.
5. Finish with the self-audit checklist at the end and report the counts.

If the project already has a design system or brand guide, it wins. Use this skill to find where the output drifted away from it into defaults.

## Set the system first

Write these down (as CSS variables or design tokens) before building:

- **One brand color.** A single hue with 2 to 3 tonal steps (base, hover/darker, tint for backgrounds). Everything else is neutral.
- **A neutral ramp.** 5 to 7 grays from the same family (slightly warm or slightly cool, not mixed). Page background, subtle surface, border, muted text, body text, heading text.
- **Type scale.** At most 6 font sizes on a screen. Example for marketing pages: 14, 16, 20, 28, 40, 56 px. Example for app screens: 12, 14, 16, 20, 28 px.
- **Spacing scale.** A 4 or 8 px base, at most 8 distinct values in use. Example: 4, 8, 12, 16, 24, 32, 48, 80 px.
- **Radii.** At most 2 values plus 0 (and full-round only for avatars or toggles). Example: 6 px for inputs and buttons, 12 px for containers.
- **Elevation.** Default is none. Separate surfaces with a 1 px border or a tonal background step. Reserve a shadow for things that truly float above the page (menus, popovers, modals, a sticky bar).

## The tells

### 1. Purple/blue hero gradient

- **Detect:** a `linear-gradient` or `radial-gradient` on a large area (hero, page background, primary button, heading text) where the stops fall in the blue to violet range (roughly hue 220 to 290), for example indigo to purple, or blue to pink via violet. Also `bg-clip-text` gradient headings.
- **Why it is flagged:** it has become the default look of generated landing pages, so it signals "no brand decision was made". It also lowers text contrast across part of the area and competes with the actual product imagery.
- **Replace with:** a flat background from the neutral ramp (for example `#FAFAF9` or `#0B0B0C`) and the one brand color used only where it carries meaning: the primary action, one key highlight, links. If the brand needs atmosphere, use a real product screenshot, photograph, or a single tonal block in a 6 to 10 percent tint of the brand color. Solid text color for headings.

### 2. Three equal icon feature cards

- **Detect:** a grid of 3 (or 4, or 6) sibling cards with identical size, each with an icon in a tinted circle or square, a short bold title, and 1 to 2 lines of text. Typical markup: `grid-cols-3` with the same component repeated.
- **Why it is flagged:** equal weight says every feature matters the same, which is never true. Readers cannot tell what the product is actually best at, and the icons rarely add information the title does not.
- **Replace with:** rank the features. Give the most important one a larger cell (for example a 2:1 column split, or a full-width row with a real screenshot) and list the rest as compact rows of title plus one line, no icon boxes. A 7/5 or 8/4 column split, or one large item followed by a 2-column list, works well. Show product evidence (UI crop, number, quote) instead of decorative icons.

### 3. Shadow on everything

- **Detect:** count elements with a non-`none` `box-shadow`. If cards, buttons, inputs, sections, and badges all have one, or more than 2 resting (non-hover, non-overlay) elements per screen have one, it fires. Large soft shadows like `0 20px 50px rgba(...)` and colored shadows are strong signals.
- **Why it is flagged:** shadow means "this floats above the page". When everything floats, nothing does, depth stops carrying information, and the page looks muddy.
- **Replace with:** `border: 1px solid` the border gray (for example `#E7E5E4` on light, `#27272A` on dark), or a tonal step in background (page `#FAFAF9`, card `#FFFFFF`). Keep shadow only for overlays: menus, popovers, modals, toasts. Target: 0 resting shadows; at most 1 if a single element genuinely sits above the page.

### 4. Pill badges everywhere

- **Detect:** small inline labels with full-round radius (`rounded-full`, `border-radius: 9999px`) and tinted backgrounds: "New", "LIVE", "Beta", "Most popular", "AI-powered", announcement chips above the hero. It fires at more than 1 per screen, or any badge that does not carry state.
- **Why it is flagged:** badges are for status. Used as decoration they add noise and train the eye to ignore them, so the one that matters (an error, a plan state) gets missed.
- **Replace with:** plain text in the muted gray or the brand color, for example a small uppercase eyebrow label (12 to 13 px, `letter-spacing: 0.04em`, weight 600) with no background. Keep a badge only for real state (Active, Overdue, Draft), and give it the same small radius as buttons, not full-round.

### 5. Emoji bullets and emoji icons

- **Detect:** emoji characters (for example rocket, sparkles, lightning, check mark, fire) at the start of list items, headings, buttons, or used as feature icons.
- **Why it is flagged:** emoji render differently on each platform, do not match the type, and read as filler. They are among the most recognized signs of generated copy and UI.
- **Replace with:** no marker at all with good spacing, a simple 1.5 px stroke icon from one consistent set at the text color, or a short muted label. For checklists use a single SVG check in the brand color. Target: 0 emoji in UI chrome.

### 6. One radius everywhere

- **Detect:** collect every `border-radius` value. It fires when one large value (often 16 to 24 px) is applied to everything from buttons to page sections, or when there are more than 3 distinct non-zero values with no logic.
- **Why it is flagged:** radius should scale with element size and role. A 24 px radius on a 36 px button turns it into a blob; the same radius on a large section looks bubbly. Uniform large radii are a template default.
- **Replace with:** at most 2 radii plus 0. Small (4 to 8 px) for controls: buttons, inputs, badges, chips. Larger (10 to 14 px) for containers: cards, panels, images. Page sections and full-bleed bands get 0. Nested elements use a radius equal to or smaller than the parent minus its padding.

### 7. Centered hero with two buttons

- **Detect:** a hero where everything is center-aligned (eyebrow badge, headline, subhead, then a primary button and a secondary "Learn more" or "Watch demo" button side by side), with nothing visual beside or below it except perhaps a floating mockup.
- **Why it is flagged:** it is the most common generated layout, it puts two competing actions in the most valuable spot, and centered multi-line text is harder to read than left-aligned text.
- **Replace with:** left-aligned headline and subhead (measure 45 to 65 characters for body copy), one primary action, and the secondary path as a text link. Put real product proof (screenshot, number, short customer quote) in the same viewport, beside the copy on desktop (for example a 5/7 split) or directly below. Centered is fine for very short single-statement pages; then still use one button.

### 8. Glassmorphism

- **Detect:** `backdrop-filter: blur(...)` together with semi-transparent white or black backgrounds (`bg-white/10`, `rgba(255,255,255,0.1)`) and thin light borders, on cards or panels that do not sit over moving or image content.
- **Why it is flagged:** frosted glass only reads when there is something interesting behind it. Over a flat gradient it is just low contrast. It also costs rendering performance and often fails WCAG contrast for text.
- **Replace with:** an opaque surface from the neutral ramp with a 1 px border. Keep blur only on a sticky header or overlay that actually scrolls over content, with at least 85 percent opacity so text passes 4.5:1 contrast.

### 9. Flat hierarchy

- **Detect:** compute the H1 font size divided by body font size. It fires below 2.0 on marketing pages and below 1.6 on app screens. It also fires when more than about 3 text styles share the same weight (for example everything 500 or 600), when every section heading is the same size as card titles, or when there is no single element that is clearly the first thing to look at.
- **Why it is flagged:** if everything is equally loud, readers scan instead of read, and the main message or main action is lost. Hierarchy is the core of a designer's job, so its absence is very visible.
- **Replace with:** H1 at least 2x body on marketing pages (for example 16 px body, 40 to 56 px H1) and at least 1.6x on app screens (14 px body, 24 to 28 px title). Use at most 2 to 3 weights (400 body, 500 or 600 labels, 600 or 700 headings). Use muted color (for example `#57534E`) for secondary text instead of smaller size alone. One focal element per screen: one H1, one primary filled button in the viewport, the key number or screenshot clearly larger than its neighbors.

### Smaller tells to check in the same pass

- **Generic copy:** "Unlock the power of", "Supercharge your workflow", "Seamless", "Elevate". Replace with what the product does, with a number if one is real. Never invent metrics, customers, or quotes; use clearly marked placeholders instead.
- **Fake social proof strip:** a row of gray placeholder logos with no real names. Remove it or mark it as a placeholder.
- **Same section rhythm:** every section is heading, subhead, 3-column grid, with identical vertical padding. Vary layout by content and keep padding on the spacing scale (for example 80 px between major sections, 32 to 48 px inside).
- **Over-wide text:** paragraphs spanning the full container. Cap body copy at about 65ch.

## Self-audit checklist

Run this on the finished output and report the numbers. Targets are for a single screen or page.

| Check | How to count | Target |
|---|---|---|
| Blue/purple gradients on large areas or text | count gradients with stops in hue 220 to 290 | 0 |
| Equal-size icon card grids | count grids of 3+ identical cards with icon boxes | 0 |
| Resting shadows | elements with box-shadow, excluding overlays and hover | 0 to 1 |
| Decorative pill badges | full-round tinted labels that do not show state | 0 |
| Emoji in UI | emoji characters in headings, buttons, lists, icons | 0 |
| Distinct non-zero radii | unique border-radius values (ignoring full-round avatars/toggles) | 2 or fewer |
| Hero primary buttons | filled buttons in the hero | 1 |
| Glass surfaces | elements with backdrop-filter not over scrolling content | 0 |
| H1 to body ratio | H1 px / body px | 2.0+ marketing, 1.6+ app |
| Distinct font sizes | unique font-size values | 6 or fewer |
| Distinct font weights | unique font-weight values | 3 or fewer |
| Distinct spacing values | unique margin/padding/gap values | 8 or fewer |
| Brand hues | distinct saturated hues (excluding semantic red/green/amber for status) | 1 |
| Focal element | can you name the one thing the eye lands on first? | yes |

If any target is missed, either fix it or state the deliberate reason in one sentence. Do not report the checklist as passed without counting.
