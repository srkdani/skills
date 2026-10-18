# Halde FM-1, sample

Deal used: Operable document. Rejected: Bench in stages, because the brief is one finished voice, not a milling sequence, and stage notes would invent a factory. Rejected: Unlike objects on a surface, because Halde has one instrument, and four knobs are controls on that panel, not four goods.

Motion kept: mechanical, `steps(6)` or linear, 80 to 160ms a step, no overshoot, because the knobs are detents. Repeated controls are instant.

Picture kept: cut paper. The face is a flat machined plane, so flat sheets fit. Two papers (aluminium, oak cheek) and one ink. Shadows are a second sheet offset 6px, not a box-shadow.

# Harvest

1. The chassis is a small aluminium plate, cool on the fingers, mill-flat, not a keyboard.
2. Four knobs and no screen. The hand spans the whole face.
3. One wooden side panel, a cheek. You lift the box by the wood. The palm warms it. The metal stays cold.
4. FM means a modulator pushes a carrier. Integer ratios ring. Odd ratios go metallic and inharmonic.
5. Index is how hard the modulator bites. Low index is nearly a sine. High index is a clang.
6. Feedback lets an operator push itself. The tone grows a rasp.
7. Decay is how fast the metal ring dies. Short decay is a knock. Long decay is a bell that hangs.
8. Two people build it in Gothenburg, on a bench, not a line. The wood-to-aluminium joint is a hand joint.
9. Gothenburg harbor light is grey and low. On 18 October the sun is gone late afternoon, so a bench lamp is the working light.
10. Brushed aluminium takes fingerprints and a dull oxide skin. It is not chrome.
11. A small knob lands in detents. The fingertip feels a click, not a fader glide.
12. Close operators beat: a slow throb when two frequencies almost match.
13. The legend is small and bent over: ratio, index, feedback, decay. You read it on the bench.
14. The instrument is one voice. It does not play a song by itself.
15. The cheek shows edge grain. The end of the wood is visible at the corner.

At least six are physical or sensory: cool aluminium, warm cheek, harbor light, lamp, fingerprint oxide, detent click, clang, beating throb.

# Truths

1. Four knobs and no screen. The whole voice is ratio, index, feedback, and decay. Rival: Korg Volca FM, which keeps the algorithm behind a tiny screen and a menu. The Volca does not let four turns be the entire instrument.
2. You lift it by one wooden cheek. The face you turn is cold aluminium. Rival: an all-metal desktop module (a steel pedal, a blank Eurorack plate). That rival is one material and has nothing warm to lift by.
3. Two people, one Gothenburg bench. The lamp follows the harbor hour, because daylight there drops early. Rival: Yamaha's FM factory. A line does not have a bench lamp or a cheek screwed on by two people.

# Emotion

Itch.

"I stepped the index and the wooden disc shoved into the aluminium one until the legend said clang."

# Concepts

1. The site is the FM-1 panel you are holding, where the four knobs become the only chapters and turning index detents a wooden modulator into an aluminium carrier. Rival: a many-knob guitar pedal brand. Their panel has no operator pair and no cheek you lift by. Keep.
2. The site is a Gothenburg work ticket, where build stages become stamps and a pencil tick mills the face. Rival: a contract metal shop. A work ticket fits them. FAIL.
3. The site is a speaker cloth, where partials become holes and a scrub opens the grille. Rival: a loudspeaker maker. A grille fits them. FAIL.

# Pick

The held panel. The visitor turns index and sees the wood disc step into the aluminium disc, which is the sentence they would tell. No second concept mixed in. The bench is only the desk under the document, which this world already requires.

# Visual system

- Material: mill aluminium sheet plus one oiled oak cheek, because the chassis is aluminium and the side panel is the only wood.
- Light: a tungsten bench lamp in Gothenburg, because harbor daylight is gone by late afternoon in October and two people work under that lamp. The lamp hits the panel. The desk outside the pool is the darker oak. This is not a chosen dark mode.
- Palette: aluminium `#E4E2D8` because mill sheet under tungsten goes warm grey, not chrome. Cheek `#BE8A50` because oiled oak in the lamp is this brown and the engraved word on it stays readable. Bench `#5C3E2A` because the same oak outside the lamp goes dark. Ink `#1B1612` because the legend is engraved dark. Four hexes, all from the sheet, the cheek, the unlit bench, and the engraving.
- Type: display "Antonio" from `https://fonts.googleapis.com/css2?family=Antonio:wght@700&family=Azeret+Mono:wght@500&family=Schibsted+Grotesk:wght@400;600&display=swap` because a pantograph cuts tall condensed letters into a nameplate. Body "Schibsted Grotesk" because the small print is a Swedish workshop grotesque. Legends "Azeret Mono" at 12 to 14px because knob scales are tick labels. Display 88px, body 18px, just under 5 times, because the nameplate has to stay on the document and still clear the 4 times rule. Tracking on the display `-0.03em` because the condensed face can take it.
- Picture: cut paper, kept. The drawing shows the panel, the cheek, four knobs, and two operator discs. No photograph exists, so a stamp says placeholder. One grade for the whole page.
- Motion: mechanical. Knob travel uses linear 120ms a step, or `steps(6)` across a full swing. No overshoot. Scroll detents by quantizing to six steps. Menus, the sound toggle, and patch taps are instant.
- Sound: opt-in, off by default. A 160ms FM blip when a detent moves, only after the visitor taps Sound. Never autoplay.
- Grade: tungsten cut-paper. Aluminium and oak sheets, one ink, shadow offset 6px. Named in a `GRADE:` comment.

# Objects

- `#panel` `data-object="face"`: the aluminium document, `min(960px, 100%)` wide. The page is this sheet. It differs by being the only full face.
- `#cheek` `data-object="cheek"`: oak strip on the right edge, grain cut in ink, narrower than the face. The lift lives here.
- `#knob-ratio` `data-object="knob-ratio"`: smallest sweep marks, spoke count follows it.
- `#knob-index` `data-object="knob-index"`: larger disc, a double wear ring, because this is the knob fingers hit most.
- `#knob-feedback` `data-object="knob-feedback"`: a loop tick on the cap, pointer starts low.
- `#knob-decay` `data-object="knob-decay"`: six tail ticks, fewer filled when the ring dies fast.
- `#operators` `data-object="operators"`: wood modulator disc and aluminium carrier disc, ink bridge, sizes differ.
- `#slip` `data-object="slip"`: small oak ticket on the face with place, sample price, and the placeholder stamp. Shorter than the cheek.
- `#joint` `data-object="joint"`: bottom screw line, two different slot angles, the footer engraved in the metal.

# Budget

- Small, truth 3, `#lamp-note` `data-live="time"`: on load, the Europe/Stockholm hour sets the engraved line to early bench, harbor light, or lamp on. Under 300ms, a text swap, does not cover the headline.
- Small, truth 1, `#voice-state`: the legend reads BELL, METAL, or CLANG as index steps, and the tab title follows. Visible on the discs.
- Small, truth 2, `#oxide`: an ink fingerprint arc on the aluminium beside the index knob. Static, the oxide fact.
- Small, truth 2, `#cheek`: a tap stamps LIFT on the wood in one linear step under 300ms. Hover only adds a grain emphasis on fine pointers.
- Small, truth 3, `#photo-stamp`: "Bench photo: placeholder." The missing picture, same grade, no stock photo.
- Small, truth 1, `#empty-state`: all four at zero shows "All four at zero: a sine with nothing to modulate."
- Small, truth 3, `#joint`: the footer is the screw line, not a link row.
- Medium, truth 1, `#knob-bay`: four stepped knobs redraw spokes, overlap, feedback arc, and decay ticks. Touch path: range inputs at least 44px, keys work.
- Medium, truth 1, `#patches`: three unequal punch stubs (different width, one rotated, one overlapping) set the four detents. Touch path: tap a stub.
- Medium, truth 3, `#lamp-flap`: tap the lamp flap to read the other Gothenburg hours. Touch path: a 44px flap. Initial state comes from the live hour.
- Big, truth 1, `#operators`: the signature. 0 to 30% of the scroll: the wood modulator steps into the aluminium carrier across six detents, because index is a shove and there is no screen to hide it. Touch: the index knob and the "Step the index" key run the same six steps. Reduced motion: no scroll travel, the key and the knob still step, layout stays.

Technique: big moment is a scroll and drag scrub (list item 20) quantized to mechanical steps. Mediums add an instrument readout (item 18) and the live hour (item 28). Nothing else.

# Rhythm

1. Panel: a held face. Nameplate, discs, knobs, and the slip are parts of one sheet.
2. Punches: three overlapping stubs of different sizes, names stamped on them, no heading and no caption row.
3. Joint: one horizontal screw bar with the footer cut into it.

No section is heading, then text, then cards. The slip's place, sample price, and action sit on the panel in the first viewport.

# Removal

A continuous orbit: a dashed ink ring spinning around the carrier. It will be built, then deleted, because truth 1 is a detent shove and an idle orbit does not land on a step. The `REMOVED:` comment stays.

# Voice

- Headline: "Four knobs. No screen."
- Subhead: "Halde FM-1, sample. An aluminium FM voice with one wooden cheek, made by two people in Gothenburg."
- Button: "Step the index"
- Empty: "All four at zero: a sine with nothing to modulate."
- Footer: "Two people, one wooden cheek, Gothenburg. The face stays cold. Halde is a sample."
- Missing: "Bench photo: placeholder. The panel stands in."
- Loading: "The aluminium is still cold."

The empty line is the oddly specific one. No banned words.

# Genericness

A similar brief is any four-knob desktop synth from a small European shop. For that page I would have written a dark field, a product photo, and three cards: small, handmade, musical. That part is gone. Here the document is the face, the wood is a cheek you can stamp, and the picture moves only when index detents. Swap in a generic mini synth and the cheek-plus-operator collision stops making sense.

# Batch 1 gate

Batch 1 gate: The page is still the FM-1 panel you hold, with the headline, the Gothenburg sample price, and Step the index on the aluminium sheet, and index already steps a pair of discs.

# Batch 2 gate

Batch 2 gate: The signature is the oak modulator stepping into the aluminium carrier across six detents, by scroll and by the index key, because four knobs and no screen means the shove is the whole voice.

# Batch 3 gate

Batch 3 gate: The knob bay, the three unequal sample punches, and the lamp flap each change a real detent or hour, and no fourth control was added.

# Batch 4 gate

Batch 4 gate: The Stockholm hour, the bell or clang legend, the fingerprint, the lift stamp, the placeholder, the zero-sine line, and the screw footer sit on the document and stay off the Step the index key.

# Batch 5 gate

Batch 5 gate: After the shots, the stuck cold-aluminium bar was taken off the bench, the discs were enlarged so the shove reads first, and the spinning orbit was deleted because a detent does not idle in a circle.
