from build import AUTHOR_NAME, BASE, SITE

EVENTBRITE = "https://www.eventbrite.ca/e/2004284399593"
MAVEN = "https://maven.com/hicham-zein-eddine/anchor-bolts-workshop"
PRIVATE = "https://canadacorp.gumroad.com/l/anchor-bolt-workshop"
EMAIL = "canada.servcorp@gmail.com"
WS_NAME = "Anchor Bolts & Steel-Structure Foundations: Get It Right Before the Pour"
PERSON_REF = {"@type": "Person", "name": AUTHOR_NAME, "url": f"{SITE}/about/"}

TOPICS = [
    ("Reading the anchor-bolt plan", "Check the issued-for-construction drawings, bolt schedule and base-plate details before anything is set out."),
    ("Setting out, alignment and levelling", "Survey control, offset pegs, template centring, diagonals, projection and top-of-bolt level."),
    ("Casting conditions and 9 pre-pour hold points", "What must be signed off before the pump arrives, and how to pour without moving the bolts."),
    ("Deviations, corrections and alternatives", "What to do when bolts are out of tolerance, and which fixes must go back to the structural engineer."),
    ("Protection until erection", "Thread protection, capping, marking and keeping equipment away from cast-in bolts."),
    ("Torch-cutting measures and practices", "Cutting projection, enlarging holes, heat and galvanising: what is allowed and who approves it."),
    ("Washers, plate washers and spring washers", "Which washer goes where, and why only the drawings decide."),
    ("Base plates, grouting and erection readiness", "Levelling nuts or shims, non-shrink grout, and the handover to the erection crew."),
]

FORMATS = [("3-hour workshop", "CAD $900", "One topic block, for a site team or a class"),
           ("Full day", "CAD $1,500", "The full sequence with case studies and exercises"),
           ("3-day program", "CAD $4,500", "Civil site practice, anchor bolts and foundations, steel erection method")]

FAQ = [
    ("Who is this anchor-bolt training for?", "QA/QC inspectors and engineers, site engineers, technicians, foremen and steel erection supervisors, and students in civil construction programs."),
    ("Is the training online or in person?", "Both. Live on Zoom or Teams for any country, or in person in Montréal–Laval and elsewhere in Québec on request."),
    ("Which languages are available?", "English, French and Arabic."),
    ("Is there a certificate?", "Each participant receives the digital field guide and a certificate of attendance. The workshop does not grant accredited credits or PDH."),
    ("Is it a recorded course?", "No. Every session is taught live, with time for your own site questions."),
    ("Does it cover anchor-bolt design?", "No. Design belongs to the structural engineer. The training covers site execution: verification, setting out, installation, protection, inspection and corrections."),
]

TRAINING_BODY = f"""<main><div class="wrap">
<p class="crumbs"><a href="{BASE}/">Home</a> / Training</p>
<h1>Anchor bolt training for QA/QC inspectors, site engineers and erection crews</h1>
<div class="key"><strong>In short:</strong> live, practical training on anchor bolts and steel-structure foundations by {AUTHOR_NAME}, from 20+ years on steel-structure and foundation sites in Qatar, the UAE, Poland and Canada. On Zoom or Teams, or in person in Montréal–Laval. In English, French or Arabic.</div>
<figure><img src="{BASE}/img/workshop.jpg" alt="Anchor bolts and steel-structure foundations workshop" loading="lazy"></figure>
<h2 id="next-workshop">Next public session: December 3, 2026</h2>
<p><strong>{WS_NAME}</strong>. Live on Zoom, 8:00–11:00 Montréal time (13:00 London, 16:00 Doha, 17:00 Dubai). Digital guide and certificate of attendance included (no accredited credit or PDH).</p>
<p><a class="btn" href="{EVENTBRITE}">Book on Eventbrite (CA$129 + tax) &rarr;</a> <a class="btn amz" href="{MAVEN}">Book on Maven (US$200)</a></p>
<h2>What the training covers</h2>
<table><tr><th>Topic</th><th>What you learn</th></tr>
{''.join(f'<tr><td>{t}</td><td>{d}</td></tr>' for t, d in TOPICS)}</table>
<p class="note">Several of these topics, such as capping, torch-cutting practice and washers, go further than the book and are explained in detail during the live session.</p>
<h2>Private sessions for your company, college or university</h2>
<table><tr><th>Format</th><th>Price</th><th>Content</th></tr>
{''.join(f'<tr><td>{f}</td><td>{p}</td><td>{c}</td></tr>' for f, p, c in FORMATS)}</table>
<p><a class="btn" href="{PRIVATE}">Book a private session &rarr;</a> or email <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
<h2>Questions</h2>
<dl class="faq">{''.join(f'<dt>{q}</dt><dd>{a}</dd>' for q, a in FAQ)}</dl>
<h2>Free reading before the session</h2>
<p>Start with the <a href="{BASE}/checklist/">free pre-pour checklist</a>, <a href="{BASE}/articles/anchor-bolt-setting-out-alignment-levelling/">setting out and levelling anchor bolts</a> and <a href="{BASE}/articles/misaligned-anchor-bolts/">fixing misaligned anchor bolts</a>.</p>
</div></main>"""

EVENT_LD = {"@context": "https://schema.org", "@type": "EducationEvent", "name": WS_NAME,
    "description": "3-hour live online workshop on anchor bolts, steel-structure foundations and pre-pour QA/QC, by Hicham Zein Eddine. Ideal for QA/QC engineers and inspectors, site engineers, foremen and erection supervisors.",
    "startDate": "2026-12-03T08:00:00-05:00", "endDate": "2026-12-03T11:00:00-05:00",
    "eventStatus": "https://schema.org/EventScheduled", "eventAttendanceMode": "https://schema.org/OnlineEventAttendanceMode",
    "location": {"@type": "VirtualLocation", "url": MAVEN}, "inLanguage": ["en", "fr", "ar"],
    "image": f"{SITE}/img/workshop.jpg", "performer": PERSON_REF, "organizer": PERSON_REF,
    "offers": [{"@type": "Offer", "name": "Maven seat", "price": "200", "priceCurrency": "USD", "availability": "https://schema.org/InStock", "url": MAVEN, "validFrom": "2026-11-03"},
               {"@type": "Offer", "name": "Eventbrite seat", "price": "129", "priceCurrency": "CAD", "availability": "https://schema.org/InStock", "url": EVENTBRITE, "validFrom": "2026-11-03"}]}

COURSE_LD = {"@context": "https://schema.org", "@type": "Course", "name": "Anchor Bolts and Steel-Structure Foundations: site training",
    "description": "Live training on anchor-bolt plan reading, setting out, alignment, levelling, pre-pour hold points, protection until erection, corrections, washers, base plates and grouting.",
    "url": f"{SITE}/training/", "provider": PERSON_REF, "inLanguage": ["en", "fr", "ar"],
    "teaches": [t for t, _ in TOPICS], "educationalLevel": "Professional",
    "audience": {"@type": "Audience", "audienceType": "QA/QC inspectors, site engineers, foremen, steel erection supervisors, civil construction students"},
    "offers": [{"@type": "Offer", "category": "Paid", "name": f, "price": p.replace("CAD $", "").replace(",", ""), "priceCurrency": "CAD", "url": PRIVATE} for f, p, _ in FORMATS],
    "hasCourseInstance": [{"@type": "CourseInstance", "courseMode": "Online", "startDate": "2026-12-03T08:00:00-05:00",
                           "endDate": "2026-12-03T11:00:00-05:00", "location": {"@type": "VirtualLocation", "url": MAVEN},
                           "instructor": PERSON_REF, "courseWorkload": "PT3H"}]}

FAQ_LD = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
    {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]}

TRAINING_LD = [COURSE_LD, EVENT_LD, FAQ_LD]
