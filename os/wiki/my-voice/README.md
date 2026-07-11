---
type: concept
created: 2026-07-10
updated: 2026-07-10
tags: [my-voice, writing, tone, style, meta]
sources: []
---

# My Voice

Writing samples from a user, and the voice profiles derived from them. The goal: collect enough authentic samples that an agent can write in that user's tone and style on demand, enforced through a user-specific rule or skill.

## Structure

```text
my-voice/
  README.md                 This page
  <user-slug>/              One folder per user (e.g. the owner's first name as a slug)
    README.md               Sample inventory: what samples exist, of which kinds
    voice-profile.md        The derived profile: tone, style, patterns, vocabulary, rules
    sources/                Ingest summary pages for the samples
```

Raw samples live in `os/raw/my-voice/<user-slug>/` (immutable, created on first ingest). Good samples span types: emails, documents, posts, messages; formal and casual; short and long. More variety yields a better profile.

## The workflow

1. **Collect:** the user provides writing samples; each is ingested per the schema (raw copy with origin metadata, source summary page). Note the register of each sample (formal/casual, audience, medium).
2. **Analyze:** with several samples filed, build or update `voice-profile.md`: sentence rhythm and length, vocabulary and recurring phrases, punctuation habits, structure preferences, tone markers, things the user never does. Every observation cites the samples it came from.
3. **Derive the enforcement artifact:** distill the profile into a rule or skill (for example `.cursor/skills/write-as-<user>/SKILL.md` or a rules page under [rules](../rules/README.md)) so any agent can be told "write this in <user>'s voice" and produce consistent output.
4. **Iterate:** when the user corrects generated writing, capture the correction into the profile via `/improve-system`; the profile is living, the samples are immutable.

## Conventions

- Voice profiles describe *how the user writes*, not *what they know*; facts still come from the rest of the wiki.
- The owner's universal writing rules ([rules/writing-style.md](../rules/writing-style.md)) always apply on top of any voice profile; a voice profile never overrides an enforced rule.
- Samples may contain personal or business-sensitive content; sensitivity notes carry through per the usual conventions.

## Users

- [Raymond Tayse](raymond/README.md) - 52 email samples (~2.5 years, Sent folder); [voice profile](raymond/voice-profile.md) distilled. Defense/B2B work email; second extraction and Word-doc samples pending.
