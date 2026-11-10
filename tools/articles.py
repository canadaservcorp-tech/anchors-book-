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
{
"slug": "anchor-bolt-embedment-depth",
"title": "Anchor bolt embedment depth: how deep should anchor bolts go?",
"desc": "Embedment depth is a design value, not a site estimate. The common 10 x diameter rule of thumb, what governs the real figure (ACI 318 Ch. 17, EN 1992-4) and how to hold it during the pour.",
"chapter": 11, "img": "p-standards",
"answer": "Anchor bolt embedment depth is set by the structural design (ACI 318 Chapter 17 or EN 1992-4 calculations for the actual load case). A common field rule of thumb is at least about 10 times the bolt diameter, with an edge distance of at least about 5 times the diameter, but these are not code minimums: always read the depth from the drawing and set the bolts to it exactly.",
"body": """
<p>The embedment depth is what lets an anchor bolt develop its capacity and transfer the column's load into the foundation. It is a structural value. It is never a figure to estimate on site.</p>
<h2>Rule of thumb vs design value</h2>
<table><tr><th>Item</th><th>Field rule of thumb</th><th>What actually governs</th></tr>
<tr><td>Embedment depth</td><td>About 10 x bolt diameter (minimum)</td><td>Design drawing (ACI 318 Ch. 17 / EN 1992-4)</td></tr>
<tr><td>Edge distance</td><td>About 5 x bolt diameter (minimum)</td><td>Design drawing</td></tr></table>
<p class="note">Appendix A of the guide. The rules of thumb help you spot an obvious error on a drawing or on site; they never replace the design figure.</p>
<h2>Why it matters most under uplift</h2>
<p>On PEB portals under wind suction, cantilevered poles and open canopies, the bolts are not only holding the column down. They resist pull-out forces that try to overturn it. There the embedment, the outward orientation of L- and J-bolt hooks and the non-shrink grout under the base plate become structural elements, not installation details.</p>
<h2>Holding the depth on site</h2>
<ol>
<li>Read the required embedment and projection from the drawing before the template is made.</li>
<li>Fit two nuts and two washers per bolt, one set below the template and one above, so the bolt is clamped and its height can be adjusted.</li>
<li>Set the depth by the nuts: no more, no less than the drawing.</li>
<li>Check the top level of every bolt again just before the pour, then protect the bolts while the concrete is placed.</li>
</ol>
""",
"faq": [
("What is the minimum embedment depth for an anchor bolt?", "It is set by the structural design for the load case. A common field rule of thumb is at least about 10 times the bolt diameter, but that is not a code minimum; use the figure on the drawing."),
("Which code governs anchor bolt embedment?", "ACI 318 Chapter 17 in North America and EN 1992-4 in Europe, through calculations for the specific load case."),
("Can the site change the embedment depth?", "No. Embedment is a structural value. Any change must come from the structural engineer, in writing."),
],
"related": ["astm-f1554-grades", "l-bolt-j-bolt-hook-orientation", "anchor-bolt-template"],
},
{
"slug": "base-plate-levelling-nuts-shims",
"title": "Levelling nuts or shims under a column base plate?",
"desc": "Why the base plate sits above the concrete on levelling nuts or shims, how the gap is used to level and plumb the column, the tolerances to check, and why the gap is then filled with non-shrink grout.",
"chapter": 12, "img": "p-grout",
"answer": "The column base plate is not seated directly on the concrete. It sits slightly above the foundation on levelling nuts (or shims) on the anchor bolts, leaving a deliberate gap. The nuts are adjusted until the plate is level and the column plumb, the nuts are tightened, and the gap is then filled with non-shrink grout.",
"body": """
<p>The column arrives with its base plate welded on, drilled to the same pattern as the anchor bolts. The plate drops over the projecting bolts, and the column is brought to its correct position and level.</p>
<h2>Why there is a gap</h2>
<ul>
<li>The plate sits on <strong>levelling nuts or shims</strong>, not on the concrete.</li>
<li>The gap lets you level and align the column exactly, adjusting until the plate is level and the column is plumb, before anything is made permanent.</li>
<li>Once the column is levelled, plumbed and the nuts are tightened, the gap is ready for grout.</li>
</ul>
<h2>Tolerances to check before grouting</h2>
<table><tr><th>Item</th><th>Typical tolerance</th></tr>
<tr><td>Bolt group centre from column centre-line</td><td>&plusmn;6 mm</td></tr>
<tr><td>Spacing between bolts within a group</td><td>&plusmn;3 mm</td></tr>
<tr><td>Bolt projection above concrete</td><td>+25 mm / &minus;6 mm (per detail)</td></tr>
<tr><td>Bolt top elevation</td><td>&plusmn;13 mm</td></tr></table>
<p class="note">Table 12.1 of the guide: representative values. Always verify against the project specification.</p>
<h2>Then grout</h2>
<p>The gap is filled with non-shrink grout so the plate bears evenly on the foundation. Ordinary mortar shrinks and leaves voids under the plate; see the grouting article for why non-shrink grout is required.</p>
""",
"faq": [
("Should a base plate sit directly on the concrete?", "No. It sits slightly above the foundation on levelling nuts or shims, leaving a gap that is used to level and plumb the column and is then grouted."),
("When is the gap under the base plate grouted?", "After the column is levelled, plumbed and the nuts are tightened."),
("What tolerance applies to anchor bolt projection?", "A typical value is +25 mm / -6 mm per the detail, but the project specification governs."),
],
"related": ["base-plate-non-shrink-grout", "anchor-bolt-tolerances", "misaligned-anchor-bolts"],
},
{
"slug": "post-installed-anchors-chemical-vs-mechanical",
"title": "Post-installed anchors: chemical vs mechanical vs undercut",
"desc": "When you need drilled-in anchors instead of cast-in bolts, how chemical, expansion and undercut anchors work, the standards behind them, and the installation rules that prevent failures.",
"chapter": 13, "img": "p-troubleshooting",
"answer": "Post-installed anchors are drilled and fixed into concrete that has already cured (ACI 318 Chapter 17, EN 1992-4). Chemical anchors bond a bolt with injected epoxy or vinylester resin (ACI 355.4, ETAG 001); mechanical expansion anchors expand against the hole (ACI 355.2); undercut anchors expand into a shaped undercut for the highest capacity (ACI 355.2). They are a repair or an addition, never a substitute for correctly set cast-in bolts.",
"body": """
<p>Cast-in anchor bolts, set before the concrete is poured, are always the strongest and preferred method. Post-installed anchors are for situations where that was not possible: bolts were missed, a new attachment must be added to hardened concrete, or a repair is needed.</p>
<h2>The three types</h2>
<table><tr><th>Type</th><th>How it works</th><th>Key standards</th></tr>
<tr><td>Chemical (adhesive)</td><td>Epoxy or vinylester resin is injected into a drilled hole; the bolt is inserted and the resin cures to bond it.</td><td>ACI 355.4, ETAG 001</td></tr>
<tr><td>Mechanical expansion</td><td>A wedge- or sleeve-type anchor expands against the hole.</td><td>ACI 355.2</td></tr>
<tr><td>Undercut</td><td>The anchor expands into an undercut at the base of a specially shaped hole, for the highest capacity.</td><td>ACI 355.2</td></tr></table>
<h2>Installation rules</h2>
<ul>
<li><strong>Edge distance and spacing:</strong> meet the manufacturer's and ACI 318 minimums. Too close to an edge and the concrete can blow out under load.</li>
<li><strong>Clean holes for chemical anchors:</strong> correct hole diameter, brush and compressed air twice, the specified volume of adhesive with no air gaps. A dirty hole is the most common cause of adhesive-anchor failure.</li>
<li><strong>Exact torque for mechanical anchors:</strong> under-torqued, the anchor slips; over-torqued, it damages the concrete or the anchor.</li>
<li><strong>Load testing:</strong> for critical applications, field pull-out tests (ASTM E488) may be required before the connection is accepted.</li>
</ul>
<div class="key">A post-installed anchor is a repair or an addition, not a substitute for planning. A correctly set cast-in bolt is always stronger and cheaper than fixing a missed one later.</div>
""",
"faq": [
("Are chemical anchors as strong as cast-in anchor bolts?", "Cast-in bolts set before the pour are always the strongest and preferred method. Post-installed anchors are for repairs and additions, designed per ACI 318 Chapter 17 or EN 1992-4."),
("What is the most common cause of chemical anchor failure?", "A dirty hole. Clean it thoroughly with a brush and compressed air, twice, before injecting the adhesive."),
("How are post-installed anchors tested on site?", "For critical applications, by field pull-out tests per ASTM E488 when the specification requires them."),
],
"related": ["misaligned-anchor-bolts", "anchor-bolt-embedment-depth", "pre-pour-checklist"],
},
{
"slug": "steel-structure-foundation-sequence",
"title": "Steel structure foundation sequence: from drawing to grouted base plate",
"desc": "The site sequence for PEB, warehouse, tower and canopy foundations in 15 steps: drawings, survey, access, excavation, blinding, formwork, rebar, anchor bolts, base plate, grout, QA/QC and fixes.",
"chapter": 1, "img": "p-contents",
"answer": "For PEB buildings, steel frames, warehouses, towers, poles and canopies the foundation workflow is the same: verify the drawings, set out with the surveyor, make the site safe, excavate, prepare the trench bottom, lay the polyethylene sheet and blinding, build the footing formwork, fix the rebar, set the anchor bolts in a template, then place the base plate on levelling nuts and grout it, with QA/QC hold points throughout.",
"body": """
<p>Whether you are building a pre-engineered building (PEB), a hot-rolled frame, a metal warehouse, a transmission tower, a telecom mast, a car-park shade or a lighting pole, the anchor-bolt workflow is the same. The bolts must be set to the exact pattern, at the precise level, with the correct embedment, and held rigidly during casting.</p>
<h2>The sequence</h2>
<ol>
<li><strong>Before the site:</strong> read and verify the drawings.</li>
<li><strong>Setting out:</strong> the surveyor turns the drawing into points, lines and benchmarks on the ground.</li>
<li><strong>Safe access</strong> to the site.</li>
<li><strong>Excavation</strong> and spoil management.</li>
<li><strong>Preparing the trench bottom.</strong></li>
<li><strong>Anti-termite soil treatment</strong> where the region requires it.</li>
<li><strong>Polyethylene sheet.</strong></li>
<li><strong>Blinding</strong> (lean concrete), set to level with the surveyor.</li>
<li><strong>Footing formwork</strong> on the surveyor's new marks.</li>
<li><strong>Reinforcement.</strong></li>
<li><strong>Anchor bolts</strong> in a template: pattern, level, embedment, hook orientation.</li>
<li><strong>Base plate and grouting:</strong> levelling nuts, plumb column, non-shrink grout.</li>
<li><strong>Post-installed anchors</strong>, only for repairs and additions.</li>
<li><strong>QA/QC hold points</strong> from pre-blinding to post-curing.</li>
<li><strong>Troubleshooting and field fixes.</strong></li>
</ol>
<p class="note">These are the 15 chapters of the guide.</p>
<h2>Casting before the steel arrives</h2>
<p>Steel is fabricated in the workshop for weeks or months before delivery. Waiting for it before starting the foundations would cripple the schedule. An accurate template, made from the base-plate detail and later used to drill the plates, lets the foundations be cast first with the confidence that the steel will fit.</p>
""",
"faq": [
("What is the construction sequence for a PEB foundation?", "Drawings, survey, excavation, trench bottom, polyethylene sheet, blinding, formwork, rebar, anchor bolts in a template, concrete, then base plate on levelling nuts and non-shrink grout, with QA/QC hold points throughout."),
("Can foundations be cast before the steel is delivered?", "Yes, if the anchor bolts are set with an accurate template made from the base-plate detail. The same template is then used to drill the base plates."),
("Is the sequence different for towers and poles?", "No. The anchor-bolt workflow is the same; uplift and overturning make embedment, hook orientation and grout even more critical."),
],
"related": ["pre-pour-checklist", "anchor-bolt-template", "first-day-on-site-new-engineer"],
},
{
"slug": "pole-tower-anchor-bolts-uplift",
"title": "Anchor bolts for poles, towers and canopies under uplift",
"desc": "Telecom masts, transmission towers, lighting poles and open canopies put anchor bolts in tension. What changes on site: embedment, hook orientation, grout and tolerances.",
"chapter": 11, "img": "p-hooks",
"answer": "On cantilevered poles, masts, towers, PEB portals under wind suction and open canopies, anchor bolts resist pull-out forces that try to overturn the structure. The embedment depth from the design, the outward orientation of L- and J-bolt hooks and full non-shrink grout under the base plate become critical structural elements, and the bolt group must still match the base plate exactly.",
"body": """
<p>For most buildings the anchor bolts hold the column down and locate it. For a pole, a mast or an open canopy, wind tries to overturn the structure, and the bolts on one side are pulled out of the concrete. They are working in tension.</p>
<h2>What becomes critical</h2>
<ul>
<li><strong>Embedment depth:</strong> exactly as designed. It is what lets the bolt develop its pull-out capacity.</li>
<li><strong>Hook orientation:</strong> L- and J-bolt hooks always face toward the outside of the foundation. Turned the wrong way, the bolt looks the same from above but is not anchored as the design assumed.</li>
<li><strong>Non-shrink grout</strong> under the base plate, so the plate bears evenly.</li>
<li><strong>The pattern:</strong> a template with the exact number, diameter, spacing and arrangement of holes, aligned to the surveyed centre point.</li>
</ul>
<h2>Typical structures</h2>
<p>Electric transmission towers and poles, telecommunication masts and monopoles, lighting poles, traffic-signal masts, sign supports, car-park shades and service canopies.</p>
""",
"faq": [
("Why are anchor bolts critical for telecom masts and poles?", "Wind-induced overturning puts the bolts in tension, so they resist pull-out. Embedment, hook orientation and grout then decide whether the structure holds."),
("Which way should J-bolt hooks face on a pole foundation?", "Toward the outside of the foundation, away from the centre."),
("Is the installation method different for poles?", "The workflow is the same as for buildings, but tension makes the embedment, orientation and grout checks more critical."),
],
"related": ["l-bolt-j-bolt-hook-orientation", "anchor-bolt-embedment-depth", "base-plate-non-shrink-grout"],
},
{
"slug": "anchor-bolt-setting-out-alignment-levelling",
"title": "Setting out anchor bolts: alignment and levelling on site",
"desc": "How to set out anchor bolt groups from survey control: offset pegs, template centring, diagonals, top-of-bolt level and projection, and the check right after the pour.",
"chapter": None, "img": "p-template",
"answer": "Set out every bolt group from the survey grid, not from the formwork. Fix offset pegs outside the excavation so they survive the works, centre the template on the surveyed column point, check the diagonals between groups, set the top-of-bolt level from the benchmark, then check position and level again immediately after the pour.",
"body": """
<p>Most anchor-bolt problems are setting-out problems. A bolt group that is 20 mm off grid was usually set from the wrong reference, not cast badly.</p>
<h2>Work from survey control, not from the formwork</h2>
<ul><li>Use the gridlines and benchmarks given by the surveyor, the same ones the steel was detailed to.</li>
<li>Fix offset pegs or profile boards outside the excavation, so the grid can be re-established after digging, blinding and formwork.</li>
<li>Never measure a bolt group from the edge of the formwork: formwork moves.</li></ul>
<h2>Alignment</h2>
<ul><li>Centre the template on the surveyed column point (the centre nail on the template).</li>
<li>Check the template is square to the gridlines, not just centred.</li>
<li>Check the distances and diagonals between neighbouring bolt groups. The steel frame needs the groups right relative to each other.</li></ul>
<h2>Levelling and projection</h2>
<ul><li>Set the top-of-bolt level from the benchmark with a level or total station.</li>
<li>Check the projection above the concrete against the drawing: enough thread for levelling nut, base plate, washer and top nut.</li>
<li>Use the two nuts on the template to raise or lower each bolt to the exact height.</li></ul>
<h2>Check again after the pour</h2>
<p>Recheck position and level immediately after the pour, while small corrections are still possible, then record an as-built survey of every group before the steel is ordered to site. The erector should receive that as-built, not discover the errors with a crane on hook.</p>
""",
"faq": [
("Where do you measure anchor bolt positions from?", "From the survey gridlines and benchmarks, using offset pegs fixed outside the excavation. Not from the formwork."),
("How do you set the top level of anchor bolts?", "From the benchmark with a level or total station, adjusting each bolt with the nuts above and below the template until the projection matches the drawing."),
("When should anchor bolts be checked after casting?", "Immediately after the pour, then again with an as-built survey of every bolt group before steel erection."),
],
"related": ["anchor-bolt-tolerances", "anchor-bolt-template", "pre-pour-checklist"],
},
{
"slug": "anchor-bolt-protection-until-erection",
"title": "Protecting anchor bolts until steel erection: caps, marking and site rules",
"desc": "Cast-in anchor bolts can wait weeks for the steel. How to protect the threads and the bolt group: caps, tape, nuts left on, marking, keeping equipment away, and no welding or bending.",
"chapter": None, "img": "p-troubleshooting",
"answer": "After the pour, keep the nuts on, cover the threads with caps or tape, mark each bolt group so it is visible to machines, keep equipment and loads away from it, and never weld to, bend or use anchor bolts as tie points. Check the threads again before the erection crew arrives.",
"body": """
<p>Between the pour and the erection crew there can be weeks of excavation, backfill, slab work and traffic. Bolts that were perfect at the pour can be damaged before the first column arrives.</p>
<h2>Protect the threads</h2>
<ul><li>Keep the nuts and washers on the bolts.</li>
<li>Cover the exposed thread with plastic caps, a short pipe sleeve or tape.</li>
<li>On galvanised bolts, protect the coating too: damaged zinc must be repaired before erection, for example with a zinc-rich repair product as the specification allows.</li></ul>
<h2>Make the bolts visible</h2>
<ul><li>Paint or flag each bolt group so excavator, loader and truck drivers can see it.</li>
<li>Barricade groups that sit in traffic routes or near backfill work.</li>
<li>Tell every subcontractor where the bolt groups are before they start.</li></ul>
<h2>Site rules for cast-in bolts</h2>
<ul><li>No welding to anchor bolts and no heating them.</li>
<li>No bending them to clear equipment or to "correct" position.</li>
<li>Do not use them as tie-down or lifting points.</li></ul>
<h2>Before the erection crew arrives</h2>
<p>Remove the caps, clean and check every thread by running the nut down by hand, and confirm the as-built survey. Damaged threads are repaired with a thread file, die or chaser; badly damaged bolts go back to the structural engineer.</p>
""",
"faq": [
("How do you protect anchor bolts after the pour?", "Keep the nuts on, cover the threads with caps, sleeves or tape, mark the bolt groups and keep equipment away until steel erection."),
("Can you weld to anchor bolts?", "No, not unless the structural engineer specifically allows it. Heat can change the steel and damage galvanising."),
("What is checked before erection?", "Clean threads that take the nut by hand, undamaged coating, and an as-built survey of every bolt group."),
],
"related": ["damaged-anchor-bolt-threads", "anchor-bolt-torch-cutting", "misaligned-anchor-bolts"],
},
{
"slug": "anchor-bolt-torch-cutting",
"title": "Torch-cutting anchor bolts and base plate holes: what is allowed?",
"desc": "Can you cut anchor bolt projection with a torch, or enlarge base plate holes by flame cutting? The field rules: saw first, engineer approval, heat, galvanising and fire safety.",
"chapter": None, "img": "p-troubleshooting",
"answer": "Cut excess anchor bolt projection with a saw or abrasive disc rather than a torch where possible, and only after checking enough thread remains. Enlarging or slotting base plate holes, or cutting bolts off for a repair, is done only with the structural engineer's approval, followed by cleaning, hardened plate washers where required and coating repair.",
"body": """
<p>The torch is the fastest tool on site, and that is the problem. A few minutes of flame cutting can turn a small error into a structural repair.</p>
<h2>Cutting excess projection</h2>
<ul><li>First confirm the bolt is at the right level: a bolt that looks too long may be correct and the base plate level wrong.</li>
<li>Leave enough thread for the full nut engagement shown on the drawing.</li>
<li>Prefer a saw or abrasive disc: less heat into the bolt and the concrete.</li>
<li>Dress the cut end so the nut starts cleanly, and repair galvanising.</li></ul>
<h2>Enlarging or slotting base plate holes</h2>
<p>When bolts are slightly out, the temptation is to flame-cut the plate holes bigger. This changes how the connection works. It needs the structural engineer's approval, a clean finished hole and normally a thick hardened plate washer over the enlarged hole.</p>
<h2>Never use the torch to</h2>
<ul><li>Heat and bend a bolt into position.</li>
<li>Cut a bolt off "to fix later" without an approved repair.</li>
<li>Burn through a bolt and weld a new piece on.</li></ul>
<h2>Hot-work safety</h2>
<p>Hot-work permit, fire watch, protection of formwork, membranes and nearby materials, and the right PPE, every time.</p>
""",
"faq": [
("Can you torch cut anchor bolts?", "Cutting excess projection is better done with a saw or abrasive disc. Any cut that shortens bolts below the required thread, or cuts them off for a repair, needs the structural engineer's approval."),
("Can base plate holes be enlarged on site?", "Only with the structural engineer's approval, normally with a thick hardened plate washer over the enlarged or slotted hole."),
("Can you heat anchor bolts to bend them?", "No. Heating and bending reduces their capacity. Misaligned bolts are corrected by an approved repair."),
],
"related": ["misaligned-anchor-bolts", "anchor-bolt-washers-plate-washers", "anchor-bolt-protection-until-erection"],
},
{
"slug": "anchor-bolt-washers-plate-washers",
"title": "Washers on anchor bolts: plate washers, hardened washers and spring washers",
"desc": "Which washers go on anchor bolts under a column base plate: thick plate washers over oversized holes, hardened washers where specified, and why spring washers are used only when the drawings call for them.",
"chapter": None, "img": "p-hooks",
"answer": "Base plate holes for anchor bolts are oversized, so a standard washer is not enough: the drawings normally call for a thick plate washer over each hole, sometimes welded to the base plate. Hardened washers are used where specified. Spring or lock washers are not a standard anchor-bolt detail; use them only if the drawings specify them.",
"body": """
<p>Washers are small, cheap and often forgotten until the inspector asks for them. On anchor bolts they matter more than on ordinary bolts, because the holes in the base plate are deliberately oversized.</p>
<h2>Plate washers over oversized holes</h2>
<ul><li>Base plate holes are larger than the bolt, so a normal washer can sit partly over the hole.</li>
<li>The usual detail is a thick plate washer with a hole just larger than the bolt.</li>
<li>Where the bolts carry shear, the drawings may require the plate washer to be welded to the base plate. Follow the detail exactly.</li></ul>
<h2>Hardened washers</h2>
<p>Hardened washers (such as ASTM F436) are used where the specification calls for them, for example under a turned element or with high-strength bolts. Check the material list, not the stock in the container.</p>
<h2>Spring and lock washers</h2>
<p>Spring washers are not part of a standard anchor-bolt detail. Where vibration or loosening is a concern, such as on poles and towers, the design normally uses a double nut or a specified tightening method. Use spring washers only if the drawings say so.</p>
<h2>During casting</h2>
<p>Two nuts and two washers per bolt hold the template: one set below, one above. These are setting washers, not the final connection hardware.</p>
""",
"faq": [
("What washer goes on an anchor bolt over a base plate?", "Normally a thick plate washer, because the base plate holes are oversized. The size and thickness come from the drawings."),
("Are spring washers used on anchor bolts?", "Not as a standard detail. Use them only if the drawings specify them; vibration is usually handled with double nuts or a specified tightening method."),
("Why are plate washers sometimes welded to the base plate?", "So the bolts can take shear through the washer when the holes are oversized. Only when the drawings require it."),
],
"related": ["base-plate-levelling-nuts-shims", "anchor-bolt-torch-cutting", "astm-f1554-grades"],
},
{
"slug": "anchor-bolt-failures-common-causes",
"title": "Why anchor bolts fail on site: 9 common causes and how to prevent them",
"desc": "The site causes behind misplaced, damaged and failed anchor bolts: wrong drawing revision, no template, poor setting out, movement during the pour, damaged threads, wrong grade or diameter, and unapproved fixes.",
"chapter": None, "img": "p-qaqc",
"answer": "Most anchor-bolt failures on site come from nine causes: wrong drawing revision, no template, setting out from formwork, bolts not fixed rigidly, concrete pumped at the bolts, wrong grade or diameter, unprotected threads, damage before erection and unapproved fixes such as bending or heating. Each one is stopped by a hold point before the pour.",
"body": """
<table><tr><th>Cause</th><th>Prevention</th></tr>
<tr><td>1. Wrong drawing revision</td><td>Check the bolt plan against the latest issued-for-construction drawings and the steel shop drawings.</td></tr>
<tr><td>2. No template</td><td>One template per bolt pattern, drilled to the base plate detail.</td></tr>
<tr><td>3. Setting out from the formwork</td><td>Set out from survey control with offset pegs.</td></tr>
<tr><td>4. Bolts tied but not fixed</td><td>Tie, check level and alignment, then fix rigidly as specified.</td></tr>
<tr><td>5. Concrete aimed at the bolts</td><td>Direct the pump onto the reinforcement; vibrate away from the assembly.</td></tr>
<tr><td>6. Wrong grade or diameter</td><td>Measure every bolt with a caliper and check the grade marking.</td></tr>
<tr><td>7. Concrete on the threads</td><td>Tape or cap the threads before the pour.</td></tr>
<tr><td>8. Damage before erection</td><td>Caps, marking and keeping equipment away.</td></tr>
<tr><td>9. Unapproved fixes</td><td>No bending, heating or cutting without the structural engineer.</td></tr></table>
<p>None of these needs advanced calculation. They need someone with the authority to stop the pour until every check is signed.</p>
""",
"faq": [
("What is the most common cause of misplaced anchor bolts?", "Setting out from the wrong reference or without a rigid template, so the bolt group moves before or during the pour."),
("How do you prevent anchor bolt problems?", "With hold points before the pour: drawing check, survey, template, fixing, thread protection and sign-off."),
("Who decides the repair when anchor bolts fail?", "The structural engineer."),
],
"related": ["pre-pour-checklist", "misaligned-anchor-bolts", "anchor-bolt-setting-out-alignment-levelling"],
},
]

HOLD_POINTS = [
    ("1. Pre-excavation", "Survey control points verified", "Surveyor / Engineer", "Control-point log"),
    ("2. Post-excavation", "Depth, width and compaction (field density test, FDT)", "Geotechnical", "FDT and compaction report"),
    ("3. Pre-blinding", "Polyethylene sheet and anti-termite treatment", "Engineer / Inspector", "Daily log"),
    ("4. Post-blinding", "Blinding level verified", "Surveyor / Engineer", "Level check"),
    ("5. Pre-reinforcement", "Rebar grade and diameter against mill certificates", "Engineer / QA-QC", "Mill certificates"),
    ("6. Anchor-bolt setting", "Bolt grade, diameter and pattern against the drawing", "Engineer / Fabricator", "Template check"),
    ("7. Pre-concrete (final gate)", "All bolts, rebar, formwork, levels, cleanliness", "Consultant / Client", "Cast-in sign-off"),
    ("8. Fresh concrete", "Slump and temperature recorded; cubes cast", "Technician / Engineer", "Delivery ticket and test report"),
    ("9. Post-curing", "7-day cube result received", "Laboratory", "Lab report"),
    ("10. Final acceptance", "28-day cube result received", "Laboratory", "Lab report"),
]
HOLD_TABLE = ("<table><tr><th>Hold point</th><th>What is checked</th><th>Responsible</th><th>Record</th></tr>"
              + "".join(f"<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td></tr>" for a, b, c, d in HOLD_POINTS) + "</table>")

ARTICLES += [
{
"slug": "qa-qc-hold-points-steel-structure-foundations",
"title": "QA/QC hold points for steel-structure foundations and anchor bolts (10-stage plan)",
"desc": "For QA/QC engineers and inspectors: the 10 mandatory hold points from survey to 28-day cubes, who signs each one, and the record that proves it.",
"chapter": 14, "img": "p-qaqc",
"answer": "A steel-structure foundation has 10 hold points: survey control, excavation and compaction, polyethylene and anti-termite, blinding level, rebar against mill certificates, anchor-bolt setting, the pre-concrete final gate, fresh-concrete tests, the 7-day cubes and the 28-day cubes. Each stage is signed by a named person and leaves a record; no stage is passed without it.",
"body": f"""
<p>Quality is not inspected into the work; it must be built into the work. The QA/QC plan turns that idea into hold points: stages the site cannot pass until someone has inspected them, signed, and filed a record. The guide references this plan to ACI 318 Chapter 26 and ISO 9001.</p>
<h2>The 10 mandatory hold points</h2>
{HOLD_TABLE}
<p class="note">Chapter 14 of the guide. Adapt the responsible party and record names to your project's inspection and test plan (ITP).</p>
<h2>Three rules that make the plan work</h2>
<ul><li><strong>Verify at each stage.</strong> A defect found at blinding costs a few hours; the same defect found at erection costs a cut bolt and a post-installed anchor.</li>
<li><strong>Document what you verify.</strong> A check without a record did not happen, as far as the client and the consultant are concerned.</li>
<li><strong>Keep it traceable.</strong> Mill certificates, delivery tickets and cube reports must link to the element they belong to.</li></ul>
<h2>The final gate: hold point 7</h2>
<p>Before concrete, everything is checked one last time: latest IFC drawings, bolt alignment and position, formwork, rebar and cover, anchor grade and diameter, template locked and welded to the rebar, debris blown out and washed, threads taped, safe access, lighting and a tested vibrator. Then the consultant or client signs. <a href="{BASE}/checklist/">The free printable checklist</a> has every line.</p>
<h2>When a result fails</h2>
<p>If the 28-day result comes back below the specified grade, notify the designer immediately and never hide it. The designer decides: a capacity re-check, core testing, or strengthening.</p>
{fig("p-qaqc", "Page 50 of the guide: the mandatory hold points.")}
""",
"faq": [
("What are the hold points for a steel-structure foundation?", "Survey control, excavation and compaction, polyethylene and anti-termite treatment, blinding level, rebar against mill certificates, anchor-bolt setting, the pre-concrete final gate, fresh-concrete tests, and the 7-day and 28-day cube results."),
("Who signs the pre-concrete final gate?", "The consultant or the client, after a formal inspection. No signature, no pour."),
("Which standards does a foundation QA/QC plan reference?", "The guide references ACI 318 Chapter 26 and ISO 9001; your project specification and ITP govern."),
("What does a QA/QC engineer record for rebar?", "Grade and diameter checked against the mill certificates, before reinforcement is fixed."),
],
"related": ["pre-pour-checklist", "concrete-testing-foundations-slump-cubes", "anchor-bolt-interview-questions-qa-qc"],
},
{
"slug": "concrete-testing-foundations-slump-cubes",
"title": "Concrete testing for foundations: slump, temperature and 7/28-day cubes",
"desc": "What the QA/QC engineer checks when concrete arrives and after curing: slump, temperature, cube sampling, 7-day and 28-day results, and what to do with a low result.",
"chapter": 14, "img": "p-qaqc",
"answer": "On delivery, check the ticket, record slump (BS EN 12350 / ASTM C143) and temperature (BS EN 206 / ASTM C1064), and cast cubes: typically 3 per sample, broken at 7, 14 and 28 days (BS EN 12390 / ASTM C39). The 28-day result must reach the specified grade; a low result goes straight to the designer.",
"body": """
<table><tr><th>Test</th><th>Standard</th><th>Acceptance</th></tr>
<tr><td>Slump</td><td>BS EN 12350 / ASTM C143</td><td>Per project specification (for example 75-100 mm)</td></tr>
<tr><td>Temperature</td><td>BS EN 206 / ASTM C1064</td><td>The guide uses &lt; 32 &deg;C (moderate) / &lt; 37 &deg;C (hot climate); the project specification governs</td></tr>
<tr><td>Compressive, 7 days</td><td>BS EN 12390 / ASTM C39</td><td>Early check</td></tr>
<tr><td>Compressive, 28 days</td><td>BS EN 12390 / ASTM C39</td><td>At least the specified grade (for example 30 MPa)</td></tr>
<tr><td>Cubes per sample</td><td>BS EN 12390</td><td>3 cubes, broken at 7 / 14 / 28 days</td></tr></table>
<p class="note">Appendix B of the guide. Ready-mix specification and delivery: BS EN 206 / ASTM C94. In-place soil density before the foundation: sand cone, ASTM D1556.</p>
<h2>At the truck</h2>
<ul><li>Check the delivery ticket against the mix ordered, and keep it: it is the record for hold point 8.</li>
<li>Record slump and temperature before the concrete is accepted.</li>
<li>Cast and label the cubes so each result traces back to the element poured.</li></ul>
<h2>A low 28-day result</h2>
<p>Example: 25 MPa against a specified 30 MPa. Notify the designer immediately; never hide a failed result. The designer may re-check the foundation at the lower strength, call for cores drilled from the hardened concrete for a true in-situ value, and, if it is genuinely insufficient, require strengthening such as an enlarged footing or bonded steel plates.</p>
""",
"faq": [
("How many cubes are taken per concrete sample?", "Typically 3 cubes per sample, broken at 7, 14 and 28 days (BS EN 12390); follow your project specification."),
("What slump is acceptable for foundation concrete?", "Whatever the project specification states, for example 75-100 mm, measured to BS EN 12350 or ASTM C143."),
("What happens if the 28-day cube result is low?", "The designer is notified at once and decides: capacity re-check, core testing, or strengthening."),
],
"related": ["qa-qc-hold-points-steel-structure-foundations", "src-vs-opc-cement-foundations", "pouring-concrete-around-anchor-bolts"],
},
{
"slug": "anchor-bolt-foundation-standards-codes",
"title": "Anchor bolt and foundation standards worldwide: ACI, Eurocode, AISC, ASTM, ISO, BS EN",
"desc": "Which standard covers what on a steel-structure foundation, from concrete design and base plates to bolt grades, galvanising, grout and concrete testing, for projects in North America, Europe, the Gulf and beyond.",
"chapter": None, "img": "p-standards",
"answer": "Concrete design: ACI 318 or EN 1992-1-1. Anchor (fastening) design: ACI 318 Chapter 17 or EN 1992-4. Base plates: AISC Design Guide 1 or EN 1993-1-8. Bolt material: ASTM F1554 (Grades 36, 55, 105) or ISO 898-1 classes 8.8 / 10.9. Galvanising: ASTM A153 / A123 or ISO 1461. Grout: ASTM C1107. Concrete tests: BS EN 12350 / 12390 or ASTM C143 / C39. Use the edition your project specification names.",
"body": """
<p>The guide lists these standards on page 4. Projects specify one family or the other; cite the edition applicable to your jurisdiction, and the local project specification wins wherever it differs.</p>
<table><tr><th>Subject</th><th>American</th><th>European / British</th></tr>
<tr><td>Concrete design</td><td>ACI 318</td><td>EN 1992-1-1 (Eurocode 2)</td></tr>
<tr><td>Fastenings / anchors in concrete</td><td>ACI 318 Chapter 17</td><td>EN 1992-4</td></tr>
<tr><td>Steel design and base plates</td><td>AISC Steel Construction Manual, AISC Design Guide 1 (Base Plate and Anchor Rod Design)</td><td>EN 1993-1-8 (Eurocode 3, joints); BS 5950 on older UK-based specifications</td></tr>
<tr><td>Anchor bolt material</td><td>ASTM F1554 Grades 36, 55, 105</td><td>ISO 898-1 property classes 8.8, 10.9</td></tr>
<tr><td>Hot-dip galvanising</td><td>ASTM A153 (hardware), ASTM A123 (structural)</td><td>ISO 1461</td></tr>
<tr><td>Non-shrink grout</td><td>ASTM C1107</td><td>Per project specification</td></tr>
<tr><td>Fresh concrete (slump)</td><td>ASTM C143</td><td>BS EN 12350</td></tr>
<tr><td>Hardened concrete (cubes / cylinders)</td><td>ASTM C39</td><td>BS EN 12390</td></tr>
<tr><td>Ready-mix specification and delivery</td><td>ASTM C94</td><td>BS EN 206</td></tr>
<tr><td>Soil in-place density</td><td>ASTM D1556 (sand cone)</td><td>Per project specification</td></tr>
<tr><td>Quality management</td><td>ACI 318 Chapter 26</td><td>ISO 9001</td></tr></table>
<h2>Two rules on site</h2>
<ul><li><strong>Do not mix systems on one bolt.</strong> A bolt is ASTM F1554 or ISO 898-1, not both. Match whichever system your drawings use.</li>
<li><strong>Rules of thumb are not code minimums.</strong> Embedment around 10 &times; diameter and edge distance around 5 &times; diameter are field rules; ACI 318 Chapter 17 or EN 1992-4 calculations for the actual load case govern.</li></ul>
<h2>Other national codes</h2>
<p>Many countries publish their own concrete and steel codes (for example CSA A23.3 and CSA S16 in Canada, IS 456 and IS 800 in India). The guide does not cover them; the site sequence and hold points are the same, and the numbers come from your project specification.</p>
""",
"faq": [
("Which standard covers anchor bolt grades?", "ASTM F1554 (Grades 36, 55, 105) in the American system; ISO 898-1 property classes such as 8.8 and 10.9 in the metric system."),
("Which code governs anchor design in concrete?", "ACI 318 Chapter 17 or EN 1992-4, depending on the project."),
("What is AISC Design Guide 1?", "The AISC design guide for base plates and anchor rods."),
("Which standard applies to non-shrink grout under base plates?", "ASTM C1107 (packaged dry, hydraulic-cement grout, non-shrink)."),
],
"related": ["astm-f1554-grades", "anchor-bolt-embedment-depth", "base-plate-non-shrink-grout"],
},
{
"slug": "anchor-bolts-for-civil-engineering-students",
"title": "Anchor bolts explained for civil engineering students",
"desc": "What anchor bolts do, the grades, the template method, the site sequence and the mistakes new engineers make, in one page for civil and structural engineering students.",
"chapter": None, "img": "p-contents",
"answer": "Anchor bolts are cast into the concrete foundation and connect it to the steel column's base plate. On site they are set with a template that matches the base plate, levelled and fixed before the pour, protected until erection, and checked at hold points. Design sets the grade, diameter and embedment; site execution decides whether the column will fit.",
"body": f"""
<p>University teaches you how to design a foundation. The site asks you to build one. Whether it is a warehouse, a pre-engineered building, a transmission tower or a car-park shade, the anchor bolts are the silent, permanent link between the concrete below and the steel above, and a 2 mm error is enough to stop the erection crew.</p>
<h2>The five things to know before your first site</h2>
<ol><li><strong>The drawings come first.</strong> Check the bolt plan against the latest issued-for-construction revision and the steel shop drawings. <a href="{BASE}/articles/steel-structure-foundation-sequence/">The full foundation sequence</a></li>
<li><strong>Grade and diameter are set by design.</strong> ASTM F1554 Grade 36, 55 or 105, or ISO 8.8 / 10.9. Measure every bolt with a caliper. <a href="{BASE}/articles/astm-f1554-grades/">Grades explained</a></li>
<li><strong>The template holds the pattern.</strong> Same holes, diameter, spacing and arrangement as the base plate, with a centre nail on the survey point. <a href="{BASE}/articles/anchor-bolt-template/">Template method</a></li>
<li><strong>Tolerances are small.</strong> <a href="{BASE}/articles/anchor-bolt-tolerances/">Typical tolerances</a> for position, spacing, projection and level.</li>
<li><strong>Nothing is poured without a signature.</strong> <a href="{BASE}/articles/qa-qc-hold-points-steel-structure-foundations/">The 10 QA/QC hold points</a></li></ol>
<h2>Mistakes new engineers make</h2>
<ul><li>Setting out from the formwork instead of survey control.</li>
<li>Approving a shortcut on the spot to be polite. <a href="{BASE}/articles/first-day-on-site-new-engineer/">Your first site as a new engineer</a></li>
<li>Bending or heating a misaligned bolt instead of asking the structural engineer. <a href="{BASE}/articles/misaligned-anchor-bolts/">The right corrections</a></li></ul>
<h2>For a thesis, a report or an interview</h2>
<p>The <a href="{BASE}/articles/anchor-bolt-foundation-standards-codes/">standards table</a> lists which code covers what, and the <a href="{BASE}/articles/anchor-bolt-interview-questions-qa-qc/">interview questions page</a> has short answers to the questions site and QA/QC interviews ask.</p>
""",
"faq": [
("What is an anchor bolt in a steel structure?", "A bolt cast into the concrete foundation that connects it to the steel column's base plate."),
("Do civil engineering students learn anchor bolt installation?", "Courses usually cover design; site execution (template, setting out, hold points, fixes) is learned on site or from field guides and training."),
("What is the most important tool for setting anchor bolts?", "The anchor bolt template, drilled to match the column base plate."),
],
"related": ["first-day-on-site-new-engineer", "anchor-bolt-interview-questions-qa-qc", "steel-structure-foundation-sequence"],
},
{
"slug": "anchor-bolt-interview-questions-qa-qc",
"title": "Anchor bolt and foundation interview questions for site and QA/QC engineers (with answers)",
"desc": "15 questions asked in site engineer and QA/QC engineer interviews on anchor bolts, templates, grades, hold points, concrete tests and field fixes, with short field answers.",
"chapter": None, "img": "p-troubleshooting",
"answer": "Interviews for site and QA/QC roles on steel-structure projects test the template method, ASTM F1554 grades, tolerances and corrections for misaligned bolts, the pre-pour final gate, cube testing and who approves field fixes. The short answers below come from the field guide.",
"body": """
<p>Use these to prepare, then explain each answer with an example from your own site. Interviewers listen for the sequence and for who has authority to approve.</p>
<h2>Questions and short answers</h2>
<ol>
<li><strong>What is an anchor bolt template for?</strong> It holds the bolt group in the base plate's exact pattern during the pour, and is kept to drill the base plates.</li>
<li><strong>What are the ASTM F1554 grades?</strong> Grade 36 (250 MPa yield), 55 (380 MPa), 105 (720 MPa).</li>
<li><strong>Can a bolt be specified as both F1554 and ISO 8.8?</strong> No. They are separate systems; follow the drawings.</li>
<li><strong>How do you verify bolt diameter?</strong> With a caliper, on every bolt, yourself. 22 mm and 24 mm look identical by eye.</li>
<li><strong>Where do you set out anchor bolts from?</strong> Survey control and offset pegs, never from the formwork.</li>
<li><strong>Bolts are 4 mm out after casting. What do you do?</strong> Check the base plate first: holes are normally oversized (bolt diameter + 3-6 mm).</li>
<li><strong>And 10 mm out?</strong> Consult the structural engineer; slotted holes with thick hardened plate washers may be permitted.</li>
<li><strong>And 20 mm out?</strong> Do not bend the bolts. With the structural engineer's approval, cut them and install post-installed anchors next to them.</li>
<li><strong>Can you heat a bolt to bend it into place?</strong> Not without the structural engineer's approval; bending and heating reduce capacity.</li>
<li><strong>What is the final gate?</strong> The pre-concrete inspection of bolts, rebar, formwork, levels and cleanliness, signed by the consultant or client. No signature, no pour.</li>
<li><strong>Blow or wash first?</strong> Blow out debris with compressed air, then wash. Washing first makes mud.</li>
<li><strong>How do you protect threads during the pour?</strong> Masking tape or caps, then caps and marking until erection.</li>
<li><strong>How many cubes per sample, and when are they broken?</strong> Typically 3, at 7, 14 and 28 days (BS EN 12390), per project specification.</li>
<li><strong>The 28-day result is low. What do you do?</strong> Notify the designer immediately. The designer decides on re-check, cores or strengthening.</li>
<li><strong>Which grout goes under base plates?</strong> Non-shrink grout to ASTM C1107; for gaps over 50 mm, a coarse-aggregate or epoxy grout.</li>
</ol>
""",
"faq": [
("What do QA/QC interviews ask about anchor bolts?", "Template method, grades, tolerances, corrections for misaligned bolts, the pre-pour final gate, cube testing, and who approves field fixes."),
("What should you never do with a misaligned anchor bolt?", "Bend or heat it without the structural engineer's approval."),
("Who approves anchor bolt field fixes?", "The structural engineer."),
],
"related": ["qa-qc-hold-points-steel-structure-foundations", "misaligned-anchor-bolts", "anchor-bolts-for-civil-engineering-students"],
},

{"slug": "steel-structure-inspection-checklist", "chapter": None, "src": "Steel inspection reference note &middot; the guide itself covers the foundation stage", "img": "p-qaqc",
"title": "Steel structure inspection checklist for QA/QC inspectors (receiving to final bolting)",
"desc": "Steel structure inspection in 6 stages: anchor-bolt survey, material receiving, erection, bolting, welding and coatings, with the standard and the record for each.",
"answer": "A steel-structure inspection runs in six stages: as-built survey of the anchor bolts before erection, material receiving against mill certificates, erection and plumbness, bolting, welding, then coatings and touch-up. Each stage is checked against the project specification and the referenced standard, and each leaves a signed record.",
"body": f"""<p>Steel is inspected at every hand-over: from the foundation crew to the erector, from the fabricator to the site, and from the erector to the painter. A defect found at the right stage costs a phone call; found after the cladding is on, it costs a crane.</p>
<h2>The 6 stages</h2>
<table><tr><th>Stage</th><th>What the inspector checks</th><th>Typical reference</th><th>Record</th></tr>
<tr><td>1. Before erection</td><td>As-built survey of anchor-bolt positions, projection and top-of-grout levels</td><td>Project tolerances, AISC Code of Standard Practice</td><td>Anchor-bolt as-built survey</td></tr>
<tr><td>2. Material receiving</td><td>Grade, heat number, section size, marking, damage; mill certificates</td><td>ASTM A6 / EN 10204 type 3.1</td><td>Receiving report</td></tr>
<tr><td>3. Erection</td><td>Column plumbness, alignment, elevations, temporary bracing</td><td>AISC 303 / EN 1090-2</td><td>Erection survey</td></tr>
<tr><td>4. Bolting</td><td>Bolt grade, washers, snug-tight or pretension method</td><td>RCSC Specification / EN 1090-2</td><td>Bolting inspection log</td></tr>
<tr><td>5. Welding</td><td>Welder qualification, WPS, visual inspection, NDT as specified</td><td>AWS D1.1 / ISO 5817 / CSA W59</td><td>Weld inspection and NDT reports</td></tr>
<tr><td>6. Coatings</td><td>Surface preparation, dry film thickness, galvanizing damage repair</td><td>SSPC / ISO 8501-1 / ISO 19840 / ISO 1461</td><td>Coating inspection report</td></tr></table>
<h2>Start with the foundation</h2>
<p>Most erection problems begin at the anchor bolts. Before the first column arrives, survey every bolt group: position, projection above concrete and thread condition. A bolt that is 20 mm out is a fix on paper today and a problem with a column hanging on the crane tomorrow. The guide's <a href="{BASE}/articles/pre-pour-checklist/">pre-pour checklist</a> and <a href="{BASE}/articles/anchor-bolt-tolerances/">tolerance table</a> cover that stage.</p>
<h2>What governs</h2>
<p>The project specification and the inspection and test plan (ITP) govern. The standards in the table are the common references; the project names the ones that apply and the acceptance criteria.</p>""",
"faq": [("What are the stages of steel structure inspection?", "Anchor-bolt survey before erection, material receiving, erection and plumbness, bolting, welding, and coatings."),
        ("Which standard governs steel erection inspection?", "The project specification. Common references are the AISC Code of Standard Practice (AISC 303) in North America and EN 1090-2 in Europe."),
        ("Why survey anchor bolts before steel erection?", "Because misplaced bolts are cheapest to correct before a column is lifted, and the correction must be approved by the structural engineer.")],
"related": ["high-strength-bolt-tightening-inspection", "structural-welding-visual-inspection", "steel-erection-tolerances-plumbness"]},

{"slug": "high-strength-bolt-tightening-inspection", "chapter": None, "src": "Steel inspection reference note &middot; the guide itself covers the foundation stage", "img": "p-standards",
"title": "High-strength bolt tightening inspection: snug-tight, turn-of-nut, DTI and TC bolts",
"desc": "How QA/QC inspectors check structural bolting: snug-tight vs pretensioned joints, turn-of-nut rotation, calibrated wrench, DTI washers and twist-off bolts (RCSC, ASTM F3125).",
"answer": "First confirm the joint type on the drawings: snug-tight, pretensioned or slip-critical. Pretensioned joints are tightened by one of four methods (turn-of-nut, calibrated wrench, twist-off tension-control bolts or direct tension indicators), and the inspector verifies the method with a pre-installation check on site, not by torquing finished bolts at random.",
"body": f"""<h2>Three joint types</h2>
<ul><li><strong>Snug-tight:</strong> plies in firm contact, tightened by a few impacts of an impact wrench or the full effort of an ironworker with an ordinary spud wrench.</li>
<li><strong>Pretensioned:</strong> bolts brought to a minimum tension by an approved method.</li>
<li><strong>Slip-critical:</strong> pretensioned, plus faying surfaces prepared to the specified slip class (no paint or galvanizing unless qualified).</li></ul>
<h2>Four pretensioning methods (RCSC Specification)</h2>
<table><tr><th>Method</th><th>What the inspector watches</th></tr>
<tr><td>Turn-of-nut</td><td>Snug first, match-mark nut and bolt, then the specified rotation (1/3 turn for bolt length up to 4 diameters, 1/2 turn over 4 to 8, 2/3 turn over 8 to 12, for faces normal to the axis)</td></tr>
<tr><td>Calibrated wrench</td><td>Daily calibration with a tension calibrator (Skidmore-Wilhelm) for each lot, diameter and length</td></tr>
<tr><td>Twist-off (TC) bolts</td><td>Spline sheared off; bolts pre-checked in the tension calibrator</td></tr>
<tr><td>Direct tension indicator (DTI)</td><td>Feeler-gauge refusals in the specified number of gaps</td></tr></table>
<h2>Material checks before any bolting</h2>
<p>Bolt grade marking (ASTM F3125 Grade A325 or A490, or ISO property class 8.8 / 10.9 under EN 14399), nut and washer grades, galvanized or plain as specified, and storage: bolts kept dry and lubricated, not left loose in the rain.</p>
<h2>Common mistakes</h2>
<ul><li>Checking torque on finished bolts as the acceptance test.</li><li>Reusing pretensioned A490 or galvanized bolts.</li><li>Tightening from the edges of a large joint inwards instead of from the stiffest part outwards.</li></ul>
<p>Anchor rods in the foundation are a different item: they are usually snug-tight unless the drawings say otherwise. See <a href="{BASE}/articles/astm-f1554-grades/">ASTM F1554 grades</a>.</p>""",
"faq": [("What is the turn-of-nut method?", "The bolt is first snug-tightened, nut and bolt are match-marked, then the nut is rotated a specified amount depending on bolt length, for example 1/3 turn for lengths up to 4 diameters."),
        ("Can you check pretension with a torque wrench after installation?", "Not as the acceptance test. The RCSC approach is a pre-installation verification of the method, then routine observation that the method is followed."),
        ("Can A490 bolts be reused?", "No. A490 bolts and galvanized A325 bolts must not be reused once pretensioned.")],
"related": ["steel-structure-inspection-checklist", "structural-welding-visual-inspection", "astm-f1554-grades"]},

{"slug": "structural-welding-visual-inspection", "chapter": None, "src": "Steel inspection reference note &middot; the guide itself covers the foundation stage", "img": "p-qaqc",
"title": "Structural welding visual inspection: defects, NDT methods and AWS D1.1 / ISO 5817",
"desc": "What a welding inspector checks on structural steel before, during and after welding: WPS, welder qualification, cracks, undercut, porosity, and when MT, UT, PT or RT is used.",
"answer": "Visual inspection is done before, during and after welding. Before: WPS, welder qualification, fit-up and cleanliness. During: preheat, interpass temperature and consumables. After: weld size and profile, cracks, undercut, porosity, overlap and incomplete fusion. NDT (MT, PT, UT or RT) is added where the specification requires it.",
"body": f"""<h2>Before welding</h2><ul><li>Approved welding procedure specification (WPS) for the joint and position.</li><li>Welder qualification valid for the process and position.</li><li>Fit-up: root opening, bevel angle, alignment, backing.</li><li>Joint clean and dry; consumables stored as specified (low-hydrogen electrodes kept in an oven).</li></ul>
<h2>During welding</h2><ul><li>Preheat and interpass temperature measured.</li><li>Settings within the WPS range.</li><li>Cleaning between passes; back-gouging where required.</li></ul>
<h2>After welding: visual defects</h2>
<table><tr><th>Defect</th><th>What it looks like</th></tr>
<tr><td>Crack</td><td>Any crack is rejected under the common codes</td></tr>
<tr><td>Undercut</td><td>Groove melted into the base metal at the toe</td></tr>
<tr><td>Porosity</td><td>Gas pores on the surface</td></tr>
<tr><td>Overlap</td><td>Weld metal rolled onto the base metal without fusion</td></tr>
<tr><td>Incomplete fusion or penetration</td><td>Lack of bond with base metal or root</td></tr>
<tr><td>Undersize or excessive convexity</td><td>Fillet size measured with a weld gauge</td></tr></table>
<p>Acceptance limits come from the code the project names: AWS D1.1 (USA), CSA W59 (Canada) or the quality level of ISO 5817 called by EN 1090-2 (Europe).</p>
<h2>NDT methods</h2>
<ul><li><strong>MT</strong> (magnetic particle): surface and near-surface cracks in ferromagnetic steel.</li><li><strong>PT</strong> (dye penetrant): surface-breaking defects.</li><li><strong>UT</strong> (ultrasonic): internal defects in full-penetration welds.</li><li><strong>RT</strong> (radiography): internal defects, less common on site.</li></ul>""",
"faq": [("What does a welding inspector check?", "WPS and welder qualification before welding, preheat and parameters during welding, and size, profile and defects after welding, plus NDT when specified."),
        ("Which standard sets weld acceptance on structural steel?", "AWS D1.1 in the USA, CSA W59 in Canada, and ISO 5817 quality levels under EN 1090-2 in Europe, as named by the project."),
        ("What is the difference between MT and UT?", "MT finds surface and near-surface cracks; UT finds internal defects in full-penetration welds.")],
"related": ["steel-structure-inspection-checklist", "steel-inspector-certifications", "high-strength-bolt-tightening-inspection"]},

{"slug": "steel-erection-tolerances-plumbness", "chapter": None, "src": "Steel inspection reference note &middot; the guide itself covers the foundation stage", "img": "p-standards",
"title": "Steel erection tolerances: column plumbness, base plates and anchor bolts",
"desc": "Steel erection tolerances for QA/QC inspectors: column out-of-plumb 1/500 (AISC 303), base plate and anchor-bolt checks, and how the foundation tolerances feed the erection survey.",
"answer": "Under the AISC Code of Standard Practice (AISC 303), an individual column may be out of plumb by no more than 1/500 of its height between working points. EN 1090-2 sets its own erection tolerances. Erection accuracy starts at the foundation: anchor-bolt position and top-of-grout level must be within tolerance before the column is set.",
"body": f"""<h2>What the erection survey checks</h2>
<ul><li>Column plumbness at each level against 1/500 (AISC 303) or the EN 1090-2 limit the project names.</li><li>Column base position against grid lines.</li><li>Base plate elevation and full bearing on grout.</li><li>Beam elevations and alignment.</li></ul>
<h2>Why the foundation decides</h2>
<p>The erector can shim and plumb a column only within the play allowed by the base-plate holes. If the bolts are out of tolerance, the column cannot be set where the drawing shows it. That is why the guide treats the <a href="{BASE}/articles/anchor-bolt-tolerances/">anchor-bolt tolerances</a> and the <a href="{BASE}/articles/pre-pour-checklist/">pre-pour gate</a> as the start of the steel tolerance chain.</p>
<h2>Base plates and grout</h2>
<p>Columns are set on levelling nuts or shims, plumbed, then grouted with non-shrink grout. Check grout fill under the whole plate before final loading. See <a href="{BASE}/articles/base-plate-non-shrink-grout/">base plate grouting</a>.</p>""",
"faq": [("What is the column plumbness tolerance in AISC 303?", "An individual column may be out of plumb by up to 1/500 of the distance between working points, with additional limits for exterior and elevator columns."),
        ("Where do steel erection tolerances start?", "At the foundation: anchor-bolt position, projection and top-of-grout level."),
        ("Which European standard covers steel erection tolerances?", "EN 1090-2.")],
"related": ["anchor-bolt-tolerances", "steel-structure-inspection-checklist", "misaligned-anchor-bolts"]},

{"slug": "steel-coating-galvanizing-inspection", "chapter": None, "src": "Steel inspection reference note &middot; the guide itself covers the foundation stage", "img": "p-qaqc",
"title": "Steel coating and galvanizing inspection: surface preparation, DFT and repair",
"desc": "Coating inspection on structural steel: blast cleaning grade (Sa 2½, SSPC-SP 10), dry film thickness measurement (SSPC-PA 2, ISO 19840), galvanizing (ASTM A123, ISO 1461) and touch-up.",
"answer": "Coating inspection checks four things: surface preparation grade and profile before painting, ambient conditions (dew point), dry film thickness with a calibrated gauge to SSPC-PA 2 or ISO 19840, and repair of damage after erection. Galvanized steel is checked for coating thickness to ASTM A123 or ISO 1461, and damaged areas are repaired as the project specifies.",
"body": f"""<h2>Before painting</h2><ul><li>Surface preparation grade: for example Sa 2½ (ISO 8501-1) or SSPC-SP 10 near-white blast.</li><li>Surface profile measured with replica tape or a profile gauge.</li><li>Steel temperature at least 3 &deg;C above the dew point (common rule in coating specifications).</li></ul>
<h2>Dry film thickness (DFT)</h2>
<p>Measured with a calibrated magnetic gauge. SSPC-PA 2 sets the number and location of readings in North America. ISO 19840 is often used with an acceptance rule that no more than 20% of readings fall below nominal and none below 80% of nominal, unless the specification says otherwise.</p>
<h2>Galvanizing</h2><ul><li>Coating thickness against ASTM A123 or ISO 1461 tables for the steel thickness.</li><li>No bare spots, dross or flux inclusions.</li><li>Damaged areas repaired with zinc-rich paint or another method the specification accepts (ASTM A780 in the USA).</li></ul>
<p>Galvanized anchor rods follow ASTM F2329 / A153; check that nuts were tapped oversize after galvanizing so they run freely.</p>""",
"faq": [("What is Sa 2½?", "A near-white blast-cleaning grade defined in ISO 8501-1, equivalent in practice to SSPC-SP 10."),
        ("How is dry film thickness measured?", "With a calibrated magnetic gauge, following SSPC-PA 2 or ISO 19840 for the number of readings and acceptance."),
        ("How is damaged galvanizing repaired?", "With zinc-rich paint, zinc spray or solder as the specification allows; ASTM A780 covers repair methods in the USA.")],
"related": ["steel-structure-inspection-checklist", "steel-material-receiving-mill-certificates", "anchor-bolt-foundation-standards-codes"]},

{"slug": "steel-material-receiving-mill-certificates", "chapter": None, "src": "Steel inspection reference note &middot; the guide itself covers the foundation stage", "img": "p-standards",
"title": "Steel material receiving inspection and mill test certificates (EN 10204 3.1)",
"desc": "How to receive structural steel, bolts and anchor rods on site: check the mill test certificate, heat number traceability, grade marking, dimensions and damage.",
"answer": "Match every delivery to its mill test certificate: grade, heat number, chemical composition and mechanical results must match the specification, and the heat number on the piece must match the certificate. Then check marking, dimensions, straightness and damage, and quarantine anything that does not match.",
"body": f"""<h2>Receiving checklist</h2>
<ol><li>Delivery note matches the order and the drawing marks.</li><li>Mill test certificate (EN 10204 type 3.1 where specified) for each heat.</li><li>Heat number on the steel matches the certificate.</li><li>Grade meets the specification (for example ASTM A992, A572 Gr 50 or EN 10025 S355).</li><li>Section size and plate thickness checked with a tape and calliper.</li><li>No bends, dents, lamination or coating damage from transport.</li><li>Bolts, nuts and washers: grade markings, lot numbers, certificates.</li><li>Anchor rods: grade colour code (ASTM F1554 Grade 36 blue, 55 yellow, 105 red), thread length, galvanizing.</li></ol>
<h2>What to do with a mismatch</h2>
<p>Tag it, keep it apart, and write a non-conformance report. Do not install material without a matching certificate.</p>
<p>The same check applies to reinforcement before it goes into the foundation: <a href="{BASE}/articles/qa-qc-hold-points-steel-structure-foundations/">hold point 5</a>.</p>""",
"faq": [("What is an EN 10204 3.1 certificate?", "An inspection certificate issued by the manufacturer's authorized inspector, independent of production, with actual test results for the delivered product."),
        ("What is the colour code for ASTM F1554 anchor rods?", "Grade 36 blue, Grade 55 yellow, Grade 105 red, on the end of the rod."),
        ("What if the heat number does not match the certificate?", "Quarantine the material and raise a non-conformance report; do not install it.")],
"related": ["astm-f1554-grades", "steel-structure-inspection-checklist", "steel-coating-galvanizing-inspection"]},

{"slug": "steel-inspector-certifications", "chapter": None, "src": "Steel inspection reference note &middot; the guide itself covers the foundation stage", "img": "p-contents",
"title": "Steel structure and welding inspector certifications: CWI, CSWIP 3.1, CWB, ASNT, AMPP",
"desc": "Which certifications QA/QC inspectors and engineering graduates pursue for steel structures worldwide: AWS CWI, CSWIP 3.1, CWB/CSA W178.2, ASNT NDT, AMPP coating inspector, ISO 9001 auditor.",
"answer": "The main credentials are AWS CWI (USA and many international projects), CSWIP 3.1 Welding Inspector (UK, Middle East, Asia), CWB inspector certification to CSA W178.2 (Canada), ASNT or ISO 9712 NDT levels for testing, and the AMPP (formerly NACE) Coating Inspector Program. The right one depends on where you work and which code the projects use.",
"body": f"""<table><tr><th>Credential</th><th>Body</th><th>Where it is common</th></tr>
<tr><td>Certified Welding Inspector (CWI)</td><td>American Welding Society</td><td>USA, AWS D1.1 projects worldwide</td></tr>
<tr><td>CSWIP 3.1 Welding Inspector</td><td>TWI Certification</td><td>UK, Gulf, Asia</td></tr>
<tr><td>Welding inspector (CSA W178.2)</td><td>Canadian Welding Bureau</td><td>Canada</td></tr>
<tr><td>NDT Level II / III</td><td>ASNT or ISO 9712 schemes</td><td>Worldwide, method by method</td></tr>
<tr><td>Coating Inspector Program</td><td>AMPP (formerly NACE)</td><td>Oil and gas, industrial, worldwide</td></tr>
<tr><td>ISO 9001 internal or lead auditor</td><td>Various training bodies</td><td>Quality systems</td></tr></table>
<h2>What certifications do not cover</h2>
<p>None of these teach the foundation stage: survey, anchor-bolt setting, pre-pour hold points and concrete testing. Most steel problems on site start there. That gap is what the <a href="{BASE}/">Anchor Bolt Field Guide</a> and the <a href="{BASE}/training/">workshop</a> cover.</p>
<p>Preparing for an interview? See <a href="{BASE}/articles/anchor-bolt-interview-questions-qa-qc/">15 QA/QC interview questions</a>.</p>""",
"faq": [("What certification does a steel structure inspector need?", "It depends on the region and code: AWS CWI, CSWIP 3.1, CWB/CSA W178.2 in Canada, plus NDT or coating certifications for those tasks."),
        ("Is CSWIP 3.1 equivalent to AWS CWI?", "Both certify welding inspectors; CSWIP 3.1 is more common on UK and Gulf projects and CWI on AWS D1.1 projects. Employers decide which they accept."),
        ("What is AMPP?", "The Association for Materials Protection and Performance, formed from NACE International and SSPC; it runs the Coating Inspector Program.")],
"related": ["structural-welding-visual-inspection", "anchor-bolt-interview-questions-qa-qc", "anchor-bolts-for-civil-engineering-students"]},

{"slug": "anchor-bolt-survey-before-steel-erection", "chapter": 14, "img": "p-troubleshooting",
"title": "Anchor bolt survey before steel erection: projection, position and thread checks",
"desc": "The as-built anchor-bolt survey before the steel erector arrives: projection above concrete (+25 / -6 mm per the guide's table), group position, spacing, top elevation and threads.",
"answer": "Before erection, survey every bolt group after the concrete has set: group position against the grid, spacing within the group, top-of-bolt elevation, projection above concrete and thread condition. The guide's table allows +25 / -6 mm on projection (per the detail). Record the results and send out-of-tolerance bolts to the structural engineer before the steel arrives.",
"body": f"""<h2>What to measure on each group</h2>
<table><tr><th>Check</th><th>How</th></tr>
<tr><td>Group position against grid lines</td><td>Total station or tape from control lines</td></tr>
<tr><td>Spacing between bolts in the group</td><td>Tape, against the base-plate hole pattern</td></tr>
<tr><td>Top-of-bolt elevation</td><td>Level from the benchmark</td></tr>
<tr><td>Projection above concrete</td><td>Tape: enough thread for washer, nut and full engagement</td></tr>
<tr><td>Threads and verticality</td><td>Run a nut on by hand; check with a square</td></tr></table>
<h2>Why projection matters</h2>
<p>Too short and the nut cannot fully engage; too long and the bolt may bottom out in the column or interfere with the finish. Projection is set on the template by the levelling nuts before the pour; see the <a href="{BASE}/articles/anchor-bolt-template/">template article</a>.</p>
<h2>What happens with a bad bolt</h2>
<p>It goes back to the structural engineer. Common approved fixes are in <a href="{BASE}/articles/misaligned-anchor-bolts/">misaligned anchor bolts</a>; heating, bending or cutting without approval is not one of them.</p>""",
"faq": [("What is the anchor bolt projection tolerance?", "The guide's table gives +25 mm / -6 mm for projection above concrete, per the detail; the project drawings govern."),
        ("When should anchor bolts be surveyed?", "After the concrete sets and before the steel erector mobilises, so fixes can be approved in time."),
        ("Who approves a fix for an out-of-tolerance anchor bolt?", "The structural engineer.")],
"related": ["anchor-bolt-tolerances", "steel-erection-tolerances-plumbness", "misaligned-anchor-bolts"]},
]

AUDIENCES = [
    ("For steel structure and welding inspectors", ["steel-structure-inspection-checklist", "anchor-bolt-survey-before-steel-erection", "steel-material-receiving-mill-certificates",
     "high-strength-bolt-tightening-inspection", "structural-welding-visual-inspection", "steel-erection-tolerances-plumbness", "steel-coating-galvanizing-inspection", "steel-inspector-certifications"]),
    ("For QA/QC engineers and inspectors", ["qa-qc-hold-points-steel-structure-foundations", "pre-pour-checklist", "concrete-testing-foundations-slump-cubes",
     "anchor-bolt-tolerances", "anchor-bolt-failures-common-causes", "anchor-bolt-interview-questions-qa-qc"]),
    ("For engineering students and new graduates", ["anchor-bolts-for-civil-engineering-students", "first-day-on-site-new-engineer", "steel-structure-foundation-sequence",
     "anchor-bolt-foundation-standards-codes", "astm-f1554-grades", "anchor-bolt-interview-questions-qa-qc"]),
]
