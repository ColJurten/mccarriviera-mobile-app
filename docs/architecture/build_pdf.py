#!/usr/bin/env python3
"""Build architecture.pdf from the PlantUML sources in this folder.

Usage (from the repository root):
    PLANTUML_JAR=/path/to/plantuml.jar python3 docs/architecture/build_pdf.py

Needs Java 17+, Graphviz, the Inter font, and Python 3 with Playwright (Chromium).
It renders every NN-*.puml to svg/, lays the diagrams out on the pages below and prints
them to architecture.pdf with Chromium. Edit the .puml files and the page texts here,
never the PDF or the SVG files.
"""
import html
import os
import pathlib
import re
import subprocess
import sys
import tempfile

HERE = pathlib.Path(__file__).resolve().parent
SVG_DIR = HERE / "svg"
OUT = HERE / "architecture.pdf"
VERSION = "Version 1 · 9 October 2026"
DOC = "MC Car Riviera staff app · planned architecture"

# ---------------------------------------------------------------- page content

ACCOUNTS = [
    ("company", "Company's account (Apple)"),
    ("developer", "Developer's accounts (F-02)"),
    ("device", "Phone or computer"),
    ("option", "Option still open (F-11)"),
]
ACCOUNTS_NO_OPTION = ACCOUNTS[:3]
OPTION_COLOURS = [
    ("developer", "Run by a provider"),
    ("you", "Built or run by the developer"),
    ("plain", "S3-compatible bucket"),
]

PAGES = [
    {"kind": "cover"},
    {
        "uml": "deployment",
        "title": "System overview: what runs where",
        "subtitle": "UML deployment diagram · the app in daily use",
        "diagrams": ["01-system-overview"],
        "layout": "side",
        "legend": ACCOUNTS,
        "notes": [
            "The app is the only part on the phones. There is no local database and no offline mode; only generated PDFs sit in the app cache, for 7 days at most.",
            "Every call goes over HTTPS to one Supabase project in the EU. The phone holds the project URL, the public anon key and the staff member's session, never a database password or a storage key.",
            "Files are private. The app opens them through signed links that expire within 5 minutes.",
            "A nightly job copies the database and the new files, encrypted, to a second EU provider. The job's key can't delete anything there.",
            "Crash reports go to Sentry in the EU, with no personal data.",
        ],
        "refs": "ADR-0004 · ADR-0005 · ADR-0012 · ADR-0013 · ADR-0014 · ADR-0015 · ADR-0017",
    },
    {
        "uml": "deployment",
        "title": "Build, release and development",
        "subtitle": "UML deployment diagram · from the developer's PC to the staff phones",
        "diagrams": ["02-build-and-release"],
        "layout": "side",
        "legend": ACCOUNTS_NO_OPTION,
        "notes": [
            "No Mac: EAS Build compiles the iOS app in the cloud. Builds are started on purpose; the free plan includes 15 iOS builds a month.",
            "Every build is installed by Ad Hoc internal distribution, signed with the company's Apple certificate. EAS holds it through the developer's Admin access; if the collaboration ends, the company revokes it and issues a new one.",
            "Staging holds synthetic data only. It serves the test iPhone and the Android emulator; production serves only the two staff phones.",
            "Migrations reach staging on merge to main, and production on a release tag after manual approval. JavaScript-only fixes go out as EAS Updates.",
        ],
        "refs": "ADR-0002 · ADR-0003 · ADR-0016 · ADR-0018 · US-001 · US-005",
    },
    {
        "uml": "component",
        "title": "Front end: the iOS app",
        "subtitle": "UML component diagram · one Expo app; each screen lists the stories that build it",
        "diagrams": ["03-app-components"],
        "layout": "below",
        "notes": [
            "Screens are in French, built with translation keys so English can be added later.",
            "Server data is kept in memory only (TanStack Query, no persister). Forms are checked with zod before anything is sent.",
            "The contract PDF is rendered on the phone from versioned HTML templates and the FR / EN catalogues, then archived and shared.",
            "Photos are resized and stripped of their location before upload. The session is encrypted, with its key in the Keychain. Crash reports carry no personal data.",
        ],
        "refs": "ADR-0002 · ADR-0010 · ADR-0011 · ADR-0012 · ADR-0013 · ADR-0017",
    },
    {
        "uml": "component",
        "title": "Back end: one Supabase project",
        "subtitle": "UML component diagram · no custom server; the database enforces the rules",
        "diagrams": ["04-backend-components"],
        "layout": "below",
        "notes": [
            "Row-level security on every table, denied by default: only staff with an active profile can read or write.",
            "Every status change (sign, close, amend, void, maintenance) is one server function running in one transaction, so two phones can't rent the same car.",
            "Status columns are read-only for the app, and evidence tables accept inserts only. Audit triggers record every write with the values before and after.",
            "Evidence buckets have no update or delete policy. The service-role key, the database credential and the storage S3 keys live only in protected CI environments.",
        ],
        "refs": "ADR-0004 · ADR-0007 · ADR-0012 · ADR-0014 · ADR-0015 · ADR-0016 · US-006 · US-007",
    },
    {
        "uml": "class",
        "title": "Database: the 17 tables",
        "subtitle": "UML class diagram · overview; the fields are on the next three pages",
        "diagrams": ["05-data-overview"],
        "layout": "below",
        "notation": True,
        "notes": [
            "Working table names from US-006. Once the migrations exist they are the reference, and these diagrams follow them.",
            "A contract is a header plus numbered revisions. Revision 1 is the Départ as signed; each amendment adds a revision with a full snapshot.",
            "Condition evidence is reused: a Départ's inspection points to the vehicle's current reference photo set and to the damage open at that moment (drawn on « What each handover records »).",
        ],
        "refs": "ADR-0007 · ADR-0008 · US-006",
    },
    {
        "uml": "class",
        "title": "Database detail: fleet, photos, damage, maintenance",
        "subtitle": "UML class diagram · vehicles, condition_baselines, photos, damages, maintenance_records",
        "diagrams": ["06-data-fleet"],
        "layout": "side",
        "notation": True,
        "notes": [
            "A reference set has the 8 exterior angles, all required, plus an optional interior photo. It is taken with the in-app camera.",
            "The optional dashboard photo (km and fuel) belongs to a handover's inspection, not to the reference set: reused later, it would show an old odometer reading.",
            "Finishing a damage repair closes the repaired damage. The car can be rented again only once a new complete reference set exists.",
            "Photos and reference sets are insert-only. Statuses change only through server functions.",
        ],
        "refs": "ADR-0008 · F-10 · US-022 · US-026 · US-080 – US-082",
    },
    {
        "uml": "class",
        "title": "Database detail: clients, contracts and their terms",
        "subtitle": "UML class diagram · clients, client_documents, contracts, contract_drivers, contract_revisions, terms_versions",
        "diagrams": ["07-data-contracts"],
        "layout": "side",
        "notation": True,
        "notes": [
            "Signing freezes revision 1: the client and vehicle values are copied as printed, so later edits to a client or a vehicle never change a signed contract.",
            "Card: brand, last four digits and expiry only. No column can hold a full card number or a CVV (F-09, PCI DSS).",
            "Every amount is typed by staff (F-06). The app computes only km driven and extra km.",
            "Each revision records the French and English terms versions in force when it was signed.",
        ],
        "refs": "ADR-0006 · ADR-0007 · ADR-0011 · US-031 · US-051 · US-052 · US-061",
    },
    {
        "uml": "class",
        "title": "Database detail: what each handover records",
        "subtitle": "UML class diagram · inspections, signatures, contract_documents (grey: drawn in full on earlier pages)",
        "diagrams": ["08-data-evidence"],
        "layout": "below",
        "notation": True,
        "notes": [
            "Each signature has an evidence record: image hash, server time, staff member, device, iOS and app versions, and the hash of the data that was signed.",
            "Every generated PDF is archived with its SHA-256, its template version and its terms version, so it can be regenerated with the same content.",
            "Completed inspections, signatures and PDF records are insert-only. Until the client signs, the Retour's km, fuel, amounts and comments can still be corrected; whether a photo or a damage entry can be taken back is open (R-10 Q5).",
        ],
        "refs": "ADR-0007 · ADR-0009 · ADR-0010 · ADR-0014 · US-053 · US-057 · US-072 · US-074",
    },
    {
        "uml": "state",
        "title": "Lifecycle of a contract",
        "subtitle": "UML state machine · every transition is a server function, recorded in the audit trail",
        "diagrams": ["09-contract-states"],
        "layout": "side",
        "notes": [
            "A draft never changes the vehicle's status. Discarding it deletes the unsigned data, and the audit trail keeps a record.",
            "Signing the Départ assigns the number, freezes revision 1 and marks the car rented, in one transaction.",
            "An amendment adds a revision, signed by the client or recorded « sans signature du client » (default for R-11).",
            "A contract can be voided, with a reason, only before its Retour. The app never deletes a signed contract.",
        ],
        "refs": "ADR-0007 · ADR-0009 · US-056 · US-057 · US-061 · US-062 · US-074",
    },
    {
        "uml": "state",
        "title": "Lifecycle of a vehicle",
        "subtitle": "UML state machine · the labels in « » are what staff see in the app",
        "diagrams": ["10-vehicle-states"],
        "layout": "side",
        "notes": [
            "A Départ is offered only for available cars with a complete reference photo set.",
            "Routine maintenance needs no new photos. After a damage repair, a new complete reference set is required before the car is available again.",
            "Only an available car, or one in maintenance, can be archived. « Restaurer » brings it back; nothing is deleted.",
            "Statuses change only through server functions, in the same transaction as the contract or maintenance change.",
        ],
        "refs": "ADR-0007 · ADR-0008 · US-022 · US-025 · US-080 – US-082",
    },
    {
        "uml": "sequence",
        "title": "Départ: from choosing the car to the signed PDF",
        "subtitle": "UML sequence diagram · US-050 to US-057",
        "diagrams": ["11-sequence-depart"],
        "layout": "portrait",
        "notes": [
            "The signature image is uploaded before the signing function runs, so a contract is never marked signed without its signature.",
            "Step 16 is one transaction. If another phone took the car meanwhile, nothing is stored as signed.",
            "The client signs before the language is chosen. The same signature serves the French and the English PDF.",
        ],
        "refs": "ADR-0005 · ADR-0007 · ADR-0009 · ADR-0010",
    },
    {
        "uml": "sequence",
        "title": "Retour: check-in, mandatory signature, final PDF",
        "subtitle": "UML sequence diagram · US-070 to US-075",
        "diagrams": ["12-sequence-retour"],
        "layout": "portrait",
        "notes": [
            "The return signature is mandatory (F-04). Without the client, the Retour waits « en attente de signature » and the car stays « En cours ».",
            "Km driven and extra km are the only values the app computes. The final amounts are typed (F-06).",
            "In the final PDF the return signature is on every page. The departure signature is on every page except amendment pages, which carry the amendment's own signature (F-08).",
        ],
        "refs": "ADR-0005 · ADR-0007 · ADR-0009 · ADR-0010 · B-08",
    },
    {"kind": "why", "diagrams": ["13-hosting-options"]},
    {"kind": "options"},
]

UML_KINDS = [
    ("deployment", "Deployment diagram", "where each part runs, and who calls whom"),
    ("component", "Component diagram", "the parts of the software, and what uses what"),
    ("class", "Class diagram", "the tables, their fields and their links"),
    ("state", "State machine", "the statuses, and what moves a record from one to the next"),
    ("sequence", "Sequence diagram", "one workflow, message by message, from top to bottom"),
]

# ---------------------------------------------------------------- helpers

NOWRAP = re.compile(r"(SHA-256|MCR-YYYY-NNNN|ADR-\d{4}|US-\d{3}(?: – US-\d{3})?|[BFRTNL]-\d{2}|PCI DSS|€\d[\d.,–]*|\$\d+)")


def esc(text):
    """Escape text for HTML and keep IDs, prices and hashes on one line."""
    text = html.escape(text, quote=False).replace("« ", "«&nbsp;").replace(" »", "&nbsp;»")
    return NOWRAP.sub(r'<span class="nw">\1</span>', text)


def page_range(pred):
    nums = [i for i, p in enumerate(PAGES, start=1) if pred(p)]
    if not nums:
        return ""
    return str(nums[0]) if nums[0] == nums[-1] else f"{nums[0]}–{nums[-1]}"


def render_svgs():
    jar = os.environ.get("PLANTUML_JAR")
    if not jar:
        sys.exit("Set PLANTUML_JAR to the path of plantuml.jar")
    SVG_DIR.mkdir(exist_ok=True)
    for old in SVG_DIR.glob("*.svg"):
        old.unlink()
    sources = sorted(str(p) for p in HERE.glob("[0-9][0-9]-*.puml"))
    subprocess.run(
        ["java", "-Djava.awt.headless=true", "-jar", jar, "-tsvg", "-charset", "UTF-8",
         "-failfast2", "-o", str(SVG_DIR), *sources],
        check=True,
    )


def inline_svg(name):
    """Return the SVG as inline markup that scales to its box, with ids made unique."""
    svg = (SVG_DIR / f"{name}.svg").read_text(encoding="utf-8")
    svg = re.sub(r"<\?plantuml[^>]*\?>", "", svg)
    svg = re.sub(r"^<\?xml[^>]*>", "", svg)
    prefix = re.sub(r"[^a-z0-9]", "", name.lower())
    svg = re.sub(r'id="([^"]+)"', lambda m: f'id="{prefix}-{m.group(1)}"', svg)
    svg = re.sub(r"url\(#([^)]+)\)", lambda m: f"url(#{prefix}-{m.group(1)})", svg)
    svg = re.sub(r'href="#([^"]+)"', lambda m: f'href="#{prefix}-{m.group(1)}"', svg)
    head, rest = svg.split(">", 1)
    head = re.sub(r'\s(width|height|style|preserveAspectRatio)="[^"]*"', "", head)
    head += ' width="100%" height="100%" preserveAspectRatio="xMidYMid meet" role="img"'
    return head + ">" + rest


def legend_html(items, vertical=False):
    chips = "".join(
        f'<span class="chip"><i class="sw {kind}"></i><span>{esc(label)}</span></span>' for kind, label in items
    )
    return f'<div class="legend{" vertical" if vertical else ""}">{chips}</div>'


NOTATION = (
    '<div class="notation"><b>Notation</b>'
    '<span><i class="glyph">◆—</i>part of (belongs to one owner)</span>'
    '<span><i class="glyph">—›</i>refers to</span>'
    '<span><i class="glyph">1 · 0..1 · 0..*</i>how many</span>'
    '<span><i class="glyph">[0..1]</i>optional field</span>'
    '<span><i class="glyph">{…}</i>rule</span></div>'
)


def header(title, subtitle, number):
    return (
        '<header><div class="kicker">MC Car Riviera · staff app · planned architecture</div>'
        f'<h1><span class="num">{number}</span>{esc(title)}</h1>'
        f'<p class="sub">{esc(subtitle)}</p></header>'
    )


def footer(page_no, total, sources, refs=""):
    src = " · ".join(f"{s}.puml" for s in sources) if sources else "build_pdf.py"
    based = f"Based on {esc(refs)}" if refs else "Drawn from the ADRs and stories in docs/"
    return (
        "<footer>"
        f'<div class="row"><span>{esc(DOC)} · {esc(VERSION)}</span><span class="pg">{page_no} / {total}</span></div>'
        f'<div class="row small"><span class="refs">{based}</span><span>source: docs/architecture/{esc(src)}</span></div>'
        "</footer>"
    )


def notes_html(notes, columns=0):
    items = "".join(f"<li>{esc(n)}</li>" for n in notes)
    if columns:
        return f'<ul class="notes cols" style="grid-template-columns: repeat({columns}, 1fr)">{items}</ul>'
    return f'<ul class="notes">{items}</ul>'


# ---------------------------------------------------------------- pages


def cover_page(total):
    why = page_range(lambda p: p.get("kind") in ("why", "options"))
    glance = [
        ("Front end", "One iOS app in Expo · React Native · TypeScript, built in the cloud with EAS (no Mac needed). Installed on the two staff iPhones by Ad Hoc distribution. Online only: no business data is kept on the phones."),
        ("Back end", "One Supabase project in the EU, on the Free plan to start: Auth for staff sign-in, a REST + RPC Data API, and private Storage with signed links that expire within 5 minutes. No custom server."),
        ("Database", "PostgreSQL, 17 tables. Row-level security on every table, status changes only through server functions, signed data insert-only, an audit row for every write."),
        ("Contract PDF", "Rendered on the phone from versioned HTML templates, in French or English, with the signatures at the bottom right of every page. Archived with its SHA-256."),
        ("Operations", "Nightly encrypted backup to a second EU provider, crash reports to Sentry EU without personal data, database migrations by CI."),
        ("Accounts", "Apple Developer Program: the company. Expo, GitHub, Supabase, backup storage and Sentry: the developer (F-02), who pays the hosting (F-07)."),
        ("Still open", f"F-11: keep the files in Supabase Storage, or move them to an EU S3 bucket (recommended, pages {why}). Legal checks L-01 to L-07 before go-live."),
    ]
    rows = "".join(f"<tr><th>{esc(k)}</th><td>{esc(v)}</td></tr>" for k, v in glance)
    contents = []
    for i, p in enumerate(PAGES[1:], start=2):
        title = p.get("title") or {"why": "Why Supabase, and not plain Postgres + S3?",
                                   "options": "Hosting options compared (F-11)"}[p["kind"]]
        contents.append(f"<li><span>{esc(title)}</span><b>{i}</b></li>")
    read = "".join(
        f"<div class='read-item'><div><b>{esc(name)}</b><span class='pg'>p. {page_range(lambda p, k=kind: p.get('uml') == k)}</span></div>"
        f"<span>{esc(what)}</span></div>"
        for kind, name, what in UML_KINDS
    )
    return f"""
<section class="page cover">
  <div class="cover-top">
    <div class="kicker">MC Car Riviera · staff app</div>
    <h1 class="title">Planned architecture</h1>
    <p class="lead">UML diagrams of the iOS app, the back end and the database, and the hosting
    options you asked about (F-11). Drawn from the decisions (ADRs) and stories in <code>docs/</code>.</p>
    <p class="meta">{esc(VERSION)} · first version of the diagrams · kept up to date by US-004, US-006, US-050 and US-070</p>
  </div>
  <div class="cover-grid">
    <div>
      <h2>At a glance</h2>
      <table class="glance">{rows}</table>
    </div>
    <div>
      <h2>Contents</h2>
      <ol class="contents">{''.join(contents)}</ol>
    </div>
    <div>
      <h2>How to read the diagrams</h2>
      <div class="read">{read}</div>
      <h2>Colours</h2>
      {legend_html(ACCOUNTS, vertical=True)}
    </div>
  </div>
  {footer(1, total, [])}
</section>"""


def diagram_page(p, page_no, total):
    layout = p["layout"]
    top = header(p["title"], p["subtitle"], page_no)
    legend = legend_html(p["legend"]) if p.get("legend") else ""
    notation = NOTATION if p.get("notation") else ""
    dia = f'<div class="dia">{inline_svg(p["diagrams"][0])}</div>'
    if layout == "side":
        legend_side = legend_html(p["legend"], vertical=True) if p.get("legend") else ""
        body = (
            f'<div class="body side">{dia}'
            f'<aside>{legend_side}<h3>Key points</h3>{notes_html(p["notes"])}{notation}</aside></div>'
        )
    elif layout == "below":
        body = (
            f'<div class="body below">{dia}'
            f'<div class="under">{notes_html(p["notes"], columns=len(p["notes"]))}{notation}{legend}</div></div>'
        )
    elif layout == "portrait":
        body = f'<div class="body below">{dia}<div class="under">{notes_html(p["notes"])}</div></div>'
    else:
        raise ValueError(layout)
    cls = "page portrait" if layout == "portrait" else "page"
    return f'<section class="{cls}">{top}{body}{footer(page_no, total, p["diagrams"], p.get("refs", ""))}</section>'


WHY_CARDS = [
    ("Traffic isn't what costs money",
     "Two staff members and a few dozen requests per handover are nothing for any of these options. What costs money is storing the files, and the security layer someone has to build and run."),
    ("The phone can't talk to Postgres directly",
     "It would need a database password on two personal phones, and Postgres open to the internet. Something must sit in between: sign staff in, check every request against the access rules, and hand out short-lived links to private files. Supabase is that layer, built and run for you."),
    ("Plain Postgres isn't cheaper here",
     "The smallest managed Postgres costs about €11.40 a month (Scaleway), plus a small server for your own API (about €5.50). Supabase Free costs €0 for the database, the logins and the API."),
    ("You're right about S3",
     "For files, an EU S3-compatible bucket costs about €0.016 per GB a month. Supabase Free stops at 1 GB of files, about 200 rentals; after that, Pro costs $25 a month. Moving only the files to S3 (option B) removes that step for years."),
]


def why_page(p, page_no, total):
    top = header("Why Supabase, and not plain Postgres + S3?",
                 "Your question of 9 October · the short answer, then the four options side by side", page_no)
    cards = "".join(f'<div class="card"><h3>{esc(t)}</h3><p>{esc(b)}</p></div>' for t, b in WHY_CARDS)
    body = (
        f'<div class="body why"><div class="cards">{cards}</div>'
        f'<div class="dia">{inline_svg(p["diagrams"][0])}</div>'
        f'<div class="under">{legend_html(OPTION_COLOURS)}</div></div>'
    )
    return f'<section class="page">{top}{body}{footer(page_no, total, p["diagrams"], "F-11 · ADR-0004 · ADR-0014")}</section>'


OPTION_HEADS = [
    ("A · Supabase for everything", "current plan (default)"),
    ("B · Supabase + S3 for the files", "recommended"),
    ("C · Managed Postgres + S3 + own API", "more to build"),
    ("D · Everything on one server", "cheapest, most to run"),
]
OPTION_ROWS = [
    ("What runs where",
     ["Logins, database, API and files on Supabase (EU)",
      "Logins, database and API on Supabase Free; files in an EU S3-compatible bucket (e.g. Scaleway, Paris)",
      "Managed Postgres, a small server for your own API, and an S3 bucket",
      "One small server (e.g. Hetzner CX23, €5.49) with Postgres and an API, or self-hosted Supabase; files in S3"]),
    ("Per month, under 1 GB of files", ["€0", "€0 + cents", "≈ €17", "≈ €6–8"]),
    ("Per month after ≈ 200 rentals", ["$25 (Pro)", "Cents: the text data stays under 500 MB for years", "≈ €17", "≈ €6–8"]),
    ("Extra work for you",
     ["None", "1–2 days: one function for file links, and the bucket set-up",
      "Weeks: logins, sessions, permissions, the API itself, TLS, monitoring",
      "Days to set up, then updates, security, backups and monitoring of a server holding ID documents"]),
    ("Who patches and watches it", ["Supabase", "Supabase and the bucket provider", "The provider for the database; you for the API server", "You"]),
    ("Limits to know", ["Free plan: no service guarantee; pauses after a week without activity", "Free-plan limits for the database, as in A", "None of the free-plan limits", "Your one server is a single point of failure"]),
]


def options_page(p, page_no, total):
    top = header("Hosting options compared (F-11)",
                 "Approximate list prices before VAT, checked on 9 October 2026 · every option stays portable (Postgres dump, S3-compatible files)", page_no)
    thead = "<tr><th></th>" + "".join(
        f'<th class="{"rec" if i == 1 else ""}">{esc(h)}<small>{esc(s)}</small></th>'
        for i, (h, s) in enumerate(OPTION_HEADS)) + "</tr>"
    rows = ""
    for label, cells in OPTION_ROWS:
        rows += f"<tr><th>{esc(label)}</th>" + "".join(
            f'<td class="{"rec" if i == 1 else ""}">{esc(c)}</td>' for i, c in enumerate(cells)) + "</tr>"
    reco = f"""
<div class="reco">
  <div class="decide">
    <h3>Recommendation: B</h3>
    <p>Keep Supabase Free for the logins, the database and the API; put the files in an EU
    S3-compatible bucket. The database rules, the audit trail and the app stay as planned,
    apart from how files are uploaded and opened.</p>
    <p class="ask">Your decision: reply <b>{esc("F-11")}: A, B, C or D</b>. Until then the plan stays A
    ({esc("ADR-0004")}, {esc("ADR-0014")}).</p>
  </div>
  <div>
    <h3>What B adds</h3>
    <ul>
      <li>One Edge Function (the Free plan includes 500,000 calls a month) that checks the staff session and returns links valid for at most 5 minutes, only for new file names chosen by the server.</li>
      <li>Versioning or object lock on the bucket, if the provider offers it, so a file can't be overwritten.</li>
      <li>The nightly backup copies the files from the bucket instead of Supabase Storage.</li>
    </ul>
  </div>
  <div>
    <h3>Caveats</h3>
    <ul>
      <li>Still the Free plan for the database: no service guarantee, and a pause after a week without activity. Daily use and the nightly backup should prevent it.</li>
      <li>The bucket provider becomes one more sub-processor in your data processing agreement with the company ({esc("L-03")}).</li>
    </ul>
  </div>
</div>"""
    sources = ('<p class="sources">Prices: Supabase pricing page (Free and Pro plans) · Scaleway price lists for Object Storage '
               '(€0.01606 per GB a month, Paris, multi-AZ) and Managed Databases (DB-DEV-S, €0.0156 an hour) · '
               'Hetzner\'s cloud price change of 15 June 2026 (CX23 from €3.99 to €5.49 a month). Check them again before committing.</p>')
    body = f'<div class="body opts"><table class="options"><thead>{thead}</thead><tbody>{rows}</tbody></table>{reco}{sources}</div>'
    return f'<section class="page">{top}{body}{footer(page_no, total, [], "F-11 · ADR-0004 · ADR-0014 · ADR-0015 · L-03")}</section>'


CSS = """
@page { size: A4 landscape; margin: 0; }
@page portrait { size: A4 portrait; margin: 0; }
:root {
  --ink: #1D2433; --slate: #4A5363; --grey: #9AA3B2; --line: #D9DDE4; --light: #F5F6F8;
  --gold: #A97E22; --gold-bg: #F6EFDC; --blue: #5A6B86; --blue-bg: #EDF1F7;
  --red: #B5523B; --red-bg: #FBE9E7;
}
* { box-sizing: border-box; }
html, body { margin: 0; padding: 0; background: #FFFFFF; }
body { font-family: Inter, sans-serif; color: var(--ink); font-size: 8.8pt; line-height: 1.38;
       -webkit-print-color-adjust: exact; print-color-adjust: exact; }
.nw { white-space: nowrap; }
.page { width: 297mm; height: 210mm; padding: 9mm 12mm 6mm; display: flex; flex-direction: column;
        break-after: page; overflow: hidden; position: relative; }
.page.portrait { page: portrait; width: 210mm; height: 297mm; padding: 10mm 11mm 6mm; }
header { flex: none; margin-bottom: 3.5mm; padding-bottom: 2.6mm; border-bottom: 0.3mm solid var(--gold); }
.kicker { font-size: 6.8pt; letter-spacing: 0.12em; text-transform: uppercase; color: var(--gold); font-weight: 600; }
h1 { font-size: 16pt; line-height: 1.15; margin: 1mm 0 0.6mm; font-weight: 650; letter-spacing: -0.01em; }
h1 .num { display: inline-block; min-width: 9mm; color: var(--gold); font-weight: 600; }
.sub { margin: 0; color: var(--slate); font-size: 8.8pt; }
h2 { font-size: 10.5pt; margin: 0 0 2mm; font-weight: 650; }
h3 { font-size: 8.8pt; margin: 0 0 1.2mm; font-weight: 650; }
.body { flex: 1; min-height: 0; display: flex; gap: 6mm; }
.dia { position: relative; flex: 1; min-height: 0; min-width: 0; }
.dia svg { position: absolute; inset: 0; width: 100%; height: 100%; }
.body.side aside { flex: none; width: 62mm; border-left: 0.25mm solid var(--line); padding-left: 5mm;
                   display: flex; flex-direction: column; gap: 2.2mm; }
.body.side aside h3 { margin-top: 1.5mm; }
.body.below { flex-direction: column; gap: 3mm; }
.under { flex: none; display: flex; flex-direction: column; gap: 2.2mm; border-top: 0.25mm solid var(--line); padding-top: 2.6mm; }
.notes { margin: 0; padding: 0; list-style: none; }
.notes li { position: relative; padding-left: 3.6mm; margin: 0 0 1.5mm; }
.notes li::before { content: ""; position: absolute; left: 0; top: 1.5mm; width: 1.5mm; height: 1.5mm;
                    border-radius: 50%; background: var(--gold); }
.notes.cols { display: grid; column-gap: 7mm; }
.notes.cols li { margin: 0; }
.legend { display: flex; flex-wrap: wrap; gap: 1.6mm 4.5mm; font-size: 7.5pt; color: var(--slate); }
.legend.vertical { flex-direction: column; gap: 1.4mm; }
.chip { display: inline-flex; align-items: center; gap: 1.8mm; white-space: nowrap; }
.sw { display: inline-block; width: 6mm; height: 3.4mm; border-radius: 1mm; flex: none; }
.sw.company { background: var(--gold-bg); border: 0.45mm solid var(--gold); }
.sw.developer { background: var(--blue-bg); border: 0.3mm solid var(--blue); }
.sw.device { background: #FFF; border: 0.45mm solid var(--ink); }
.sw.option { background: #FFF; border: 0.3mm dashed var(--grey); }
.sw.you { background: var(--red-bg); border: 0.45mm solid var(--red); }
.sw.plain { background: #FFF; border: 0.3mm solid var(--slate); }
.notation { display: flex; flex-wrap: wrap; gap: 1.2mm 4.5mm; font-size: 7.5pt; color: var(--slate); }
aside .notation { flex-direction: column; gap: 1mm; margin-top: auto; }
.notation b { color: var(--ink); font-weight: 600; }
.glyph { font-style: normal; font-weight: 600; color: var(--ink); margin-right: 1.5mm; }
footer { flex: none; margin-top: 2.6mm; padding-top: 1.8mm; border-top: 0.25mm solid var(--line);
         font-size: 6.8pt; color: var(--slate); display: flex; flex-direction: column; gap: 0.6mm; }
footer .row { display: flex; justify-content: space-between; gap: 6mm; }
footer .row.small { font-size: 6.4pt; color: var(--grey); }
footer .refs { color: var(--blue); }
footer .pg { font-weight: 600; color: var(--ink); }
code { font-family: "DejaVu Sans Mono", monospace; font-size: 0.9em; background: var(--light); padding: 0 0.8mm; border-radius: 0.6mm; }

/* cover */
.cover { padding: 13mm 14mm 6mm; }
.cover-top { flex: none; border-bottom: 0.4mm solid var(--gold); padding-bottom: 4.5mm; margin-bottom: 6mm; }
.cover .title { font-size: 28pt; margin: 2mm 0 2mm; font-weight: 700; letter-spacing: -0.02em; }
.lead { font-size: 11pt; margin: 0 0 2mm; max-width: 215mm; color: var(--ink); }
.meta { margin: 0; color: var(--slate); font-size: 8.4pt; }
.cover-grid { flex: 1; min-height: 0; display: grid; grid-template-columns: 1.5fr 1fr 0.95fr; gap: 9mm; }
.cover-grid > div { display: flex; flex-direction: column; min-width: 0; }
.cover-grid h2 + * { margin-bottom: 5mm; }
table { border-collapse: collapse; width: 100%; }
.glance th { text-align: left; vertical-align: top; width: 24mm; padding: 1.6mm 3mm 1.6mm 0; color: var(--gold); font-weight: 650; }
.glance td { padding: 1.6mm 0; }
.glance tr + tr th, .glance tr + tr td { border-top: 0.25mm solid var(--line); }
.contents { margin: 0; padding: 0; list-style: none; }
.contents li { display: flex; justify-content: space-between; align-items: baseline; gap: 3mm; padding: 1mm 0; border-bottom: 0.2mm dotted var(--grey); }
.contents li b { color: var(--gold); font-weight: 650; }
.read { display: flex; flex-direction: column; gap: 1.6mm; }
.read-item > div { display: flex; justify-content: space-between; gap: 2mm; }
.read-item > span { color: var(--slate); display: block; }
.read-item .pg { color: var(--gold); white-space: nowrap; }

/* why page */
.body.why { flex-direction: column; gap: 3.5mm; }
.cards { flex: none; display: grid; grid-template-columns: repeat(4, 1fr); gap: 4mm; }
.card { background: var(--light); border-radius: 2mm; padding: 3mm 3.5mm; border-top: 0.6mm solid var(--gold); }
.card p { margin: 0; }
.body.why .dia { flex: none; }
.body.why .dia svg { position: static; display: block; height: auto; }

/* options page */
.body.opts { flex-direction: column; gap: 4mm; }
.options { flex: none; table-layout: fixed; font-size: 8.2pt; }
.options th, .options td { border: 0.25mm solid var(--line); padding: 1.3mm 2.2mm; vertical-align: top; text-align: left; }
.options thead th { background: var(--light); font-weight: 650; font-size: 8.6pt; }
.options thead th small { display: block; font-weight: 500; color: var(--slate); font-size: 7.4pt; }
.options tbody th { width: 34mm; font-weight: 600; color: var(--slate); background: #FFF; }
.options .rec { background: var(--blue-bg); }
.options thead th.rec { background: #DDE5F0; box-shadow: inset 0 0.8mm 0 var(--blue); }
.reco { flex: none; display: grid; grid-template-columns: 1.15fr 1.1fr 1fr; gap: 5mm; }
.reco > div { background: var(--light); border-radius: 2mm; padding: 2.8mm 3.4mm; }
.reco .decide { background: var(--gold-bg); border: 0.35mm solid var(--gold); }
.reco p { margin: 0 0 1.5mm; }
.reco p.ask { margin: 0; }
.reco ul { margin: 0; padding-left: 4mm; }
.reco li { margin-bottom: 1mm; }
.sources { flex: none; margin: 0; font-size: 7pt; color: var(--slate); }
"""


def build_html():
    total = len(PAGES)
    parts = []
    for i, p in enumerate(PAGES, start=1):
        kind = p.get("kind", "diagram")
        if kind == "cover":
            parts.append(cover_page(total))
        elif kind == "why":
            parts.append(why_page(p, i, total))
        elif kind == "options":
            parts.append(options_page(p, i, total))
        else:
            parts.append(diagram_page(p, i, total))
    return (
        '<!doctype html><html lang="en"><head><meta charset="utf-8">'
        f"<title>{html.escape(DOC)}</title><style>{CSS}</style></head><body>"
        + "".join(parts)
        + "</body></html>"
    )


def print_pdf(html_text):
    from playwright.sync_api import sync_playwright

    with tempfile.TemporaryDirectory() as tmp:
        page_file = pathlib.Path(tmp) / "architecture.html"
        page_file.write_text(html_text, encoding="utf-8")
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto(page_file.as_uri())
            page.evaluate("document.fonts.ready")
            page.pdf(path=str(OUT), prefer_css_page_size=True, print_background=True)
            browser.close()


def main():
    if "--no-render" not in sys.argv:
        render_svgs()
    html_text = build_html()
    if "--html" in sys.argv:
        (HERE / "architecture.html").write_text(html_text, encoding="utf-8")
    print_pdf(html_text)
    print(f"Wrote {OUT} ({len(PAGES)} pages)")


if __name__ == "__main__":
    main()
