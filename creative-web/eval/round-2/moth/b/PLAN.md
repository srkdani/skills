# Moth Night, sample

Deal used: Walk into the place. Motion accepted: Calm. Picture accepted: Material swatch.

Rejected worlds: Traveling object, because a moth shipped through states would be a mascot journey and the visitor walks into a hall that is already dark. Letters as objects, because the product is the night, not a phrase, and a mineral stuffed in a letter counter would be a headline costume.

## Harvest

Facts only this night has:

1. The house lights are switched off at the oak door before anyone enters.
2. Each visitor is handed one metal UV torch with a single switch.
3. A cello plays live and unamplified, bow hair on string, no PA.
4. The stone floor of the court gives the note back.
5. Moth wing scales sit like dust. A brush lifts them.
6. Fluorite faces answer the torch in a dusty green.
7. Calcite answers the same torch in an earthy orange.
8. The cases are oak, lined with dark baize.
9. Labels are pinned paper slips with catalog numbers such as F-14 and M-22.
10. After the day galleries close, the court is cooler than the street.
11. Open drawers smell of oak and camphor.
12. Torches are returned to a basket by the oak door.
13. One case on the route stays locked and dark.
14. Place: West Mineral Court, a sample hall.
15. Sample hours: torches 19:00 to 22:00, cello from 19:30, basket by 22:40.
16. People whisper, because the bow is bare.

At least six are physical or sensory: lights off, torch metal, bow sound, stone echo, scale dust, fluorite color, calcite color, cool air, camphor.

## Truths

1. One UV lamp is answered by both moth scales and fluorite. Rival: a gallery cocktail night. They dim a room and never put one lamp on a moth and a mineral. They do not have this in this form.
2. The cello is unamplified on stone, so the hall is the amplifier. Rival: a museum DJ night. They bring a PA. They do not leave a bare bow in the court.
3. The building lights are off, so a visitor sees only the face the torch finds. Rival: the same court at noon. House lights stay on and every label is lit at once.

## Emotion

Hush.

"I swept one torch and the moth scales and the fluorite took the same night color, while the cello stayed a quiet line on the stone."

## Concepts

1. The site is a specimen case where moth scales and fluorite become two answers of one UV lamp, and sweeping the torch does the lighting. Rival: a gallery cocktail night. Their dim room has no shared lamp on a moth and a mineral. Keep.
2. The site is a concert poster where the cello is the headline and the insects are footnotes. Rival: a chamber concert. FAIL. It fits them. Replaced: the site is a spreading board where each moth is a pinned scale map and a tap turns that specimen toward the torch. Rival: a butterfly house. They keep living insects in a bright greenhouse, not pinned scales in a lights-off court with a bare bow. Keep.
3. The site is a field notebook where the night is a list of entries. Rival: a museum class page. FAIL. Replaced: the site is the oak-door basket where returned torches are the guest list and taking one leaves a gap. Rival: a coat check. A coat check has hooks, not UV torches that wake fluorite. Keep.

## Pick

The specimen case. The visitor sweeps one torch and sees moth scales and fluorite take the same night color, which is the sentence they would say. The spreading board and the basket stay as rooms inside this hall. They are not a second concept.

## Visual system

- Material: oak case, dark baize lining, pinned paper, moth scales, and mineral faces, because those are the things in the hand and in the case.
- Light source: the handheld UV torch, because the house lights are off and that torch is the only lamp. Brightness is the oak and the paper. The torch does not draw a neon edge. It chooses which shade of the material is forward.
- Palette: baize `#2A2420`, oak `#6B4E3A`, label paper and daylight scale `#E4D3B4`, fluorite under the torch `#6E8F7A`, calcite under the torch `#C4623E`, because those are the lining, the case, the slip, the green face, and the orange face.
- Type: display Cinzel, file from `https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700&family=Newsreader:opsz,wght@6..72,400;6..72,600&display=swap`, because the case plate is engraved classical caps. Body Newsreader at 18px, because the slip is a field note read by torch. Display `clamp(64px, 7vw, 96px)`, which is at least 4 times the body, because a brass plate is the loudest thing on the case and still has to sit on the wood without pushing the torch button out of the first view. Tracking 0.03em, because engraved brass needs air between letters.
- Picture rule: accepted, material swatch. The hero is moth scales and mineral faces built from a few shades of those materials. No glow, no neon edge, no gradient blob. A missing court photograph is a drawn plate marked placeholder.
- Motion: accepted, Calm. `sine.inOut`, 0.8s to 1.6s, opacity or a move under 12px, because the hall is hushed and the answer is a shade change, not a flying beam. Repeated controls are instant or under 150ms. Parallax is capped at 10px so the dealt drift stays under 12px. The world's 1% to 3% layer shift is kept on a narrow screen, and on a wide screen the cap wins so the case does not sway.
- Sound: opt-in, one short bow tone, off by default, because the cello is live and a page must not autoplay. The button is the only way it starts.
- Grade: one flat torch light on scale and stone. Daylight shade and torch shade are two flat fills of the same material, one opacity between them. No second grade.

## Objects

- Hours and status: brass door plate `#door-plate`, object `plate`. The words change with the hour. One screw is drawn missing.
- Place: hanging paper tag `#court-tag`, object `tag`. It hangs from the left stile and names West Mineral Court.
- Action: UV torch `#torch`, object `torch`. One barrel on the lip. Taking it lifts the barrel 6px.
- Shared lamp: hawk-moth wing `#hawk-wing`, object `hawk-moth`. Wide scale field, one loose scale.
- Shared lamp: fluorite `#fluorite`, object `fluorite`. Large chunk, one corner chipped, slip F-14.
- Second stone: calcite chip `#calcite`, object `calcite`. Smaller than the fluorite, warmer face, slip C-3.
- Drawer moth: `#drawer-moth`, object `drawer-moth`. Narrower than the hero wing, one row of scales missing.
- Cello: `#cello`, object `cello`. Two bouts, a neck, one string. Geometric, not a portrait.
- Bow: `#bow`, object `bow`. A thin stick that settles on the pegbox, the bridge, or the stone.
- Return: basket `#basket`, object `basket`. Three torches of different lengths and one gap.
- Shut route: locked drawer `#locked-drawer`, object `locked`. A closed front, no specimens inside.
- Missing photo: `#placeholder-plate`, object `placeholder`. A paper plate that says placeholder.

## Budget

Big, truth 1, technique 10 (the torch is the tool). Element `#signature`.

Storyboard: 0 to 30% of the scroll, the shared progress moves from 0.72 to 1, so the moth scales and the fluorite (and the small calcite chip) ease from a mixed shade to a full torch shade, and the wing settles 8px, because truth 1. The colors are already in the first viewport at rest, so the lamp is visible before any scroll. Touch: the range "Sweep the torch" sets the same progress, including back to daylight. Fine pointer: moving across the case sets the same progress, gated on `(hover: hover) and (pointer: fine)`. Reduced motion: no settle, no parallax, the slider still lights the faces.

Medium, truth 1. Element `#drawer`. Tap fluorite, calcite, or the drawer moth. Only that object takes the torch shade. The others stay daylight. Touch path: the objects are buttons. Swap is under 150ms.

Medium, truth 2. Element `#alcove`. Tap pegbox, bridge, or stone. The bow settles under 12px with `sine.inOut` in 1.1s, and the plate names where the note goes. Touch path: three buttons. Reduced motion: the plate changes and the bow jumps, no travel.

Small, truth 3. `#door-plate` with `data-live="time"`. Local hour sets the plate and the rail: before 19:00 "House lights still on", 19:00 to 21:59 "Torches are out", after 22:00 "Last bow, then the basket". The rail color changes with that state.

Small, truth 1. `#loose-scale`. A tap shifts one scale 4px and flips its shade, under 100ms.

Small, truth 1. `#last-lit`. A slip names the face last lit, and the tab title follows.

Small, truth 3. `#basket`. Returned torches, unequal, one gap, the footer line on the door.

Small, truth 3. `#empty-sweep`. When the torch progress is near daylight: "This face is still daylight. Sweep the torch."

Small, truth 3. `#locked-drawer`. Tap shows "That case is not on tonight's route."

Small, truth 1. `#placeholder-plate`. "Placeholder. No archive photo of the court." The drawn swatches are the grade.

No intro. The headline and the torch button are in the first paint. A task-like event page does not get a preloader.

## Rhythm

1. Case mouth: one framed room, scales and stone inside, words on the brass plate and the hanging tag.
2. Drawer: a pulled tray of three unequal specimens you aim, stamped on the drawer front.
3. Alcove: one tall cello against stone courses, three taps on the instrument and the floor.
4. Door: a pile of torches in a basket, the return line on the oak.

No section is a heading, then text, then cards.

## Removal

Case-dust grain. An SVG turbulence overlay on the case, opacity about 0.08, because scale dust is in the harvest. It will be built, then deleted. The scales are already the dust. A second dust layer does not serve the lamp.

## Voice

- Headline: "Moth and stone."
- Subhead: "One UV lamp finds both. Lights off. The cello has no amp."
- Button: "Take a torch"
- Empty: "This face is still daylight. Sweep the torch."
- Footer: "Leave the torch in the oak basket. The moth stays in the case. Moth Night, sample."
- Missing: "That case is not on tonight's route."
- Loading: "Waiting for the house lights to die."
- Odd line, on the fluorite slip: "If your cuff goes green, you leaned on the fluorite."

No banned words. Sample sits beside the brand in the plate and the footer.

## Genericness

Similar brief: a museum late night with a DJ and a bar.

The part that would have fit them: a dark full-bleed hall, one bright accent, and three highlight cards for music, drinks, and tickets.

Changed: the page is the inside of an oak specimen case. The only strong colors are fluorite green and calcite orange, as flat faces of those stones. The action is sweeping one torch so moth scales and fluorite answer together. A DJ night has no spreading board, no F-14, and no basket of UV torches. This does not escape into cream paper, an italic serif, glass, or a black field with an acid accent. The dark is baize inside oak, because the case is lined.

## Gates

Batch 1 gate: The grey case still holds one lamp for moth and stone, with hours, the torch button, and a working sweep in the first view. I shortened the grey blocks so the action was not pushed below the fold.

Batch 2 gate: The signature is now the oak case itself: scale wing, fluorite, and calcite share one torch shade, and the sweep, the torch button, and the court hours stay in the first view. I clipped the scales into a wing and lifted the stones so the lip stopped covering their slips.

Batch 3 gate: The mineral drawer is a pulled tray of unequal faces, and a tap rests the same lamp on one of them, which is truth 1 with an aim instead of a shared sweep. I redrew the hawk moth in oak so its scales were not the same color as the paper tray. The alcove is the second medium: a geometric cello on stone courses, and a tap names where the bare bow sends the note.

Batch 4 gate: The smalls are on the objects: the door plate reads the local hour, a loose scale can be tapped, the basket has unequal torches and a gap, the locked case and the placeholder plate sit by the door. I moved the cuff line onto the brass plate because it was covering the calcite slip.

Batch 5 gate: Reduced motion and the narrow screen keep the torch button, the sweep, and the court hours in the first view, and the case-dust grain is deleted because the scales already are the dust. Score after the 300px thumbnail and the scroll: T1 2, T2 2, T3 1, T4 2, R1 2, R2 1, R3 2, creative 12, floor 4. The lining stays dark because the house lights are off and the oak frame is the room. The idea still matches the pick: a specimen case where one UV torch makes moth scales and fluorite answer together.
