# 05 — Realism Protocol

The complete protocol for getting AI-generated UGC to look indistinguishable from a real iPhone photo or video.

This is built from comparing a real iPhone POV photo (provided as reference IMG_8650) against multiple AI-generated attempts. The differences in the real photo became the realism upgrades to the prompt vocabulary.

---

## The 8 tells of "AI-looking" UGC

1. **Hands have no hair** — clean smooth skin
2. **Hands are bare** — no jewelry, no watch, no scars
3. **Hands are perfectly still** — no motion blur
4. **No shadows under fingers** — hand floats above surface
5. **Background props are perfect** — no dead leaves, no scuffs
6. **Lighting is even and soft** — studio-style
7. **Composition is centered** — too clean
8. **Surface textures are smooth** — no wear, no use signs

---

## The 8 tells of "real iPhone" UGC

1. **Visible arm hair** — natural hair pattern
2. **Personal jewelry** — rings, bracelets, watches
3. **Slight motion blur** on fingertips — caught mid-action
4. **Real shadows** under fingers and palms
5. **Lived-in clutter** — partially-eaten things, draped chargers, half-empty mugs
6. **Directional sunlight harshness** OR **uneven indoor mixed light**
7. **Off-center, slightly tilted framing**
8. **Worn surfaces** — scuffs, wear, browning plant tips, slight stains

---

## The fix — additions to image prompts

### Enhanced hand block

Replace standard hand block with:

```
Hand details: light olive skin with visible pores, visible dark arm hair across the forearm, a small scar on the second knuckle, a faint vein on the back of the hand, short clean nails, a silver signet ring on the pinky finger, a thin gold bead bracelet on the wrist, slight motion blur on the fingertips, natural finger shadows cast on the surface beneath the hand.
```

### Setting realism boosts

For each background prop, add one imperfection:

| Generic AI | Real-phone version |
|---|---|
| `a small green plant` | `a small green plant with a few browning lower leaves` |
| `a wooden fence` | `a weathered wooden fence with visible grain and one slightly broken slat` |
| `a coffee mug` | `a half-empty coffee mug with a faint lipstick mark on the rim` |
| `a side table` | `a side table with a faint water ring near the edge` |
| `a hardwood floor` | `a hardwood floor with a few faint scuffs near the corner` |

### Lighting realism boost

For outdoor:

```
Lighting is bright direct midday sunlight from one side, casting hard-edged shadows under the [product] and on the fingers, with the opposite side slightly underexposed.
```

For indoor:

```
Lighting is flat and slightly uneven, normal indoor warm tungsten room light mixed with diffuse daylight from a window — neither side perfectly balanced, slight color cast warm overall.
```

### One-line phone-camera vibe override

Add before the closer:

```
The image has slight phone-camera characteristics: subtle grain in the shadows, slightly off-axis tilt of about three degrees, natural unedited color cast.
```

This is a single sentence that consistently improves realism.

---

## The fix — additions to video prompts

### Hand realism in motion

Replace hand action with:

```
Hand action timeline:
0-5s: fingers hover over the [surface] then settle into a relaxed grip, with slight natural finger tremor and faint motion blur on the edges of the moving fingers.
```

The "slight natural finger tremor" and "faint motion blur" instructions make Kling animate the hand more naturally.

### Light response

Include the realism phrase (mandatory):

```
As the hand moves, the [warm room light / daylight / amber glow] shifts subtly across the [surface], with the shadows under the fingers moving with the hand.
```

Adding "with the shadows under the fingers moving with the hand" is the key. It tells Kling to animate light AND shadow response.

---

## Real iPhone reference observation log

When the user sends a real iPhone photo for comparison, capture observations like:

```
Real photo IMG_8650 (patio chair):
- Arm hair: dark, dense on forearm, visible
- Jewelry: silver signet ring on pinky, gold bead bracelet on wrist
- Motion: hand caught mid-reach, slight blur on the fingertips
- Shadows: hard shadows from midday sun
- Background: dying brown plant tips, weathered wooden fence
- Composition: arm enters from bottom-right corner, slightly off-center
- Light direction: harsh from camera-right side
- Surface: chair fabric shows soft creases, blanket bunched messily
```

Each observation becomes a token to add to future prompts.

---

## The realism A/B protocol

When testing a new realism token:

1. Generate 2 versions of the same product
   - Version A: current prompt
   - Version B: current prompt + new token
2. Compare side-by-side
3. Keep tokens that visibly improve realism
4. Drop tokens that have no effect or make it worse
5. Update this protocol with the verified improvements

Don't add untested tokens. Don't keep tokens that don't visibly help.

---

## What still doesn't work (open problems)

These are areas where AI still falls short, even with the protocol:

1. **Fingernail texture** — AI tends toward unnaturally clean nails
2. **Wedding rings + signet ring combinations** — model gets confused
3. **Tattoos on the arm** — Nano Banana struggles with consistent tattoo placement
4. **Cracked phone screen reflections** — when the phone itself is visible
5. **Very subtle lipstick smudges** — gets exaggerated

For these areas, the only fix is real-world capture or careful manual touch-up.

---

## When realism matters most

Apply the full enhanced protocol when:
- Showing a face-on creator avatar (lipsync)
- High-stakes hero videos (campaign launches)
- BOF closing videos

Apply standard protocol (lighter realism) when:
- Faceless POV product UGC (current default workflow)
- Volume production
- A/B testing variations

For 15s TOF product UGC: standard hand block + 3 named clutter items + "flat and slightly uneven lighting" + locked closer is usually enough.
