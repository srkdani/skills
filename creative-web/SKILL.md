---
name: creative-web
description: Makes brand websites inventive and specific, with visuals, illustration, and motion that come from the brand, and steers away from basic text pages and from the usual award-site costume. Make sure to use this skill whenever you build, design, redesign, restyle, or animate a website, landing page, brand site, campaign page, or marketing page, even if the user only says make a website, make it more creative, it looks basic, it looks like just text, it looks generic, it looks templated, or it should feel award-level. It forces three brand truths, then several small details, two or three medium interactions, and one signature moment, before any code. Not for app dashboards, settings screens, or tasks with no page.
---

# Creative web

A page of big type, blank bands, and cards is a failed page. So is a page where every section has the same rhythm (heading, text, card grid), where motion only decorates, or where the pictures are not art-directed as one set. A page in the usual costume is also a failed page: particle networks, a ring cursor, fade-up on every block, black with one acid accent, cream with an italic serif, glass panels, numbered labels. Creativity comes first. The brand is the anchor, not the ceiling: three truths only this brand has, then every idea hung on those truths, from the smallest label to one signature moment.

If the user already named a style, a typeface, a grid, or "no animation", follow that exactly, even if it is listed in `bans.md`. Inside that constraint, still harvest facts and keep one idea.

Pages under `eval/` are measurements, not templates. Do not copy them. A site named in `techniques.md` is a source for one number or one decision. Taking its concept, layout, or palette is a failure.

## Read, then draw, then plan

From this folder, before any markup:

```sh
python3 draw.py "Brand name" page
```

Pass a third argument (a salt) when you are repeating a brief, so the deal changes. The draw prints three worlds, one motion, and one picture rule.

Then read `bans.md`, `techniques.md`, `examples.md`, and `rubric.md`. The dealt world is a build spec, not a mood. Copy the examples' specificity, not their worlds, colors, or fonts. If the SVG can be deleted and a themed landing page remains, you skipped the world. Rebuild the scene.

Write the plan below in full and save it as `CREATIVE_PLAN.md` before any HTML. That file is the north star. A missing heading means the plan is invalid. Do not open the page "to explore". Do not start batch 1 until `CREATIVE_PLAN.md` is saved.

### Harvest
At least 12 facts only this brand has: materials, place, tools, process, ritual, history, vocabulary, enemies, customers' words, and sensory detail (smell, sound, temperature, light, time of day). At least 6 are physical or sensory. None is a generic virtue (quality, innovation, passion, craft).

### Truths
Three truths, each a harvest fact a rival does not have in this form. Under each, name the rival. If the rival has it in the same form, replace the truth. Not a virtue (quality, craft, innovation). Every later idea names truth 1, truth 2, or truth 3. An idea that names none is cut.

### Emotion
One emotion word. One sentence a visitor would say to a friend afterwards. The sentence names something they saw or did on the page.

### Concepts
Three lines, each a different metaphor, not three skins of one idea. Pattern: "The site is a [object, place, or process] where [content] becomes [thing] and [user action] does [verb]." Under each line, name a competitor (or "a rival in this category"). If the line still fits them, write FAIL and replace the line. Keep only lines that break when the name is swapped.

### Pick
One concept. Why it makes the visitor sentence come true. No "plus elements of" another concept. Merging worlds is a failed plan.

### Visual system
Every token ends with `because` and a harvest fact. A token you could paste onto another brand is invalid.
- Material the page is made of (paper, ice, enamel, flour, aluminium, wool). Not "dark" and not "minimal".
- Palette: 2 to 5 hex values taken from that material. You do not pick light mode or dark mode. The harvest's lamp, sun, or room picks the brightness. Name that light source.
- Type: a display face and a text face, the file or the font URL, and the size jump. Display is at least 4 times the body size. Say why the display face belongs to this world.
- Picture rule: the dealt rule, or a rejection with a reason, and what the picture depicts.
- Motion: one easing family and a duration range (the deal, or a rejection). UI that people repeat (menus, tabs) is instant or under 150ms.
- Sound: none, or opt-in and off by default. Never autoplay.
- Grade: one picture treatment for the whole page (one ink, one duotone, one light, or one crop). Name it in a `GRADE:` comment. Two grades is a failed page. If a real photo, signature, or archive is missing, build a stand-in and mark it placeholder. Do not mix in an unrelated stock style.

### Objects
Map every content type (products, features, people, prices, hours, chapters) to an object or event in the world. Give each a real element id. Say how each instance differs in size, wear, label, or state. No row of identical cards unless the concept is literally a deck.

### Budget
Hang every idea on a truth. Counts are required.
- Small: at least 5. Quick, specific, under 300ms, never covering the headline or the action. A live line, a mark, a hover that does the brand's verb, a tab title that changes, a missing-page or empty state, a stamp, the grade itself.
- Medium: 2 or 3. An interaction the visitor can use (a swap, a short guide, a scrub, a map, a second state). Each has a touch path.
- Big: exactly 1. The signature, visible in the first viewport or the first scroll, and the thing a person would describe tomorrow.

At least one small or medium idea uses real context when the harvest has a time, a place, or a status: time of day, weekday, season, location, or live status. Mark it `data-live` with one of `time`, `weekday`, `season`, `place`, `status`. If the harvest truly has none, write a `NO-LIVE:` comment saying why.

Prefer real assets (photo, signature, archive, product). Missing assets are placeholders, labeled.

Storyboard only the big moment: "0 to 30% of the scroll: X happens because truth N." Include the touch version in the same beats. A hover-only signature is unfinished.

In the HTML, each idea is a visible element with `data-tier="small|medium|big"` and `data-truth="1|2|3"`. An attribute on an empty node does not count. The visitor can see or trigger each one.

### Rhythm
List each section's rhythm in a few words. If two match, change one. Do not repeat heading, then text, then a card grid. A section that could swap with the one above it, and only the words would change, is a failed section.

### Removal
Name one effect you will build and then delete, and why it does not serve the concept. A console log does not count. A second animation, a grain overlay, a cursor, or an extra scene does.

### Voice
Headline under 8 words. One subhead. Five lines: button, empty state, footer, consent or missing page, loading. At least one line is funny, surprising, or oddly specific. A stranger should tell the brand from the footer alone. No banned words (`bans.md`).

### Genericness
Name a similar brief in the same industry. Which part of this plan would you have written for them? Change that part and say what changed. Escaping a ban into another ban is a failed check. The dealt world stays unless you rejected it in Pick.

## Build

Default stack is one HTML file. CSS and script are inline. Load GSAP from a CDN, only the plugins you use:

```html
<script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/gsap.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/ScrollTrigger.min.js"></script>
```

If the project already has a framework or a motion library, stay in it. Do not add a second one. Load fonts the plan names. Do not use a font from `bans.md`.

Native scroll. Do not add a smooth-scroll library unless a pin would feel broken without it. One pin at most, shorter than 250vh. Do not scroll-jack the reading text. Horizontal movement only inside a gallery or a stack the storyboard names.

Doing the whole page in one pass fails. The concept gets lost under decoration. Build only the batch in front of you.

### Batch 1. Structure
Grey boxes only: flat fills, real type sizes, no finished illustration. Section rhythms differ. The practical fact and the main action are placed. The big moment's mechanism works (it moves, scrubs, or steps) as a grey box. Finished art in this batch is a failed batch.

### Batch 2. Signature
Build only the big moment, fully: picture, motion, and the touch path. Medium and small stay quiet placeholders.

### Batch 3. Medium, one at a time
Build one medium feature, then gate it, then the next. Two or three total. Do not start the next feature while the current one is broken.

### Batch 4. Small details
Add the small details. Each one is visible, tied to a truth, and stays off the action.

### Batch 5. Polish
Reduced motion, touch, the 390 width, contrast, a voice pass on every string, delete the named effect, then score with `rubric.md`.

### Gate after every batch
Do this before the next batch. Never continue while the current batch is broken.
1. `python3 shoot.py index.html shots/batch-N` (for each medium feature, `shots/batch-3a`, then `shots/batch-3b`).
2. Re-read `CREATIVE_PLAN.md`. Look at the picked concept and the three truths.
3. Append `Batch N gate:` and one sentence: how this batch still serves that concept, and what you fixed.
4. `python3 check.py index.html CREATIVE_PLAN.md --batch N`
5. If the shot drifted or check.py fails, fix and shoot again. Only then start the next batch.

The scene is the page. A weak scene cannot be saved by sections below it.

Scene contract (the finished page, after batch 5). Earlier batches only have to satisfy `check.py --batch N`. Do not pull later batches forward to satisfy this list:
- `#scene` fills at least 70% of the first viewport. It is a picture, not a text column.
- At least 8 drawn parts (SVG shapes) or a canvas that draws the world. Parts that carry no harvest fact are deleted.
- At least 4 elements with `data-object`, each a different value, matching the objects table.
- At least 5 `data-tier="small"`, 2 or 3 `data-tier="medium"`, exactly one `data-tier="big"`. Each has `data-truth`. The big tier is the signature.
- `data-facts` on `#scene`: at least 4 facts, each at least 8 characters.
- The main action is inside the first viewport, on the scene, and its label is a verb from the world. It is visible without waiting for an intro.
- You can blur the letters and still tell the business from the picture.
- Do not default to a two-column hero (words left, picture right) unless the dealt world says that.
- No blank band. A section that is only a heading and a paragraph is a failed section. Put the words on an object.
- No full-bleed empty color with a centered headline.

Motion contract:
- Motion tells a truth or it is cut. A bobbing icon, a decorative loop, and a fade-up are not ideas. Body text does not fade, rise, or stagger in.
- Use the motion personality from the plan. Do not put one "premium" curve on everything.
- An intro is under 1.2 seconds, skippable, and skipped on a repeat visit (`sessionStorage`). Task-focused pages get no intro.
- `prefers-reduced-motion`: keep the layout and the picture, drop travel and pins, leave the action usable.
- Touch, designed first: every signature works with a tap, a slider, or scroll. Pointer behavior is an extra, gated on `(hover: hover) and (pointer: fine)`.

Usable on purpose. The headline, the main action, and the practical fact the visitor came for (hours, place, price, status, or contact) are findable without finishing the big moment. Task-focused pages (money, medicine, tools, anything the visitor must finish): the signature teaches the job in one glance. Headline and action are immediate. No pin longer than one viewport. No playful delay on the form, the price, or the menu. Small and medium ideas stay out of the way of that action.

Copy a named award site's concept and the page fails. Invented prices, counts, quotes, and staff are sample data: write the word sample beside the brand or in the footer. No fake testimonials, fake logos, or fake metrics.

No em dash and no en dash, in the plan, the title, or the page. Use a comma, a colon, or a hyphen.

The HTML starts with a comment: `CONCEPT:`, `WORLD:`, `SIGNATURE:`, `GRADE:`, `REMOVED:`.

## Render, score, remove one effect

Run, from this folder:

```sh
python3 check.py path/to/index.html path/to/CREATIVE_PLAN.md --batch 5
python3 shoot.py path/to/index.html path/to/shots/batch-5
```

`check.py` is the contract for that batch, not the taste test. Fix every failure. A warning is wrong unless you can defend it in one sentence in the plan. Batch 5 also requires the earlier `Batch N gate` lines, so a one-pass page cannot pass.

`shoot.py` writes a first viewport and a full page at 1440 and at 390, and a scroll capture of about 10 seconds with the pointer crossing the hero once. If the browser cannot run, say so. Do not claim you saw a screenshot you did not take.

Look at the 1440 shot shrunk until the page is about 300px wide, and at the 390 shot. List the top three problems a stranger would see in one second. Fix them. Then score the page with `rubric.md`. Creative score under 10, or a floor under 4, means you are not done.

Then delete the effect named in the plan. Leave the `REMOVED:` comment. If the first viewport changed, shoot again.

Stop only when the thumbnail reads as this brand's world: the material, the object, and the signature are obvious with the text blurred.
