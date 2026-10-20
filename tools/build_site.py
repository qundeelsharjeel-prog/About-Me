#!/usr/bin/env python3
"""Builds the Material 3 portfolio site (docs/) and the root README.md.

Case-study content lives in each project's README.md. Profile data (skills,
experience, project cards) is defined below. Run from anywhere:

    python tools/build_site.py
"""
from __future__ import annotations

import html
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "docs"
ASSETS = Path(__file__).resolve().parent / "assets"
SITE_URL = "https://qundeelsharjeel-prog.github.io/About-Me/"

NAME = "Qundeel Chaudhary"
ROLE = "Senior Full Stack Web & App Developer"
LOCATION = "Lahore, Pakistan"
EMAIL = "qundeelsharjeel@gmail.com"
PHONE = "+923715622246"
LINKEDIN = "https://www.linkedin.com/in/qundeelch"
SUMMARY = (
    "I design, build and deploy web applications and cross-platform mobile apps across "
    "finance, healthcare, e-learning, marketplace and B2B procurement. I build products end "
    "to end: responsive frontends in React, Angular and Tailwind CSS, mobile apps in Flutter, "
    "and backends in Node.js / NestJS, ASP.NET Core and FastAPI on PostgreSQL, MySQL, MongoDB "
    "and SQL Server. I have built business platforms from scratch with role-based access, admin "
    "dashboards, payments and third-party integrations (OpenAI, Meta Messenger, SMS / OTP, "
    "payment gateways, Microsoft 365, Salesforce), and I use agentic AI and AI-assisted "
    "engineering (Claude Code, Antigravity, OpenAI API) to take products from concept to production."
)

# (folder, display name, one-line description, filter tags, stack line, material icon)
PROJECTS = [
    ("ikarus", "Ikarus", "Online learning platform with live teacher booking, real-time chat and a unified wallet.",
     ["Flutter", "Angular", "Node.js"], "Flutter, Angular, Node.js, MongoDB, Socket.IO", "school"),
    ("carelink", "CareLink (PulseAI)", "AI healthcare platform with a draft, review, refine pipeline, built in 10 days.",
     ["Flutter", "FastAPI"], "Flutter, FastAPI, PostgreSQL, OpenAI", "health_and_safety"),
    ("procuremate", "ProcureMate", "B2B procurement: RFQs, quotations, negotiation, purchase orders, KYC and payments.",
     ["React", "NestJS"], "React, NestJS, Prisma, PostgreSQL", "request_quote"),
    ("munasib", "Munasib (Talenzo)", "Bilingual careers and freelance gig platform for the Gulf, with an AI résumé builder.",
     ["FastAPI"], "FastAPI, PostgreSQL, Redis, Docker", "work"),
    ("bar-w-bar", "Bar w Bahr", "Kuwait classifieds marketplace with three payment gateways and admin moderation.",
     ["Flutter", "FastAPI"], "Flutter, FastAPI, PostgreSQL", "storefront"),
    ("abby", "Abby", "AI product search and price comparison across stores, with admin dashboard and mock-mode mobile app.",
     ["Flutter", "NestJS", "React"], "Flutter, NestJS, React, MongoDB, Redis", "price_check"),
    ("azala", "Azala", "Multi-store marketplace with one cart, per-store checkout and a wallet.",
     ["NestJS", "React"], "NestJS, MongoDB, React", "shopping_cart"),
    ("khayyat", "Khayyat", "Kuwait fashion marketplace connecting customers with designers and tailors.",
     ["FastAPI"], "FastAPI, PostgreSQL, DDD", "checkroom"),
    ("rabt", "Rabt", "Group finance app: shared expenses plus Kamati / Jameia savings circles.",
     ["FastAPI"], "FastAPI, PostgreSQL, DDD", "groups"),
    ("coffee-wallet", "Coffee Wallet", "Prepaid coffee card app for Kuwait: SRS, client questions and architecture.",
     ["FastAPI", "React"], "FastAPI, React, MongoDB", "coffee"),
    ("icaremanager", "iCareManager", "Healthcare management platform on microservices, with a centralized logging service.",
     [".NET", "Angular"], "ASP.NET, .NET Core, Angular, SQL Server", "medical_services"),
    ("messenger-ai-chatbot", "Messenger AI Chatbot", "Custom Odoo 19 module that answers Messenger customers with AI.",
     ["Odoo"], "Odoo 19, Python, Meta Messenger", "smart_toy"),
    ("pepsi-cola-erp", "Pepsi Cola ERP", "Sales and purchase ERP module: .NET 3 to .NET 8 upgrade and faster reports.",
     [".NET"], ".NET 8, ADO.NET, Azure Functions", "inventory_2"),
]

SKILLS = [
    ("Web", "web", ["React", "Angular", "TypeScript", "JavaScript (ES6+)", "HTML5", "CSS3", "Tailwind CSS",
                    "Bootstrap", "TanStack Query"]),
    ("Mobile", "smartphone", ["Flutter", "Dart", "FCM push", "Socket.IO", "SignalR"]),
    ("Backend & APIs", "dns", ["Node.js", "NestJS", "ASP.NET Core", "ASP.NET Web API & MVC", "FastAPI",
                               "REST APIs", "Microservices", "Hangfire"]),
    ("Data", "database", ["PostgreSQL", "MySQL", "MongoDB", "MS SQL Server", "Redis", "Entity Framework",
                          "Dapper", "ADO.NET", "Prisma", "SQLAlchemy 2.0", "Alembic"]),
    ("Auth & Security", "lock", ["JWT", "OAuth 2.0", "KeyCloak", "RBAC", "OTP verification", "Argon2"]),
    ("Integrations", "hub", ["OpenAI API", "Meta Messenger", "Stripe", "MyFatoorah", "UPayments", "Tap", "KNet",
                             "Infobip", "SMSBox", "Gmail API", "Microsoft 365", "Salesforce"]),
    ("Cloud & DevOps", "cloud", ["Azure", "Azure Functions", "Azure DevOps", "CI/CD", "Docker", "AWS EC2",
                                 "Linux VPS", "Nginx"]),
    ("Architecture & Testing", "architecture", ["Clean Architecture", "Domain-Driven Design", "Repository",
                                                "Unit of Work", "Service Layer", "Strategy", "xUnit", "NUnit"]),
    ("AI & ERP", "auto_awesome", ["OpenAI API", "Multi-agent pipelines", "Claude Code", "Antigravity",
                                  "Odoo (consulting, custom modules)"]),
    ("Languages", "terminal", ["C#", "Python", "JavaScript", "TypeScript", "Dart", "C/C++"]),
]

# (company, title, meta, bullets, case-study folder or None)
EXPERIENCE = [
    ("iCareManager", "Senior Software Engineer", "Full-time · Remote (US) · 02/2022 – Present", [
        "Designed a centralized logging microservice with Serilog and OpenTelemetry, plus an SDK wrapper that enforces one logging standard across services.",
        "Built and improved ASP.NET MVC 4.7 and .NET Core 6/9 modules: dynamic labels, complex forms, module permissions, UI in Jade and Angular 10.",
        "Fixed production issues and refactored features to cut bugs and latency.",
        "Use AI-assisted engineering (OpenAI API, Claude Code, Antigravity) to speed up delivery, refactors and debugging.",
    ], "icaremanager"),
    ("ITInSync Technology", "Software Engineer", "Full-time · On-site · 02/2021 – 01/2022", [
        "Built a data security project with FTP monitoring, real-time file tracking, encryption, MS SQL and Hangfire job queues.",
        "Built a room reservation and employee management system on ASP.NET 6 / 8 with JWT, integrated with Microsoft 365 and Salesforce.",
        "Built ERP forms and reports in Angular with Ag-Grid, backed by APIs and microservices using the Repository pattern.",
    ], None),
    ("Pepsi Cola", "Software Engineer", "Full-time · On-site · 02/2020 – 01/2021", [
        "Upgraded a legacy .NET Framework 3 project to .NET 8.",
        "Fixed Azure Functions issues and implemented Unit of Work with ADO.NET.",
        "Designed secure, high-performance REST APIs and improved endpoint security.",
    ], "pepsi-cola-erp"),
]

STATS = [("6+", "Years of experience"), (str(len(PROJECTS)), "Case studies"), ("7", "Industry domains")]

SECTION_ICONS = {
    "Overview": "info", "My Role": "person", "The Problem": "report", "The Solution": "lightbulb",
    "Tech Stack": "code", "Architecture & Key Decisions": "account_tree", "Key Features": "star",
    "Challenges & How I Solved Them": "extension", "Outcome": "flag", "Deployment": "cloud_upload",
}

FONTS = (
    '<link rel="preconnect" href="https://fonts.googleapis.com">'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
    '<link href="https://fonts.googleapis.com/css2?family=Roboto+Flex:opsz,wght@8..144,300..700'
    '&family=Roboto+Mono:wght@400&display=swap" rel="stylesheet">'
    '<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:'
    'opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200&display=block" rel="stylesheet">'
)
THEME_BOOT = (
    "<script>(function(){try{var t=localStorage.getItem('theme');"
    "if(!t){t=matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light'}"
    "document.documentElement.setAttribute('data-theme',t)}catch(e){}})()</script>"
)
FAVICON = (
    "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E"
    "%3Ccircle cx='32' cy='32' r='32' fill='%23006a6a'/%3E%3Ctext x='32' y='41' font-size='26' "
    "font-family='Arial' font-weight='700' text-anchor='middle' fill='white'%3EQC%3C/text%3E%3C/svg%3E"
)


# --------------------------------------------------------------------- helpers
def esc(s: str) -> str:
    return html.escape(s, quote=True)


def inline(s: str) -> str:
    """Tiny Markdown subset: code, links, bold, italics."""
    s = html.escape(s, quote=False)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(
        r"\[([^\]]+)\]\(([^)]+)\)",
        lambda m: f'<a href="{esc(m.group(2))}" target="_blank" rel="noopener">{m.group(1)}</a>',
        s,
    )
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", s)
    return s


def icon(name: str, fill: bool = False) -> str:
    return f'<span class="icon{" fill" if fill else ""}" aria-hidden="true">{name}</span>'


def initials(name: str) -> str:
    parts = name.split()
    return (parts[0][0] + parts[-1][0]).upper()


class Doc:
    def __init__(self, title: str, intro: list[list[str]], sections: list[tuple[str, list]], links: list[tuple[str, str]]):
        self.title, self.intro, self.sections, self.links = title, intro, sections, links


def parse_readme(path: Path) -> Doc:
    """Returns title, overview paragraphs, other sections as blocks, and links."""
    title = path.parent.name
    sections: dict[str, list[str]] = {}
    current = None
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.rstrip()
        if line.startswith("# "):
            title = re.sub(r"\s+[—-]\s+Case Study$", "", line[2:].strip())
        elif line.startswith("## "):
            current = line[3:].strip()
            sections[current] = []
        elif current and not line.startswith("[←"):
            sections[current].append(line)

    def blocks(lines: list[str]) -> list:
        out: list = []
        para: list[str] = []
        items: list[str] = []

        def flush() -> None:
            nonlocal para, items
            if para:
                out.append(("p", " ".join(para)))
                para = []
            if items:
                out.append(("ul", items))
                items = []

        for ln in lines:
            if not ln.strip():
                flush()
            elif ln.startswith("- "):
                if para:
                    flush()
                items.append(ln[2:].strip())
            else:
                if items:
                    flush()
                para.append(ln.strip())
        flush()
        return out

    links: list[tuple[str, str]] = []
    for ln in sections.pop("Links", []):
        m = re.match(r"-\s+([^:]+):\s+(\S+)", ln.strip())
        if m:
            links.append((m.group(1).strip(), m.group(2).strip()))

    overview = [b[1] for b in blocks(sections.pop("Overview", [])) if b[0] == "p"]
    body = [(name, blocks(lines)) for name, lines in sections.items()]
    return Doc(title, overview, body, links)


def render_blocks(blocks: list) -> str:
    out = []
    for kind, val in blocks:
        if kind == "p":
            out.append(f"<p>{inline(val)}</p>")
        else:
            out.append("<ul>" + "".join(f"<li>{inline(i)}</li>" for i in val) + "</ul>")
    return f'<div class="prose">{"".join(out)}</div>'


def link_button(label: str, url: str, style: str) -> str:
    return (f'<a class="btn {style}" href="{esc(url)}" target="_blank" rel="noopener">'
            f'{icon("open_in_new")}{esc(label)}</a>')


def page(title: str, description: str, body: str, *, home: bool, bottom: str = "") -> str:
    prefix = "" if home else ""
    return f"""<!doctype html>
<html lang="en" class="no-js" data-theme="light">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
<meta name="theme-color" content="#006a6a">
<link rel="icon" href="{FAVICON}">
{THEME_BOOT}
{FONTS}
<link rel="stylesheet" href="{prefix}assets/style.css">
</head>
<body{' class="has-bottomnav"' if home else ''}>
{body}
{bottom}
<script src="{prefix}assets/app.js" defer></script>
</body>
</html>
"""


def appbar(home: bool) -> str:
    nav = ""
    brand_href = "#top" if home else "index.html"
    if home:
        items = [("about", "About"), ("skills", "Skills"), ("experience", "Experience"),
                 ("projects", "Projects"), ("contact", "Contact")]
        nav = '<nav class="topnav" aria-label="Sections">' + "".join(
            f'<a href="#{i}" data-nav="{i}">{t}</a>' for i, t in items) + "</nav>"
    back = ""
    if not home:
        back = (f'<a class="icon-btn" href="index.html#projects" aria-label="Back to all projects">'
                f'{icon("arrow_back")}</a>')
    return f"""<header class="appbar"><div class="wrap">
{back}<a class="brand" href="{brand_href}"><span class="logo">{initials(NAME)}</span><span>{NAME}</span></a>
<span class="spacer"></span>{nav}
<button class="icon-btn" id="theme-toggle" type="button" aria-label="Switch theme">{icon("dark_mode")}</button>
</div></header>"""


# ----------------------------------------------------------------------- index
def build_index(docs: dict[str, Doc]) -> str:
    tags = sorted({t for p in PROJECTS for t in p[3]})
    chips = ['<button class="chip" type="button" data-filter="all" aria-pressed="true">All</button>'] + [
        f'<button class="chip" type="button" data-filter="{esc(t)}" aria-pressed="false">{esc(t)}</button>' for t in tags
    ]

    skills = "".join(
        f'<div class="card reveal"><h3>{icon(ic)}{esc(name)}</h3>'
        f'<div class="chips">{"".join(f"""<span class="chip static">{esc(s)}</span>""" for s in items)}</div></div>'
        for name, ic, items in SKILLS
    )

    jobs = ""
    for company, title, meta, bullets, case in EXPERIENCE:
        action = ""
        if case:
            action = (f'<div class="btn-row" style="margin-top:12px"><a class="btn tonal" href="{case}.html">'
                      f'{icon("arrow_forward")}Case study</a></div>')
        jobs += (f'<div class="job reveal"><div class="dot">{icon("work")}</div><div class="card">'
                 f'<h3>{esc(company)}</h3><div class="meta"><strong>{esc(title)}</strong> · {esc(meta)}</div>'
                 f'<ul>{"".join(f"<li>{esc(b)}</li>" for b in bullets)}</ul>{action}</div></div>')

    cards = ""
    for folder, name, blurb, ptags, stack, ic in PROJECTS:
        doc = docs[folder]
        ext = "".join(
            f'<a class="btn text" href="{esc(u)}" target="_blank" rel="noopener">{esc(l)}</a>' for l, u in doc.links)
        cards += (
            f'<article class="pcard reveal" data-tags="{esc("|".join(ptags))}">'
            f'<div class="top"><span class="pi">{icon(ic)}</span><h3>{esc(name)}</h3></div>'
            f'<p>{esc(blurb)}</p>'
            f'<div class="chips">{"".join(f"""<span class="chip static">{esc(s.strip())}</span>""" for s in stack.split(","))}</div>'
            f'<div class="actions"><a class="btn text" href="{folder}.html">Case study{icon("arrow_forward")}</a>{ext}</div>'
            f'</article>'
        )

    stats = "".join(f'<div class="stat"><b>{n}</b><span>{esc(t)}</span></div>' for n, t in STATS)

    body = f"""{appbar(True)}
<main>
<section class="hero" id="top"><div class="wrap">
  <div class="hero-card">
    <div class="avatar" aria-hidden="true">{initials(NAME)}</div>
    <div class="hero-body">
      <h1>{NAME}</h1>
      <p class="role">{ROLE}</p>
      <p class="loc">{icon("location_on")}{LOCATION}</p>
      <div class="btn-row">
        <a class="btn tonal" href="mailto:{EMAIL}">{icon("mail")}Email</a>
        <a class="btn outlined" href="{LINKEDIN}" target="_blank" rel="noopener">{icon("link")}LinkedIn</a>
        <a class="btn outlined" href="tel:{PHONE}">{icon("call")}Call</a>
      </div>
    </div>
  </div>
  <div class="stats">{stats}</div>
</div></section>

<section class="block" id="about"><div class="wrap reveal">
  <h2 class="eyebrow">{icon("person")}About</h2>
  <p class="lead">{esc(SUMMARY)}</p>
</div></section>

<section class="block" id="skills"><div class="wrap">
  <h2 class="eyebrow">{icon("code")}Skills</h2>
  <div class="skills">{skills}</div>
</div></section>

<section class="block" id="experience"><div class="wrap">
  <h2 class="eyebrow">{icon("work")}Experience</h2>
  <div class="timeline">{jobs}</div>
</div></section>

<section class="block" id="projects"><div class="wrap">
  <h2 class="eyebrow">{icon("folder_open")}Case studies <span class="chip static" id="project-count" style="margin-left:8px">{len(PROJECTS)} projects</span></h2>
  <div class="filters" role="group" aria-label="Filter by technology">{"".join(chips)}</div>
  <div class="grid">{cards}</div>
</div></section>

<section class="block" id="contact"><div class="wrap">
  <div class="contact-card reveal">
    <h2>Let's build something</h2>
    <p class="lead" style="color:inherit">Open to senior full stack and mobile roles and to project work. The fastest way to reach me is email.</p>
    <div class="btn-row">
      <a class="btn filled" href="mailto:{EMAIL}">{icon("mail")}{EMAIL}</a>
      <a class="btn outlined" href="tel:{PHONE}">{icon("call")}{PHONE}</a>
      <a class="btn outlined" href="{LINKEDIN}" target="_blank" rel="noopener">{icon("link")}LinkedIn</a>
    </div>
  </div>
</div></section>
</main>
<footer><div class="wrap">© {NAME} · {LOCATION}</div></footer>"""

    bottom = (
        '<nav class="bottomnav" aria-label="Sections">'
        + "".join(
            f'<a href="#{i}" data-nav="{i}"><span class="pill">{icon(ic)}</span>{label}</a>'
            for i, ic, label in [("top", "home", "Home"), ("skills", "code", "Skills"),
                                 ("experience", "work", "Work"), ("projects", "apps", "Projects"),
                                 ("contact", "mail", "Contact")]
        )
        + "</nav>"
    )
    return page(f"{NAME} · {ROLE}", SUMMARY[:200], body, home=True, bottom=bottom)


# ------------------------------------------------------------------ case study
def build_project(i: int, docs: dict[str, Doc]) -> str:
    folder, name, blurb, ptags, stack, ic = PROJECTS[i]
    doc = docs[folder]
    lead = "".join(f"<p>{inline(p)}</p>" for p in doc.intro) or f"<p>{esc(blurb)}</p>"
    chips = "".join(f'<span class="chip static">{esc(t)}</span>' for t in ptags)
    buttons = "".join(link_button(l, u, "filled" if k == 0 else "outlined") for k, (l, u) in enumerate(doc.links))
    buttons = f'<div class="btn-row">{buttons}</div>' if buttons else ""

    cards = ""
    for sname, blocks in doc.sections:
        if not blocks:
            continue
        size = sum(len(str(b[1])) for b in blocks)
        wide = " wide" if size > 650 else ""
        cards += (f'<section class="card{wide} reveal"><h3>{icon(SECTION_ICONS.get(sname, "label"))}{esc(sname)}</h3>'
                  f'{render_blocks(blocks)}</section>')

    prev_btn = next_btn = "<span></span>"
    if i > 0:
        p = PROJECTS[i - 1]
        prev_btn = f'<a class="btn tonal" href="{p[0]}.html">{icon("arrow_back")}{esc(p[1])}</a>'
    if i < len(PROJECTS) - 1:
        n = PROJECTS[i + 1]
        next_btn = f'<a class="btn tonal" href="{n[0]}.html">{esc(n[1])}{icon("arrow_forward")}</a>'

    body = f"""{appbar(False)}
<main><div class="wrap">
<div class="page-head">
  <a class="btn text crumb" href="index.html#projects">{icon("arrow_back")}All projects</a>
  <div class="title-card">
    <span class="kind">Case study</span>
    <h1>{esc(doc.title)}</h1>
    <div class="lead">{lead}</div>
    <div class="chips">{chips}</div>
    {buttons}
  </div>
</div>
<div class="sections">{cards}</div>
<div class="pager">{prev_btn}{next_btn}</div>
</div></main>
<footer><div class="wrap">© {NAME} · <a href="index.html">Portfolio</a></div></footer>"""
    return page(f"{doc.title} · {NAME}", blurb, body, home=False)


# ---------------------------------------------------------------------- README
def build_readme() -> str:
    rows = "\n".join(
        f"| [{n}]({f}/README.md) | {b} | {s} |" for f, n, b, _t, s, _i in PROJECTS
    )
    skills = "\n".join(f"- **{n}:** {', '.join(items)}" for n, _ic, items in SKILLS)
    jobs = "\n\n".join(
        f"**{c}** — {t} · {m}\n" + "\n".join(f"- {b}" for b in bullets) for c, t, m, bullets, _x in EXPERIENCE
    )
    return f"""# {NAME}

**{ROLE}** · {LOCATION}

[Email](mailto:{EMAIL}) · [{PHONE}](tel:{PHONE}) · [LinkedIn]({LINKEDIN}) · [**Portfolio site**]({SITE_URL})

## About
{SUMMARY}

## Skills
{skills}

## Experience
{jobs}

## Case Studies
| Project | What it is | Stack |
|---|---|---|
{rows}

> The portfolio site ({SITE_URL}) shows the same case studies in a Material Design layout.
> It is generated by `python tools/build_site.py`; edit the content in each project's `README.md`
> and in `tools/build_site.py`, then run the script.
"""


# ------------------------------------------------------------------------ main
def main() -> None:
    docs = {}
    for folder, *_ in PROJECTS:
        path = ROOT / folder / "README.md"
        if not path.exists():
            raise SystemExit(f"missing {path}")
        docs[folder] = parse_readme(path)

    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / "assets").mkdir(parents=True)
    for f in ("style.css", "app.js"):
        shutil.copy(ASSETS / f, OUT / "assets" / f)
    (OUT / ".nojekyll").write_text("", encoding="utf-8")

    (OUT / "index.html").write_text(build_index(docs), encoding="utf-8")
    for i, (folder, *_rest) in enumerate(PROJECTS):
        (OUT / f"{folder}.html").write_text(build_project(i, docs), encoding="utf-8")
    (ROOT / "README.md").write_text(build_readme(), encoding="utf-8")
    print(f"built {1 + len(PROJECTS)} pages in {OUT}")


if __name__ == "__main__":
    main()
