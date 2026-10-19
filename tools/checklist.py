from build import BASE, GUMROAD, SITE, TITLE

ITEMS = [
("Drawings", "Latest IFC revisions in use"),
("Survey", "Bolts checked for alignment and position"),
("Formwork", "Secure, braced, and at the correct top elevation"),
("Rebar", "Size, spacing, and cover confirmed with spacers"),
("Anchors", "Grade and diameter verified against spec"),
("Template", "Locked nuts tight, assembly welded to the rebar"),
("Cleanliness", "Debris blown out and washed down"),
("Threads", "Masking tape applied"),
("Access", "Safe walkway with handrail for the pump crew"),
("Lighting", "Adequate for the planned pour time"),
("Vibrator", "Fuelled and tested"),
("Inspector sign-off", "Written approval received"),
]

rows = "".join(f"<li><strong>{a}:</strong> {b}</li>" for a, b in ITEMS)
CHECKLIST_BODY = f"""<main><div class="wrap">
<p class="crumbs noprint"><a href="{BASE}/">Home</a> / Free checklist</p>
<h1>Pre-concrete cast-in inspection checklist (final gate)</h1>
<p>Copy this checklist for daily site use. Nothing is poured until every line is confirmed and the inspector has signed. Free, no sign-up.</p>
<p class="noprint"><a class="btn" href="javascript:window.print()" style="color:#13213a">Print or save as PDF</a></p>
<div class="card">
<p><strong>Project:</strong> ____________________ &nbsp; <strong>Element / grid:</strong> __________ &nbsp; <strong>Date:</strong> __________</p>
<ul class="check">{rows}</ul>
<p><strong>Inspected by:</strong> ____________________ &nbsp; <strong>Signature:</strong> ____________________</p>
</div>
<p class="note">From Chapter 14 of <em>{TITLE}</em>. The book also covers the ten mandatory hold points, from survey control to 28-day cube results.</p>
<div class="noprint">
<h2>Why each line matters</h2>
<p>Read the <a href="{BASE}/articles/pre-pour-checklist/">pre-pour checklist explained</a>, or the full sequence in the guide: <a href="{GUMROAD}?utm_source=guide-site&amp;utm_medium=web&amp;utm_campaign=checklist">get the 62-page guide</a>.</p>
</div>
</div></main>"""

CHECKLIST_LD = [{"@context": "https://schema.org", "@type": "WebPage", "name": "Pre-concrete cast-in inspection checklist (final gate)",
                 "url": f"{SITE}/checklist/", "isAccessibleForFree": True,
                 "mainEntity": {"@type": "ItemList", "itemListElement": [
                     {"@type": "ListItem", "position": i + 1, "name": f"{a}: {b}"} for i, (a, b) in enumerate(ITEMS)]}}]
