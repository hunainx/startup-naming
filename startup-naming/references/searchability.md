# Searchability

A free .com proves the registry is clear. It does not prove the name is clear. A name can be unregistered and still be buried under a Wikipedia article, a novel, a band or a same-name app. Run this on the top 5–10 available names, before social handles.

## 1. Wikipedia collision

WebFetch `https://en.wikipedia.org/wiki/<Name>` (and the two-word form with an underscore), or WebSearch `site:en.wikipedia.org "<name>"`.

- An article with that exact title: high collision. Wikipedia holds that search result almost permanently and blocks the knowledge panel.
- Only a disambiguation mention or a partial match: medium.
- Nothing: low.

For two-word names, a Wikipedia article on the exact pair matters; articles on each word alone do not.

## 2. Exact-phrase search

WebSearch `"<name>"` in quotes. Look at the first page:

- A live company, product or brand in software, finance or a major consumer category → drop (rule 3).
- A drama, novel, game, film, album or D&D race by that title → drop.
- Scattered small uses in unrelated fields (a local café, a dormant blog) → keep, and note them.

Also check `"<name>" app` and GitHub (`https://github.com/<name>`). A free registry name that already means something to people is not a clear name.

## 3. The "name + category" test

WebSearch `"<name>" <category>` using the one-line description from intake (e.g. `"Tidecarved" logistics`). If anything in the category comes up, that is a direct conflict: drop it.

## 4. Qualifier count

Imagine the company is live. How many extra words would a stranger need to add to reach it?

| Qualifiers needed | Example query | Searchability score |
|-------------------|---------------|---------------------|
| 0: the name alone finds it | `tenfoldarc` | 5 |
| 0, but shares the first page with minor unrelated uses | `founding order` | 4 |
| 1: category word needed | `<name> consulting` | 3 |
| 2: category and place/type needed | `<name> consulting india` | 2 |
| 3+ or a Wikipedia/major-brand wall | — | 1 (cut) |

Compounds and unused two-word pairs usually land at 4–5; single dictionary words at 1–2. Carry the score into `scoring.md`.

## Report line

For each checked name, one line in working notes:
`Name — Wikipedia: none/partial/article · Web: clear / minor uses (…) / conflict (…) · Category test: clear/conflict · Qualifiers: n → score`
