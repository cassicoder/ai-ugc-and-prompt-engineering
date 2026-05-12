# 02.01 — Image Prompt Rules

For Higgsfield Nano Banana 2. 4k. 9:16. Reference image ALWAYS attached as media input with `role: "image"`.

---

## The skeleton (use this every time)

```
[FORMAT]. [POV/FRAMING]. [HUMAN BLOCK — arm/hand/clothing/imperfections]. The [PRODUCT] matches the attached reference image exactly: [PRODUCT SPEC BLOCK]. Setting: [3 NAMED CLUTTER ITEMS, no more]. Lighting is flat and slightly uneven, [LIGHT SOURCE]. [AUTHENTICITY CLOSER].
```

Total length: 130–180 words. Single paragraph. No JSON. No CAPS for emphasis.

---

## Section 1 — Format

Always lead with this exact opening:

```
iPhone photo, vertical 9:16, held at chest height in [setting], casual off-center framing slightly tilted [right/left].
```

Or for true first-person POV:

```
First-person POV, vertical 9:16, the camera is the creator's own eyes looking [direction] at [product] in [setting].
```

Pick **First-person POV** when the user wants the camera to feel like it IS the creator's eyes (arm extends forward from bottom of frame, hand reaches into the scene from below).

Pick **iPhone photo selfie** when the user wants a more traditional held-phone-at-chest framing (arm reaches in from the side).

Default is First-person POV for product UGC unless told otherwise.

---

## Section 2 — POV / Framing

**For first-person POV:**

```
A man's right arm extends forward from the bottom-right of the frame, hand resting [on/touching/gripping] the [specific part of product] at [waist/chest] height.
```

Key words that matter:
- "extends forward from the bottom-right" — anchors arm direction
- "hand resting on [specific part]" — anchors what the hand touches
- "at [waist/chest] height" — anchors vertical position
- "the camera is the creator's own eyes" — locks POV mode

---

## Section 3 — Human Block

For the IMG_8401 avatar (Isaac's avatar): the face is never shown. Only the arm.

Standard arm block:

```
[ARM CLOTHING — varies by product], no jewelry.
Hand details: light olive skin with visible pores, a small scar on the second knuckle, a faint vein on the back of the hand, short clean nails, no rings.
```

**Arm clothing — rotate across products to avoid templating:**
- Sage green quarter-zip pullover sleeve cuff at the wrist
- White short-sleeve t-shirt edge at the shoulder, bare forearm
- Navy plaid flannel shirt sleeve rolled at the elbow
- Charcoal grey hoodie sleeve cuff at the wrist
- Black short-sleeve t-shirt edge at the shoulder, bare forearm + thin black silicone watch
- Grey short-sleeve t-shirt edge at the shoulder, bare forearm

**Enhanced realism (use when "more realistic" is requested):**

Add these to the hand block:
- "visible dark arm hair"
- "silver signet ring on pinky finger"
- "thin gold bead bracelet on the wrist"
- "slight motion blur on the fingertips"
- "natural finger shadows on the surface beneath"

These mimic the tells visible in real iPhone POV photos.

---

## Section 4 — Product Block

```
The [product] matches the attached reference image exactly: [color], [shape/silhouette], [3-5 specific features visible in reference].
```

**Required precision:**
- Color: specific shade name (cream, dove grey, charcoal black, warm tan, sage green — not just "white" or "grey")
- Shape: silhouette word (L-shaped, rectangular, round, tall narrow, low wide)
- Features: only those visible in reference

**Forbidden words in product block:**
- "premium," "luxurious," "high-end" — vague aesthetic
- "modern" by itself — meaningless filler
- Any feature you cannot point to in the reference image

---

## Section 5 — Setting

```
Setting: [item 1], [item 2], [item 3].
```

Hard cap: **3 named clutter items.** More items = AI gets confused and renders cleaner studio look.

**Good clutter examples (lived-in tells):**
- "an unmade beige sofa edge"
- "a half-empty water glass on a side table"
- "a phone charger draped on the floor"
- "a folded throw blanket on the corner of a rug"
- "a half-empty coffee mug"
- "a stack of two open books"
- "a small green plant in a glass jar"
- "a pair of sneakers off to the side"

**Bad clutter (signals "styled by interior decorator"):**
- "decorative pillows arranged"
- "fresh flowers in a vase"
- "matching coordinated decor"
- "carefully placed accents"

---

## Section 6 — Lighting

Use this exact construction:

```
Lighting is flat and slightly uneven, [light source].
```

**Light source options:**
- "normal indoor warm tungsten room light"
- "soft natural daylight from the window"
- "warm overhead lamp mixed with afternoon daylight"
- "natural late-afternoon daylight from the side"
- "soft natural daylight mixed with the [product's own light source if applicable]"

**Forbidden lighting language:**
- "cinematic lighting"
- "soft golden hour"
- "studio lit"
- "professional lighting"
- "rim light"
- "soft focus"

---

## Section 7 — Authenticity Closer (locked, do not modify)

Every image prompt ends with this exact sentence:

```
Real person, real room, real phone — casual amateur capture, no professional lighting, no beauty filter, no glamour.
```

This is non-negotiable. It tells the model to suppress the polished commercial photography defaults Nano Banana ships with.

---

## Common pitfalls

### Pitfall 1 — "iPhone selfie capture"

Triggers Nano Banana's polished influencer selfie aesthetic. Use **"iPhone photo"** or **"First-person POV"** instead.

### Pitfall 2 — "0.5x ultrawide lens"

Banned. Triggers fisheye distortion + AI artifacts. Use natural framing language instead.

### Pitfall 3 — "Cinematic" / "4k quality" inside the prompt

Banned. Triggers commercial polish. The model is already 4k; don't ask for it again inside the prompt.

### Pitfall 4 — Too many setting items

5+ named items in the setting block → model averages them into a vague "decorated room" rather than placing them.

### Pitfall 5 — Skipping the reference image attachment

Always attach the product reference as media input. Never generate from text alone.

---

## Full prompt template (copy this)

```
First-person POV, vertical 9:16, the camera is the creator's own eyes looking slightly down at a [PRODUCT TYPE] in [SETTING]. A man's right arm extends forward from the bottom-right of the frame, hand resting [VERB] the [SPECIFIC PART OF PRODUCT] at [WAIST/CHEST] height. [ARM CLOTHING], no jewelry. Hand details: light olive skin with visible pores, a small scar on the second knuckle, a faint vein on the back of the hand, short clean nails, no rings. The [PRODUCT] matches the attached reference image exactly: [COLOR], [SHAPE], [FEATURE 1], [FEATURE 2], [FEATURE 3], [FEATURE 4]. Setting: [CLUTTER 1], [CLUTTER 2], [CLUTTER 3]. Lighting is flat and slightly uneven, [LIGHT SOURCE]. Real person, real room, real phone — casual amateur capture, no professional lighting, no beauty filter, no glamour.
```

---

## Settings to send to Higgsfield

- Model: `nano_banana_2`
- Resolution: `4k`
- Aspect ratio: `9:16`
- Count: `1`
- Medias: `[{"role": "image", "value": "<UUID of attached product reference>"}]`
