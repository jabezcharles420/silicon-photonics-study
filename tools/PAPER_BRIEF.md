# Brief: first-principles study page for a research paper

You are writing study pages for a plain-English, first-principles study website (MkDocs Material, deployed to GitHub Pages). The reader is a student entering silicon photonics / photonic inverse design from outside the field (background: maths/data science, some undergraduate EM). They want the **whole content of the paper**, explained from first principles, in easy English. **Length does not matter; completeness and clarity do.** Do not skip any section of the paper.

## Paths
- Paper sources (markdown + figures): `/Users/fenqinyang/Documents/PHD/papers_md_src/papers_md/<slug>.md`; figures in `.../papers_md/assets/`.
- The figures are ALREADY copied to the site at `/Users/fenqinyang/Documents/PHD/reading-packets/study-site/docs/assets/papers/` (same filenames). From a page in `docs/week-NN/`, reference them as `../assets/papers/<filename>.png`.
- Site root: `/Users/fenqinyang/Documents/PHD/reading-packets/study-site/`. Python venv with numpy, matplotlib, mkdocs: `.venv/bin/python`, `.venv/bin/mkdocs`.
- Style reference: read the first ~150 lines of `docs/week-01/day-01-mon-21-sep-2026.md` and copy its tone (short sentences, analogies, every term defined on first use).
- The study schedule (to quote the day's task): `/Users/fenqinyang/Documents/PHD/Path_B_Daily_Study_Schedule.md` — it is ~1 MB; do NOT read it whole. Use grep to find your day's heading (e.g. `grep -n "### TUESDAY 29 Sep 2026" ...`) and read only that day's block (~25–40 lines), which includes a `▸ HOW` block with useful pointers and gotchas.

## Page structure (one page per paper)
1. `# Week N · Day D — <Weekday> <D Mon YYYY> · <Short paper name>` then an italic line: *Simple-English study version of <Authors>, "<Title>", <Journal> (<Year>)*
2. `!!! abstract "Today's slot"` — quote the schedule task line(s) for this paper and the slot time; say what the student should be able to do after reading (from the schedule's EXIT / HOW block if present). If the schedule revisits this paper on other dates (given in your assignment), list them here.
3. `## Before you start: the big picture` — what problem the paper solves and why anyone cares, with an everyday analogy. No jargon yet.
4. `## Background you need` — build every prerequisite from zero that the paper assumes (e.g. modes, effective index, coupling, phase, interference, Q factor, gradients, chain rule, Lagrange multipliers / adjoint idea, convolution filters, neural nets — whatever THIS paper needs). Each with a short worked example or picture where helpful.
5. Then walk through **every section of the paper in order**, using the paper's own section headings/numbering. For each section: what it says in plain words, then the equations — every equation the paper has that matters, with each symbol defined, said in words, and *why* it has that form. Derive key results step by step (show the algebra, don't skip steps). Add small worked numeric examples using realistic silicon-photonics numbers (λ = 1550 nm, n_Si ≈ 3.48, n_SiO2 ≈ 1.44, 220 nm SOI, etc.).
6. **Figures:** include EVERY figure from the paper markdown, in the place it belongs, as `![Fig. N — short title](../assets/papers/<file>.png)` followed by a 2–4 sentence plain-English "How to read this figure" (axes, what to look at, the takeaway). Check each referenced file exists in `docs/assets/papers/`. Where a concept would be much clearer with an extra picture the paper doesn't have, generate one with matplotlib (white background, clear labels) and save it to `docs/assets/papers/gen/<slug>-<name>.png`; reference it as `../assets/papers/gen/<slug>-<name>.png`. Look at every generated image (Read tool) to make sure it's right. Aim for 1–4 generated diagrams per paper where they genuinely help (e.g. power transfer vs length, self-imaging pattern, ring transmission dip, adjoint "two simulations" picture, erosion/dilation of a density, a tiny neural net sketch).
7. Where it clarifies, a short runnable numpy snippet (≤ 40 lines) that reproduces a key equation/result, with plain comments and what the student should see.
8. `## How this connects to your project` — 1 short section: how this paper feeds the student's project (robust, fabrication-aware inverse design of silicon photonic devices with Meep/Tidy3D, Monte-Carlo yield, possible ML surrogate).
9. `!!! warning "Common confusions"`, then `## Check yourself` — 8–12 questions, each answer in a collapsible `??? note "Answer"` block, then `## Key takeaways` (bulleted).
10. `## Glossary` — table of every technical term used on the page with a one-line plain definition.

## Formatting rules
- Math: `$...$` inline and `$$...$$` display (MathJax via pymdownx.arithmatex). Don't put `$$` blocks inside list items. Escape nothing unusual; avoid `\begin{align}` with `&` inside tables.
- Admonitions `!!! note`, `!!! tip`, `!!! warning`, collapsible `??? note "Answer"`; their bodies MUST be indented 4 spaces.
- Explain in your own words — do not paste the paper's prose verbatim (short quotes of a key sentence are fine).
- No fragile raw HTML.

## Verify
`cd /Users/fenqinyang/Documents/PHD/reading-packets/study-site && .venv/bin/mkdocs build -d /private/tmp/claude-501/-Users-fenqinyang-Documents-PHD-reading-packets/008c3f12-5f2f-4cce-812e-4cb3e3a4831c/scratchpad/build-<slug> 2>&1 | grep -iE "warning|error" | grep -i "<your page filename stem>"` — fix any warnings about YOUR pages (broken image links etc.). "Not included in nav" INFO is expected; ignore it. Delete your build dir afterwards.

## Do NOT
Do not edit `mkdocs.yml`, any `index.md`, or any page other than the ones assigned to you. Do not run git. Many agents work in this repo in parallel.

## Report back (short)
For each page: path, approx line count, figures used (count), generated images created, and a proposed nav title like `"Tue 29 Sep · Yariv 1973 — Coupled-mode theory"`. Mention anything you couldn't do.
