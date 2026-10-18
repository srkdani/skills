---
name: creative-web
description: Makes brand websites inventive and specific, with visuals, illustration, and motion that come from the brand, and steers away from basic text pages and from the usual award-site costume. Make sure to use this skill whenever you build, design, redesign, restyle, or animate a website, landing page, brand site, campaign page, or marketing page, even if the user only says make a website, make it more creative, it looks basic, it looks like just text, it looks generic, it looks templated, or it should feel award-level. It forces a written world from the brand's own facts, then one signature moment, before any code. Not for app dashboards, settings screens, or tasks with no page.
---

# Creative web

A page of big type, blank bands, and cards is a failed page. A page in the usual costume is also a failed page: particle networks, a ring cursor, fade-up on every block, black with one acid accent, cream with an italic serif, glass panels, numbered labels. Creativity comes first. The brand is the anchor, not the ceiling: one physical world, built from facts only this brand has, carried through the picture, the objects, the motion, and the smallest label.

If the user already named a style, a typeface, a grid, or "no animation", follow that exactly, even if it is listed in `bans.md`. Inside that constraint, still harvest facts and keep one idea.

Pages under `eval/` are measurements, not templates. Do not copy them. A site named in `techniques.md` is a source for one number or one decision. Taking its concept, layout, or palette is a failure.

## Read, then draw, then plan

From this folder, before any markup:

```sh
python3 draw.py "Brand name" page
```

Pass a third argument (a salt) when you are repeating a brief, so the deal changes. The draw prints three worlds, one motion, and one picture rule.

Then read `bans.md`, `techniques.md`, `examples.md`, and `rubric.md`. The dealt world is a build spec, not a mood. Copy the examples' specificity, not their worlds, colors, or fonts. If the SVG can be deleted and a themed landing page remains, you skipped the world. Rebuild the scene.

Write the plan below in the conversation, in this order, before you create or edit a page. If you are saving files, save it as `PLAN.md` beside the page first, and only then build. A missing heading means the plan is invalid. Do not open the page "to explore".

### Harvest
At least 12 facts only this brand has: materials, place, tools, process, ritual, history, vocabulary, enemies, customers' words, and sensory detail (smell, sound, temperature, light, time of day). At least 6 are physical or sensory. None is a generic virtue (quality, innovation, passion, craft).

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

### Objects
Map every content type (products, features, people, prices, hours, chapters) to an object or event in the world. Give each a real element id. Say how each instance differs in size, wear, label, or state. No row of identical cards unless the concept is literally a deck.

### Storyboard
Budget, then beats. Exactly one hero signature, visible in the first viewport. One or two supporting moments. One hidden delight. One branded small surface (footer, missing page, consent line, or button hover). Everything else is static and readable.
Write beats as "0 to 30% of the scroll: X happens because Y." Include the touch version in the same beats. A hover-only signature is unfinished.

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

Order: build `#scene` and the hero signature until they work, then the objects, then a voice pass on every string (title, button, error, footer). The scene is the page. A weak scene cannot be saved by sections below it.

Scene contract:
- `#scene` fills at least 70% of the first viewport. It is a picture, not a text column.
- At least 8 drawn parts (SVG shapes) or a canvas that draws the world. Parts that carry no harvest fact are deleted.
- At least 4 elements with `data-object`, each a different value, matching the objects table.
- One `data-signature` on the hero moment. One `data-delight`. One `data-small`.
- `data-facts` on `#scene`: at least 4 facts, each at least 8 characters.
- The main action is inside the first viewport, on the scene, and its label is a verb from the world. It is visible without waiting for an intro.
- You can blur the letters and still tell the business from the picture.
- Do not default to a two-column hero (words left, picture right) unless the dealt world says that.
- No blank band. A section that is only a heading and a paragraph is a failed section. Put the words on an object.
- No full-bleed empty color with a centered headline.

Motion contract:
- Spend motion on the budgeted moments. Body text does not fade, rise, or stagger in.
- Use the motion personality from the plan. Do not put one "premium" curve on everything.
- An intro is under 1.2 seconds, skippable, and skipped on a repeat visit (`sessionStorage`). Task-focused pages get no intro.
- `prefers-reduced-motion`: keep the layout and the picture, drop travel and pins, leave the action usable.
- Touch, designed first: every signature works with a tap, a slider, or scroll. Pointer behavior is an extra, gated on `(hover: hover) and (pointer: fine)`.

Task-focused pages (money, medicine, tools, anything the visitor must finish): the signature teaches the job in one glance. Headline and action are immediate. No pin longer than one viewport. No playful delay on the form, the price, or the menu.

Copy a named award site's concept and the page fails. Invented prices, counts, quotes, and staff are sample data: write the word sample beside the brand or in the footer. No fake testimonials, fake logos, or fake metrics.

No em dash and no en dash, in the plan, the title, or the page. Use a comma, a colon, or a hyphen.

The HTML starts with a comment: `CONCEPT:`, `WORLD:`, `SIGNATURE:`, `REMOVED:`.

## Render, score, remove one effect

Run, from this folder:

```sh
python3 check.py path/to/index.html path/to/PLAN.md
python3 shoot.py path/to/index.html path/to/outdir
```

`check.py` is the contract, not the taste test. Fix every failure. A warning is wrong unless you can defend it in one sentence in the plan.

`shoot.py` writes a first viewport and a full page at 1440 and at 390, and a scroll capture of about 10 seconds with the pointer crossing the hero once. If the browser cannot run, say so. Do not claim you saw a screenshot you did not take.

Look at the 1440 shot shrunk until the page is about 300px wide, and at the 390 shot. List the top three problems a stranger would see in one second. Fix them. Then score the page with `rubric.md`. Creative score under 10, or a floor under 4, means you are not done.

Then delete the effect named in the plan. Leave the `REMOVED:` comment. If the first viewport changed, shoot again.

Stop only when the thumbnail reads as this brand's world: the material, the object, and the signature are obvious with the text blurred.
