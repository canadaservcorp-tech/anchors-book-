#!/usr/bin/env python3
"""Generate the static Anchor Bolt Field Guide site. Run: python3 tools/build.py"""
import html, json, os, pathlib, shutil

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT
SITE = "https://canadaservcorp-tech.github.io/anchors-book-"
BASE = "/anchors-book-"
GUMROAD = "https://canadacorp.gumroad.com/l/anchor-bolt-guide"
TITLE = "The Steel-Structure Foundation & Anchor Bolt Field Guide"
AUTHOR = "Hicham Zein Eddine, Eng."
AUTHOR_NAME = "Hicham Zein Eddine"
UPDATED = "2026-10-19"
DISCLAIMER = ("This content is provided for professional educational use and does not replace a licensed "
              "structural engineer or the governing code for your jurisdiction. Always verify against the "
              "approved documents for your project.")

def buy(campaign, label="Get the full 62-page guide"):
    return (f'<a class="btn" href="{GUMROAD}?utm_source=guide-site&amp;utm_medium=web&amp;utm_campaign={campaign}">'
            f'{label} &rarr;</a>')

CSS = """
:root{--navy:#0e203a;--navy2:#16304f;--gold:#f0aa3c;--ink:#1c2533;--muted:#5b6678;--bg:#f6f7f9;--line:#dde2ea}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}
body{margin:0;font-family:system-ui,-apple-system,"Segoe UI",Roboto,Arial,sans-serif;color:var(--ink);background:var(--bg);line-height:1.65;font-size:17px}
a{color:#1d4f91}img{max-width:100%;height:auto;display:block}
header.top{background:var(--navy);color:#fff}
.wrap{max-width:860px;margin:0 auto;padding:0 20px}
.top .wrap{display:flex;align-items:center;justify-content:space-between;gap:12px;padding-top:14px;padding-bottom:14px;flex-wrap:wrap}
.brand{color:#fff;text-decoration:none;font-weight:800;letter-spacing:.3px}.brand span{color:var(--gold)}
header nav a{color:#d7e0ee;text-decoration:none;margin-left:16px;font-size:15px}header nav a:hover{color:#fff}
footer nav a{color:var(--muted);margin:0 4px}
.hero{background:linear-gradient(160deg,var(--navy),var(--navy2));color:#fff;padding:44px 0 52px}
.hero .wrap{display:grid;grid-template-columns:1fr 260px;gap:36px;align-items:center}
.hero h1{font-size:34px;line-height:1.2;margin:0 0 14px}.hero p{color:#d7e0ee;margin:0 0 18px}
.kicker{color:var(--gold);font-weight:700;letter-spacing:2px;font-size:13px;text-transform:uppercase}
.btn{display:inline-block;background:var(--gold);color:#13213a;font-weight:800;text-decoration:none;padding:13px 22px;border-radius:8px;margin:6px 0}
.btn:hover{filter:brightness(1.05)}.btn.ghost{background:transparent;color:#fff;border:2px solid #ffffff55}
.price{color:#fff;font-weight:700;margin-left:10px}
main{padding:34px 0 10px}main h1{font-size:30px;line-height:1.25;margin:.2em 0 .5em}
h2{font-size:23px;margin:1.6em 0 .5em;color:var(--navy)}h3{font-size:19px;margin:1.3em 0 .4em}
.card{background:#fff;border:1px solid var(--line);border-radius:12px;padding:22px 24px;margin:18px 0}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:16px}
.grid a.card{display:block;text-decoration:none;color:inherit;margin:0}.grid a.card:hover{border-color:var(--gold)}
.grid h3{margin:0 0 6px;font-size:17px;color:var(--navy)}.grid p{margin:0;color:var(--muted);font-size:15px}
table{border-collapse:collapse;width:100%;background:#fff;font-size:15px;margin:12px 0}
th,td{border:1px solid var(--line);padding:9px 10px;text-align:left;vertical-align:top}th{background:var(--navy);color:#fff}
.note{font-size:14px;color:var(--muted)}
.key{border-left:4px solid var(--gold);background:#fff;padding:14px 18px;border-radius:0 10px 10px 0;margin:18px 0}
.cta{background:var(--navy);color:#fff;border-radius:14px;padding:24px;margin:30px 0;display:grid;grid-template-columns:110px 1fr;gap:20px;align-items:center}
.cta p{margin:.2em 0;color:#d7e0ee}.cta strong{color:#fff}
figure{margin:18px 0}figure img{border:1px solid var(--line);border-radius:8px;background:#fff}figcaption{font-size:14px;color:var(--muted);margin-top:6px}
.pages{display:grid;grid-template-columns:repeat(auto-fill,minmax(170px,1fr));gap:14px}
.crumbs{font-size:14px;color:var(--muted)}.crumbs a{color:var(--muted)}
.faq dt{font-weight:700;margin-top:14px}.faq dd{margin:4px 0 0}
footer{color:var(--muted);font-size:14px;padding:30px 0 40px;border-top:1px solid var(--line);margin-top:30px}
ul.check{list-style:none;padding:0}ul.check li{padding:9px 0 9px 34px;border-bottom:1px solid var(--line);position:relative}
ul.check li:before{content:"";position:absolute;left:2px;top:12px;width:18px;height:18px;border:2px solid var(--navy);border-radius:3px}
@media(max-width:720px){.hero .wrap{grid-template-columns:1fr}.hero .cover{max-width:220px}.hero h1{font-size:27px}.cta{grid-template-columns:1fr}.cta img{max-width:110px}nav a{margin:0 14px 0 0}}
@media print{header.top,.cta,.btn,footer nav,.noprint{display:none!important}body{background:#fff;font-size:13pt}.card{border:0;padding:0}}
"""

def page(path, title, desc, body, jsonld=None, og_type="article", image="img/og.jpg"):
    url = f"{SITE}/{path}"
    ld = ""
    for block in (jsonld or []):
        ld += f'<script type="application/ld+json">{json.dumps(block, ensure_ascii=False)}</script>\n'
    full_title = title if title.endswith("Field Guide") else f"{title} | Anchor Bolt Field Guide"
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(full_title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{url}">
<meta name="author" content="{AUTHOR_NAME}">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta property="og:type" content="{og_type}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/{image}">
<meta property="og:site_name" content="Anchor Bolt Field Guide">
<meta name="twitter:card" content="summary_large_image">
<meta name="referrer" content="strict-origin-when-cross-origin">
<meta name="theme-color" content="#0e203a">
<link rel="icon" href="{BASE}/img/favicon.png">
<style>{CSS}</style>
{ld}</head>
<body>
<header class="top"><div class="wrap">
<a class="brand" href="{BASE}/">Anchor Bolt <span>Field Guide</span></a>
<nav><a href="{BASE}/articles/">Articles</a><a href="{BASE}/checklist/">Free checklist</a><a href="{GUMROAD}?utm_source=guide-site&amp;utm_medium=web&amp;utm_campaign=nav">Get the book</a></nav>
</div></header>
{body}
<footer><div class="wrap">
<p>{DISCLAIMER}</p>
<p>&copy; 2026 {AUTHOR}. Content adapted from <em>{TITLE}</em>.</p>
<nav><a href="{BASE}/">Home</a> &middot; <a href="{BASE}/articles/">Articles</a> &middot; <a href="{BASE}/checklist/">Free pre-pour checklist</a> &middot; <a href="{GUMROAD}">Buy the guide</a></nav>
</div></footer>
</body>
</html>
"""

def cta(campaign):
    return f"""<div class="cta"><img src="{BASE}/img/cover.jpg" alt="Cover of the Anchor Bolt Field Guide" width="110" loading="lazy">
<div><p><strong>{TITLE}</strong></p>
<p>62 pages, the full site sequence from drawing to grouted base plate: survey, excavation, blinding, rebar, the anchor-bolt template, QA/QC hold points and field fixes. Written by a civil engineer with 20+ years on sites in Lebanon, Qatar, the UAE, Poland and Canada.</p>
{buy(campaign)}</div></div>"""

AUTHOR_LD = {"@type": "Person", "name": AUTHOR_NAME, "honorificSuffix": "Eng.",
             "description": "Civil engineer with 20+ years of international project experience (Lebanon, Qatar, UAE, Poland, Canada)."}

def article_ld(a):
    return [{
        "@context": "https://schema.org", "@type": "Article", "headline": a["title"], "description": a["desc"],
        "author": AUTHOR_LD, "datePublished": UPDATED, "dateModified": UPDATED,
        "image": f"{SITE}/img/{a.get('img','og')}.jpg", "mainEntityOfPage": f"{SITE}/articles/{a['slug']}/",
        "isPartOf": {"@type": "WebSite", "name": "Anchor Bolt Field Guide", "url": f"{SITE}/"},
        "citation": {"@type": "Book", "name": TITLE, "url": GUMROAD}},
        {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": ans}} for q, ans in a["faq"]]},
        {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE}/"},
            {"@type": "ListItem", "position": 2, "name": "Articles", "item": f"{SITE}/articles/"},
            {"@type": "ListItem", "position": 3, "name": a["title"], "item": f"{SITE}/articles/{a['slug']}/"}]}]

def fig(img, cap):
    return f'<figure><img src="{BASE}/img/{img}.jpg" alt="{html.escape(cap)}" loading="lazy"><figcaption>{cap}</figcaption></figure>'


def write(rel, text):
    p = OUT / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8")

def build():
    from articles import ARTICLES
    for a in ARTICLES:
        faq = "".join(f"<dt>{html.escape(q)}</dt><dd>{html.escape(ans)}</dd>" for q, ans in a["faq"])
        body = f"""<main><div class="wrap">
<p class="crumbs"><a href="{BASE}/">Home</a> / <a href="{BASE}/articles/">Articles</a></p>
<h1>{html.escape(a['title'])}</h1>
<p class="note">By {AUTHOR} &middot; From Chapter {a['chapter']} of the Anchor Bolt Field Guide</p>
<div class="key"><strong>Short answer:</strong> {a['answer']}</div>
{a['body']}
<h2>Questions engineers ask</h2>
<dl class="faq">{faq}</dl>
{cta(a['slug'])}
<h2>Keep reading</h2>
<div class="grid">{''.join(f'<a class="card" href="{BASE}/articles/{o["slug"]}/"><h3>{html.escape(o["title"])}</h3><p>{html.escape(o["desc"][:110])}…</p></a>' for o in [x for x in ARTICLES if x['slug'] in a['related']])}</div>
</div></main>"""
        write(f"articles/{a['slug']}/index.html", page(f"articles/{a['slug']}/", a["title"], a["desc"], body, article_ld(a)))

    cards = "".join(f'<a class="card" href="{BASE}/articles/{a["slug"]}/"><h3>{html.escape(a["title"])}</h3><p>{html.escape(a["desc"][:120])}…</p></a>' for a in ARTICLES)
    write("articles/index.html", page("articles/", "Anchor bolt and foundation articles for site engineers",
          "Free, practical articles on anchor bolts, templates, tolerances, grouting and pre-pour QA/QC for steel-structure foundations.",
          f'<main><div class="wrap"><h1>Articles for site engineers and engineering students</h1><p>Practical answers taken from the field guide. Each one is short, sourced from the book, and ends with what to check on site.</p><div class="grid">{cards}</div>{cta("articles")}</div></main>',
          og_type="website"))

    from checklist import CHECKLIST_BODY, CHECKLIST_LD
    write("checklist/index.html", page("checklist/", "Free pre-pour checklist for anchor bolts and foundations",
          "Free printable pre-concrete cast-in checklist (final gate) for steel-structure foundations: drawings, survey, formwork, rebar, anchor bolts, template, cleanliness, threads, access, lighting, vibrator and sign-off.",
          CHECKLIST_BODY, CHECKLIST_LD))

    from home import HOME_BODY, HOME_LD
    write("index.html", page("", TITLE, "A 62-page field guide for site engineers and engineering students: set anchor bolts right the first time, from drawing to grouted base plate. Template method, tolerances, QA/QC hold points, troubleshooting.",
          HOME_BODY, HOME_LD, og_type="book"))

    write("404.html", page("404.html", "Page not found", "This page does not exist.",
          f'<main><div class="wrap"><h1>Page not found</h1><p><a href="{BASE}/">Go to the home page</a> or read the <a href="{BASE}/articles/">articles</a>.</p></div></main>').replace('content="index,follow,max-image-preview:large"', 'content="noindex"'))

    urls = ["", "articles/", "checklist/"] + [f"articles/{a['slug']}/" for a in ARTICLES]
    write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
          "".join(f"  <url><loc>{SITE}/{u}</loc><lastmod>{UPDATED}</lastmod></url>\n" for u in urls) + "</urlset>\n")
    bots = ["GPTBot", "OAI-SearchBot", "ChatGPT-User", "ClaudeBot", "Claude-SearchBot", "Claude-User", "PerplexityBot",
            "Perplexity-User", "Google-Extended", "Applebot-Extended", "Bingbot", "DuckAssistBot", "Meta-ExternalAgent", "CCBot"]
    # GitHub Pages serves robots.txt only at the user-site root, so this file documents intent; the meta robots tag governs.
    write("robots.txt", "".join(f"User-agent: {b}\nAllow: /\n\n" for b in bots) + f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
    llms = [f"# {TITLE}", "", f"> A 62-page field guide by {AUTHOR} (20+ years on sites in Lebanon, Qatar, the UAE, Poland and Canada) "
            "on setting anchor bolts for steel structures right the first time, from drawing review to grouted base plate. "
            f"Price: CAD$30 on Gumroad: {GUMROAD}", "",
            "Applies to pre-engineered buildings (PEB), hot-rolled steel frames, warehouses, transmission towers and poles, telecom masts and monopoles, car-park shades and canopies.",
            "", "## Free articles", ""] + [f"- [{a['title']}]({SITE}/articles/{a['slug']}/): {a['desc']}" for a in ARTICLES] + [
            "", "## Free resources", "", f"- [Pre-pour checklist (final gate)]({SITE}/checklist/): printable, no sign-up.",
            "", "## Book contents", "", "15 chapters: drawings, setting out, safe access, excavation, trench bottom, anti-termite treatment, polyethylene sheet, blinding, footing formwork, rebar, anchor bolts, base plate and grouting, post-installed anchors, QA/QC, troubleshooting; appendices on anchor-bolt specifications, concrete testing, inspection checklist and unit conversions.",
            "", "## Note", "", DISCLAIMER, ""]
    write("llms.txt", "\n".join(llms))
    write(".nojekyll", "")

if __name__ == "__main__":
    import sys
    sys.path.insert(0, str(ROOT / "tools"))
    build()
    print("built")
