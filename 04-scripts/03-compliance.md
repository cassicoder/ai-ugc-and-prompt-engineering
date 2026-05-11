# 04.03 — Compliance

TikTok Shop and TikTok's general Community Health framework. Violating these triggers CHR (Creator Health Rating) drops and eventually account removal under the six-strikes rule.

---

## CHR — the scoring system

- Starts at 200 / 1000 for new accounts
- Each violation drops the score
- Score must stay above thresholds to maintain product link access
- Six strikes of the same violation type in 90 days = permanent removal

This means: **one wrong claim per 30-50 videos is the ceiling.** A script that goes viral with a violation gets the entire account flagged.

---

## Forbidden claim categories

### Medical / health
- "Cures" / "treats" / "heals"
- "FDA approved" (unless literally true)
- "Doctor recommended"
- "Medical-grade"
- Disparaging healthcare professionals ("my dentist couldn't do this")
- Curing specific conditions
- Anything implying medical efficacy

### Disparaging competitors by name
- HomeGoods, Costco, Wayfair, Amazon, Target, Walmart — never name competitors
- "Way cheaper than [brand]" — use "the home store" / "online" / "the other place"

### False scarcity
- "Only 3 left" if there are 300
- "Sale ends tonight" if it doesn't
- "Last chance" repeated daily

### Misleading specs
- Claiming features that don't exist on the product
- Claiming dimensions / weight / capacity that aren't in the listing
- Claiming materials that aren't real (e.g. "solid wood" for wood-look)

### Whole-room or extreme utility
- "Heats the entire room" for accent fireplaces
- "Burns 500 calories" for a piece of fitness gear
- "Cleans 10x better than [thing]"

### Before / after weight loss
- Specific weight loss numbers
- "I lost X pounds with this"
- Body transformation claims

### Health benefit claims
- "Boosts immunity"
- "Improves digestion"
- "Reduces stress" (allowed: "feels relaxing")
- "Better sleep" (allowed: "I sleep better with this" if subjective)

The line: **subjective sensory claims allowed, specific health outcomes forbidden.**

OK: "Makes my teeth feel cleaner."
Not OK: "Whitens teeth in 3 days."

OK: "I sleep better with this."
Not OK: "Cures insomnia."

---

## Required actions

### AI label
Every AI-generated video uploaded to TikTok must have the AI label toggled ON. Not optional.

### Real product
The product shown in the video must match the product being sold. No bait-and-switch.

### In-app CTA
"Click the orange cart below" is in-app and safe. "DM me," "link in bio," "click my profile" risk being flagged as off-platform routing.

---

## Pre-publish checklist

Before uploading any video to TikTok Shop:

- [ ] Script audited against `01-accuracy-protocol.md` — every claim verified
- [ ] No medical/health claims
- [ ] No competitor brand names
- [ ] AI label toggled ON
- [ ] CTA is "orange cart below"
- [ ] Caption matches script tone (no $ or % in TOF)
- [ ] On-screen text under 8 words
- [ ] Captions and on-screen text aligned with video claims

---

## Violation playbook

If a video gets flagged:

1. **Don't delete immediately** — deletion can be read as admission
2. **Read the violation reason carefully** — TikTok sends a specific category
3. **Submit appeal within 24 hours** if the flag seems wrong
4. **Pull the video** if the flag is correct (avoid further strikes)
5. **Audit the next 5 videos in your queue** for the same pattern
6. **Update this repo's `06-failure-modes.md`** with the new pattern

Standing appeal template (Isaac's vault has the long version):

> "This video accurately represents the product as listed in the [seller name] product page. The features mentioned ([list]) are explicitly stated in the product title and visible in the seller's primary product image. Requesting review."

---

## Six-strikes rule monitoring

Track every violation in the vault:

```
| Date | Product | Violation type | CHR drop | Appeal status |
```

If the same violation type appears 4+ times in 90 days, **pause that content style entirely** until the 90-day window resets.

---

## Categories Isaac currently runs (compliance notes)

| Category | Safe? | Notes |
|---|---|---|
| Furniture (large) | ✅ Yes | Stay on visible features, no material overclaim |
| Bedding / mattress | ⚠️ Careful | "Better sleep" is a health claim, use sensory language |
| Pet products | ✅ Yes | Avoid "trains your pet to..." claims |
| Outdoor | ✅ Yes | Stay on visible features |
| Kitchen | ⚠️ Careful | Food contact safety claims are regulated |
| Health / beauty | 🔴 High risk | Use sensory language only, never efficacy |
| Baby | 🔴 High risk | Safety claims are heavily regulated |
| Fitness | ⚠️ Careful | No weight loss numbers, no body claims |

---

## When unsure: the "lawyer test"

Before saying anything in a script, ask:

> If a lawyer reviewed this claim, could the product be sued for not delivering?

If yes, soften or remove.

OK: "I'm obsessed with how this feels."
Not OK: "This will fix your X."

OK: "Looks insanely real."
Not OK: "Indistinguishable from real X."

OK: "Makes my [thing] feel [sensory adjective]."
Not OK: "Makes my [thing] [measurable improvement]."
