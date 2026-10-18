# Halde FM-1

Sample brand. A small aluminium FM synthesizer, four knobs, one wooden side panel, two people in Gothenburg.

## Harvest

Facts only this instrument has. Sensory and physical ones are marked.

1. The body is a small brushed aluminium plate, cool on the palm. (physical, sensory)
2. One side is a single oiled ash cheek, the only warm face, and it smells of linseed for the first weeks. (physical, sensory)
3. Four knobs, and each detent clicks loud enough to hear over a quiet room. (physical, sensory)
4. There is no screen. The patch is wherever the four knobs are standing.
5. FM on this plate means one modulator pulling one carrier. A low index is a soft bell. A high index buzzes. (sensory)
6. Two people in Gothenburg build it. One mills. One wires the operators.
7. The name Halde is the pile of aluminium chips on the bench after a plate is milled. (physical)
8. They work by a north window. In winter the bench lamp stays off until 15:00. (sensory, light, time)
9. Four brass screws hold the cheek. One is left a quarter-turn proud so a thumb finds it. (physical, sensory)
10. A paper strip tucked under the ash records the last ratio they wanted to keep. (physical)
11. The output jack clicks when a patch cable seats. (sensory)
12. Milling days and wiring days swap across the week. The bench changes jobs with the weekday.
13. The plate is small enough that one hand covers two knobs. (physical)
14. Ratios are small integers, stamped, never a decimal on a display.
15. The enemy is menu FM: operators buried behind a screen and a shift button.

## Truths

1. The whole patch is four detents on the face, and the ratio knob steps an integer relationship you can see. Rival: a compact FM box with a screen and a menu. That rival keeps the operators on pages. It does not stamp the patch as a click.
2. One ash cheek is screwed to the aluminium, and one brass screw is left proud. Rival: an all-metal desktop module. It has no single warm cheek and no screw left proud as a findable mark.
3. The name is the chip pile beside the mill, and the two Gothenburg builders split milling and wiring by the weekday. Rival: a factory FM keyboard. The factory does not name the instrument after its own scrap, and the day's job does not swap between two people.

## Emotion

Focus.

"I stepped the big knob and a comb of ink lines grew beside it until the plate read 3 to 1."

## Concepts

The site is a detent knob where each click is an FM ratio and turning it stamps sidebands into the aluminium. Rival: a guitar pedal brand with knobs. Their click does not stamp a carrier ratio or draw sidebands. Swap the name and the line breaks. Keep.

The site is a chip heap you sift, each shaving a frequency. Rival: a metal shop that sells offcuts. FAIL. The heap fits them. Replaced with: the site is a paper strip under an ash cheek where the only saved setting is the last ratio two people kept. Rival: a notebook brand. A notebook is not screwed to an FM plate. Keep as an unused line.

The site is a north window that retunes the room at 15:00. Rival: a cafe that changes lamps in the afternoon. FAIL. The hour lamp fits them. Replaced with: the site is a proud brass screw that opens the cheek onto today's milling or wiring. Rival: a furniture shop. A furniture screw does not open onto an FM ratio. Keep as an unused line.

## Pick

World dealt, pick one: The verb. The verb is tune, and the real control is the ratio knob. `#scene` is the plate where that knob is turned. The headline is the ratio the click just stamped. Scroll and a range input drive the same six detents. A paragraph does not explain the verb before the knob can be turned.

Rejected world: Letters as objects. The product is not a phrase. A giant letter with a picture in the counter would hide the detent, which is the only control that matters.

Rejected world: Clock in the room. Halde does not sell an hour, a shift, or a sell-out. The 15:00 lamp is a small mark on the plate, not a timepiece filling the viewport. A giant clock would steal the knob.

Concept picked: the detent knob. The visitor sentence comes true because stepping that knob is the first thing the page lets you do, and the comb of sidebands is the picture that changes. No second concept is merged in. The cheek, the paper strip, and the chip pile are parts of this same plate, hung on the truths, not a second metaphor.

## Visual system

Material the page is made of: a brushed aluminium plate with one ash cheek along the left edge, because the FM-1 body is that plate and that one wooden side.

Light source: the Gothenburg north window before 15:00, because that is the light they mill by. The page takes that brightness. It is daylight on metal, not a dark booth and not a chosen theme.

Palette, from that metal and that wood:
- `#D5D8D2` aluminium in the north window, because the brushed plate reads as this grey under that light.
- `#1C1F1A` graphite ink, because the filings leave a dark smear on the fingers.
- `#8F6436` oiled ash, because the cheek is oiled ash, warm only on that one edge.
- `#C6A15A` brass, because the four screws are brass.
- `#E4D7C3` paper strip, because the saved ratio is written on unsized paper, a small object, not the page.

Type: display face Big Shoulders Display, extra bold, loaded from `https://fonts.googleapis.com/css2?family=Big+Shoulders+Display:wght@800&family=Familjen+Grotesk:wght@400;600&display=swap`. At 1440 the display is 128px and the body is 18px, a jump of about seven times, because the ratio is stamped in condensed caps on a short plate and must dwarf the note. Tracking `-0.03em`, because those stamps sit tight on the metal. Body face Familjen Grotesk at 18px, because the paper strip is a plain note written in Gothenburg, not a poster.

Picture rule: accepted, ink and one color. 1.75px round caps, ink `#1C1F1A`, fill `#D5D8D2`, wobble of 3px through a displacement filter. The picture depicts the ratio knob, its six ticks, the partial comb, the four smaller knobs, the ash cheek, and the chip pile. Ash and brass are flat material pieces, not a second shading style. No gradients as shading.

Motion: mechanical, accepted from the deal. `steps(6)` behavior, 120ms per detent, no overshoot, because a detent clicks and does not glide. Repeated swaps (which knob is explained) are instant, under 150ms. The proud screw answers in under 100ms.

Sound: opt-in and off by default, because this object makes a tone and a tone must not start by itself. One FM blip, about 160ms, only after a visible toggle is turned on. No autoplay.

Grade: one picture treatment. North-window ink on the aluminium. Every drawing uses the same ink and the same fill. `GRADE:` names it in the page comment. A missing photograph of the real milled plate is a labeled placeholder in that same ink, not a stock photo.

## Objects

Content lives on the plate. Nothing is a row of identical cards.

- `plate` is the aluminium face, element `#scene`. It is the full first viewport. Wear is the brush of the metal, no second texture.
- `ratio-knob` is element `#ratio-knob`. Largest object. Six ticks. Pointer starts at rest. This is the signature.
- `index-knob` is element `#index-knob`. Smaller than the ratio knob, a scratch through the 2 o'clock tick.
- `decay-knob` is element `#decay-knob`. Mid size, pointer tip shortened as if chipped.
- `level-knob` is element `#level-knob`. Smallest, rotated about 8 degrees, the legend worn at the loud end.
- `partial-comb` is element `#partial-comb`. A set of ink lines whose count changes with the ratio detent. At 1 to 1 it is a single carrier line.
- `ash-cheek` is element `#ash-cheek`. The left wood edge, taller than the knobs, overlapping the plate by a few pixels.
- `brass-screw` is element `#proud-screw`. One of four screws, the one left proud. The other three sit flush and are not separate objects.
- `paper-strip` is element `#paper-strip`. Narrower than the cheek, the handwriting place, hidden until the cheek is asked to move.
- `offcut` is element `#offcut-pile`. Footer heap. Chips differ in size. One chip carries the milled name.
- `builder-mill` is element `#builder-mill`. The wider stamp. It is the milling day.
- `builder-wire` is element `#builder-wire`. The narrower stamp. It is the wiring day.
- `placeholder-photo` is element `#plate-photo`. A marked empty frame, same ink, labeled placeholder.

## Budget

Every idea names a truth.

Big, exactly one, truth 1. Element `#ratio-knob` with `data-tier="big"`. The ratio knob is the largest thing in the first viewport. Six detents. Each detent rotates the pointer 60 degrees, restamps the headline with the ratio, and adds ink lines to `#partial-comb`. Ratios in order: 1 to 1, 2 to 1, 3 to 2, 3 to 1, 4 to 1, 5 to 2. The visitor can do this before reading anything below the plate.

Storyboard, including touch. 0% of the scroll: detent 0, pointer at rest, one carrier line, headline "1 to 1, carrier alone", because truth 1 says the patch starts as a position, not a menu. The Gothenburg line, the sample mark, and the button are already visible. 0 to 30% of the scroll: progress across the top of the plate quantizes into the six detents. Each step is 120ms, mechanical, no glide. The comb thickens because truth 1 is the click you can see. Touch, designed first: a range input with six stops sits on the plate and reaches the same states. The button "Step the ratio" advances one detent. Nothing important is hover-only. A fine pointer may drag the same range. It is extra.

Medium, two, built one at a time.

- Medium A, truth 1. Element `#operator-strip`. Tap Ratio, Index, Decay, or Level. The strip writes that knob's one job, and that knob's ring doubles. The other rings stay single. Touch path: the tap. The swap is instant. Jobs: Ratio is the integer between carrier and modulator. Index is how hard the modulator pushes. Decay is how fast the bell dies. Level is how loud it leaves the jack.
- Medium B, truth 2. Element `#cheek-panel`. Tap the ash cheek. It shifts one mechanical step, 120ms, and `#paper-strip` shows the ratio the two people kept. Tap again and the cheek sits back. Touch path: the tap. On a narrow screen the strip opens under the cheek, not over the main button.

Small, at least five. Each stays off the button and the headline.

- Small, truth 3, `data-live="time"`. Element `#bench-lamp`. On load, read the local hour once. Before 15:00 the label is "North window". From 15:00 a cluster of ink ticks appears and the label is "Bench lamp". A tap shows the other hour without covering the knob.
- Small, truth 1. Element `#heard-stamp`. The document title and this stamp change to the ratio just clicked.
- Small, truth 2. Element `#proud-screw`. A tap turns it a quarter-turn, under 100ms, proud or flush.
- Small, truth 3. Element `#offcut-pile`. The footer is the chip pile, the name milled into one chip, not a row of links.
- Small, truth 1. Element `#empty-partials`. At detent 0 it reads "No sidebands. The carrier is sitting alone." Later detents replace the sentence with the partial count.
- Small, truth 3. Element `#plate-photo`. Placeholder frame: the real milled plate has no photograph here. Same ink as the rest.

Technique for the big moment: scroll and drag scrub of a stepped sequence (the detent), mechanical steps. Medium A is a state swap and uses no extra catalog technique. Medium B is one short move of the cheek. Small ideas are not extra techniques. Live hour is the one context hook.

## Rhythm

- Plate: one giant knob, the comb on its shoulder, the stamped ratio under it, the slider in the metal.
- Operator offcut: one long chip, a single sentence that swaps, knobs of unequal size along it.
- Cheek: a tall wood column, screws stacked, the paper strip behind the wood.
- Two stamps: mill stamp wide, wire stamp narrow, different heights, the weekday written on the wide one.
- Heap: scattered chips, words cut into the largest chip.

No section is a heading, then a paragraph, then a card grid. No two rhythms match.

## Removal

Build a filing-dust grain overlay across the plate (turbulence, low opacity), then delete it. It does not serve the concept. The detent and the ink comb already show the mill. A full-plate grain fights the ink picture rule, which asks for one clean line and a small wobble, not a fog on every surface.

## Voice

Headline, under eight words, restamped by the knob. Each state stays under eight words: "1 to 1, carrier alone", "2 to 1, a wooden bell", "3 to 2, a fifth buzz", "3 to 1, nasal metal", "4 to 1, a tight clang", "5 to 2, a bright heap".

Subhead, one: "Four knobs, one ash cheek, Gothenburg. Sample."

- Button: "Step the ratio"
- Empty state: "No sidebands. The carrier is sitting alone."
- Footer: "The name is the pile of chips beside the mill."
- Missing page: "This plate was never milled."
- Loading: "Filing the edge."

The footer is the oddly specific line. A stranger can tell the brand from it. The sound consent line sits by the toggle: "Sound stays off until you ask."

## Genericness

A similar brief is a two-person desktop synth with wooden end cheeks and a filter knob. The part this plan would have shared is a large knob in the first screen as a volume prop. That part is changed: the knob is not a prop and not a filter. It stamps an integer FM ratio and grows a comb of sidebands, because truth 1 is the screenless patch. The wood is one cheek you open onto a paper strip, not a pair of end caps in a lifestyle band. The dealt world stays The verb.

Batch 1 gate: The page is still the detent knob, drawn as grey plate, cheek, and comb, and the ratio restamps when the slider, the button, or the first scroll steps it. The comb was moved onto the knob's shoulder so it no longer sat on the headline.

Batch 2 gate: The signature is the ink ratio knob on the aluminium plate, and each detent still restamps the headline and grows the partial comb, with the range and the button as the touch path. The carrier line had collapsed to zero height, so it now stands on the baseline at rest. The jobs, cheek panel, stamps, and heap stay grey placeholders.

Batch 3 gate: The detent knob is still the signature. Tapping a job on the offcut doubles that knob's ring, and the ash cheek steps aside onto the ratio the two people kept. The shut label was sliding off the wood, so the screws stay on the edge that remains in view, and on a narrow screen the strip opens under the cheek.

Batch 4 gate: The small marks sit on the same plate: the north-window lamp, the heard stamp, the proud screw, the empty carrier line, the placeholder, and the chip pile named Halde. The paper note was peeking out while the cheek was shut, so it stays hidden until the cheek is asked to move.

Batch 5 gate: The plate still tunes by detent, with the range and the button immediate under reduced motion, and sound stays off until asked. The filing-dust grain is gone, the morning lamp no longer draws its hatch, and the shut cheek is wood instead of a blank paper field.
