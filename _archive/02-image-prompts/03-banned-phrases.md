# 02.03 — Banned Phrases for Image Prompts

These phrases produce the opposite of what you want. Each entry includes why it fails.

---

## Camera / lens vocabulary

| Banned | Why it fails | Use instead |
|---|---|---|
| `0.5x ultrawide` | Triggers fisheye distortion + lens artifacts | Natural framing language |
| `wide-angle lens` | Same | Same |
| `fisheye effect` | Same | Same |
| `bokeh background` | Forces artificial blur | "Background slightly soft" |
| `shallow depth of field` | Same | Same |
| `tilt-shift` | Stylized look | Skip |

---

## Quality / polish vocabulary

| Banned | Why it fails | Use instead |
|---|---|---|
| `professional photography` | Triggers studio polish | "Casual amateur capture" |
| `commercial photo` | Same | Same |
| `magazine quality` | Same | Same |
| `high-end shoot` | Same | Same |
| `cinematic` | Triggers film-grade color grading | Skip |
| `4k` | Already the resolution; saying it again triggers oversharpened look | Skip |
| `ultra detailed` | Pushes toward CGI | Skip |
| `hyperrealistic` | Pushes toward CGI | Skip |
| `raw HDR` | Triggers heavy contrast | Skip |
| `crisp` | Pushes toward polish | Skip |

---

## Lighting vocabulary

| Banned | Why it fails | Use instead |
|---|---|---|
| `soft golden hour` | Every-shot-looks-the-same problem | Be specific about time and direction |
| `cinematic lighting` | Hollywood polish | "Flat and slightly uneven" |
| `studio lit` | Studio polish | Same |
| `rim light` | Stylized | Skip |
| `key light` | Stylized | Skip |
| `natural lighting` | Too vague; defaults to glamour | Specify direction and intensity |

---

## Composition vocabulary

| Banned | Why it fails | Use instead |
|---|---|---|
| `centered composition` | Too clean, signals stock photo | "Casual off-center framing" |
| `rule of thirds` | Too clean | "Slightly tilted right/left" |
| `symmetrical` | Too clean | Skip |
| `perfectly framed` | Same | Skip |
| `eye-level shot` | Robotic | "Held at chest height" |

---

## People vocabulary

| Banned | Why it fails | Use instead |
|---|---|---|
| `model` | Triggers fashion model defaults | "Man" / "person" |
| `beautiful` | Triggers beauty filter | Skip |
| `young woman / model` | Same | Be specific about age/role |
| `smiling at camera` | Triggers fake smile | "Mouth caught mid-word" |
| `posing` | Triggers static pose | "Mid-motion" |
| `looking elegant` | Glamour trigger | Skip |
| `flawless skin` | Beauty filter | "Visible pores, natural skin" |

---

## Product vocabulary

| Banned | Why it fails | Use instead |
|---|---|---|
| `premium` | Vague aesthetic, not a feature | Specific feature |
| `luxurious` | Same | Same |
| `high-end` | Same | Same |
| `modern` (alone) | Filler | Specific design language |
| `elegant` | Filler | Same |
| `sleek` (alone) | Filler | Same |
| `state-of-the-art` | Filler | Same |
| `top-quality` | Filler | Same |

---

## Background vocabulary

| Banned | Why it fails | Use instead |
|---|---|---|
| `pristine background` | Studio look | "Lived-in" |
| `clean modern setting` | Too generic | Specific room with specific clutter |
| `minimalist scene` | Same | Same |
| `aesthetic` (alone) | Influencer cliche | Specific items |
| `tastefully decorated` | Same | Same |

---

## Composite phrases that fail together

Even individually OK words combine into AI tells:

- "young attractive person in modern home" — every word is a trigger together
- "professionally styled bedroom" — too clean
- "beautifully composed shot" — too clean
- "stunning natural beauty" — beauty filter

---

## Why the bans matter

Nano Banana 2 is trained on millions of stock and commercial images. Default outputs lean polished. The bans suppress the polish defaults so the model produces something closer to a real phone photo.

The closer (`Real person, real room, real phone — casual amateur capture, no professional lighting, no beauty filter, no glamour`) is the strongest single anti-polish lever. Banned phrases reinforce it.
