# Halde FM-1

## Harvest

Facts only this instrument has. Physical or sensory items are marked.

1. The body is aluminium: cool, pale, hard-edged sheet. (physical)
2. One side is a wooden panel, the only warm face, and the part a hand actually holds. (physical, sensory)
3. There are four knobs and no other controls. (physical)
4. It is small enough to sit on a desk, not a rack row. (physical)
5. The method is FM: one carrier frequency bent by a modulator. (vocabulary, process)
6. A low index is nearly a plain tone. A high index throws off uneven partials and the ear reads a bell. (sound, sensory)
7. Two people make it. (people)
8. The shop is in Gothenburg, a harbour city with flat overcast daylight off the water, not a spotlight. (place, light)
9. Aluminium under that harbour light goes cool grey-green. The wood stays the only warm surface. (sensory, light)
10. The wooden cheek is the grip. The metal is what you avoid holding for long, because it stays cold. (ritual, temperature)
11. Four jobs fit the four knobs: ratio, index, loop (feedback), and out. (vocabulary)
12. The model mark is FM-1: one small box, a first instrument, one carrier through it. (vocabulary)
13. Plywood glue lines on a cheek are uneven, because two people clamp a sheet, they do not print a texture. (physical)
14. The out end of a small box sits at the far edge of the hand, often partly out of view when you lean in. (physical)

No generic virtues. Price is not invented: the page says sample and lists no number.

## Emotion

Recognition.

"I watched a plain line go into the aluminium box and come out a bell after the four knobs."

## Concepts

1. The site is one aluminium FM box on a journey from a plain carrier to a bell, where the four knobs are the only bends and scrolling raises the index.
   Rival: a Berlin desktop analog synth with sliders. A slider box does not end in an FM bell, and it does not carry one wooden cheek on four knobs. Keep.

2. The site is the wooden cheek as a handle, where each chapter is a glue line and pulling the cheek opens a spec.
   Rival: a wooden-cabinet speaker maker. A cheek-as-handle page could be skinned onto them. FAIL.
   Replacement: The site is a ratio stamp, where each spec is a fraction and the visitor cancels one to retune.
   Rival: a pocket calculator. Fractions fit them better. FAIL.
   Replacement: The site is the 6px wooden lip under the aluminium, and the carrier may leave only when that lip shows.
   Rival: a wood-cheeked analog keyboard. They do not send one FM carrier through four knobs. Keep.

3. The site is a two-person handoff on a Gothenburg bench: one person holds the wood, the other parks the knobs, and the visitor completes the pass.
   Rival: a ceramics duo. They do not pass a carrier into aluminium. Keep.

## Pick

Concept 1, the dealt world Traveling object.

The visitor sentence comes true because the same ink line is on screen the whole pin: plain at the wooden edge, bent at the knobs, uneven at the cropped out. They see the bell happen. They do not read about it on cards.

Rejected worlds, not merged:

- Bench in stages. A bench fits any two-person shop, including a pedal maker. The fact that breaks the swap is the carrier becoming a bell inside this box, not the workbench.
- Unlike objects on a surface. Halde has one instrument. Four knobs are one control row on a journey, not four goods on a tray.

Motion, accepted. Calm drift, `sine.inOut`, 0.8 to 1.6s, moves under 12px. Harbour daylight and cut paper drift. The carrier at a low index drifts. It does not snap. The pin scrub is the journey the world requires, not a tween. The one repeated control (a knob detent) stays under 150ms.

Picture, accepted. Cut paper. The aluminium sheet and the wooden cheek are the two papers. Ink is the carrier, the knob bodies, and the type. Shadows are a second piece of paper offset by 6px. Hard edges, overlaps only, no blur. The 6px wooden lip is how the cheek shows under the metal, which is the harvest, not a second idea.

## Visual system

- Material: two cut sheets, aluminium and wood, because the body is aluminium and one side is a wooden panel.
- Light: overcast late-morning daylight off the Gothenburg harbour, because that is the room. The page is bright. The aluminium is the field. Nothing glows.
- Palette: `#D9DCD6` aluminium sheet, because milled aluminium under that harbour light is pale and slightly green-grey. `#B8862F` wooden cheek, because the side panel is the only warm surface and it reads as oiled birch plywood, the sheet a two-person shop clamps on. `#1C241F` ink, because the carrier is drawn, not lit. Two papers and one ink.
- Type: display "Archivo Narrow" 700, from `https://fonts.googleapis.com/css2?family=Archivo+Narrow:wght@600;700&family=Archivo:wght@400;500;600&display=swap`, because four legends have to sit on a short aluminium face and a condensed gothic is how a panel is engraved. Body "Archivo" 400 at 18px, the same family at reading size, because the manual should match the panel. One idea: condensation. Display is `clamp(4rem, 8vw, 6.22rem)` so it is 72px at the small end and about 112px at 1440, four times the body and about 6.2 times on a desk. Tracking `-0.03em`, because the condensed face can take it.
- Picture rule: cut paper, kept. The picture depicts the FM-1 as an aluminium rectangle cropped on the right, a wooden cheek on the left, four ink knobs of different sizes, and one ink carrier.
- Motion: calm, `sine.inOut`, 0.8 to 1.6s, opacity or a move under 12px, because the light is flat daylight and the low index drifts. Menus do not exist. The detent is 120ms. No `cubic-bezier(0.16, 1, 0.3, 1)`.
- Sound: opt-in FM tone, off by default, because the product is a sound and a clip the visitor did not ask for must not start. The toggle is "Hear the bell". Never autoplay.

## Objects

Features are states of one traveler, not cards. Shared metal, cheek, and knobs stay on the box. Each state group changes the line.

| Content | Object | id | data-object | How it differs |
| --- | --- | --- | --- | --- |
| Plain tone | entry tab and the carrier line | `#state-carrier` | carrier | Mild line, wood tab at the cheek, index near rest |
| Rising index | uneven sideband ticks | `#state-index` | sidebands | Three ticks, different heights, only in the middle of the pin |
| Bell | partial peaks at the cropped out | `#state-bell` | bell | Five ink circles, different radii, only when the index is high |
| Body | aluminium sheet | `#chassis` | chassis | One rectangle, cropped on the right, ink outline |
| Grip | wooden cheek with uneven glue lines | `#cheek` | cheek | Wide wood slab, five glue lines at uneven gaps |
| Knob | ratio | `#knob-ratio` | ratio | Largest radius, pointer near 2:1, one tick missing |
| Knob | index | `#knob-index` | index | Mid size, the only pointer that turns with the scroll |
| Knob | loop | `#knob-loop` | loop | Smaller, scratch ring, the detent |
| Knob | out | `#knob-out` | out | Cropped by the viewport edge, label parked before the crop |
| Makers | two punch marks | `#makers` | makers | Two circles, different diameters, no names |
| Price | sample tag | `#price` | price | Rotated -11 degrees, overlaps the cheek, says SAMPLE, no number |
| Place and consent | wooden offcut | `#offcut` | offcut | Irregular polygon, not a rectangle, after the pin |

`#traveler` is the SVG. Its three state groups are `#state-carrier`, `#state-index`, `#state-bell`.

## Storyboard

Budget: one hero signature (the carrier's journey), one supporting drift (the cheek, under 12px), one hidden delight (loop detent), one small surface (the offcut). Sound is the opt-in, off unless asked. Everything else is static. No intro. The headline and the button are visible on first paint.

- 0 to 30% of the scroll: the ink line is almost plain and the index pointer sits back, because the modulation index is still low. The out knob is already cropped. Caption: "A plain carrier waits at the aluminium edge." Touch: the same scrub on scroll. No drag. The button "Bend the carrier" is in the first viewport.
- 30 to 70% of the scroll: the line grows uneven peaks and the index knob turns, because scrolling raises the index. Sideband ticks show. Caption: "Index rises and the four knobs bend the line." Touch: the same scroll.
- 70 to 100% of the pin: the line is a bell and the peak circles appear at the cropped out, because a high FM index reads as a bell, not a louder copy of the sine. Caption: "It leaves as a bell, held at the wooden side." Touch: the same scroll. The pin is 200vh, scrub 0.8, under the 220vh cap. Captions stay beside the box, one line, under 18 words, never on a card.
- After the pin: only the offcut. Place, sample price with no invented number, consent, the missing-ratio line.

Reduced motion: no pin, no cheek drift, no travel. The same picture stays. A range labeled "Step the index" sets the three states. The button jumps that range to the bell and back. Touch targets are at least 44px.

Supporting: `#cheek` drifts 8px, `sine.inOut`, 1.4s, yoyo, because cut paper in daylight shifts a little. Off when reduced motion is set.

Delight: a tap on `#knob-loop` advances one detent in 120ms, `sine.inOut`, and the note "Knob three is the one people over-turn." appears. Touch is the tap. Hover does nothing required.

Small surface: `#offcut` in the footer.

Sound: "Hear the bell" starts a two-operator tone (carrier 220, ratio 3.49) only after the click, index following the scroll. "Stop the bell" fades it. If the context fails, the empty line shows.

## Removal

An idle spin on the ratio, loop, and out pointers. Built, then deleted. A row of spinning knobs is a synth-site costume. Only the index travels with the carrier. The other three stay where the two people left them.

## Voice

Headline: Bend a plain tone.

Subhead: One aluminium box, four knobs, a wooden side. Two people in Gothenburg.

- Button: Bend the carrier
- Empty: The oscillator stayed quiet. Tap the switch again.
- Footer: Halde FM-1, sample. Two people in Gothenburg. Hold the wood, not the metal.
- Consent: Knobs stay on this page. Nothing is saved.
- Missing: That ratio is not on the four knobs.
- Loading: Waiting for the carrier to sit still.

The funny line is the footer: hold the wood, not the metal. The brand is labeled sample on the mast, the tag, and the footer. No banned words.

## Genericness

Similar brief: a one-person pocket analog synth sold from Berlin, sliders, no wood.

The part this plan would have reused is "a line crosses a box and gets bigger." That part changed. The exit is an uneven bell at ratio 3.49, because FM partials are not a filter opening, and the second paper is the wooden cheek offset 6px, because this box has a wooden side and that Berlin slider does not. The dealt world stays Traveling object.
