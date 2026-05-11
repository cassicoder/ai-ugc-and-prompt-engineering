# 01 — Accuracy Protocol (The 100% Rule)

This is the most important file in this repo. Read it before writing a single prompt.

---

## The rule

Every claim made about a product — in the image, in the video, in the script, in the caption — must be **100% verified** against the actual product reference image and listing.

Not 99%. Not "probably." Not "the title implies it." **100% visible or 100% stated in the listing title.**

If you cannot verify, leave it out.

---

## Why this rule exists

When the generated content doesn't match the actual product:
1. Buyer receives the product → it doesn't match the video → return
2. Buyer leaves a 1-star review with photo → conversion crashes
3. TikTok flags video as "misleading product claim" → CHR violation
4. Repeated violations → account permanently removed (six-strikes rule)

A single inaccurate spec claim can kill a product's funnel.

---

## The verification checklist

Before generating any image or writing any script, complete this checklist:

### Step 1 — View the reference image directly

Do not rely on the listing title or description text alone. Open the image file. Look at it.

Note specifically:
- Exact color (be precise — "cream" not "white"; "dove grey" not "grey")
- Material finish (matte, glossy, brushed, woven, fabric, wood-look vs solid wood)
- Knobs / pulls / handles (round, bar, finger cutout, none)
- Leg style (silver tapered, black metal X-frame, no legs flush)
- Number of drawers / shelves / panels
- Branding visible (logo color, where it sits)
- Anything attached or included (cushions, scoop, mat, cover)

### Step 2 — Cross-check against the listing title

Read the full product title in the TikTok Shop listing. Note every feature explicitly stated. Common explicit-claim sources:
- Weight capacity (e.g. "450 LBS Heavy Duty")
- Dimensions (e.g. "55 Inch Tall")
- Number of something ("7 Drawers", "16 Colors LED")
- Specific feature names ("Cup Holder", "Mosquito Net", "Drawer for Easy Cleaning")

### Step 3 — Only claim what survives BOTH checks

A feature is safe to claim if:
- ✅ Visible in the image AND
- ✅ Stated in the listing title

A feature is risky to claim if:
- 🟡 Visible in the image but not in the title (still usually fine if obvious)
- 🟡 Stated in title but not visible in this image (request another angle from the user)

A feature is **forbidden** to claim if:
- 🔴 Neither visible nor stated
- 🔴 You're guessing based on what "most products like this have"

### Step 4 — When in doubt, ask

Ask the user for additional reference angles. Phrase it: "Can you send me a side angle / open angle / detail shot of [feature]? I want to verify before I write the script."

---

## Specific failure patterns we have already lived through

### Failure 1 — "Real wood" claim on wood-look furniture

Pukami Fireplace TV Stand. The product is **black high-gloss finish with wood-tone accents**. Title says "Wooden TV Stand." Script said "real wood top."

❌ Wrong. "Wooden" in the title is a category label, not a material declaration. The visible product is wood-look, not solid hardwood.

✅ Fix: "wood-tone top" or "wooden look" or drop the wood claim entirely. Don't make material claims unless the listing explicitly says "solid hardwood / solid acacia / real oak / etc."

### Failure 2 — "Hollywood lights all the way around" on a 3-color lighted mirror

Vowner Vanity. Product has a **3-color lighted mirror** (LED edge lighting, single mirror). Script claimed "Hollywood lights all the way around" (which implies bulb-bordered frame).

❌ Wrong. Different lighting style entirely.

✅ Fix: "three color lighted mirror" or "LED edge lighting."

### Failure 3 — "Bench included"

Vowner Vanity. Title says "55" Tall Makeup Vanity Set with 3 Color Lighted Mirror 7 Drawers Outlet." **No bench mentioned.** Script invented one.

❌ Wrong. Adding features the product doesn't have is the worst kind of inaccuracy.

✅ Fix: Never add features. Only describe what's verified.

### Failure 4 — "Enclosed" on a semi-enclosed open-top product

Sweetcrispy Cat Litter Box. Title says "Semi-Enclosed Design." Product is a high-walled open-top box, NOT a covered/lidded enclosure.

❌ Wrong. "Enclosed" and "semi-enclosed" are different products to a buyer.

✅ Fix: "high-walled" or "semi-enclosed" — match the listing language.

### Failure 5 — "Finger pulls hidden on top"

FUFU&GAGA Dresser. The drawers have **finger-pull cutouts on the bottom edge**, not the top.

❌ Wrong. Specific mechanism is wrong direction.

✅ Fix: "no handles, just press and pull" or "finger pulls along the edge" — vague enough to be accurate.

### Failure 6 — "Heats up the whole room"

Pukami Fireplace TV Stand. Electric fireplace inserts are accent heaters. Not whole-room heaters.

❌ Wrong. Health/utility overclaim.

✅ Fix: "electric fireplace built in" — describes the feature without overclaiming function.

---

## The image prompt accuracy section

Every image prompt should include a sentence like:

> The [product] matches the attached reference image exactly: [color], [shape], [3-5 specific features visible in ref].

The "matches the attached reference image exactly" phrase is a hard instruction to the model. Combined with the attached reference image, it dramatically improves fidelity.

Things to include in the product specification:
- Exact color (cream, dove grey, charcoal black — be precise)
- Material/finish (matte, glossy, brushed, woven, fabric)
- Specific feature with location (e.g. "small green Creality triangle logo on front center")
- Counts (3 drawers, 4 wheels, 6 legs)

Things to leave out:
- "Premium," "luxurious," "high-end" — these are vague aesthetic words, not features
- Anything you couldn't point to in the reference image

---

## The script accuracy section

Every script should pass this filter before generation:

1. List every spec claim in the script
2. For each claim, mark: visible in image (V), in listing title (T), or assumed (A)
3. Drop any claim marked A only

Example:

Script: "Big and tall executive, flip up armrests, hidden footrest, reclines all the way back."

- "Big and tall executive" → T (listing title) ✅
- "Flip up armrests" → T + V ✅
- "Hidden footrest" → T says "Foot Rest", V shows it extended — "hidden" is wrong, it's retractable ⚠️
- "Reclines all the way back" → T ✅

Action: Change "hidden footrest" to "retractable footrest" or just "footrest."

---

## TL;DR

- View the image. Read the title. Match exactly. Claim only what's verified.
- When in doubt, leave it out.
- When in deeper doubt, ask for more reference angles.
- Never invent features.
- Never make health, medical, or whole-room utility claims.
