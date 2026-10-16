---
name: ai-ui-tells
description: Use this skill whenever you build, review, restyle, or polish a web or app interface (landing page, pricing page, dashboard, settings screen, or component), including when the user only says it looks generic, looks AI-made, looks like a template, should feel less AI, or asks to make it better or more professional. It makes you commit to a named art direction before any markup, replace generated-interface defaults (including the looks people pick to escape those defaults), and check a rendered screenshot. Not for backend, data, or copy tasks that have no interface.
---

# AI UI tells

Removing the usual tells lands on the next default: cream paper, a serif, a clay button. This skill makes you commit to one named world, then build only that. If the user already named a style, follow it exactly, even if it is listed below. Pages under `eval/` are past measurements, not templates. Do not copy them.

## Pass 1. Plan before markup

From this folder, run:

```sh
python3 draw.py "Product name" landing
```

The second argument is the surface: `landing`, `pricing`, or `app`. Pass a third argument (a salt) when you are repeating a brief, so you do not draw the same block twice. Use the printed direction. Do not swap its palette or face for one you prefer.

Write the plan, then stop and read it:

1. Three things only this subject has (materials, tools, words people in that job say).
2. The direction name, plus one sentence that ties it to those three things.
3. Four to six named hex values. Start from the direction. Shift a hex only to pass contrast, and say so.
4. Type roles: display, body, meta. For each: family, file, size, weight, unitless line-height, letter-spacing.
5. An ASCII wireframe of the first viewport. Mark the one bold place.
6. What you will cut (filler sections, extra accents).

## Pass 2. Genericness check

Ask: would a similar prompt (another SaaS landing page, another pricing page, another app dashboard) produce this same plan? If any part would, rewrite that part and say what changed. Escaping a listed default into another listed default is a failed check. Keep the drawn direction's band, face, and signature while you revise.

## Avoid these, and do this instead

First-order defaults (what a quick page uses when nobody decides):

- Blue-violet gradient or glow (hue about 220 to 290) on a hero, button, or word. Do: one flat full-bleed band in the direction's dominant hex. No gradient on that band.
- Gradient text. Do: a solid ink or paper color from the plan.
- Centered hero, a pill that says the product is new, two buttons. Do: the direction's wireframe, one filled button, the second path as a text link.
- Inter, Roboto, Open Sans, Lato, system-ui, or Segoe UI as the marketing display. Do: the display file named in the direction. Inter is fine for body text inside an app screen.
- Same soft shadow and the same large radius on every card. Do: zero resting shadows. At most two radii plus 0 (full-round only for a toggle or avatar). Separate surfaces with the band or a 1 px line.
- Three equal icon cards, then a bento, then more cards. Do: one product UI, about 40 percent of the hero. Under it, one ranked feature as rows, no icons.
- Emoji as bullets or icons. Do: no marker, or the direction's one signature mark.
- Eyebrow captions (small uppercase tracked labels) over every heading. Do: at most one eyebrow on the whole page. Elsewhere, start with the heading.
- Fake logo walls, fake quotes, round stats (`10x`, `99.9%`, `4,200+`). Do: delete them. Show a labeled sample from the real product (a row, a price, an item count) or show nothing.
- Banned words: seamless, powerful, stunning, next-level, elevate, unlock. Also "not just X, it's Y" and triplets such as "fast, simple, and secure". Do: a headline that breaks if you swap the product name for a competitor. Use the subject's nouns.
- Light gray text, gray text on a colored band, and true black `#000`. Do: neutrals tinted toward the band (8 to 10 steps available). Text on a band is a light or dark solid that passes WCAG AA. Body contrast at least 4.5:1. Large text (24 px, or 19 px and bold) at least 3:1. Failures: 0.
- Facts written as labels (`In stock: 12`). Do: `12 left in stock`.
- Scattered hover bounces, pulses, animated gradients. Do: one page-load reveal, headline then the product UI, with a short stagger. Honor `prefers-reduced-motion`.

Second-order defaults (what appears after the list above is banned). Landing on one of these counts as a miss:

- Cream page near `#F4F1EA`, a serif display, terracotta or clay near `#C46B3A` or `#D97757`. Do: go back to the drawn band. Cream is allowed only on a small UI object the direction names (a ticket, a sheet), never as the page.
- Near-black (`#000`, `#0A0A0A`, `#111`) plus one acid green (`#B6FF3B`, `#CCFF00`, `#39FF14`) or a single vermilion dot. Do: the direction's named material. A dark band is a room color, not a black canvas.
- Broadsheet: hairlines on every edge, radius 0 as the personality, newspaper columns. Do: the direction's two radii. A perforation or a flap gap is a signature, not a page system.
- Space Grotesk, Instrument Serif, or Geist, and mono captions over every heading. Do: the direction's face. A mechanical face (Anton, Allerta Stencil) is allowed only when that direction names it.

## Build

- Marketing H1 is at least 3 times the body size. With a 16 px body, the H1 is 56 to 80 px. App titles are at least 1.6 times the body. The one bold number may be larger.
- Weights are far apart: display 700 to 900 (or a single-weight display face) and body 400. Do not set every heading to 600.
- Letter-spacing: headings at 24 px or larger use `-0.02em` to `-0.01em`. Stencil and flap faces may use `0` to `0.04em` instead, and the plan must say so. Uppercase labels at 14 px or smaller use `+0.05em`. Body uses `0`.
- Line-height is unitless and inverse to size: display `1.0` to `1.1`, headings `1.1` to `1.25`, body `1.5` to `1.6`.
- Body measure is 45 to 75 characters. A heading has more space above it than below it.
- The dominant color owns one full band (the whole first viewport on a marketing page). One accent sits on the primary action and on one highlight, nowhere else.
- The product UI is built in HTML and CSS, with sample data labeled sample. No external images. No invented customers.
- At most six sizes and eight spacing values. Focus states visible. The page does not overflow sideways.

Spend boldness in one place. Before you finish, remove one accessory (a second badge, a second accent, a divider you do not need).

## Render and fix

Open the first viewport in a browser (1280 px wide for a marketing page; a phone screen for an app, centered on the band). Look at a screenshot, including a copy shrunk to about 300 px wide. List the top three problems a stranger would see in one second. Fix them. Repeat up to three rounds. Stop early only when the thumbnail reads as this direction: the band, the huge type, and the signature are obvious.

## Self-audit

Count on the rendered page. Do not claim a pass without numbers.

| Check | Target |
|---|---|
| Blue-violet gradients on a band or on text | 0 |
| Listed second-order looks (cream/serif/clay, black/acid, broadsheet, Space Grotesk, Instrument Serif) | 0 |
| Resting shadows | 0 |
| Decorative pills | 0 |
| Emoji in the UI | 0 |
| Eyebrows on the page | 0 or 1 |
| Distinct non-zero radii | 2 or fewer |
| Filled buttons in the hero | 1 |
| H1 size / body size | 3 or more marketing, 1.6 or more app |
| H1 letter-spacing | `-0.02em` to `-0.01em` (or the stencil exception) |
| H1 line-height | `1.0` to `1.1` if the H1 is the display |
| Contrast pairs below WCAG AA | 0 |
| Banned words | 0 |
| Font sizes | 6 or fewer |
| Spacing values | 8 or fewer |
| Bold place, name it in one sentence | yes |
| Thumbnail reads as the direction at 300 px | yes |

## Worked examples

Bakery cake orders, pricing page. Draw: Ticket window. Tie: a cake order is a ticket on a spike, not a software plan. Bold place: one perforated stub. Band `#5C1A2E`, ticket `#F7F1E6`, ink `#2A1218`, brass button `#D6B15E`. Three equal plan cards would fail the genericness check, so the tiers are lines on the stub.

Hospital linen closet, phone dashboard. Draw: Locker enamel. Tie: each closet is a numbered door. Bold place: `214` at 72 px in Anton. Band `#12357A`, panel `#E6E8EC`, button `#F25C1A`. A row of equal stat tiles would fail, so the number is the only loud thing and the list under it is quiet.

## Further reading

Hierarchy and spacing: Refactoring UI. Measure, line-height, and letter-spacing: Practical Typography. Type scale in a public system: USWDS typography. Contrast floor: WCAG 1.4.3.
