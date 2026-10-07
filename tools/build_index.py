#!/usr/bin/env python3
"""
Regenerate the site's navigation and index pages from one catalog.

Writes:
  mkdocs.yml            (only the `nav:` block is replaced)
  docs/index.md         (home page: hero + week cards)
  docs/week-NN/index.md (one per week)
  docs/calendar.md      (every reading, by date, incl. revisits)

Run from anywhere:  python3 tools/build_index.py
Pages listed in CATALOG whose file does not exist yet are skipped.
"""

import datetime as dt
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(ROOT, "docs")
START = dt.date(2026, 9, 21)  # Monday of week 1

# (date, file stem, card title, source label, kind)
#   kind: book = Chrostowski & Hochberg, fdtd = Taflove & Hagness, paper = research paper
CATALOG = [
    ("2026-09-21", "day-01-mon-21-sep-2026", "Waveguide design, slab modes", "Chrostowski §3.2.1–3.2.4", "book"),
    ("2026-09-23", "day-03-wed-23-sep-2026", "Effective index method, bends", "Chrostowski §3.2.5–3.2.6, §3.3", "book"),
    ("2026-09-24", "day-04-thu-24-sep-2026-taflove-ch3", "Maxwell's equations & the Yee algorithm", "Taflove & Hagness Ch. 3", "fdtd"),
    ("2026-09-24", "day-04-thu-24-sep-2026-taflove-ch4", "Numerical dispersion & stability (Courant)", "Taflove & Hagness Ch. 4", "fdtd"),
    ("2026-09-28", "day-01-mon-28-sep-2026", "Directional couplers", "Chrostowski §4.1.1–4.1.3", "book"),
    ("2026-09-29", "day-02-tue-29-sep-2026-yariv-1973", "Coupled-mode theory", "Yariv 1973", "paper"),
    ("2026-09-30", "day-03-wed-30-sep-2026", "Mach–Zehnder, dispersion, compact models", "Chrostowski §4.3, §3.2.9–3.2.10", "book"),
    ("2026-10-02", "day-05-fri-2-oct-2026-soldano-1995", "MMI couplers & self-imaging", "Soldano & Pennings 1995", "paper"),
    ("2026-10-03", "day-06-sat-3-oct-2026-bogaerts-2012", "Silicon microring resonators", "Bogaerts et al. 2012", "paper"),
    ("2026-10-05", "day-01-mon-5-oct-2026", "Y-branch", "Chrostowski §4.2", "book"),
    ("2026-10-06", "day-02-tue-6-oct-2026", "Fabrication variation, waveguide loss", "Chrostowski §11.1, §3.2.11", "book"),
    ("2026-10-07", "day-03-wed-7-oct-2026", "Active tuning, thermo-optic switch", "Chrostowski §6.5–6.6, §3.1.1", "book"),
    ("2026-10-08", "day-04-thu-8-oct-2026", "Plasma dispersion, pn-junction phase shifters", "Chrostowski §6.1–6.2", "book"),
    ("2026-10-10", "day-06-sat-10-oct-2026-molesky-2018", "Inverse design in nanophotonics (review)", "Molesky et al. 2018", "paper"),
    ("2026-10-12", "day-01-mon-12-oct-2026-lalau-keraly-2013", "Adjoint shape optimisation", "Lalau-Keraly et al. 2013", "paper"),
    ("2026-10-13", "day-02-tue-13-oct-2026-hammond-2019", "Designing devices with neural networks", "Hammond & Camacho 2019", "paper"),
    ("2026-10-13", "day-02-tue-13-oct-2026-hammond-2022", "Meep's hybrid time/frequency adjoint solver", "Hammond et al. 2022", "paper"),
    ("2026-10-14", "day-03-wed-14-oct-2026", "Grating couplers", "Chrostowski §5.2", "book"),
    ("2026-10-19", "day-01-mon-19-oct-2026", "Ring resonators, ring modulators", "Chrostowski §4.4, §6.3", "book"),
    ("2026-10-21", "day-03-wed-21-oct-2026-hughes-2018", "Forward-mode differentiation of Maxwell's equations (ceviche)", "Hughes et al. 2019", "paper"),
    ("2026-10-26", "day-01-mon-26-oct-2026", "Tapers & adiabaticity", "Chrostowski §4.2, §5.3.1", "book"),
    ("2026-11-02", "day-01-mon-2-nov-2026", "Grating coupler theory", "Chrostowski §5.2.2", "book"),
    ("2026-11-03", "day-02-tue-3-nov-2026", "PDK & mask layout", "Chrostowski §10.1–10.2", "book"),
    ("2026-11-23", "day-01-mon-23-nov-2026-piggott-2015", "Inverse-designed WDM demultiplexer", "Piggott et al. 2015", "paper"),
    ("2026-11-23", "day-01-mon-23-nov-2026-piggott-2017", "Fabrication-constrained inverse design", "Piggott et al. 2017", "paper"),
    ("2026-11-24", "day-02-tue-24-nov-2026-schubert-2022", "Inverse design with strict foundry constraints", "Schubert et al. 2022", "paper"),
    ("2026-11-24", "day-02-tue-24-nov-2026-vercruysse-2019", "Analytical level-set fabrication constraints", "Vercruysse et al. 2019", "paper"),
    ("2026-11-25", "day-03-wed-25-nov-2026-lu-vuckovic-2013", "Objective-first nanophotonic design", "Lu & Vučković 2013", "paper"),
    ("2026-11-25", "day-03-wed-25-nov-2026-su-2020", "SPINS-B software architecture", "Su et al. 2020", "paper"),
    ("2026-11-26", "day-04-thu-26-nov-2026-hammond-2021", "Topology optimisation with foundry design rules", "Hammond et al. 2021", "paper"),
    ("2027-04-19", "day-01-mon-19-apr-2027-jiang-2021", "Deep neural networks for photonic design", "Jiang, Chen & Fan 2021", "paper"),
    ("2027-04-20", "day-02-tue-20-apr-2027-melati-2019", "Mapping the global design space with ML", "Melati et al. 2019", "paper"),
]

# Days the schedule sends you back to an earlier page: (date, stem of the page, what to do)
REVISITS = [
    ("2026-10-05", "day-05-fri-2-oct-2026-soldano-1995", "MMI self-imaging length for the Meep 1×2 MMI sweep"),
    ("2026-10-17", "day-01-mon-23-nov-2026-piggott-2015", "Choosing the Sprint 2 target — Piggott 2015 is reading, not the target"),
    ("2026-10-19", "day-06-sat-3-oct-2026-bogaerts-2012", "Critical coupling, intrinsic vs loaded Q"),
    ("2026-11-19", "day-01-mon-23-nov-2026-piggott-2017", "How Piggott 2017 defines erosion and dilation"),
    ("2026-11-19", "day-02-tue-24-nov-2026-schubert-2022", "How Schubert 2022 defines erosion and dilation"),
    ("2026-11-27", "day-06-sat-10-oct-2026-molesky-2018", "Re-read with the code in hand: bounds vs what is achievable"),
    ("2027-02-09", "day-01-mon-23-nov-2026-piggott-2017", "Re-read the constraint formulation with your own code"),
    ("2027-03-09", "day-02-tue-24-nov-2026-schubert-2022", "How they report robustness — steal the format"),
]

KIND_ICON = {"book": ":material-book-open-variant:", "fdtd": ":material-grid:", "paper": ":material-file-document-outline:"}


def week_of(d):
    return (d - START).days // 7 + 1


def short(d):
    return d.strftime("%a ") + str(d.day) + d.strftime(" %b")


def entries():
    out = []
    for ds, stem, title, src, kind in CATALOG:
        d = dt.date.fromisoformat(ds)
        w = week_of(d)
        rel = f"week-{w:02d}/{stem}.md"
        if os.path.exists(os.path.join(DOCS, rel)):
            out.append(dict(date=d, week=w, stem=stem, rel=rel, title=title, src=src, kind=kind))
    return out


def revisits(by_stem):
    out = []
    for ds, stem, what in REVISITS:
        if stem in by_stem:
            d = dt.date.fromisoformat(ds)
            out.append(dict(date=d, week=week_of(d), page=by_stem[stem], what=what))
    return out


def card(e, prefix):
    pdf = os.path.join(DOCS, e["rel"][:-3] + ".pdf")
    extra = f" · [:material-file-pdf-box: PDF]({prefix}{e['stem']}.pdf)" if os.path.exists(pdf) else ""
    return (f"-   <span class=\"day\">{short(e['date'])}</span>\n\n"
            f"    **[{e['title']}]({prefix}{e['stem']}.md)**\n\n"
            f"    <span class=\"secs\">{KIND_ICON[e['kind']]} {e['src']}</span>{extra}\n")


def revisit_card(r, link):
    p = r["page"]
    return (f"-   <span class=\"day\">{short(r['date'])} · revisit</span>\n\n"
            f"    **[{p['src']}]({link})**\n\n"
            f"    <span class=\"secs\">{r['what']}</span>\n")


def write(path, text):
    with open(path, "w") as f:
        f.write(text)


def main():
    es = entries()
    by_stem = {e["stem"]: e for e in es}
    rv = revisits(by_stem)
    weeks = sorted({e["week"] for e in es} | {r["week"] for r in rv})

    # ---- week index pages
    for w in weeks:
        we = [e for e in es if e["week"] == w]
        wr = [r for r in rv if r["week"] == w]
        lines = [f"# Week {w}\n",
                 f"<p class=\"lede\">{len(we)} reading{'s' if len(we) != 1 else ''} this week"
                 + (f", plus {len(wr)} revisit{'s' if len(wr) != 1 else ''}" if wr else "") + ".</p>\n"]
        if we:
            lines.append("<div class=\"grid cards\" markdown>\n")
            lines += [card(e, "") for e in we]
            lines.append("</div>\n")
        if wr:
            lines.append("<p class=\"week-label\">Revisit</p>\n\n<div class=\"grid cards\" markdown>\n")
            for r in wr:
                lines.append(revisit_card(r, "../" + r["page"]["rel"]))
            lines.append("</div>\n")
        os.makedirs(os.path.join(DOCS, f"week-{w:02d}"), exist_ok=True)
        write(os.path.join(DOCS, f"week-{w:02d}", "index.md"), "\n".join(lines))

    # ---- calendar
    rows = [(e["date"], f"[{e['title']}]({e['rel']})", e["src"], "Read") for e in es]
    rows += [(r["date"], f"[{r['page']['title']}]({r['page']['rel']})", r["page"]["src"], "Revisit — " + r["what"]) for r in rv]
    rows.sort(key=lambda x: (x[0], x[3] != "Read"))
    cal = ["# Reading calendar\n",
           "<p class=\"lede\">Every textbook section, FDTD chapter and research paper in the schedule, on the date you study it.</p>\n",
           "| Week | Date | Page | Source | |", "|---|---|---|---|---|"]
    for d, link, src, what in rows:
        cal.append(f"| {week_of(d)} | {d.strftime('%a')} {d.day} {d.strftime('%b %Y')} | {link} | {src} | {what} |")
    write(os.path.join(DOCS, "calendar.md"), "\n".join(cal) + "\n")

    # ---- home page: replace everything between the hero and "## How each day works"
    home_path = os.path.join(DOCS, "index.md")
    home = open(home_path).read()
    head = home.split("<p class=\"week-label\">", 1)[0]
    tail = home[home.index("## How each day works"):]
    body = []
    for w in weeks:
        we = [e for e in es if e["week"] == w]
        if not we:
            continue
        body.append(f"<p class=\"week-label\">Week {w}</p>\n\n<div class=\"grid cards\" markdown>\n")
        body += [card(e, f"week-{w:02d}/") for e in we]
        body.append("</div>\n")
    write(home_path, head + "\n".join(body) + "\n" + tail)

    # ---- mkdocs.yml nav
    nav = ["nav:", "  - Home: index.md", "  - Calendar: calendar.md"]
    for w in weeks:
        nav.append(f"  - Week {w}:")
        nav.append(f"      - week-{w:02d}/index.md")
        for e in [e for e in es if e["week"] == w]:
            label = f"{short(e['date'])} · {e['title']} ({e['src']})".replace('"', "'")
            nav.append(f"      - \"{label}\": {e['rel']}")
    yml_path = os.path.join(ROOT, "mkdocs.yml")
    yml = open(yml_path).read()
    yml = re.sub(r"\nnav:\n(?:  .*\n?)*", "\n" + "\n".join(nav) + "\n", yml)
    write(yml_path, yml)

    print(f"{len(es)} pages, {len(rv)} revisits, weeks {weeks}")


if __name__ == "__main__":
    main()
