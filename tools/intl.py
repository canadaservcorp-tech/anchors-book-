from build import AMAZON, AUTHOR_NAME, BASE, GUMROAD, SITE, TITLE
from training import EVENTBRITE, MAVEN, PRIVATE, EMAIL, EVENT_LD

def nav(items):
    return "".join(f'<a href="{h}">{t}</a>' for t, h in items)

FR_BODY = f"""<section class="hero"><div class="wrap">
<div><p class="kicker">Guide de terrain · Formation · Québec et en ligne</p>
<h1>Boulons d'ancrage et fondations de charpente d'acier : réussir avant le bétonnage</h1>
<p>Un guide de terrain de 62 pages et une formation en direct par {AUTHOR_NAME}, avec plus de 20 ans sur des chantiers de structures d'acier et de fondations au Qatar, aux Émirats arabes unis, en Pologne et au Canada. Basé à Laval.</p>
<a class="btn" href="{BASE}/training/">Voir la formation &rarr;</a> <a class="btn amz" href="{GUMROAD}?utm_source=guide-site&amp;utm_medium=web&amp;utm_campaign=fr">Le guide (en anglais, 30 $ CA)</a></div>
<img class="cover" src="{BASE}/img/cover.jpg" alt="Couverture du guide de terrain sur les boulons d'ancrage" width="260"></div></section>
<main><div class="wrap">
<h2>Pour qui ?</h2>
<p>Inspecteurs et techniciens en contrôle de la qualité (AQ/CQ), chargés de projet, surveillants de chantier, contremaîtres, monteurs de charpente d'acier, ainsi que les élèves et étudiants en génie civil, en construction et en montage de structures.</p>
<h2>Ce que couvre la formation</h2>
<ul>
<li>Lecture du plan des boulons d'ancrage et vérification des dessins émis pour construction.</li>
<li>Implantation, alignement et mise à niveau des boulons, gabarit (template) et projection.</li>
<li>Conditions de bétonnage et 9 points d'arrêt avant la coulée.</li>
<li>Écarts, corrections et solutions de rechange quand les boulons ne concordent pas.</li>
<li>Protection des filets et capuchons jusqu'au montage.</li>
<li>Pratiques de coupage au chalumeau, rondelles, rondelles de plaque et rondelles ressorts.</li>
<li>Plaques d'assise, cales ou écrous de mise à niveau, coulis sans retrait.</li>
</ul>
<p class="note">La formation porte sur l'exécution au chantier, pas sur la conception : le dimensionnement relève de l'ingénieur en structure.</p>
<h2>Formats et prix</h2>
<table><tr><th>Format</th><th>Prix</th></tr>
<tr><td>Atelier de 3 heures</td><td>900 $ CA</td></tr><tr><td>Journée complète</td><td>1 500 $ CA</td></tr><tr><td>Programme de 3 jours</td><td>4 500 $ CA</td></tr></table>
<p>En français, en anglais ou en arabe. En personne à Montréal–Laval (ailleurs au Québec sur demande) ou par Zoom/Teams. Chaque participant reçoit le guide numérique et une attestation de participation (aucun crédit accrédité).</p>
<p><a class="btn" href="{PRIVATE}">Réserver une session privée &rarr;</a> ou écrire à <a href="mailto:{EMAIL}">{EMAIL}</a></p>
<h2>Prochaine session publique : 3 décembre 2026</h2>
<p>En direct sur Zoom, de 8 h à 11 h (heure de Montréal), en anglais. <a href="{EVENTBRITE}">Eventbrite (129 $ CA + taxes)</a> · <a href="{MAVEN}">Maven (200 $ US)</a></p>
<h2>Lectures gratuites (en anglais)</h2>
<ul><li><a href="{BASE}/checklist/">Liste de vérification avant bétonnage</a></li>
<li><a href="{BASE}/articles/anchor-bolt-tolerances/">Tolérances d'implantation des boulons d'ancrage</a></li>
<li><a href="{BASE}/articles/misaligned-anchor-bolts/">Boulons d'ancrage mal alignés : les bonnes corrections</a></li>
<li><a href="{BASE}/articles/anchor-bolt-template/">Fabriquer et utiliser un gabarit de boulons d'ancrage</a></li></ul>
<h2>Questions fréquentes</h2>
<dl class="faq"><dt>Le guide existe-t-il en français ?</dt><dd>Le guide est en anglais. La formation est offerte en français, en anglais ou en arabe.</dd>
<dt>La formation est-elle enregistrée ?</dt><dd>Non. Chaque session est donnée en direct, avec du temps pour vos questions de chantier.</dd>
<dt>Peut-on l'offrir dans un cégep, un CFP ou une université ?</dt><dd>Oui : conférence pour les étudiants, perfectionnement pour les enseignants ou module de formation continue.</dd></dl>
</div></main>"""

AR_BODY = f"""<section class="hero"><div class="wrap">
<div><p class="kicker">دليل ميداني · تدريب مباشر · عبر الإنترنت</p>
<h1>براغي التثبيت وأساسات المنشآت الفولاذية: نفّذها صحيحة قبل صبّ الخرسانة</h1>
<p>دليل ميداني من 62 صفحة وتدريب مباشر يقدّمه هشام زين الدين ({AUTHOR_NAME})، بخبرة تزيد على 20 عامًا في مواقع المنشآت الفولاذية والأساسات في قطر والإمارات وبولندا وكندا.</p>
<a class="btn" href="{BASE}/training/">تفاصيل التدريب &larr;</a> <a class="btn amz" href="{GUMROAD}?utm_source=guide-site&amp;utm_medium=web&amp;utm_campaign=ar">الدليل (بالإنجليزية)</a></div>
<img class="cover" src="{BASE}/img/cover.jpg" alt="غلاف الدليل الميداني لبراغي التثبيت" width="260"></div></section>
<main><div class="wrap">
<h2>لمن هذا التدريب؟</h2>
<p>مهندسو ومفتشو ضبط الجودة (QA/QC)، مهندسو الموقع، المراقبون ورؤساء العمال، مشرفو تركيب الهياكل الفولاذية، وطلاب الهندسة المدنية والبناء.</p>
<h2>محاور التدريب</h2>
<ul>
<li>قراءة مخطط براغي التثبيت ومراجعة المخططات المعتمدة للتنفيذ.</li>
<li>التوقيع المساحي، الاستقامة، ضبط المنسوب، القالب (Template) وطول البروز.</li>
<li>شروط الصبّ و9 نقاط توقف للفحص قبل الصبّ.</li>
<li>الانحرافات والتصحيحات والبدائل عند الخطأ.</li>
<li>حماية الأسنان وتغطية البراغي حتى التركيب.</li>
<li>ممارسات القطع بالشعلة، الوردات، وردات الصفائح والوردات النابضية.</li>
<li>صفائح القاعدة، صواميل أو رقائق التسوية، والجراوت غير الانكماشي.</li>
</ul>
<p class="note">التدريب يخص التنفيذ في الموقع وليس التصميم؛ التصميم من مسؤولية المهندس الإنشائي.</p>
<h2>الصيغ والأسعار</h2>
<table><tr><th>الصيغة</th><th>السعر</th></tr>
<tr><td>ورشة 3 ساعات</td><td>900 دولار كندي</td></tr><tr><td>يوم كامل</td><td>1,500 دولار كندي</td></tr><tr><td>برنامج 3 أيام</td><td>4,500 دولار كندي</td></tr></table>
<p>بالعربية أو الإنجليزية أو الفرنسية، مباشرة عبر Zoom أو Teams لأي بلد، أو حضوريًا في مونتريال–لافال. يحصل كل مشارك على الدليل الرقمي وشهادة حضور (دون ساعات معتمدة).</p>
<p><a class="btn" href="{PRIVATE}">احجز جلسة خاصة &larr;</a> أو راسلنا: <a href="mailto:{EMAIL}">{EMAIL}</a></p>
<h2>الجلسة العامة القادمة: 3 ديسمبر 2026</h2>
<p>مباشرة على Zoom، من 8:00 إلى 11:00 بتوقيت مونتريال (16:00 الدوحة، 17:00 دبي)، بالإنجليزية. <a href="{EVENTBRITE}">Eventbrite</a> · <a href="{MAVEN}">Maven</a></p>
<h2>أسئلة شائعة</h2>
<dl class="faq"><dt>هل الدليل متوفر بالعربية؟</dt><dd>الدليل بالإنجليزية، والتدريب متاح بالعربية والإنجليزية والفرنسية.</dd>
<dt>هل التدريب مسجّل؟</dt><dd>لا، كل جلسة تُقدَّم مباشرة مع وقت لأسئلتكم من الموقع.</dd>
<dt>هل يناسب الشركات في الخليج؟</dt><dd>نعم، توقيت 8:00 صباحًا في مونتريال يوافق ما بعد الظهر في الدوحة ودبي.</dd></dl>
</div></main>"""

def course_ld(lang, name, desc):
    return {"@context": "https://schema.org", "@type": "Course", "name": name, "description": desc, "inLanguage": lang,
            "url": f"{SITE}/{lang}/", "provider": {"@type": "Person", "name": AUTHOR_NAME, "url": f"{SITE}/about/"},
            "offers": {"@type": "Offer", "category": "Paid", "price": "900", "priceCurrency": "CAD", "url": PRIVATE},
            "hasCourseInstance": {"@type": "CourseInstance", "courseMode": "Online", "startDate": "2026-12-03T08:00:00-05:00",
                                  "endDate": "2026-12-03T11:00:00-05:00", "courseWorkload": "PT3H",
                                  "location": {"@type": "VirtualLocation", "url": MAVEN}}}

FR_DESC = "Formation en direct sur les boulons d'ancrage et les fondations de charpente d'acier : implantation, mise à niveau, points d'arrêt avant bétonnage, corrections. Québec et Zoom, en français, anglais ou arabe."
AR_DESC = "تدريب مباشر على براغي التثبيت وأساسات المنشآت الفولاذية: التوقيع، ضبط المنسوب، نقاط الفحص قبل الصب، التصحيحات. عبر Zoom بالعربية والإنجليزية والفرنسية."

PAGES = {
    "fr": {"title": "Formation boulons d'ancrage et fondations de charpente d'acier (Québec et en ligne)", "desc": FR_DESC, "body": FR_BODY,
           "ld": [course_ld("fr", "Formation : boulons d'ancrage et fondations de charpente d'acier", FR_DESC), EVENT_LD],
           "nav": nav([("Formation", f"{BASE}/training/"), ("Liste avant bétonnage", f"{BASE}/checklist/"), ("Auteur", f"{BASE}/about/"), ("EN", f"{BASE}/"), ("عربي", f"{BASE}/ar/")])},
    "ar": {"title": "تدريب براغي التثبيت وأساسات المنشآت الفولاذية", "desc": AR_DESC, "body": AR_BODY,
           "ld": [course_ld("ar", "تدريب: براغي التثبيت وأساسات المنشآت الفولاذية", AR_DESC), EVENT_LD],
           "nav": nav([("التدريب", f"{BASE}/training/"), ("قائمة الفحص", f"{BASE}/checklist/"), ("المؤلف", f"{BASE}/about/"), ("EN", f"{BASE}/"), ("FR", f"{BASE}/fr/")])},
}
