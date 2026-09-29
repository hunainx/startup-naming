# startup-naming

**The naming skill that never shows you a name you can't own.**

An Agent Skill for Claude (and other agents that read `SKILL.md`) that names a startup, product or parent brand, and only puts a name in front of you once its exact `.com` has been checked at the registry.

## What makes it different

- **Exact-match .com or nothing.** No `.io`/`.ai`/`.co` fallbacks, no `get-`/`try-` prefixes, no misspellings. If the .com is taken, the only alternative offered is buying it, with a realistic price band.
- **Verified at the registry, not guessed.** A bundled script (`scripts/rdap.py`) queries Verisign's RDAP service, the authoritative .com registry, for 100–300 candidates per run.
- **Registration dates.** Taken domains come back with registration and expiry dates, so the skill can show you which similar names were grabbed in the last 90 days.
- **Parked-domain detection.** Registrars that hold domains for resale (DropCatch, NameBright/TurnCommerce, Sea Wasp, Atom.com) are flagged, so you know a taken name may be buyable.
- **Religion pass.** No name borrows or contradicts a sacred metaphor of any faith. Known claimed words are listed in the skill.
- **Pronunciation pass.** Each finalist is read the way a speaker in India, the UK and the US would most likely say it; anything that drifts is flagged.
- **Competitor scan first.** Before generating, it maps how 10–20 companies in your space are named and aims for the open space.
- **Scored finalists.** Six criteria, 1–5 each, total out of 30: meaning depth, phone test, signboard test, searchability, architecture, pronunciation.
- **It takes rejection well.** Rejected words are retired for the session and the next batch moves to the register you actually responded to.

## Install

The skill is the `startup-naming/` folder in this repo.

### Claude Code

Personal (all projects):

```bash
git clone https://github.com/hunainx/startup-naming.git
mkdir -p ~/.claude/skills
cp -r startup-naming/startup-naming ~/.claude/skills/
```

One project only: copy the same folder to `.claude/skills/startup-naming/` inside that project.

As a plugin:

```
/plugin marketplace add hunainx/startup-naming
/plugin install startup-naming@startup-naming
```

### claude.ai

1. Download `startup-naming.zip` from the [v1.0.0 release](https://github.com/hunainx/startup-naming/releases/tag/v1.0.0).
2. In claude.ai, open Settings, find Skills, and upload the zip. Code execution must be enabled for the registry check to run.

### Other agents

Any agent that loads `SKILL.md` folders can use it: copy `startup-naming/` into that agent's skills directory, or point the agent at `startup-naming/SKILL.md`. The files in `references/` are loaded on demand at the step that names them.

### Requirements

- `python3` and `curl` for the registry checker.
- Outbound HTTPS to `rdap.verisign.com`. If your environment blocks it, the checker prints `? http 000` and the skill tells you it could not verify. It will not show names as available without a real check.
- Web search and web fetch for the searchability, web and social-handle checks.

## The checker on its own

```bash
python3 startup-naming/scripts/rdap.py tenfoldarc.com foundingorder.com
python3 startup-naming/scripts/rdap.py --file candidates.txt   # one domain per line, # comments allowed
```

Output format, one line per domain:

```
name.com               AVAILABLE
name.com               TAKEN  reg YYYY-MM-DD  exp YYYY-MM-DD  Registrar name               client…
name.com               ? http 000
```

## Example output

Illustrative only: the names below were not checked for this README, and domain status changes daily. The skill always runs a live check first.

```
| # | Name          | .com                     | Score /30 |
|---|---------------|--------------------------|-----------|
| 1 | Tenfold Arc   | tenfoldarc.com ✓ free    | 26        |
| 2 | Keelwrought   | keelwrought.com ✓ free   | 22        |

**1. TENFOLD ARC** — tenfoldarc.com · 26/30
*Tenfold* = ten times over. *Arc* = a curve with direction. A company that compounds
what it touches and keeps its heading. Life meaning: patience, multiplied.
⚠ "Arc" is common in software names; "Tenfold Arc" as a pair is not.

**My picks:** Tenfold Arc (strongest meaning, clean phone test) …
Register today — <similar domains registered in the last 90 days, with RDAP dates>.
Preliminary registry + web check only — formal trademark search still required.
```

## Limits

- **Preliminary checks only.** Registry, web and social checks catch the obvious conflicts. They are **not** trademark clearance. Run a formal trademark search (home country plus international, in the relevant Nice classes) before you commit.
- Registry status is a snapshot. A name free now can be registered minutes later, so register the one you want the same day.
- Aftermarket prices are rough bands, not quotes.
- Sound symbolism and the pronunciation pass are English-centric heuristics.

## Layout

```
startup-naming/
  SKILL.md               main procedure
  scripts/rdap.py        Verisign RDAP bulk checker
  references/
    competitor-scan.md   how competitors are named; clusters and open space
    word-banks.md        starting vocabulary by territory
    sound-symbolism.md   what consonants and vowels signal
    searchability.md     Wikipedia collision, name + category, qualifier count
    scoring.md           six-criterion rubric, total out of 30
    taglines.md          three tagline directions per final pick
```

## Credits

Parts of the references adapt ideas from MIT-licensed work by GlacierPhonk and Cofoundy SAC, rewritten for this skill. Other projects inspired ideas only. See [NOTICE](NOTICE) for exactly what came from where.

## License

[MIT](LICENSE) © 2026 Hunain Ahmed
