# Moth Night sample

## Harvest

Facts only this night has:

1. The day hall lights are switched off before anyone is let in.
2. At the cloak desk each visitor is handed a UV torch: matte aluminium body, black filter glass, a wrist loop.
3. The filter glass is cold to the touch. The galleries cool once public hours end, and the calcite faces feel cold too.
4. Moth wings here are overlapping chitin scales. Open the drawer glass and they wipe off as dust.
5. In the white day light those scales read as melanin and buff dust.
6. Under the torch some scales answer rose and some answer a dull gold, the same rose as the calcite in the next case.
7. Calcite rhombs sit buff until a face is in the beam, then that face goes rose along the cleavage.
8. Insect drawers are glass-topped, cork-lined, with black enamel pins and a typed locality slip under each pin.
9. One tray has a bare pin: that moth was not set tonight.
10. One cello plays between the mineral wall and the insect drawers. It is acoustic: horsehair, a cake of rosin, no speaker.
11. The wings make no sound. What you hear is the bow and shoes on the stone floor.
12. The cabinets smell of camphor and old cork. The bow smells of rosin.
13. Phone flash is the enemy. It blinds the case and washes the rose back to buff.
14. People whisper. They say the rocks answer.
15. Torches go back in a basket before the day lights return, because white light undoes the color.
16. Vocabulary of the night: unit tray, locality, long-wave, scale, rhomb, rosin, cloak desk.
17. Time: after the day hall closes, night at the clerestory.

At least six are sensory: cold filter glass, cold calcite, camphor, rosin, the bow, silent wings, shoes on stone, buff dust versus rose.

## Emotion

Hush.

A visitor tells a friend: "I walked one moth wing from the drawer into the torch, and the dusty scales turned the same rose as the calcite while the cello sat there."

## Concepts

The site is a cloakroom ticket where the night is a perforated stub and tearing it starts the walk. Rival: any evening concert. FAIL, a concert already lives on tickets.

Replaced: The site is one moth wing where the drawer, the calcite, and the cello are three states of the same scales, and scrolling walks the torch. Rival: a planetarium night. A planetarium has a dark room and a beam, and it does not have chitin shingles, a calcite rhomb, or a cello bridge. Keep.

The site is a species name in huge letters, each counter holding a specimen. Rival: a poetry night. FAIL, cropped letters fit them, and this is also the rejected letters world.

Replaced: The site is a calcite rhomb you turn, each face a chapter of the night. Rival: a mineral club. They can turn a stone, and they do not have a moth wing or a cello on a face. Keep, but do not use it.

The site is the cello bow, the night one stroke, specimens as finger stops. Rival: a recital series. FAIL, the bow fits a recital.

Replaced: The site is the torch wrist loop, shed scales threaded on the cord, a pull sounding the open string. Rival: a cave tour with headlamps. They do not thread moth scales and they do not sound a cello. Keep, but do not use it.

## Pick

The moth wing. The visitor sentence is someone walking one wing from drawer dust into the torch until the scales match the calcite, with the cello as the last state. A stone you turn, or a cord you pull, is a different action. No merging.

Rejected world, operable document: a specimen card or a program would fit a rival museum late, and the page would be paper with the torch as a picture on the paper. The light source has to stay the handheld UV torch, not a desk lamp on a form.

Rejected world, letters as objects: giant cropped words would still be a type poster. Swap the name for a string quartet night and the letters still work. The wing does not.

## Visual system

Material the page is made of: overlapping chitin scale shingles, because the wings are platelets of chitin that wipe off as dust, and the picture rule is a swatch of one material.

Light source: the handheld UV torch in a hall whose day lights are already off, because that is the only lamp of the night. Brightness is the unlit oak case and melanin scales, not a black field and not a neon edge. The torch does not add a halo. It chooses which shade of the same shingles you see.

Palette, five hex values from that material:

- `#221C16` melanin scale and the oak case in the dark, because unlit wings and the wood drawers are this brown-black, not lamp black.
- `#8C7355` buff chitin, cork, unlit calcite, and the cello's maple, because day-light scales and the unlit stone are the same dry tan.
- `#E6D3B0` worn scale tip and the typed locality slip, because the scale tips are pale and the slips are that paper.
- `#D15A5A` rose answer, because calcite and some scales go this dusty rose under the torch, a stone color, not a lamp.
- `#D4B25A` gold answer, because other scales answer a dull mineral gold under the same torch.

Type: display face Petrona (https://fonts.googleapis.com/css2?family=Petrona:wght@600;700&family=Karla:wght@400;500;700&display=swap), because species names on a museum plate are a sturdy serif and this night is a plate of scales. Body face Karla, because the locality slips and the cloak card are plain humanist text, not the plate. Display `clamp(4.5rem, 6.6vw, 6rem)` (72px to 96px). Body `1.125rem` (18px). Smallest ratio is 72/18 = 4. Desktop is about 96/18 = 5.3. Letter-spacing on the display `-0.03em`, because the plate face at that size can take it. No italic second family.

Picture rule: accept the dealt material swatch. The hero depicts chitin shingles built from the shades above. Fluorescence is a flat fill on the shingles that the torch has reached, rose and gold, with hard edges. Rejected glow, neon stroke, and gradient wash, because the picture rule forbids them and the harvest's torch has a hard filter, not a halo. Grain is not the picture. It is the effect named for removal.

Motion: accept the dealt spring. One `back.out(1.4)` over 0.48s, once, on the wing at first arrival, because a moth overshoots a landing and then stops. The walk itself is a ScrollTrigger scrub at 0.8 with ease `none`, because the hall is a continuous path from drawer to stone to cello, and the dealt traveling-object build asks for scrub between 0.6 and 1. The pin flip and the bow toggle are instant, because people repeat them. Nothing else bounces. Menus are not on this page.

Sound: opt-in, default off, because the night has one acoustic cello and autoplay would break the hush. The toggle is "Hear the bow". On, it holds a quiet open C made in the browser. Off, silence.

## Objects

The page is the journey of one wing. Features are states of that wing, not cards.

| Content | Object | id | How instances differ |
| --- | --- | --- | --- |
| The night's insect, the traveler | Chitin shingles of one wing | `#wing` `data-object="wing"` | Each shingle differs in size, rotation, and state: melanin, buff, rose, or gold. A band of them is still dust until the torch arrives. |
| The mineral | Calcite rhomb with a cleavage and a chip | `#calcite` `data-object="calcite"` | Upper face starts buff, lower face is already rose, chip is the pale tip. The upper face turns rose when the torch reaches it. |
| The tool and the hours of darkness | UV torch, filter, wrist loop, click switch | `#torch` `data-object="torch"` | One torch in the hand. In the footer basket, three returned torches differ in length. |
| The music | Cello bridge, two strings, rosin cake with a groove | `#cello` `data-object="cello"` | Hidden until the last state. The bridge is maple-buff, the rosin is the rose of the calcite, the groove is worn. |
| The cloak desk, the ending | Basket of returned torches | `#basket` `data-object="basket"` | Three torches, different lengths, plus one empty loop for the bare pin's news. |
| The empty tray | Bare enamel pin and its slip | `#bare-pin` | The only pin you can flip. The other pins are smaller or larger and stay put. |

## Storyboard

Budget: one hero signature (the torch edge across the shingles), visible in the first viewport. One supporting moment (the calcite face finishes turning rose). One supporting moment (the bridge and rosin arrive). One hidden delight (flip the bare pin). One small surface (the footer basket). Everything else is static and readable. Techniques used: the traveling-object pin scrub, one fidget, opt-in sound. That is three.

Beats, inside a pin of about 130vh, scrub 0.8, under the 220vh cap:

0 to 30% of the scroll: the waiting shingles along the beam turn from dust shades to rose and gold, because you are still walking out of the drawer and the filter has not reached them yet. Caption, beside the wing: "The drawer looks like dust." Touch: the same scroll. The button "Lift the torch" jumps this stretch. No drag.

30% to 65% of the scroll: the calcite's upper face swaps from buff to rose, and the drawer cork and spare pins fade, because the mineral answers only when the torch reaches that face. Caption: "The torch asks. Calcite answers rose." Touch: the same scroll.

65% to 100% of the scroll: the cello bridge, two strings, and the rosin cake appear beside the wing, because the cello sits between the mineral wall and the drawers. No second bounce. Caption: "One cello. The wings stay silent." Touch: the same scroll.

Reduced motion: no pin, no travel, no spring. The signature picture stays, the bridge is shown in place, and "Lift the torch" jumps to the basket. Touch targets stay at least 44px.

First visit only: the wing settles 16px with `back.out(1.4)` in 0.48s. Headline and button are visible the whole time. The settle is killed on wheel, touch, or the button. Repeat visits skip it via `sessionStorage` key `moth-night-seen`.

Delight: tap the bare pin. Its locality slip turns upside down in 80ms. It is the empty state, and it is a tap, not a hover.

Small surface: the footer basket.

Live hour, read once: if the local hour is 19, 20, or 21, the footer line says the hall lights are off right now and two shingles start already gold. Any other hour, the line says the day lights are still on outside this page. A clock that does not change the page is not used.

After the pin, the spacer carries a non-interactive continuation of the same wing, stone, and bridge so the long pin is not an empty band in a full-page capture. It is the same three states, not a second concept. The live viewport stays on the pinned scene until the basket.

## Removal

Build a full-scene scale-dust grain: `feTurbulence` base frequency 0.72, 3 octaves, stitched, on one rect at opacity 0.08, blend soft-light. Then delete it. The shingles are already the dust, the picture rule refuses grain as a default, and a noise veil does not walk the torch. A console log does not count. The `REMOVED` comment stays.

## Voice

Headline (5 words): Dust, until the torch asks.

Subhead: Lights off in the hall: moth scales, calcite, and one cello.

Button: Lift the torch

Empty state: No moth in this tray. The pin is waiting.

Footer: Return the torch to the basket. Day lights wash the rose off the calcite.

Consent: No visitor list. The moths were pinned long before you.

Loading: The filter glass is still cold.

The footer line is the oddly specific one. A stranger can tell the brand from the basket alone. The brand is marked sample on the stamp and in the footer. No banned words.

## Genericness

Similar brief: an aquarium bioluminescence night, or a planetarium after-hours. For them this plan would have been a dark room and a beam that reveals a hidden glow.

That part changed. The beam is not a glow. It is a hard edge across chitin shingles, the lit shades are the same rose and gold as a calcite rhomb, and the last state is a cello bridge and a rosin cake. An aquarium night has no calcite cleavage and no bridge. The dealt world stays the traveling object. Escaping into black-plus-acid, or into a cream page with an italic serif, was refused. The dark is melanin and oak. The rose and the gold are flat mineral fills.
