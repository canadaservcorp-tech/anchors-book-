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
