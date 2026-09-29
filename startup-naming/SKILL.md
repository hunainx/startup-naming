---
name: startup-naming
description: Name a startup, product, or parent brand for any founder, and verify the exact .com is free at the registry before showing it. Maps competitor naming first, checks every candidate against Verisign RDAP (registration dates, parked-for-resale detection), tests searchability, runs religion and pronunciation passes, and scores finalists out of 30. Use for any naming, brand-name, rename, or domain-availability request.
---

# Startup Naming

A repeatable method for producing brand names that feel discovered, not manufactured, and that arrive with the exact .com already verified. Built from a 3,400-domain naming project (Sept 2026) and the naming principles behind the world's most durable companies.

## The one permanent rule

**Exact-match .com or nothing.** The brand name, with no hyphen, no misspelling, no added word, must be free as a `.com` at the registry at the moment it is shown. No .co, .io, .ai, .in, .group or any other TLD is offered as a substitute, and no get-/try-/use- prefix or -app/-hq suffix either. If the user wants a taken .com, the only alternative offered is the aftermarket (buy it from the owner), with a realistic price band. This rule is never asked about in intake. It is assumed.

## Non-negotiable rules

1. **Never show a name without checking its exact .com first**, in the same session. Don't wait to be asked. If the registry cannot be reached, say so plainly and show no name as available.
2. **Every real English dictionary word is taken.** Single words (Monument, Utmost, Holdfast, Keel, Edify…) were registered 1993–2005. Do not spend a round on them; go straight to compounds and two-word names unless the user accepts aftermarket prices.
3. **Web-check the finalists** (exact phrase in quotes). Drop names with a live company, product or brand in software, finance or a major consumer category; drop titles of dramas, novels, games and D&D races. Say: "Preliminary registry + web check only — formal trademark search still required." Never claim legal clearance.
4. **Check social handles** for the top 3 (X, Instagram, GitHub, LinkedIn company slug) with WebSearch; report taken/free as a note, not a veto.
5. **Every name carries meaning**: dictionary meaning → business meaning → (for deep names) life meaning. No meaning, no name.
6. **Religion pass.** No name may borrow or contradict a sacred metaphor of any faith. Known claimed words: foam (Qur'an 13:17 — falsehood that passes), light, lamp, crescent, trinity, genesis, clay, refiner's fire, tried by fire, halo, spirit, soul, grace, covenant, gospel, dharma, karma, om, lotus, trident (Shiva). Say so plainly and drop or reframe.
7. **Pronunciation pass.** Flag silent letters (*wrought*), unfamiliar vowels (*halcyon*), and anything an Indian receptionist and a London receptionist would say differently.
8. **Vocabulary rotation.** No first word and no participle more than 3 times in one round. Every round introduces at least two territories not used in the previous round. Words the user calls out go on a **session-retired list** and are not shown again in that session.
9. **Urgency line with evidence.** Name which similar domains were registered in the last 90 days (RDAP shows dates). Tell the user to register the same day; typical cost ₹1–₹1,500 / $1–$15.

## Principles from the most durable names

- **Real words beat invented ones** (Apple, Amazon, Oracle, Stripe, Square, Blue Origin). Coined names age like the decade that coined them.
- **Evocative, not descriptive.** Amazon says "vast", not "online books". The name must survive a pivot (10× / 100× / different industry test).
- **Two-word gravitas** = evocative adjective or noun + short abstract noun (General Catalyst, First Round, Founders Fund, High Alpha, Deep Mind, Blue Origin, Silver Lake, Black Rock).
- **Compound depth** = a natural force or human condition + a participle of formation (Foamborn, Tidecarved, Pressureformed, Timedistilled, Strugglebred). The best of these let an overthinker build a whole philosophy from one word.
- **Signboard test:** the name alone on a building reads as a serious company.
- **Signature test:** the pair is a phrase nobody has used, so search is owned from day one.
- **Architecture test:** NAME ERP / NAME Pay / NAME Ventures sound natural; existing products keep their names with "a NAME company" beneath.
- **Phone test:** pronounceable on a call, spellable after one hearing, 1–3 syllables per word, ≤ 13 letters total for compounds.

## Procedure

### 1. Intake (always, before any name)

Ask with `AskUserQuestion`. Two calls, four questions each. Ask only about *their* business: never about domains (settled), never about words retired in some other session. If a brief or website is attached, still confirm; if the user says "just go", state the assumed defaults in one line and proceed.

**Call 1 — the business**
1. **What is being named?** Parent / holding company · Single product or app · Service or agency brand · Sub-brand under an existing parent (which?)
2. **In one line, what does it do, and what must the name NOT be tied to?** One technology · one product category · one market/geography · one founder · nothing, it must outlive all of these. (Other = free text.)
3. **What should a stranger feel on reading the name?** Established institution · Deep philosophical · Inspiring / uplifting · Modern minimal · Warm / human · Playful (multiSelect)
4. **Is there a number, origin story or philosophy the name may quietly carry?** Number of founders · A founding principle (e.g. patience, craft, resilience) · A place or nature the founders relate to · None, pure meaning only (multiSelect + Other)

**Call 2 — the shape**
5. **Name shape** (multiSelect): One real-word compound (Foamborn, Tidecarved) · Two short words (Tenfold Arc, Founding Order) · Single real word (warn: exact .com will not be free; aftermarket only) · Coined but natural-sounding word · Open to all
6. **Metaphor worlds to draw from** (multiSelect): time & patience · human effort & struggle · earth, root, seed, mountain · sea & tide · weather & sky · fire, metal & craft · light & dawn · numbers & multiples · navigation & direction · none, keep it abstract
7. **Hard exclusions** (multiSelect): religious or sacred imagery of any faith · founder-name mashups · surnames or place-names · technology/AI/trend words · crutch suffixes (Labs, Studios, Tech, Hub, Works) · anything that sounds like gaming or fantasy · specific words to avoid (Other)
8. **Sub-brands it must sit above** (free text): list existing product names, so the "a NAME company" line can be tested.

Record answers at the top of working notes. They are the constraints for the whole session; the user's later corrections update them. If two answers pull against each other (e.g. "playful" + "established institution"), name the tension in one line and get a priority before generating. Don't let it swing from round to round. If a website exists, read it with WebFetch and write one line: what the company *is* beyond its services.

### 2. Competitor scan

**Read `references/competitor-scan.md` now.** Map how 10–20 companies in the space are named, find the crowded clusters and the open space, and write the five-line scan brief. Competitors' distinctive words join the exclusions.

### 3. Territories and candidates

**Read `references/word-banks.md` now.** Choose 3–5 territories from the intake and the scan's open space, then assemble 150–300 candidates that obey the exclusions and the rotation rule. Aim the sound at the feeling from question 3; **read `references/sound-symbolism.md`** when you need to steer or break a tie on sound. Write every candidate as `name.com`, one per line, to a file such as `candidates.txt`.

### 4. Bulk registry check

Port-43 WHOIS is often blocked in sandboxes; the bundled checker uses Verisign RDAP over HTTPS. `SKILL_DIR` below is the folder holding this SKILL.md (e.g. `~/.claude/skills/startup-naming`):

```
python3 SKILL_DIR/scripts/rdap.py --file candidates.txt
python3 SKILL_DIR/scripts/rdap.py a.com b.com …
```

Run 100–300 per call (allow a long timeout, e.g. 600000 ms). Only `AVAILABLE` proceeds. Reading `TAKEN` lines: registrars such as DropCatch, TurnCommerce/NameBright, Sea Wasp, Atom.com mean parked for resale (aftermarket $500–$15,000); dictionary words run $50,000+. Note registration dates in the last 90 days for the urgency line. `? http 000` = retry once. If every line is `? http 000` or `? http 403`, the network is blocking the registry: tell the user, and do not fall back to guessing, a website ping or memory.

### 5. Searchability and web check

**Read `references/searchability.md` now.** For the top 5–10 available names: Wikipedia collision, exact-phrase search, the "name + category" test, and the qualifier count. Drop live-brand collisions per rule 3.

### 6. Social handles

For the top 3 only: X, Instagram, GitHub, LinkedIn company slug. A note, not a veto (rule 4).

### 7. Religion and pronunciation pass

Apply rules 6 and 7 to every finalist. For pronunciation, write how an Indian, a British and an American speaker would each most likely say it; if the three readings differ, flag it.

### 8. Score the finalists

**Read `references/scoring.md` now.** Score each finalist 1–5 on the six criteria, total out of 30. Anything scoring 1 on any criterion is cut, whatever the total.

### 9. Present

8–12 headline names in the template below, highest score first, then the rest grouped by territory. Each headline: name, domain, score, meaning (dictionary → business → life), weakness, existing-use note. Close with up to three picks, the evidence-backed urgency line, fence domains (US/UK spellings, near variants, each RDAP-checked) and the trademark disclaimer.

### 10. Taglines (optional)

If the user asks, or once they pick a name, **read `references/taglines.md` now** and give three tagline directions per final pick.

### 11. On rejection

Don't defend. Put the rejected words on the session-retired list, identify the register the user *did* respond to (their words, the names they praised), and move the entire next batch there with two fresh territories. Re-run steps 4–8 on the new batch. Bottom line first; short.

## Output template

```
| # | Name | .com | Score /30 |
|---|------|------|-----------|
| 1 | NAME | name.com ✓ available | 26 |
…

**1. NAME** — name.com · 26/30
*Word* = dictionary meaning. Why it fits this business. Life meaning (deep names).
⚠ weakness / existing use / pronunciation / handles.
…
**My picks:** X, Y, Z (one reason each). Register today — <similar domains taken in last 90 days>.
Preliminary registry + web check only — formal trademark search (home country + international, relevant Nice classes) still required.
```
