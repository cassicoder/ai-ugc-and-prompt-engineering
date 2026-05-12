# Image Prompts (Nano Banana)

For Higgsfield Nano Banana 2. Vertical 9:16. Reference image always attached.

This file is the implementation reference. For the workflow that decides *what* to put in a prompt, read `workflows/image-accuracy-v1.md` first.

---

## Settings (always)

```
model: nano_banana_2
aspect_ratio: 9:16
count: 1
medias: [{role: "image", value: "<reference UUID>"}]
```

Higgsfield may auto-route to Nano Banana Pro and ignore `resolution`. That's fine. Don't fight the router.

---

## The locked template

```
First-person POV, vertical 9:16, the camera is the creator's eyes standing at adult height in [SETTING], looking [DIRECTION] at a [PRODUCT NAME] [POSITION].

A man's right arm extends forward from the bottom-right of the frame, [HAND ACTION on SPECIFIC PART], palm in firm contact. [ARM CLOTHING], no jewelry.

Hand details: light olive skin with visible pores, visible dark arm hair across the forearm, a small scar on the second knuckle, a faint vein on the back of the hand, short clean nails, slight motion blur on the fingertips, natural finger shadows on the [SURFACE].

CRITICAL product accuracy — the [PRODUCT NAME] matches the attached reference image exactly: [SILHOUETTE]. [COLORS WITH SURFACE LOCATIONS]. [TEXTURE WITH NEGATIVE CONTRAST]. [3-5 FEATURES WITH NEGATIVE CONTRAST AT EACH AMBIGUITY POINT].

Setting: [3 lived-in clutter items].

Lighting is flat and slightly uneven, [LIGHT SOURCE].

Real person, real room, real phone — casual amateur capture, no professional lighting, no beauty filter, no glamour.
```

Target length: 130–180 words. Single paragraph (the bracketed paragraphs above are for legibility; combine into one block when sending).

---

## Section-by-section

### POV / framing

Default is **first-person POV** at adult standing height (camera at eye level, looking forward at the product a few feet away). The arm extends forward from the bottom-right of the frame.

Wrong: "top-down view" or "bird's-eye angle" — looks like a stock-photo overhead shot.

Right: `the camera is the creator's eyes standing at adult height ... looking forward at [product] a few feet away`.

### Hand block

Use this every time:

```
A man's right arm extends forward from the bottom-right of the frame, [hand action on specific part], palm in firm contact. [arm clothing], no jewelry. Hand details: light olive skin with visible pores, visible dark arm hair across the forearm, a small scar on the second knuckle, a faint vein on the back of the hand, short clean nails, slight motion blur on the fingertips, natural finger shadows on the [surface].
```

Hand action verbs that work (locked):
- `fingers gripping the [edge / handle / tube]`
- `fingertips pressing into [the cushion / fabric / surface]`
- `palm resting flat on [the tabletop / panel]`
- `fingers wrapping around [the bar / chain / pole]`

Hand action verbs that fail (model floats the hand):
- `hand near the product`
- `hand reaching toward`
- `hand hovering above`

Specify contact. Always.

### Arm clothing rotation

Cycle across products so a batch doesn't look like one creator:

1. Sage green quarter-zip pullover sleeve cuff
2. White short-sleeve t-shirt edge, bare forearm
3. Black short-sleeve t-shirt edge, bare forearm + thin black silicone watch
4. Charcoal grey hoodie sleeve cuff
5. Navy plaid flannel sleeve rolled at the elbow
6. Grey short-sleeve t-shirt, bare forearm + thin gold bead bracelet

Never the same on adjacent products.

### Product spec sentence (the make-or-break)

This is the sentence that has to carry product accuracy. Lead with the phrase `CRITICAL product accuracy — the [PRODUCT] matches the attached reference image exactly:` and then list:

1. Silhouette (one shape word)
2. Colors mapped to specific surfaces (`yellow on top, teal on outer side band`)
3. Texture with negative contrast (`smooth flat chenille — NOT boucle, NOT bumpy`)
4. 3–5 features with negative contrast at each ambiguity point

See `workflows/image-accuracy-v1.md` for the ambiguity-audit table that tells you which words need negative contrast.

### Setting (hard cap: 3 items)

3 lived-in clutter items. More than 3 = model averages into "decorated room" instead of placing them.

Good (lived-in):
- `a half-empty coffee mug on the floor`
- `a folded throw blanket on the corner cushion`
- `a phone charger draped on the rug edge`
- `a pair of slip-on slides off to the side`
- `a green garden hose coiled on the grass`
- `a stack of two open books`

Bad (signals "interior decorator"):
- `decorative pillows arranged`
- `fresh flowers in a vase`
- `matching coordinated decor`

### Lighting

```
Lighting is flat and slightly uneven, [light source].
```

Sources:
- `normal indoor warm tungsten room light`
- `soft natural daylight from a window`
- `warm overhead lamp mixed with afternoon daylight`
- `bright direct midday sunlight from one side` (outdoor)
- `soft natural daylight from the side mixed with the [product's own light source]`

Banned: `cinematic lighting`, `soft golden hour`, `studio lit`, `professional lighting`, `rim light`, `soft focus`.

### Closer (locked, do not modify)

```
Real person, real room, real phone — casual amateur capture, no professional lighting, no beauty filter, no glamour.
```

This suppresses Nano Banana's commercial-photography defaults. Don't paraphrase it.

---

## Realism upgrades (use when high realism required)

### Enhanced hand block

```
Hand details: light olive skin with visible pores, visible dark arm hair across the forearm, a small scar on the second knuckle, a faint vein on the back of the hand, short clean nails, a silver signet ring on the pinky finger, a thin gold bead bracelet on the wrist, slight motion blur on the fingertips, natural finger shadows cast on the surface beneath the hand.
```

### Phone-camera vibe override (one sentence)

Add before the closer:

```
The image has slight phone-camera characteristics: subtle grain in the shadows, slightly off-axis tilt of about three degrees, natural unedited color cast.
```

### Setting realism boosts

| Generic | Real-phone version |
|---|---|
| `a small green plant` | `a small green plant with a few browning lower leaves` |
| `a coffee mug` | `a half-empty coffee mug with a faint lipstick mark on the rim` |
| `a side table` | `a side table with a faint water ring near the edge` |
| `a hardwood floor` | `a hardwood floor with a few faint scuffs near the corner` |

Use sparingly — these add tells without bloating the prompt.

---

## Banned phrases

| Banned | Why |
|---|---|
| `iPhone selfie capture` | Triggers polished influencer-selfie aesthetic |
| `0.5x ultrawide lens` | Fisheye distortion + AI artifacts |
| `cinematic` / `4k quality` / `HDR` | Triggers commercial polish; quality is already set |
| `top-down view` / `bird's eye` | Wrong framing for product UGC |
| `CAPS for emphasis` | Model often does the opposite |
| `--no [thing]` | Doesn't parse |
| Phonetic respellings (e.g. `OR-anj`) | Image model doesn't care; for video the dash is read literally |

---

## Worked examples

### Example 1 — RIWENGO Double Egg Chair

Spec card:
```
SILHOUETTE: wide horizontally-oval double-wide egg, two people side by side
COLORS: black PE wicker shell, cream tufted cushions, black metal stand
TEXTURE: dense woven PE wicker in curved horizontal rib pattern
FEATURES: one wide seat cushion, one wide back cushion, two cream accent pillows, one bone-shaped headrest pillow, X-shaped 4-leg cross base, two heavy black hanging chains
AMBIGUITY POINTS: "double" → could mean 2 separate chairs. "wicker" → could mean thin natural rattan.
```

Negative-contrast rewrite:
- `DOUBLE-WIDE single shell large enough for two adults side by side — NOT two separate chairs`
- `dense woven black PE plastic wicker — NOT thin natural rattan`

Final prompt:

> First-person POV, vertical 9:16, the camera is the creator's eyes standing on a wood deck at adult standing height, looking forward at a black wicker DOUBLE-WIDE hanging egg chair built for TWO PEOPLE to sit side by side. A man's right arm extends forward from the bottom-right of the frame, fingers resting on the cream tufted seat cushion, palm in firm contact. White short-sleeve t-shirt edge at the shoulder, bare forearm, no jewelry. Hand details: light olive skin with visible pores, visible dark arm hair across the forearm, a small scar on the second knuckle, short clean nails, slight motion blur on the fingertips, natural finger shadows on the cream cushion. CRITICAL product accuracy — the RIWENGO DOUBLE Hanging Egg Chair matches the attached reference image exactly: the wicker egg shell is WIDE AND HORIZONTALLY OVAL, roughly twice the width of a single egg chair, with a flattened wide horizontal silhouette so two adults can sit hip-to-hip inside, the wicker is black PE rattan woven with curved horizontal ribbed lines forming the egg shape, the inside is filled with thick CREAM tufted cushions (one wide seat cushion across the bottom, one wide tufted back cushion across the back, two small cream accent pillows in the corners, one bone-shaped cream headrest pillow), the chair hangs from two heavy black metal chains attached to a black metal arched hanger arm rising from a black metal cross-base stand on the ground (X-shaped four-leg base). This is a DOUBLE egg chair NOT a single. Setting: a half-empty coffee mug on the wood deck boards, a folded cream throw blanket draped over the seat corner, a small green plant in a terracotta pot to one side. Lighting is flat and slightly uneven, soft natural late-afternoon daylight from the side. Real person, real room, real phone — casual amateur capture, no professional lighting, no beauty filter, no glamour.

Result: produced a correct DOUBLE-WIDE oval egg chair on the first fire after the negative-contrast rewrite. Previous version without the contrast produced a single egg.

### Example 2 — Weture U-Shape Chenille

Spec card:
```
SILHOUETTE: low U-sectional with chaise on both ends
COLORS: cream off-white throughout, dark espresso brown legs
TEXTURE: smooth flat chenille fabric
FEATURES: 3 loose back cushions, 2 cream throw pillows, espresso tapered legs at each corner
AMBIGUITY POINTS: "chenille" → defaults to boucle. "U-shape" → could mean L-shape.
```

Negative-contrast rewrite:
- `SMOOTH FLAT chenille fabric, almost like fine velvet — NOT boucle, NOT bumpy, NOT ribbed`
- `U-shape with a chaise extending from each end — NOT L-shape, NOT a single straight sofa`

Resulted in a clean first-fire match (after v1 failed because the prompt just said "chenille").

---

## Post-fire verification

After generation:
1. Download generated PNG
2. Build a side-by-side with the reference (ref left, generated right, same height)
3. Audit on **product accuracy only** (color, silhouette, texture, features). Hand placement and background are separate concerns.
4. If FLAG → identify the failed spec word → add a line to the ambiguity table in `workflows/image-accuracy-v1.md` → re-fire with the contrast.
