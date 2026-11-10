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
<h2>Lectures gratuites</h2>
<ul><li><a href="{BASE}/fr/qa-qc/">Les 10 points d'arrêt AQ/CQ (en français)</a></li>
<li><a href="{BASE}/checklist/">Liste de vérification avant bétonnage</a></li>
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
<h2>مقالات</h2>
<ul><li><a href="{BASE}/ar/qa-qc/">نقاط التوقف العشر لضبط الجودة QA/QC</a></li>
<li><a href="{BASE}/articles/anchor-bolt-interview-questions-qa-qc/">أسئلة مقابلات مهندسي الموقع وQA/QC (بالإنجليزية)</a></li></ul>
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

EN_QA = "articles/qa-qc-hold-points-steel-structure-foundations/"
QA_ALTS = {"en": EN_QA, "fr": "fr/qa-qc/", "ar": "ar/qa-qc/"}

FR_HOLD = [
    ("1. Avant l'excavation", "Points de contrôle d'arpentage vérifiés", "Arpenteur / ingénieur", "Registre des points de contrôle"),
    ("2. Après l'excavation", "Profondeur, largeur et compaction (essai de densité en place)", "Géotechnique", "Rapport de densité et de compaction"),
    ("3. Avant le béton maigre", "Polyéthylène et traitement anti-termites", "Ingénieur / inspecteur", "Journal de chantier"),
    ("4. Après le béton maigre", "Niveau du béton maigre vérifié", "Arpenteur / ingénieur", "Relevé de niveau"),
    ("5. Avant l'armature", "Nuance et diamètre des barres contre les certificats d'usine", "Ingénieur / AQ-CQ", "Certificats d'usine"),
    ("6. Pose des boulons d'ancrage", "Nuance, diamètre et gabarit des boulons contre le plan", "Ingénieur / fabricant", "Vérification du gabarit"),
    ("7. Avant bétonnage (point final)", "Boulons, armature, coffrage, niveaux, propreté", "Consultant / client", "Autorisation de bétonner signée"),
    ("8. Béton frais", "Affaissement et température notés; cubes prélevés", "Technicien / ingénieur", "Bon de livraison et rapport d'essai"),
    ("9. Après la cure", "Résultat des cubes à 7 jours", "Laboratoire", "Rapport de laboratoire"),
    ("10. Acceptation finale", "Résultat des cubes à 28 jours", "Laboratoire", "Rapport de laboratoire"),
]
AR_HOLD = [
    ("1. قبل الحفر", "التحقق من نقاط التحكم المساحية", "المسّاح / المهندس", "سجل نقاط التحكم"),
    ("2. بعد الحفر", "العمق والعرض والدمك (اختبار الكثافة الحقلية FDT)", "الجيوتقني", "تقرير الكثافة والدمك"),
    ("3. قبل الخرسانة العادية", "شريحة البولي إيثيلين والمعالجة ضد النمل الأبيض", "المهندس / المفتش", "السجل اليومي"),
    ("4. بعد الخرسانة العادية", "التحقق من منسوب الخرسانة العادية", "المسّاح / المهندس", "محضر المناسيب"),
    ("5. قبل حديد التسليح", "رتبة وقطر الحديد مقابل شهادات المصنع", "المهندس / QA-QC", "شهادات المصنع"),
    ("6. تركيب براغي التثبيت", "رتبة وقطر ونمط البراغي مقابل المخطط", "المهندس / المصنّع", "فحص القالب (Template)"),
    ("7. قبل الصبّ (البوابة النهائية)", "البراغي والحديد والشدّة والمناسيب والنظافة", "الاستشاري / المالك", "إذن الصبّ الموقّع"),
    ("8. الخرسانة الطازجة", "تسجيل الهبوط ودرجة الحرارة وأخذ المكعبات", "الفني / المهندس", "تذكرة التوريد وتقرير الاختبار"),
    ("9. بعد المعالجة", "نتيجة مكعبات 7 أيام", "المختبر", "تقرير المختبر"),
    ("10. الاستلام النهائي", "نتيجة مكعبات 28 يومًا", "المختبر", "تقرير المختبر"),
]

def hold_table(rows, head):
    return ("<table><tr>" + "".join(f"<th>{h}</th>" for h in head) + "</tr>"
            + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows) + "</table>")

FR_QA_BODY = f"""<main><div class="wrap">
<p class="crumbs"><a href="{BASE}/fr/">Accueil</a> / AQ-CQ</p>
<h1>Points d'arrêt AQ/CQ pour les fondations de charpente d'acier et les boulons d'ancrage</h1>
<p class="note">Par <a href="{BASE}/about/">{AUTHOR_NAME}</a> · tiré du chapitre 14 du guide (en anglais)</p>
<div class="key"><strong>En bref :</strong> une fondation de charpente d'acier compte 10 points d'arrêt, de l'arpentage aux cubes à 28 jours. Chaque étape est vérifiée, signée par une personne nommée et laisse une trace écrite; aucune étape n'est franchie sans elle.</div>
<p>La qualité ne s'ajoute pas par l'inspection : elle se construit dans l'ouvrage. Vérifier à chaque étape, documenter ce qu'on vérifie et garder la traçabilité. Le plan du guide renvoie à l'ACI 318, chapitre 26, et à l'ISO 9001.</p>
{hold_table(FR_HOLD, ["Point d'arrêt", "Vérification", "Responsable", "Preuve"])}
<p class="note">Adaptez les responsables et les preuves au plan d'inspection et d'essais (PIE/ITP) de votre projet.</p>
<h2>Le point final avant bétonnage</h2>
<p>Plans de la dernière révision, alignement et position des boulons, coffrage, armature et enrobage, nuance et diamètre des boulons, gabarit serré et soudé à l'armature, débris soufflés puis lavés, filets protégés par du ruban, accès sécuritaire, éclairage et vibrateur testé. Puis le consultant ou le client signe. Pas de signature, pas de coulée.</p>
<h2>Résultat faible à 28 jours</h2>
<p>Avisez le concepteur immédiatement et ne cachez jamais un résultat. Le concepteur décide : nouvelle vérification de capacité, carottage ou renforcement.</p>
<p><a href="{BASE}/{EN_QA}" hreflang="en">Version anglaise</a> · <a href="{BASE}/ar/qa-qc/" hreflang="ar">العربية</a> · <a href="{BASE}/checklist/">Liste de vérification imprimable (anglais)</a></p>
<p><a class="btn" href="{BASE}/fr/">Formation en français &rarr;</a> <a class="btn amz" href="{GUMROAD}?utm_source=guide-site&amp;utm_medium=web&amp;utm_campaign=fr-qaqc">Le guide complet (30 $ CA)</a></p>
</div></main>"""

AR_QA_BODY = f"""<main><div class="wrap">
<p class="crumbs"><a href="{BASE}/ar/">الرئيسية</a> / ضبط الجودة</p>
<h1>نقاط التوقف للفحص (QA/QC) في أساسات المنشآت الفولاذية وبراغي التثبيت</h1>
<p class="note">بقلم <a href="{BASE}/about/">هشام زين الدين</a> · من الفصل 14 من الدليل (بالإنجليزية)</p>
<div class="key"><strong>باختصار:</strong> لأساسات المنشأة الفولاذية 10 نقاط توقف، من نقاط التحكم المساحية حتى مكعبات 28 يومًا. كل مرحلة تُفحص ويوقّعها شخص محدد وتترك سجلًا مكتوبًا، ولا يُسمح بتجاوزها من دونه.</div>
<p>الجودة لا تُضاف بالفحص، بل تُبنى في العمل نفسه: افحص في كل مرحلة، ووثّق ما تفحصه، واحفظ إمكانية التتبّع. يستند هذا الجدول إلى ACI 318 الفصل 26 وISO 9001.</p>
{hold_table(AR_HOLD, ["نقطة التوقف", "ما يُفحص", "المسؤول", "السجل"])}
<p class="note">عدّل المسؤولين والسجلات حسب خطة الفحص والاختبار (ITP) الخاصة بمشروعك.</p>
<h2>البوابة النهائية قبل الصبّ</h2>
<p>أحدث مخططات معتمدة للتنفيذ، استقامة البراغي ومواقعها، الشدّة الخشبية، الحديد والغطاء الخرساني، رتبة البراغي وقطرها، القالب مثبّت وملحوم بالحديد، تنظيف بالهواء المضغوط ثم بالماء، تغطية الأسنان بالشريط، ممر آمن، إضاءة وهزّاز مُجرَّب. ثم يوقّع الاستشاري أو المالك. لا توقيع، لا صبّ.</p>
<h2>نتيجة منخفضة بعد 28 يومًا</h2>
<p>أبلغ المصمم فورًا ولا تُخفِ أي نتيجة. المصمم يقرر: إعادة التحقق من القدرة، أخذ عينات لبّية، أو التدعيم.</p>
<p><a href="{BASE}/{EN_QA}" hreflang="en">النسخة الإنجليزية</a> · <a href="{BASE}/fr/qa-qc/" hreflang="fr">Français</a> · <a href="{BASE}/checklist/">قائمة الفحص قبل الصبّ (بالإنجليزية)</a></p>
<p><a class="btn" href="{BASE}/ar/">التدريب بالعربية &larr;</a> <a class="btn amz" href="{GUMROAD}?utm_source=guide-site&amp;utm_medium=web&amp;utm_campaign=ar-qaqc">الدليل الكامل (بالإنجليزية)</a></p>
</div></main>"""

def qa_ld(lang, path, title, desc):
    return [{"@context": "https://schema.org", "@type": "Article", "headline": title, "description": desc, "inLanguage": lang,
             "author": {"@type": "Person", "name": AUTHOR_NAME, "url": f"{SITE}/about/"}, "mainEntityOfPage": f"{SITE}/{path}",
             "citation": {"@type": "Book", "name": TITLE, "url": GUMROAD}}]

FR_QA_DESC = "Les 10 points d'arrêt AQ/CQ d'une fondation de charpente d'acier, de l'arpentage aux cubes à 28 jours : qui signe et quelle preuve garder. Pour inspecteurs et techniciens en contrôle de la qualité."
AR_QA_DESC = "نقاط التوقف العشر لضبط الجودة في أساسات المنشآت الفولاذية، من المساحة حتى مكعبات 28 يومًا: من يوقّع وأي سجل يُحفظ. لمهندسي ومفتشي QA/QC."

EXTRA_PAGES = {
    "fr/qa-qc/": {"lang": "fr", "title": "Points d'arrêt AQ/CQ : fondations de charpente d'acier et boulons d'ancrage", "desc": FR_QA_DESC, "body": FR_QA_BODY,
                  "ld": qa_ld("fr", "fr/qa-qc/", "Points d'arrêt AQ/CQ : fondations de charpente d'acier", FR_QA_DESC), "nav": PAGES["fr"]["nav"], "alts": QA_ALTS},
    "ar/qa-qc/": {"lang": "ar", "title": "نقاط التوقف لضبط الجودة QA/QC في أساسات المنشآت الفولاذية", "desc": AR_QA_DESC, "body": AR_QA_BODY,
                  "ld": qa_ld("ar", "ar/qa-qc/", "نقاط التوقف لضبط الجودة في أساسات المنشآت الفولاذية", AR_QA_DESC), "nav": PAGES["ar"]["nav"], "alts": QA_ALTS},
}
