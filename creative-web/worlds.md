# Worlds

`draw.py` prints three of these, plus one motion and one picture rule. Pick one world. Palette and type are not dealt. They come from the harvest.

Each world describes the DOM to build. A world you only "theme" with colors, while the page stays a headline and sections, is a rejection of the deal.

## World: Material weather

Fit: the brand's name or benefit is a physical condition you can see: heat, cold, daylight, dust, steam, ink, fog, safelight.
Build: `#scene` is the whole first viewport, layered shapes of that material. A shadow or light overlay sits at opacity 0.15 to 0.35, sways 8 to 14s, and pauses off screen. Headline and action are printed on the material.
Layout: no side column. Type lives on the stuff. Later sections are the same material in another state (cooler, wetter, baked), not new bands.
Touch: the sway is off. A tap shifts the light to the next state.
Quiet: body paragraphs are short and sit on a scrap of the material.
Fails if: a flat field of one color with a sentence in the middle.

## World: Traveling object

Fit: the product moves through a real journey (seed to loaf, crate to door, payout to match, signal to speaker).
Build: one SVG `#traveler` with three child groups, one per state. Pin it for at most 220vh with scrub between 0.6 and 1. Captions are at most 18 words, beside the object, never on a card. After the pin, a short practical footer only.
Layout: the object stays large and cropped. The page is the journey. Features are states of the object.
Touch: the same scrub on scroll. No drag required.
Quiet: one line per state.
Fails if: the object decorates a hero and the real content is cards underneath.

## World: Unlike objects on a surface

Fit: the brand has several things to show (goods, works, flavors, specimens) and they must not look like twins.
Build: a surface (table, pegboard, rack, tray) and at least four SVG objects. Different sizes. One rotated about 8 to 14 degrees. One overlapping another. One cropped by the viewport edge. A click or a scroll beat expands one object. The others do not share a height.
Layout: not a grid of equal cells. Positions are chosen, not auto-placed.
Touch: tap an object to bring it forward. Hover is extra.
Quiet: names are stamped on the objects, not in captions under cards.
Fails if: equal cards, equal shadows, equal radii.

## World: Operable document

Fit: the brand's real artifact is a log, ticket, receipt, score, panel, label, or chart.
Build: the page background is the desk or bench under that artifact. One document, `min(960px, 100%)` wide, is the page. Navigation is a part of the document (a stub, a tab, a stamped index). Controls look like the document's own controls (a punch, a knob, a pencil tick), not like pills.
Layout: no marketing hero above a picture of the document. You are holding the document.
Touch: controls are at least 44px and work by tap.
Quiet: small print is real small print, 12 to 14px, still readable.
Fails if: a hero headline, then a fake screenshot of a form.

## World: The verb

Fit: the brand has a physical verb: pour, cut, knead, match, tune, fold, strike, stamp, sweep.
Build: `#scene` is a stage where that verb happens. The control is the product's real control (slider, knob, blade, switch). The headline completes, fills, or stamps as a result of the action. Design the scroll or slider version first. On a fine pointer, the same control may track the pointer.
Layout: the verb is the largest thing in the first viewport. A paragraph does not explain the verb before you can do it.
Touch: a range input or scroll position drives the verb. Nothing important is hover-only.
Quiet: instructions are one line on the tool.
Fails if: a custom cursor follows the mouse and the page does not change.

## World: Clock in the room

Fit: the brand depends on an hour, a shift, a tide, a season, or a sell-out time.
Build: a clock, shift board, or timer as a large SVG. On load, read the local hour once and set a real state (open, working, resting, sold through). The scene's light and one object change with that state. The rest of the page is what that hour contains.
Layout: the timepiece is at least 40% of the first viewport, not a widget in a corner.
Touch: states can be tapped through, so a visitor can see the other hours.
Quiet: the practical facts (address, price, status) update with the state.
Fails if: a fake countdown, or a normal page with a small clock.

## World: Two states, one clip

Fit: the brand is a change from one state to another (raw to finished, unbalanced to matched, lights on to lights out).
Build: two full scenes, one `clip-path` driven by a single progress value (scroll or drag). Use `inset` from opposite edges. Do not crossfade opacity. Both scenes are built, not one photo and a label.
Layout: the split is the first viewport. Copy sits inside each state.
Touch: scroll drives the clip. A range input can too.
Quiet: after the split, one practical block.
Fails if: a stock before-and-after slider, or two columns of text.

## World: Worker in the room

Fit: a playful, human, food, or studio brand where a person or creature does the work.
Build: a character from circles and rounded rects. Three groups: idle, act, rest. The character pushes, carries, or reveals one interface element, then idles 2 to 4s. Pause the loop off screen and under reduced motion. The footer is where the character rests (a shelf, a hook, a bed).
Layout: the room is the page. UI elements are furniture the character touches.
Touch: scroll or a tap triggers the act pose. Do not depend on hover.
Quiet: the character does not have detailed anatomy, fingers, or a realistic face.
Fails if: a mascot parked beside normal sections.

## World: Letters as objects

Fit: words, names, or type are the product, or a single phrase is the brand's whole claim.
Build: the headline is constructed (SVG letters or separate elements), cropped by the viewport, larger than 4 times the body. At least one letter holds a picture of a harvest fact in its counter. No italic word in a second family. Supporting copy is short and sits under the letters.
Layout: the letters are the illustration. There is no separate hero image.
Touch: a tap cycles a letter's inner picture. No proximity-hover required.
Quiet: one typographic idea, not a mix of serif and sans flourishes.
Fails if: a normal heading with one emphasized word.

## World: Walk into the place

Fit: the brand is a room, a shop, a hall, a bench, or a landscape you could stand in.
Build: `#scene` has three layers (back wall, mid object, foreground crop). Pointer parallax moves a layer by 1 to 3% of its width, with lerp, and only on a fine pointer. Touch keeps the layers still. Labels are physical (a hanging tag, chalk, a stamped plate), not floating chips. Each later section is another room with its own three layers.
Layout: you see surfaces: floor, wall, tool. Not a scrim behind text.
Touch: rooms stack in normal scroll. Hotspots are taps.
Quiet: no centered sentence over a darkened picture.
Fails if: an image banner with a gradient and a headline.

## World: The stack

Fit: the things are physical and stack, file, or pack (books, records, jars, crates, slides, blankets).
Build: a stack in perspective, 1200 to 2000px. Scroll moves through it. The front item is huge and cropped. Each item differs in thickness, label, or wear. One item can be pulled out (a supporting moment).
Layout: you look along the stack, not at a list of rows.
Touch: scroll moves the stack. A tap pulls one item.
Quiet: the title is printed on a spine or a lid, not above the stack.
Fails if: equal rows pretending to be a pile.

## World: Bench in stages

Fit: the brand makes a thing by hand or by a visible process, in stages.
Build: one workbench that stays on screen. Scroll advances 3 to 5 stages. The same object changes (it grows, joins, prints, or cools). Stage copy is one note on the bench. Pin at most 220vh. Afterward, a plain practical block: place, hours, price, action.
Layout: the bench is the first viewport and the pin. Do not turn the stages into a row of steps.
Touch: scroll advances the stage. Reduced motion shows stage one with a control to step forward.
Quiet: no dotted timeline, no year labels floating in a column.
Fails if: a horizontal scroller of steps, or the main text set sideways.

## Motion: Mechanical

Detents. `steps(6)` or linear, 80 to 160ms per step, no overshoot. Use for machines, switches, stamps, and instruments. Repeated UI is instant.

## Motion: Heavy

Weight. `expo.inOut` or `power4.inOut`, 0.9 to 1.4s, distance under 80px. Use when the brand is stone, metal, architecture, or a large object. Do not use it on menus.

## Motion: Spring

Play. `back.out(1.4)` or a short overshoot, 0.35 to 0.6s, once. Use for food, toys, and characters. One bounce, then stop. Do not bounce every block.

## Motion: Calm

Drift. `sine.inOut`, 0.8 to 1.6s, opacity or a move under 12px. Use for paper, daylight, care, and reading. No snap, no bounce.

## Motion: Snap

Work. `power3.out`, under 280ms. Use for tools and task-focused pages. The signature may be longer only if it explains the job. Everything you repeat is under 150ms.

## Picture: Ink and one color

1.75px round caps, one ink hex, one fill hex, a wobble of 2 to 4px via a displacement filter if you need it. Imperfection is allowed. Detail is not. No gradients as shading.

## Picture: Cut paper

Flat shapes, hard edges, no blur, overlaps only. Two paper colors and one ink. Shadows are a second piece of paper offset by 6px, not a box-shadow.

## Picture: Screenprint

Two or three flat inks. A second pass misregistered by 2px. No photographic texture. Large shapes, few of them, confident.

## Picture: Plate and stamp

Thin rules, stamped numbers, one correction color used only on marks and the main action. The page looks handled: a crop, a punch hole, a serial. Not a hairline grid on every edge.

## Picture: Material swatch

The hero is the material itself, built from a few shades of that one material (metal, wood, dough, stone, wool). No glow, no neon edge, no grain layered on as a default. Grain only if the harvest names a print, a film, or a dusty surface, at opacity 0.05 to 0.12.
