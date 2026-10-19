from build import BASE, fig  # noqa: F401

ARTICLES = [
{
"slug": "anchor-bolt-template",
"title": "How to make and use an anchor bolt template",
"desc": "Why every anchor bolt group needs a template, how to fabricate it to match the column base plate, and why you should keep it to drill the base plates.",
"chapter": 11, "img": "p-template",
"answer": "A template is a temporary plywood or steel plate drilled with the exact number, diameter, spacing and arrangement of the column's bolts. It holds the whole bolt group in that pattern while the concrete is cast, and the same template can later be used to drill the base plates, so both ends match.",
"body": f"""
<p>Anchor bolts cannot be placed by hand and hoped into position. They must sit in the exact pattern the steel column will later bolt down to. The single most important tool for getting this right is the anchor bolt template.</p>
<h2>What the template must match</h2>
<p>The template is a physical copy of the column's bolt pattern. It must mirror the base connection hole for hole:</p>
<ul>
<li><strong>The same number of holes</strong> as bolts in the column base.</li>
<li><strong>The same diameter</strong> as the bolts, so each bolt is held snugly and cannot wander.</li>
<li><strong>The correct spacing</strong> between the bolts.</li>
<li><strong>The correct disposition</strong> (arrangement), in the same layout the column base requires.</li>
</ul>
<h2>Mark the centre with a nail</h2>
<p>The holes fix the pattern; the template still has to sit in the right place on the footing. Put a nail in the exact centre of the template. The surveyor and the engineer line this centre nail up with the surveyed column centre point when positioning the template.</p>
<h2>The template serves twice</h2>
<p>Do not throw the template away after the pour. It is a precise record of the bolt pattern, so use it as the drilling reference when the column base plates are fabricated. One pattern, one reference: the plate holes line up with the bolts already cast in, and you avoid measuring the same pattern twice from the drawing.</p>
{fig("p-template", "Page 37 of the guide: the template serves twice.")}
<h2>On site</h2>
<ol>
<li>Fabricate the template from the base-plate detail on the drawing.</li>
<li>Measure every bolt with a caliper before it goes into the template.</li>
<li>Fit two nuts and two washers per bolt, one set below the template and one above.</li>
<li>Mark the centre nail and align it with the surveyed column point.</li>
<li>Keep the template for the base-plate fabricator.</li>
</ol>
""",
"faq": [
("What is an anchor bolt template made of?", "Plywood or metal. It is a temporary plate drilled with holes that match the column base plate's bolt pattern."),
("Can the anchor bolt template be reused?", "Yes. Keep it and use it as the drilling reference for the column base plates, so the plate holes match the bolts already cast in the foundation."),
("How is the template positioned on the footing?", "With a nail in the exact centre of the template, aligned with the surveyed column centre point."),
],
"related": ["l-bolt-j-bolt-hook-orientation", "anchor-bolt-tolerances", "astm-f1554-grades"],
},
{
"slug": "astm-f1554-grades",
"title": "ASTM F1554 Grade 36 vs 55 vs 105: which anchor bolt grade?",
"desc": "The three ASTM F1554 anchor bolt grades, their yield strengths and typical uses, how they relate to ISO 8.8 and 10.9, and why you must measure the diameter yourself.",
"chapter": 11, "img": "p-standards",
"answer": "ASTM F1554 defines three anchor bolt grades by yield strength: Grade 36 (250 MPa), Grade 55 (380 MPa) and Grade 105 (720 MPa). The grade is set by the design; on site you verify the grade and measure the diameter of every bolt against the drawing.",
"body": """
<p>Anchor bolts must be checked against the design specification. The grade matters as much as the diameter, because it sets the bolt's strength.</p>
<table><tr><th>ASTM F1554 grade</th><th>Yield strength</th><th>Common use</th></tr>
<tr><td>Grade 36</td><td>250 MPa (low-strength carbon steel)</td><td>Light structures, non-seismic</td></tr>
<tr><td>Grade 55</td><td>380 MPa (medium strength)</td><td>General industrial, PEB</td></tr>
<tr><td>Grade 105</td><td>720 MPa (high strength)</td><td>Heavy loads, seismic, high tension / uplift</td></tr></table>
<p class="note">Table 11.1 of the guide. The design decides the grade, not the site.</p>
<h2>F1554 or ISO 8.8 / 10.9?</h2>
<p>ASTM F1554 (Grades 36, 55, 105) and the ISO 898-1 metric property classes (such as 8.8 and 10.9) are two separate classification systems. A bolt is specified under one or the other, not both. Match whichever system your drawings use. Hooked bolts are typically hot-dip galvanised to ASTM A153 / ISO 1461.</p>
<h2>Measure the diameter with a caliper</h2>
<p>You cannot tell a 12 mm bolt from a 14 mm bolt by looking at it, or a 22 mm from a 24 mm. They look identical in the hand. A 2 mm difference is the difference between the right bolt and the wrong one: cast the wrong diameter and the base plate holes no longer match the foundation.</p>
<ul><li>Measure each bolt with a caliper before it goes into the template.</li>
<li>Confirm it matches the diameter on the drawing, the same one the template holes and the base plate are made to.</li>
<li>Do it yourself. This is a check you make personally, not one you take on someone's word.</li></ul>
""",
"faq": [
("What is the yield strength of ASTM F1554 Grade 55?", "380 MPa. Grade 36 is 250 MPa and Grade 105 is 720 MPa."),
("Is an F1554 Grade 105 bolt the same as an ISO 10.9 bolt?", "No. ASTM F1554 grades and ISO 898-1 property classes are separate systems. Use the system your drawings specify."),
("Why measure anchor bolt diameter on site?", "Because a 2 mm difference, such as 22 mm against 24 mm, cannot be seen by eye, and the wrong diameter will not match the base plate holes."),
],
"related": ["anchor-bolt-template", "l-bolt-j-bolt-hook-orientation", "pre-pour-checklist"],
},
{
"slug": "anchor-bolt-tolerances",
"title": "Anchor bolt setting tolerances: what is acceptable?",
"desc": "Typical anchor bolt tolerances for bolt group position, spacing, projection and top elevation, based on AISC and ACI 117 practice, and what to do when bolts fall outside them.",
"chapter": 12, "img": "p-grout",
"answer": "Typical values are ±6 mm for the bolt group centre from the column centre-line, ±3 mm between bolts within a group, +25 mm / −6 mm for projection (per detail) and ±13 mm for bolt top elevation. Always use the tolerances in your own drawings and specification.",
"body": """
<table><tr><th>Item</th><th>Typical tolerance</th></tr>
<tr><td>Bolt group centre from column centre-line</td><td>±6 mm</td></tr>
<tr><td>Spacing between individual bolts within a group</td><td>±3 mm</td></tr>
<tr><td>Bolt projection above concrete</td><td>+25 mm / −6 mm (per detail)</td></tr>
<tr><td>Bolt top elevation</td><td>±13 mm</td></tr>
<tr><td>Base plate level</td><td>Corrected on levelling nuts before grouting</td></tr></table>
<p class="note">Table 12.1 of the guide. Values are representative of AISC (Code of Standard Practice / Design Guide 1) and ACI 117 anchorage tolerances. Tolerances differ between codes and projects.</p>
<h2>Check them before the pour, not after</h2>
<p>Between fixing the bolts and pouring, a lot happens around them: rebar is adjusted, people and tools move through. At the final gate, check again:</p>
<ul><li><strong>Top level of each bolt:</strong> consistent across the group so the base plate seats flat. Adjust with the nuts.</li>
<li><strong>Spacing:</strong> the distances still match the pattern.</li>
<li><strong>Alignment:</strong> the group is squared to the lines and centred on the surveyed column point, using the centre nail.</li></ul>
<h2>If bolts are out after casting</h2>
<p>Under 6 mm, the oversized base plate holes can often take it. From 6 to 12 mm, consult the structural engineer. Over 12 mm, do not bend the bolts. See <a href="../misaligned-anchor-bolts/">misaligned anchor bolts</a>.</p>
""",
"faq": [
("What is the typical tolerance for anchor bolt spacing?", "±3 mm between bolts within a group, and ±6 mm for the group centre from the column centre-line. Your project specification governs."),
("How much can anchor bolts project above the concrete?", "A typical tolerance is +25 mm / −6 mm on the projection shown on the detail."),
("How is the base plate levelled?", "On levelling nuts (or shims) on the bolts, leaving a gap under the plate that is then filled with non-shrink grout."),
],
"related": ["misaligned-anchor-bolts", "base-plate-non-shrink-grout", "anchor-bolt-template"],
},
{
"slug": "misaligned-anchor-bolts",
"title": "Misaligned anchor bolts after casting: the correct fixes",
"desc": "What to do when the bolt group does not line up with the base plate holes: under 6 mm, 6 to 12 mm, and over 12 mm. Why you should never bend anchor bolts.",
"chapter": 15, "img": "p-troubleshooting",
"answer": "Under 6 mm: the base plate holes are normally oversized, so the plate can often shift. From 6 to 12 mm: consult the structural engineer, who may allow slotted holes with thick hardened plate washers. Over 12 mm: do not bend the bolts; cut them off and install post-installed anchors, with the engineer's approval.",
"body": f"""
<p>Symptom: the bolt group does not line up with the base plate holes. What separates a strong engineer is not never having a problem; it is knowing the correct fix, and knowing which problems must go back to the designer.</p>
<h2>Minor: less than 6 mm</h2>
<p>Check the base plate first. Plate holes are normally oversized, typically bolt diameter + 3 to 6 mm, so the plate can often shift to take the bolts.</p>
<h2>Moderate: 6 to 12 mm</h2>
<p>Consult the structural engineer. They may permit slotting (elongating) the plate holes, with thick hardened plate washers over them.</p>
<h2>Severe: more than 12 mm</h2>
<p><strong>Do not bend the bolts.</strong> Bending reduces their tensile capacity. The accepted fix is to cut off the bolts and install post-installed anchors next to the originals. Structural engineer approval required.</p>
{fig("p-troubleshooting", "Page 52 of the guide: troubleshooting and field fixes.")}
<h2>Prevent it</h2>
<p>Most misalignment starts before the pour: no template, bolts tied but not welded, or the pump aimed at the bolts. Tie, check level and alignment, then weld to the rebar, and direct the concrete onto the reinforcement, never at the bolt assembly.</p>
""",
"faq": [
("Can you bend anchor bolts to fit the base plate?", "No. Bending reduces their tensile capacity. Beyond 12 mm, cut them off and install post-installed anchors with the structural engineer's approval."),
("How oversized are base plate holes?", "Typically the bolt diameter plus 3 to 6 mm, which is why small misalignments can often be absorbed."),
("Who approves a fix for misaligned anchor bolts?", "The structural engineer, for anything from 6 mm upward."),
],
"related": ["anchor-bolt-tolerances", "pouring-concrete-around-anchor-bolts", "damaged-anchor-bolt-threads"],
},
{
"slug": "l-bolt-j-bolt-hook-orientation",
"title": "L-bolt and J-bolt hooks: which way should they face?",
"desc": "Hooked anchor bolts must face the outside of the foundation. Plus the two-nuts-two-washers rule, embedment depth, and the tie-check-weld sequence.",
"chapter": 11, "img": "p-hooks",
"answer": "The hook of an L-bolt or J-bolt always faces the external side of the foundation, away from the centre. Each bolt gets two nuts and two washers, one set below the template and one above, and is embedded to the depth on the drawing.",
"body": """
<h2>Hooks face outward</h2>
<p>The bent leg of the hook grips the concrete and resists pull-out. Turned outward, away from the centre, it anchors the way the design assumed. Set the wrong way, the bolt looks the same from above, but it is not anchored as designed. This matters most where uplift and overturning govern: PEB portals under wind suction, cantilevered poles and open canopies.</p>
<h2>Two nuts and two washers on every bolt</h2>
<p>One nut and washer below the template, one above. The bolt is gripped from both sides, so it cannot move during the pour, and you can raise or lower it with the nuts to set the projection exactly.</p>
<h2>Embedment comes from the drawing</h2>
<p>Embedment depth is a structural value: it lets the bolt develop its capacity. Read it from the drawing and set it exactly. A common field rule of thumb is about 10 × the diameter minimum, with edge distance about 5 × the diameter, but these are not code minimums. ACI 318 Chapter 17 or EN 1992-4 calculations govern.</p>
<h2>Tie, check, then weld</h2>
<ol><li>Tie the anchors to the rebar with binding wire: held, but still adjustable.</li>
<li>Check level and alignment, and adjust until it is exactly right.</li>
<li>Weld the anchors to the reinforcement with horizontal rebar, so pump pressure cannot move them.</li></ol>
<p>Weld before you check, and you lock in an error. Rely on binding wire alone, and the pour will move your bolts.</p>
""",
"faq": [
("Which way does a J-bolt hook face?", "Toward the outside of the foundation, away from the centre, so it resists pull-out as designed."),
("How many nuts go on an anchor bolt during casting?", "Two nuts and two washers: one set below the template and one above."),
("Is binding wire enough to hold anchor bolts during the pour?", "No. Tie first to adjust, check, then weld the anchors to the rebar with horizontal bars."),
],
"related": ["anchor-bolt-template", "pouring-concrete-around-anchor-bolts", "astm-f1554-grades"],
},
{
"slug": "pre-pour-checklist",
"title": "Pre-pour checklist for anchor bolts and foundations (final gate)",
"desc": "The final gate before casting a steel-structure foundation: bolts, formwork, rebar, spacers, cleaning, threads, access, lighting, vibrator and the inspector's signature.",
"chapter": 14, "img": "p-qaqc",
"answer": "Nothing is poured until every line is confirmed and the inspector has signed: latest IFC drawings, bolt alignment, formwork, rebar and cover, anchor grade and diameter, template welded, debris blown and washed, threads taped, safe walkway, lighting, vibrator fuelled, and written sign-off.",
"body": f"""
<p>Quality is not inspected into the work; it is built into it. Once the pour begins, position is fixed forever, so everything is verified one last time.</p>
<p><a class="btn" href="{BASE}/checklist/" style="color:#13213a">Open the free printable checklist</a></p>
<h2>Check the bolts</h2>
<p>Top level of each bolt, spacing, and alignment to the centre nail. Rebar was adjusted and people moved through after you fixed them; anything may have been nudged.</p>
<h2>Check the element around them</h2>
<ul><li><strong>Formwork:</strong> every support and fixing firm, so the shutter does not move or bulge.</li>
<li><strong>Rebar:</strong> distributed and spaced as designed.</li>
<li><strong>Spacers:</strong> still holding the cover on every face.</li></ul>
<h2>Blow first, then wash</h2>
<p>Blow the dust, wood offcuts, nails and wire ends out with compressed air, then wash the rebar and the foundation. The other way round turns dust into mud.</p>
<h2>Before you order the pump</h2>
<ul><li>A walkway with a handrail outside the foundation, so the crew never stands on the formwork.</li>
<li>Site cleared of offcuts, spare rebar and debris.</li>
<li>Vibrator fuelled and tested; lighting set up if the pour runs into the night.</li></ul>
<h2>No signature, no pour</h2>
<p>Call the consultant or client for the formal inspection in time, walk the work with them, and get the written approval before casting.</p>
{fig("p-qaqc", "Page 50 of the guide: mandatory hold points and the final-gate checklist.")}
""",
"faq": [
("Who signs off a foundation before concrete?", "The consultant or the client, after a formal inspection. No signature, no pour."),
("Should you blow or wash the foundation first?", "Blow first with compressed air, then wash. Washing first turns dust into mud."),
("What equipment must be ready before the pump arrives?", "A fuelled and tested vibrator, lighting for night work, and a safe walkway with a handrail."),
],
"related": ["pouring-concrete-around-anchor-bolts", "damaged-anchor-bolt-threads", "anchor-bolt-tolerances"],
},
{
"slug": "pouring-concrete-around-anchor-bolts",
"title": "Pouring concrete around anchor bolts without moving them",
"desc": "Never aim the pump at the bolts, pour all ready foundations at once to avoid cold joints, and stop only at a designed construction joint.",
"chapter": 11, "img": "og",
"answer": "Direct the pump discharge onto the foundation rebar and let the concrete rise around the anchors; never aim it at the bolts. Order the full quantity and pour continuously, stopping only at a construction joint shown on the drawing.",
"body": """
<h2>Never aim the pump at the anchor bolts</h2>
<p>Concrete leaves the pump line with real force. Aimed straight at the anchor assembly, it can push the bolts out of alignment, spacing or level, despite the fixing and welding.</p>
<ul><li>Direct the concrete onto the reinforcement and let it flow around the bolts.</li>
<li>Keep the discharge away from the bolt assembly.</li>
<li>Let the concrete rise around the anchors gently.</li></ul>
<h2>Order enough to pour it all at once</h2>
<p>A continuous pour is monolithic. Stop partway and let the concrete start to set, and the next pour does not bond as one: you create a cold joint, an unplanned line of weakness. The only correct place to stop is a construction joint provided by the design. Planned joint: stop. No joint: pour it all in one.</p>
<h2>The pour cannot be paused</h2>
<p>Fuel the vibrator before you start: one that dies mid-pour leaves concrete arriving that cannot be compacted, with a risk of voids and honeycombing. If the pour runs into the night, set up the lighting first.</p>
<h2>Concrete grade and cement type</h2>
<p>For foundations and beams, the grade is commonly 30 N or 35 N, confirmed on the drawings. Below ground, order Sulfate-Resisting Cement (SRC); above ground, Ordinary Portland Cement (OPC), subject to the specification and the geotechnical report. See <a href="../src-vs-opc-cement-foundations/">SRC vs OPC</a>.</p>
""",
"faq": [
("Where should the concrete pump be aimed near anchor bolts?", "Onto the foundation reinforcement, never directly at the bolts, so pump pressure does not shift them."),
("What is a cold joint?", "An unplanned joint where fresh concrete meets concrete that has started to set, creating a line of weakness."),
("When is it acceptable to stop a pour?", "Only at a construction joint provided by the design."),
],
"related": ["pre-pour-checklist", "src-vs-opc-cement-foundations", "l-bolt-j-bolt-hook-orientation"],
},
{
"slug": "base-plate-non-shrink-grout",
"title": "Base plate grouting: why it must be non-shrink grout",
"desc": "How the base plate sits on levelling nuts, why the gap must be filled with non-shrink grout (ASTM C1107), and how to fix grout voids under the plate.",
"chapter": 12, "img": "p-grout",
"answer": "The base plate sits on levelling nuts above the concrete, and the gap is filled with a non-shrink grout. The grout is structural: it transfers the column load into the foundation, and ordinary mortar cracks under wind and column movement.",
"body": f"""
<h2>Setting the base plate</h2>
<ul><li>The base plate is not seated directly on the concrete. It sits on levelling nuts (or shims), leaving a deliberate gap.</li>
<li>That gap lets you level the plate and plumb the column before anything is permanent.</li>
<li>Once levelled, plumbed and tightened, the gap is ready for grout.</li></ul>
<h2>Why non-shrink</h2>
<p>A steel structure is never perfectly still. Wind and column movement put constant small forces into the base. Ordinary or shrinking mortar cracks, loses contact with the plate, and the connection loosens. Non-shrink grout fills the gap without shrinking and stays intact under vibration.</p>
<ul><li>Use the specified non-shrink grout, never site-mixed ordinary mortar.</li>
<li>Fill the gap completely, with no voids.</li>
<li>Follow the specified mixing and placing method.</li></ul>
{fig("p-grout", "Page 47 of the guide: the grout beneath the plate.")}
<h2>Grout voids under the plate</h2>
<p>Symptom: a hollow sound when the plate is tapped. Confirm a non-shrink grout to ASTM C1107 was used. For large gaps over 50 mm, use a coarse-aggregate or epoxy grout. Fill deep voids by pressure injection. Small voids may be acceptable; large voids require removal and re-grouting.</p>
""",
"faq": [
("Why use non-shrink grout under a base plate?", "Because it fills the gap without shrinking and does not crack under wind and column movement, so the load keeps transferring into the foundation."),
("What standard covers non-shrink grout?", "ASTM C1107, packaged dry hydraulic-cement grout."),
("How do you detect voids under a base plate?", "Tap the plate: a hollow sound means the grout did not fill the gap."),
],
"related": ["anchor-bolt-tolerances", "misaligned-anchor-bolts", "damaged-anchor-bolt-threads"],
},
{
"slug": "damaged-anchor-bolt-threads",
"title": "Protecting and repairing anchor bolt threads",
"desc": "Tape the threads before casting, and how to fix concrete-coated, impact-damaged or severely damaged anchor bolt threads.",
"chapter": 15, "img": "p-troubleshooting",
"answer": "Before casting, wrap the exposed thread and nut with masking tape and remove it after the concrete sets. If threads are damaged: clean concrete off with a thread file or die of the same size and pitch, reform impact damage with a thread chaser, and replace severely damaged bolts with post-installed anchors, with the engineer's approval.",
"body": """
<h2>Protect before casting</h2>
<p>The thread above the template is what the base plate will bolt down to. Concrete hardened on it means the nut no longer turns and the plate will not seat.</p>
<ul><li>Tape the nut and the exposed thread with masking tape.</li>
<li>Enough to keep concrete off, but easy to remove.</li>
<li>Remove it after the concrete has set.</li></ul>
<h2>Fixing damaged threads</h2>
<table><tr><th>Damage</th><th>Fix</th></tr>
<tr><td>Concrete on the thread</td><td>Chip it off carefully, then run a thread file or a die of the same size and pitch (for example M24 × 3.0).</td></tr>
<tr><td>Impact-deformed thread</td><td>Use a thread chaser, not a cutting tap, to reform the thread without removing sound material.</td></tr>
<tr><td>Severe (over 50% of thread length, or bolt bent)</td><td>Cut off the bolt and replace it with a post-installed anchor. Structural engineer approval required.</td></tr></table>
<h2>Post-installed anchors are a repair, not a plan</h2>
<p>Chemical, mechanical and undercut anchors (ACI 355.2 / 355.4, ETAG 001) recover a problem. A dirty hole is the most common cause of adhesive-anchor failure: brush and blow it twice. A correctly set cast-in bolt is always stronger and cheaper.</p>
""",
"faq": [
("How do you protect anchor bolt threads during a pour?", "Wrap the exposed thread and nut with masking tape before casting and remove it after the concrete sets."),
("Should you use a tap or a thread chaser on damaged bolt threads?", "A thread chaser. It reforms the thread without cutting away sound material."),
("When must a damaged anchor bolt be replaced?", "When more than 50% of the thread length is damaged or the bolt is bent: cut it off and install a post-installed anchor with the engineer's approval."),
],
"related": ["misaligned-anchor-bolts", "pre-pour-checklist", "base-plate-non-shrink-grout"],
},
{
"slug": "src-vs-opc-cement-foundations",
"title": "SRC vs OPC: which cement for foundations?",
"desc": "Sulfate-Resisting Cement below ground, Ordinary Portland Cement above ground, with typical grades for blinding, footings, tie beams and column necks.",
"chapter": 11, "img": "og",
"answer": "Concrete below zero level is commonly ordered with Sulfate-Resisting Cement (SRC), because it is in contact with sulfates in the soil; concrete above ground uses Ordinary Portland Cement (OPC). Always confirm against the drawings, specification and geotechnical report.",
"body": """
<p>Two things must be right when you order concrete for foundations and beams: the grade and the cement type. The wrong cement is invisible on pour day: a foundation in OPC below ground looks identical to one in SRC. Underground, over the years, it is exposed to exactly the attack it was not made to resist.</p>
<table><tr><th>Element</th><th>Position</th><th>Typical grade</th><th>Cement</th></tr>
<tr><td>Blinding (lean concrete)</td><td>Below grade</td><td>~20 N</td><td>SRC</td></tr>
<tr><td>Footings</td><td>Below grade</td><td>30–35 N</td><td>SRC</td></tr>
<tr><td>Tie / ground beams</td><td>Below grade</td><td>30–35 N</td><td>SRC</td></tr>
<tr><td>Column necks</td><td>Below grade</td><td>30–35 N</td><td>SRC</td></tr>
<tr><td>Columns / slabs</td><td>Above grade</td><td>Per design</td><td>OPC</td></tr></table>
<p class="note">Table 11.2 of the guide. Common values only: always confirm grade and cement type against the drawings, the specification and the geotechnical (sulfate/chloride) report for your site.</p>
<h2>Testing the concrete</h2>
<p>The guide follows cube testing (BS EN 12390), standard in the Gulf, Europe and much of the Middle East. ACI/ASTM jurisdictions use cylinders (ASTM C31/C39). Use whichever your project specifies, and never mix the two acceptance values: cube and cylinder strengths are not equal.</p>
<h2>Low 28-day result?</h2>
<p>Notify the designer immediately and never hide a failed result. The designer may re-check capacity, call for core testing, or require strengthening.</p>
""",
"faq": [
("Why use sulfate-resisting cement below ground?", "Because buried concrete is in contact with sulfates and salts in the soil that attack ordinary cement over time."),
("What concrete grade is typical for footings?", "Commonly 30 N to 35 N, confirmed on the drawings and specification."),
("Are cube and cylinder strengths the same?", "No. Use the test your project specifies and do not mix the acceptance values."),
],
"related": ["pouring-concrete-around-anchor-bolts", "pre-pour-checklist", "first-day-on-site-new-engineer"],
},
{
"slug": "first-day-on-site-new-engineer",
"title": "Your first site as a new engineer: earning the crew's respect",
"desc": "For engineering students and new graduates: how to work with tradesmen who have more years on site, avoid approval traps, and protect your word.",
"chapter": 0, "img": "p-contents",
"answer": "Respect the crew's experience, bring the standards and the sequence, never approve anything on the spot to be polite, approve in writing, and go back to the senior engineer before overriding an earlier instruction.",
"body": """
<p>Every engineer remembers the first day on site as <em>the</em> engineer. How do you ask a steel fixer who has done this for more years than you have been alive to do it differently? What if he is right? What if you are?</p>
<p>These worries are normal. They show you respect the work and the people. Experience and education are two halves of the same job: the tradesman knows <em>how</em> through his hands, and you know <em>why</em>: the code, the load, the tolerance, the consequence.</p>
<div class="key">"You have years of experience, and I respect it. I have studied the science and the standards, and I am here to work together with you to get this project done correctly." That is not weakness. That is leadership.</div>
<h2>Watch for the traps</h2>
<p>Most workers are honest. But sometimes a shortcut arrives dressed as a simple question, and later it becomes "but the engineer approved this".</p>
<ul><li><strong>Never approve on the spot to be polite.</strong> "Let me check and I will confirm" is always acceptable.</li>
<li><strong>Understand why before you say yes:</strong> what it does to the sequence, other trades, the code, the tolerance.</li>
<li><strong>Approve in writing, or not at all.</strong></li>
<li><strong>Respect the method and the sequence.</strong></li>
<li><strong>Your signature is your responsibility.</strong></li></ul>
<h2>Never change a senior engineer's instruction alone</h2>
<p>If a request contradicts an instruction from another engineer, go back and ask why they preferred it. There is usually a reason you cannot see from where you stand. A worker's change request is a request, not a decision.</p>
""",
"faq": [
("How should a new engineer give instructions to experienced workers?", "Respect their experience, explain the requirement and the reason from the drawing or standard, and work together rather than trying to prove you are above them."),
("Should a site engineer approve changes verbally?", "No. Approve in writing, or not at all, and never on the spot just to be polite."),
("What if a worker's request contradicts a senior engineer?", "Go back to that engineer and ask why they preferred the original method before changing anything."),
],
"related": ["pre-pour-checklist", "anchor-bolt-template", "misaligned-anchor-bolts"],
},
]
