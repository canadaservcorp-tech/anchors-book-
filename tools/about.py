from build import AMAZON, AUTHOR_NAME, BASE, GUMROAD, SITE, TITLE
from training import EVENT_LD

EMAIL = "canada.servcorp@gmail.com"
TOPICS = ["Anchor bolts and anchor-bolt templates", "Steel-structure foundations", "Steel erection method",
          "Base plates and non-shrink grout", "Pre-pour QA/QC hold points", "Civil site practice and supervision"]

ABOUT_BODY = f"""<main><div class="wrap">
<p class="crumbs"><a href="{BASE}/">Home</a> / About the author</p>
<h1>About the author: {AUTHOR_NAME}</h1>
<div class="card">
<p><strong>{AUTHOR_NAME}</strong> has worked more than 20 years on steel-structure and foundation sites in Qatar, the UAE, Poland and Canada. He is based in Laval, Québec.</p>
<p>His work covers the full site sequence for steel structures: setting out, excavation, blinding, formwork and rebar, anchor-bolt templates, pre-pour inspection, base plates, grouting and steel erection. He wrote <em>{TITLE}</em> (2026) to pass on the checks that prevent misplaced anchor bolts, rework and erection delays.</p>
</div>
<h2>Topics</h2>
<ul>{''.join(f'<li>{t}</li>' for t in TOPICS)}</ul>
<h2>The book</h2>
<p><em>{TITLE}</em>: 62 pages, from drawing review to the grouted base plate. For site supervisors, foremen, technicians, inspectors and engineering students.</p>
<p><a class="btn" href="{GUMROAD}?utm_source=guide-site&amp;utm_medium=web&amp;utm_campaign=about">Get the guide (CAD $30) &rarr;</a> <a class="btn amz" href="{AMAZON}" rel="noopener">Kindle edition on Amazon</a></p>
<h2>Training and talks</h2>
<p>Practical workshops for contractors, training centres, colleges and universities, in person in Montréal–Laval or by Zoom, in English, French or Arabic:</p>
<table><tr><th>Module</th><th>Content</th></tr>
<tr><td>1. Civil site practice</td><td>Setting out, excavation, formwork, rebar, concreting and pre-pour control</td></tr>
<tr><td>2. Anchor bolts and steel-structure foundations</td><td>Templates, AISC 303 / ACI 117 tolerances, QA/QC hold points, base plates and grout</td></tr>
<tr><td>3. Steel erection method</td><td>Column plumbness, temporary bracing, lifting, final bolting</td></tr></table>
<p>Formats: 3-hour workshop, full day or 3-day program. Each registered participant receives the digital guide and a certificate of attendance. Free one-hour Zoom session for invited student groups.</p>
<h2 id="next-workshop">Next public workshop: December 3, 2026</h2>
<p><strong>Anchor Bolts &amp; Steel-Structure Foundations: Get It Right Before the Pour</strong>. Live on Zoom, 8:00–11:00 Montréal time (13:00 London, 16:00 Doha, 17:00 Dubai). Ideal for QA/QC engineers and inspectors, site engineers, foremen and erection supervisors. Digital guide and certificate of attendance included (no accredited credit or PDH).</p>
<p><a class="btn" href="https://www.eventbrite.ca/e/2004284399593">Book a seat on Eventbrite (CA$129 + tax) &rarr;</a> <a class="btn amz" href="https://maven.com/hicham-zein-eddine/anchor-bolts-workshop">Book on Maven (US$200)</a></p>
<p>For a private session for your company or school, see the <a href="https://canadacorp.gumroad.com/l/anchor-bolt-workshop">company workshop options</a> (3 hours, full day or 3 days) and the full <a href="{BASE}/training/">training page</a>.</p>
<h2>Contact</h2>
<p>Email <a href="mailto:{EMAIL}">{EMAIL}</a> for training, talks, department licences or questions about the book.</p>
</div></main>"""

PERSON = {"@type": "Person", "@id": f"{SITE}/about/#person", "name": AUTHOR_NAME, "url": f"{SITE}/about/",
          "email": f"mailto:{EMAIL}",
          "description": "20+ years on steel-structure and foundation sites in Qatar, the UAE, Poland and Canada; author of " + TITLE + ".",
          "address": {"@type": "PostalAddress", "addressLocality": "Laval", "addressRegion": "QC", "addressCountry": "CA"},
          "knowsAbout": TOPICS, "knowsLanguage": ["en", "fr", "ar"]}

ABOUT_LD = [{"@context": "https://schema.org", "@type": "ProfilePage", "url": f"{SITE}/about/", "mainEntity": PERSON},
            {"@context": "https://schema.org", "@type": "Book", "name": TITLE, "author": {"@id": f"{SITE}/about/#person"},
             "url": f"{SITE}/", "datePublished": "2026", "numberOfPages": 62, "bookFormat": "https://schema.org/EBook",
             "sameAs": [AMAZON, GUMROAD]}, EVENT_LD]
