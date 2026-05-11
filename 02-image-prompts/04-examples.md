# 02.04 — Image Prompt Examples

Worked examples — both successful and failed prompts. Study the differences.

---

## Example 1 — Yaheetech Adirondack Folding Chair (succeeded)

```
First-person POV, vertical 9:16, the camera is the creator's own eyes looking slightly downward at an Adirondack folding chair on a sunlit backyard patio. A man's right arm extends forward from the bottom-right of the frame, hand resting palm-down on the wide flat armrest of the chair. Bare forearm visible from the shoulder, white short-sleeve t-shirt edge at the top of the arm, no jewelry. Hand details: light olive skin with visible pores, a small scar on the second knuckle, a faint vein on the back of the hand, short clean nails, no rings. The chair matches the attached reference image: solid acacia wood Adirondack folding chair in natural light brown finish with visible wood grain on every slat, wide curved seat slats, tall fanned-back, wide flat armrests, folding hinge clearly visible at the joints. Setting: a worn outdoor patio with a beige doormat, a small terracotta pot, a half-empty glass of iced tea on the ground. Lighting is flat and slightly uneven, natural late-afternoon daylight from the side. Real person, real room, real phone — casual amateur capture, no professional lighting, no beauty filter, no glamour.
```

**Why it worked:**
- True first-person POV (arm extends forward from bottom, not reaching in from side)
- Product spec block lists 5 verifiable features visible in reference
- 3 named clutter items (doormat, pot, iced tea glass) — not more
- Lighting line is specific and natural
- Locked closer at end

---

## Example 2 — Vowner Vanity (FAILED, learn from this)

**Original prompt (wrong):**

```
... iPhone capture held at chest height, vertical 9:16, in a modern furniture store showroom. ... The vanity fills the upper two-thirds of the frame: large rectangular mirror with small round LED bulbs glowing soft warm white around the perimeter ... matching white cushioned bench tucked underneath.
```

**What went wrong:**
1. ❌ "Small round LED bulbs around the perimeter" — actual product has a 3-color lighted mirror with LED edge lighting, NOT a Hollywood bulb-bordered frame
2. ❌ "Matching white cushioned bench" — bench is NOT included in the product
3. ❌ "Furniture store showroom" — actual product setting in listing is a bedroom
4. ❌ Listed "chrome bar pulls" — actual product has crystal/glass diamond knobs

**Fix:**

```
First-person POV, vertical 9:16, the camera is the creator's own eyes looking slightly down at a white makeup vanity in a sunlit bedroom. A man's right arm extends forward from the bottom-right of the frame, hand resting palm-down on the white tabletop edge of the vanity. [... arm block ...]. The vanity matches the attached reference image: 55-inch tall white modern makeup vanity, rectangular standalone 3-color lighted mirror centered on top, white cabinets and display shelves on either side of the mirror with decor items inside, long white tabletop, seven white drawers with clear crystal diamond-shaped knobs (one wide top drawer with three drawers on each side below), built-in white wall outlet visible. Setting: light hardwood floor, a small flower arrangement in a vase, sheer green curtains. Lighting is flat and slightly uneven, soft natural daylight. Real person, real room, real phone — casual amateur capture, no professional lighting, no beauty filter, no glamour.
```

**Lessons:**
- View the reference image. Don't infer features from product name.
- "Hollywood vanity" doesn't mean Hollywood-style mirror.
- Knob style matters — chrome bar pulls and crystal diamond knobs are different products.

---

## Example 3 — Pukami Fireplace TV Stand (FAILED)

**Original (wrong):**

```
A man's right hand and forearm extend into the frame from the right, fingertips resting on the top edge of the fireplace TV stand. The TV stand matches the attached reference image: long warm-brown oak console, central electric fireplace insert glowing soft amber flames, soft cyan LED accent strip under the front edge, two open shelves left and right, two cabinet doors with slim metal pulls.
```

**What went wrong:**
1. ❌ "Long warm-brown oak console" — actual product is **black high-gloss finish with wood-tone accents**, not solid oak
2. ❌ "Soft cyan LED accent strip under the front edge" — the actual product has **16-color LED lights** (any color, not specifically cyan); the cyan in the original ref was just one of the displayed colors
3. ✅ "Electric fireplace insert with amber flames" — correct
4. ✅ "Two cabinet doors" — correct (but missed the open shelf cubbies on either side)

**Fix:**

```
... The TV stand matches the attached reference image: long low entertainment console with black high-gloss finish on the cabinet doors and a wood-tone top surface, central electric fireplace insert with bright amber dancing flames, two open shelf cubbies on either side of the fireplace, two black gloss cabinet doors with slim chrome bar pulls, integrated LED accent strip glowing warm amber under the front edge ...
```

**Lessons:**
- "Wooden TV Stand" in the title doesn't mean "real wood."
- LED color in the reference image is sample only when the product description says "16 colors."

---

## Example 4 — Curvy Moon Teeth Cleaner (PARTIAL)

**Original (wrong):**

```
... white handheld electric teeth cleaner ... three small buttons on the body ...
```

**What went wrong:**
1. ❌ Actual product is **silver/stainless with black accents**, not pure white
2. ❌ Has 5 mode indicator lights running down the side, not "three small buttons"

**Fix:**

```
... silver and black handheld electric teeth cleaner with brushed stainless steel body, five small mode indicator lights running vertically down one side, slim metal cleaning tip extending up from the top, USB-C port visible at the bottom, CURVY MOON branding visible ...
```

---

## Example 5 — Riwengo Hanging Basket Chair (FAILED on color)

**Original (wrong):**

```
... large hand-woven PE rattan egg-shaped chair in warm tan, a thick autumn-toned cushion inside ...
```

**What went wrong:**
1. ❌ Actual product is **dark grey/charcoal rattan** with **grey cushions**, not warm tan
2. The product title says "FallFreshness Cushion" which I interpreted as autumn-toned — wrong, "FallFreshness" is just a product line name

**Fix:**

```
... large hand-woven dark grey PE rattan egg-shaped hanging chair suspended by a black metal chain from a freestanding black metal stand, thick grey cushioned seat inside with matching grey lumbar pillows ...
```

**Lesson:**
- Product line names ("FallFreshness," "Summer Vibes") are not material descriptions.

---

## Quick-reference accuracy decision tree

```
For each product feature you want to mention in the prompt:

  Is it clearly visible in the reference image?
  ├── YES → Is it consistent with the listing title?
  │         ├── YES → Include it confidently ✅
  │         └── NO  → Include it but note conflict to user
  │
  └── NO  → Is it explicitly named in the listing title?
            ├── YES → Include it with mild caveat ("listed as having…")
            └── NO  → DO NOT INCLUDE IT. Don't guess.
```
