# 03.02 — Multi-Shot Structure

How to write 3-shot video prompts that produce coherent 15-second clips.

---

## Why multi-shot

Kling 3.0 has known issues with single-take 15-second clips:
- Audio drifts past ~5 seconds
- Camera moves get erratic past ~7 seconds
- Hand position lock breaks past ~8 seconds

The fix: 3 shots of 5 seconds each, with explicit camera + action + endpoint for each. Kling treats each shot as a fresh prompt, resetting the drift.

---

## The 5-second beat structure

Each 5-second shot should accomplish:
1. **Establish** a fresh angle on the product
2. **Show** one specific feature or interaction
3. **End** at a defined position (sets up the next shot)

**Standard pattern:**

| Shot | Beat | Camera | Hand action |
|---|---|---|---|
| 1 (0-5s) | Wide reveal | Wide, full product visible | Anchor (tap, rest, grip) |
| 2 (5-10s) | Close-up | Dolly in OR cut to detail | Interaction (pull, slide, press) |
| 3 (10-15s) | Resolution | Pull back to start framing | Return to neutral |

---

## Camera move vocabulary (with endpoints)

### Safe dolly moves
- `slow dolly forward toward [target], ending close on [target]`
- `slow pull back to chest distance, ending at start framing`
- `slow dolly left along the [product surface], ending at the [end of surface]`

### Safe pan/tilt moves
- `slow pan right across the [surface], ending on the [right side feature]`
- `slow tilt down the [vertical surface] from [top feature] to [bottom feature], ending at [bottom]`
- `slow tilt up from [bottom] to [top], ending at [top feature]`

### Safe static moves
- `static handheld with subtle micro-shake only`
- `locked POV from start frame, no camera movement, only subtle handheld shake`

### Never use (causes artifacts)
- `tilt up` alone (no endpoint → product grows on screen)
- `whip pan` (Kling generates blur smear)
- `crash zoom` (causes lens artifacts)
- `dolly zoom` (causes warp)
- `360 rotation` (Kling can't actually rotate 360°)

---

## Hand action vocabulary (with endpoints)

### Safe hand actions
- `fingers tap the [surface] twice, ending hand still on surface`
- `hand slides from [point A] to [point B] along the [edge], ending at [point B]`
- `fingers grip the [pull/handle], pulling [direction] [distance], ending [open/extended]`
- `thumb presses the [button], ending [activated/lit]`
- `hand rotates the device [degrees] [direction], ending [angled toward camera]`
- `hand returns to [neutral position], ending at start framing`

### Never use
- `hand picks up the product` (Kling produces floating/glitchy lift)
- `tosses the product` (chaos)
- `quickly swipes` (motion blur smear)
- Anything without an endpoint

---

## Example shot timeline — Pukami Fireplace TV Stand

```
Shot 1 (0-5s): Wide on the full TV stand, hand tapping the wood top twice, ending hand still on wood.
Shot 2 (5-10s): Close on the amber flames, hand sliding to the right cabinet door pull, ending fingers on the pull.
Shot 3 (10-15s): Pull back wide to chest distance, hand resting on the wood top, ending at start framing.
```

Each line:
- States the timing range
- Specifies the camera framing (wide/close/pull-back)
- Specifies what the hand does
- Specifies where it ends

---

## Example shot timeline — Vowner Vanity

```
Shot 1 (0-5s): Wide on the full vanity with mirror centered, hand on the tabletop edge, ending fingers tapping the white surface once.
Shot 2 (5-10s): Close on the LED-lit mirror and crystal drawer knobs, hand sliding to the top drawer pull, ending the drawer pulled out two inches.
Shot 3 (10-15s): Pull back wide to chest distance, hand pushes the drawer closed, ending hand back on the tabletop at start framing.
```

---

## Example shot timeline — Curvy Moon Teeth Cleaner (single product, smaller scale)

```
Shot 1 (0-5s): Wide on the full teeth cleaner held in front of the bathroom, hand gripping the device, ending thumb pressing the top button and the LED tip lighting pale blue.
Shot 2 (5-10s): Close on the LED tip and metal cleaning probe, hand slowly rotating the device 30 degrees, ending angled toward the camera showing the tip.
Shot 3 (10-15s): Pull back to a medium shot, hand returns to neutral grip, ending at start framing.
```

---

## Sync rule — script beats to shots

Each shot should align roughly with one beat of the script:

```
Shot 1 (0-5s): HOOK + first feature
Shot 2 (5-10s): MAIN FEATURES (the demo)
Shot 3 (10-15s): WRAP + CTA
```

Example with Adirondack chair:

| Time | Shot | Script |
|---|---|---|
| 0-5s | Wide reveal | "Okay STOP — y'all need to see this chair right now." |
| 5-10s | Close on wood grain | "It folds, it's real acacia wood, and it holds like four hundred pounds." |
| 10-15s | Pull back | "I've been looking for one for my patio for months and finally found it. Huge sale right now, click the OR-anj cart below." |

---

## Lighting consistency across shots

Include this in the prompt (after the timeline blocks):

```
As the hand moves, the [warm overhead lamp / daylight from window / amber fireplace glow] shifts subtly across the [surface].
```

This single sentence makes Kling animate the light response across all 3 shots, preventing the static "CGI-lit" feel.

---

## When 3-shot doesn't fit

If the product or script demands fewer shots:

**2-shot (7.5s each):** Use when you want a slower, more luxurious feel. Common for furniture.

**Single-shot (15s):** Use for very small products where multiple angles aren't possible. Beware: audio drift risk past 8s.

In all cases, the endpoint rule still applies.

---

## Quality control checklist

Before firing a Kling generation, verify:

- [ ] Single paragraph, 110-145 words
- [ ] Three shots numbered with timing
- [ ] Every camera move has an endpoint
- [ ] Every hand action has an endpoint
- [ ] The "As the hand moves, the light shifts" realism phrase is included
- [ ] Speaker tag includes voice description + (0-15s, continuous, no pauses, starts at frame 1)
- [ ] Dialogue is ~40 words
- [ ] CTA is "click the OR-anj cart below"
- [ ] No banned phrases
- [ ] Locked closer at end
