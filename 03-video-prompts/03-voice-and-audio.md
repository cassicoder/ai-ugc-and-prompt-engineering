# 03.03 — Voice and Audio

The locked voice persona for Isaac's TikTok Shop UGC, plus all known Kling 3.0 audio gotchas.

---

## The locked voice persona

Always use this exact construction in the `[Speaker:]` tag:

```
Speaker: young American male mid-twenties, warm expressive gay-best-friend voice, animated and excited like he's telling his girl about a find, light theatrical lilt, crisp clear English with clear natural pronunciation of common words, natural inflection, not flat, not robotic, not salesy
```

Each token is doing work:

| Token | Purpose |
|---|---|
| `young American male mid-twenties` | Locks age, gender, accent |
| `warm expressive gay-best-friend voice` | Drives expressive emotional range |
| `animated and excited like he's telling his girl about a find` | Drives natural enthusiasm without forced hype |
| `light theatrical lilt` | Adds rhythm and inflection variety |
| `crisp clear English with clear natural pronunciation of common words` | Pronunciation guard without spelling words phonetically |
| `natural inflection, not flat, not robotic, not salesy` | Three negation guards |

### ⚠️ DO NOT spell ORANGE phonetically

A previous version of this guide instructed writing `orange` in dialogue and the speaker tag to prevent the "ornage" mispronunciation. **This backfired.** Kling literally read the dash and pronounced it "OR-ange" with an audible break, sounding robotic.

**Correct approach going forward:**
- Write `orange` in dialogue exactly as the audience reads it
- Do NOT put a phonetic respelling in the dialogue
- Do NOT put a phonetic respelling in the speaker tag
- Trust the model's default pronunciation, and reinforce with `crisp clear English with clear natural pronunciation of common words`
- If a specific word actually fumbles in output, REPLACE that word, don't respell it

---

## Pronunciation traps (verified problems)

Words Kling 3.0 specifically fumbles. Solution: REPLACE the word, do not respell phonetically. Phonetic respellings get read literally as dashes and break the audio.

| Word | Problem | Solution |
|---|---|---|
| Orange | Sometimes pronounced "ornage" | Use as-is — trust the model. If consistently fumbled, replace with "cart icon below" / "tap the cart below" |
| Pinterest | "Pintrest" | Don't use; replace with "online" |
| HomeGoods | "HomGoods" | Don't use; replace with "the home store" |
| Wayfair | "Wahfair" | Don't use |
| Bedrooms | "Bedrums" sometimes | Use "bedroom" singular when possible |

Generally: **avoid compound brand names** in dialogue. **Never respell words phonetically inside dialogue or speaker tags — Kling reads the dash literally.**

---

## The dialogue rules

### Length
- Target ~40 words for 15 seconds
- 35 minimum, 50 maximum

If too short: Kling loops, repeating lines.
If too long: gets cut mid-sentence.

### Pacing tag
Always include in the speaker tag:

```
(0-15s, continuous, no pauses, starts at frame 1)
```

- `continuous` — prevents Kling from inserting natural-sounding pauses
- `no pauses` — reinforcement
- `starts at frame 1` — prevents the dead-air opening

### CTA — every script ends with

```
Huge sale right now, click the orange cart below.
```

or variations:
- "Huge sale, click the orange cart below if you want it."
- "Click the orange cart below before it's gone."
- "Tap the cart below" (alternate if "orange" fumbles)

Write `orange` plainly. NEVER spell it `orange` — Kling reads the dash literally and produces robotic-sounding "OR-ange" with an audible pause.

The user sees "orange" in the on-screen text and caption.

---

## Hooks — scroll-stopping opens

The first 1-2 seconds need to stop the scroll. Tested patterns:

| Hook | Why it works |
|---|---|
| `Okay STOP — y'all need to see this.` | Imperative + Southern affectation |
| `Wait wait wait —` | Builds urgency through repetition |
| `Pause —` | One word, ear-catching |
| `I cannot BELIEVE this.` | Capped emphasis verb mid-sentence |
| `Tell me why nobody talks about this.` | Question hook with implied scarcity |
| `Yo whoever priced this needs a raise.` | Surprise praise |
| `Stop scrolling for a sec.` | Direct command |
| `Okay so —` | Casual entry, intimacy-building |

**Avoid:**
- "Hey guys" (generic)
- "What's up" (generic)
- "Today I want to show you" (script-y)
- "If you've been looking for…" (sales-y)

---

## Voice timing — the "starts at frame 1" rule

Without `starts at frame 1`, Kling adds ~0.5-1.5 seconds of breath/silence before dialogue. This kills retention.

Always include both in the audio tag:
1. `(0-15s, ... , starts at frame 1)` — pacing
2. Dialogue begins immediately with the hook word

If you see Kling still adding lead silence after these are set, the cause is usually the script not starting with a sharp consonant. Test with hooks like "Stop," "Wait," "Okay," "Pause" — they pop frame-1.

---

## When the voice sounds flat

**Cause:** The voice description in the speaker tag is too neutral.

**Fix:** Add more emotional context. Examples:
- "like he just walked into the store and stopped dead"
- "like he's been searching for this product for months"
- "like he's about to text his friend the link"

The model needs an emotional context, not just a voice description.

---

## When the voice sounds wrong gender/age

**Cause:** Kling defaults to a random voice when the speaker tag is vague.

**Fix:** Lead with the gender + age. Always say `young American male mid-twenties` first, never just `male voice`.

---

## When the voice has an accent

**Cause:** Kling defaults vary by training data weighting.

**Fix:** Add `American English with neutral Midwest accent` or `California accent` to the speaker tag.

---

## Ambient audio

By default, Kling adds soft ambient room tone. To control:

- `quiet showroom ambient` — light reverb, sparse
- `quiet living room ambient` — soft, intimate
- `outdoor backyard ambient` — birds, wind
- `no background music` — important to add; default sometimes adds light music

Default to including: `Ambient quiet [setting] tone, no music.`

---

## Track C — when to use external voiceover instead

The UGC AI Video skill in Isaac's vault defines a "Track C" pipeline:
1. Generate mouth-neutral Kling clip (no dialogue baked)
2. Generate voiceover externally with ElevenLabs
3. Lipsync via Higgsfield Lipsync Studio

**Track C is best for:**
- Face-on creator avatars (lipsync required)
- High-stakes hero videos
- When Kling native dialogue produces audio artifacts you can't fix

**Track C is unnecessary for:**
- Faceless POV (no mouth to sync)
- Quick volume production
- 15s test clips

For Isaac's current workflow (faceless first-person POV product UGC), native Kling audio is fine.
