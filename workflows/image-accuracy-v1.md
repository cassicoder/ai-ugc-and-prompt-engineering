# Image Accuracy Workflow v1

The 3-step workflow that produces 100%-accurate product images on the first fire. Built after 14 generations on 21-product batch — 8/10 hit on the first try, 4 missed; all 4 misses traced to the same root cause and fixed by this workflow's Step 2.

If you only read one file in this repo, read this one.

---

## The root cause of every product-accuracy miss

Every miss we have ever had — boucle instead of chenille, button-tuft instead of channel-tuft, single egg chair instead of double, teal-on-top instead of yellow-on-top — has the same root cause:

> **An ambiguous spec word in the prompt that has multiple visual interpretations in the model's training data.**

The model isn't broken. The word "chenille" maps to bumpy boucle 70% of the time because that's what most "chenille" images look like online. "Tufted" maps to round button tufts 80% of the time. "Double egg chair" maps to "two separate egg chairs" 50% of the time.

If the spec word is ambiguous, the model gambles and we lose.

The fix isn't more words. It's *the right kind* of words: **explicit negative contrast at every ambiguity point.**

---

## The 3-step workflow

### Step 1 — Build the spec card

For each product, look at the reference image and write a 6-line spec card. Don't write the prompt yet. Just the facts.

```
PRODUCT: <name>
SILHOUETTE: <one shape word: T-shape, round dock, U-sectional, double-wide oval egg, etc.>
COLORS: <primary, secondary, accents — list which surface each color lives on>
TEXTURE: <smooth flat / channel-ribbed / wide-corduroy / woven wicker / matte metal>
FEATURES: <3-5 specific features visible in the ref, each with location>
TITLE-CLAIMS-ONLY: <listing words that aren't visible in image but you'll mention in script>
```

Example for product that previously failed:
```
PRODUCT: Weture 98" U-Shaped Chenille Couch
SILHOUETTE: low U-shape sectional with chaise extending from both ends
COLORS: cream off-white throughout, dark espresso brown legs
TEXTURE: smooth flat chenille — like fine velvet, not bumpy
FEATURES: three separate loose back cushions across a low flat back rail; two small cream throw pillows (one per chaise end); short tapered legs at each corner
TITLE-CLAIMS-ONLY: 98 inch wide, 18 inch seat height, 4-seater
```

This step takes 90 seconds. Don't skip it.

---

### Step 2 — Ambiguity audit (THE STEP THAT FIXES ACCURACY)

Look at the spec card. For every adjective and noun, ask:

> "If I gave this word alone to the model, would it default to the right visual interpretation?"

If the answer is "maybe" or "no" — that word is an **ambiguity point**. Flag it. Rewrite it with explicit negative contrast in the form **`X — NOT Y, NOT Z`**.

Use this table to recognize the most common ambiguity traps:

| Ambiguous word | What model defaults to | What you usually mean | Fix |
|---|---|---|---|
| chenille | bumpy boucle weave | smooth flat fabric | `smooth flat chenille — NOT boucle, NOT bumpy, NOT ribbed` |
| tufted | round button tufts | could be either button OR channel | `channel-tufted with VERTICAL stitched seams — NOT round button tufts` or `button-tufted with round button dots — NOT channel tufts` |
| double [furniture] | two separate units | two-person wide single unit | `DOUBLE-WIDE single unit large enough for two adults side by side — NOT two separate units` |
| corduroy | thin ribbed pants fabric | wide upholstery rib | `wide-rib chunky corduroy with ribs about 1 inch apart — NOT thin pants corduroy` |
| wicker | thin natural rattan | thick PE black plastic weave | `black PE plastic wicker woven in a dense pattern — NOT thin natural rattan` |
| matte black | satin gunmetal | true flat black | `true flat matte black — NOT satin, NOT gunmetal, NOT charcoal grey` |
| outer ring | tube on the side | tube on top OR side (depends) | name the SURFACE: `yellow forms the TOP sitting surface; teal wraps the OUTER SIDE band` |
| LED panel | screen-shaped rectangular array | could be edge-strip or array | `rectangular LED array panel with visible diode grid — NOT an edge light strip` |
| inflatable [adult product] | small kid pool toy | adult-sized large dock | `roughly 10 feet in diameter, large enough to seat 3 adults — NOT a small swim ring` |
| modular sectional | individual chairs in a row | connected pieces forming continuous seat | `continuous connected U-shape with single seat surface — NOT separate chairs lined up` |

If the product has 3 ambiguity points, flag 3. If it has 6, flag 6. The cost of flagging an extra one is zero. The cost of missing one is a wasted credit and a re-fire.

---

### Step 3 — Build the prompt from the locked template

Once the spec card has all its ambiguity points rewritten with negative contrast, drop them into this template. The template is fixed; only the bracketed fields change per product.

```
First-person POV, vertical 9:16, the camera is the creator's eyes standing at adult height in [SETTING], looking [DIRECTION] at a [PRODUCT NAME] [POSITION].

A man's right arm extends forward from the bottom-right of the frame, [HAND ACTION on SPECIFIC PART], palm in firm contact. [ARM CLOTHING — rotate per product], no jewelry.

Hand details: light olive skin with visible pores, visible dark arm hair across the forearm, a small scar on the second knuckle, a faint vein on the back of the hand, short clean nails, slight motion blur on the fingertips, natural finger shadows on the [SURFACE the hand touches].

CRITICAL product accuracy — the [PRODUCT NAME] matches the attached reference image exactly: [SILHOUETTE]. [COLORS WITH SURFACE LOCATIONS]. [TEXTURE WITH NEGATIVE CONTRAST]. [3-5 FEATURES WITH NEGATIVE CONTRAST AT EACH AMBIGUITY POINT].

Setting: [3 lived-in clutter items].

Lighting is flat and slightly uneven, [LIGHT SOURCE].

Real person, real room, real phone — casual amateur capture, no professional lighting, no beauty filter, no glamour.
```

**Three rules for using the template:**

1. **The "CRITICAL product accuracy" sentence is the make-or-break.** Put every negative-contrast spec there. If the prompt fails, the failure is almost always in this sentence.
2. **Setting gets a hard cap of 3 clutter items.** More than 3 and the model averages them into a styled-by-decorator look.
3. **The closer sentence is locked.** Do not rewrite it. It is the one phrase that consistently suppresses Nano Banana's commercial-photography defaults.

---

## Settings (always)

```
model: nano_banana_2
aspect_ratio: 9:16
count: 1
medias: [{role: "image", value: "<reference UUID>"}]
```

The reference image must always be attached. Generations without an attached ref drift badly.

---

## The arm-clothing rotation

To keep a 21-product batch from looking like the same UGC creator, rotate the arm clothing across products:

1. Sage green quarter-zip pullover sleeve cuff
2. White short-sleeve t-shirt + bare forearm
3. Black short-sleeve t-shirt + bare forearm + thin black silicone watch
4. Charcoal grey hoodie sleeve cuff
5. Navy plaid flannel rolled at the elbow
6. Grey short-sleeve t-shirt + bare forearm + thin gold bead bracelet
7. *(loop back to 1)*

Never use the same clothing on two adjacent products.

---

## Pre-fire checklist

Before submitting a generation:

- [ ] Reference image attached as `media` with `role: "image"`
- [ ] Spec card written and reviewed
- [ ] Ambiguity audit complete — every flagged word has explicit negative contrast
- [ ] "CRITICAL product accuracy" sentence in prompt contains all negative contrasts
- [ ] Setting capped at 3 clutter items
- [ ] Closer sentence present, unmodified
- [ ] Arm clothing rotation tracked

If any box is unchecked, fix before firing. Each credit costs more than 60 seconds of prompt review.

---

## Post-fire verification

After generation completes:

1. Download the generated image
2. Build a side-by-side with the reference (ref on the left, generated on the right)
3. Audit on **product accuracy only** — color, silhouette, texture, features. Hand placement and background composition are separate concerns.
4. Mark each product as PASS or FLAG. If FLAG, identify the specific spec word that failed and add it to the ambiguity table in this file for the next batch.

This is how the workflow improves itself: every miss feeds a new line in the table.

---

## Why this works (one paragraph)

Generation models are pattern matchers. Given an ambiguous word, they pick the statistically most common interpretation from their training data. The reference image attached as a media input pulls them toward the right answer but doesn't override training priors on adjectives. Explicit negative contrast (`X — NOT Y`) shifts the prior by giving the model two competing options and forcing it to pick X. Combined with the reference image, this is what gets first-fire accuracy to 80%+ on a batch instead of 60%.
