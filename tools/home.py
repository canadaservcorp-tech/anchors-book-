from build import AUTHOR, AUTHOR_LD, BASE, GUMROAD, SITE, TITLE, buy
from articles import ARTICLES

pages = [("p-contents", "Contents: 15 chapters and appendices"), ("p-standards", "Reference standards and codes"),
         ("p-template", "The template serves twice"), ("p-qaqc", "QA/QC hold points and checklist"),
         ("p-troubleshooting", "Troubleshooting and field fixes")]
gallery = "".join(f'<figure><img src="{BASE}/img/{i}.jpg" alt="{c}" loading="lazy"><figcaption>{c}</figcaption></figure>' for i, c in pages)
cards = "".join(f'<a class="card" href="{BASE}/articles/{a["slug"]}/"><h3>{a["title"]}</h3><p>{a["desc"][:110]}…</p></a>' for a in ARTICLES[:6])

HOME_BODY = f"""<section class="hero"><div class="wrap">
<div><p class="kicker">Field guide · Site execution · 62 pages</p>
<h1>Set anchor bolts right the first time, from drawing to grouted base plate.</h1>
<p>They taught you how to design a foundation. This guide shows you how to build one: the exact site sequence, the template method, QA/QC hold points and the fixes when something goes wrong.</p>
{buy("home-hero")}<span class="price">CAD$30 · PDF</span><br>
<a class="btn ghost" href="{BASE}/checklist/">Free pre-pour checklist</a></div>
<img class="cover" src="{BASE}/img/cover.jpg" alt="Cover of {TITLE}" width="260"></div></section>
<main><div class="wrap">
<h2>Who it is for</h2>
<p>Site engineers, structural engineers, QA/QC inspectors, and engineering students who want to walk onto a site on day one knowing what to do.</p>
<h2>What is inside</h2>
<ul>
<li><strong>The complete site sequence:</strong> drawings, survey, excavation, blinding, rebar, anchor bolts, base plate, grouting.</li>
<li><strong>The anchor-bolt template method:</strong> fabricate it, set embedment, orient L/J-bolts, hold the pattern rigid through the pour.</li>
<li><strong>QA/QC:</strong> ten mandatory hold points and a pre-pour final-gate checklist.</li>
<li><strong>Troubleshooting:</strong> misaligned bolts, damaged threads, low concrete strength, grout voids.</li>
<li><strong>Standards behind every step:</strong> ACI, AISC, BS EN, ASTM, ISO.</li>
<li><strong>Site politics:</strong> how to lead experienced crews and protect your word.</li>
</ul>
<p>Works for every metal structure: PEB, hot-rolled frames, warehouses, transmission towers and poles, monopoles, car-park shades and canopies.</p>
<h2>Look inside</h2>
<div class="pages">{gallery}</div>
<h2>About the author</h2>
<p>{AUTHOR} is a civil engineer with more than 20 years of international project experience in Lebanon, Qatar, the UAE, Poland and Canada.</p>
<h2>Free articles</h2>
<div class="grid">{cards}</div>
<p><a href="{BASE}/articles/">All articles &rarr;</a></p>
<div style="text-align:center;margin:30px 0">{buy("home-bottom")}</div>
</div></main>"""

HOME_LD = [{"@context": "https://schema.org", "@type": "Book", "name": TITLE, "author": AUTHOR_LD,
            "bookFormat": "https://schema.org/EBook", "numberOfPages": 62, "inLanguage": "en", "datePublished": "2026",
            "bookEdition": "First Edition", "image": f"{SITE}/img/cover.jpg", "url": f"{SITE}/",
            "about": ["Anchor bolts", "Steel structure foundations", "Base plate grouting", "Construction QA/QC"],
            "audience": {"@type": "Audience", "audienceType": "Site engineers, structural engineers, QA/QC inspectors, engineering students"},
            "offers": {"@type": "Offer", "price": "30.00", "priceCurrency": "CAD", "availability": "https://schema.org/InStock", "url": GUMROAD}},
           {"@context": "https://schema.org", "@type": "WebSite", "name": "Anchor Bolt Field Guide", "url": f"{SITE}/"}]
