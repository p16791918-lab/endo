from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches, Pt
import copy

# Colors
NAVY = RGBColor(31, 73, 125)
WHITE = RGBColor(255, 255, 255)
DARK_GRAY = RGBColor(50, 50, 50)
RED = RGBColor(192, 0, 0)
LIGHT_BG = RGBColor(245, 247, 250)
LIGHT_NAVY = RGBColor(214, 227, 243)

prs = Presentation()
prs.slide_width = Inches(13.33)
prs.slide_height = Inches(7.5)

blank_layout = prs.slide_layouts[6]  # blank


def add_slide():
    return prs.slides.add_slide(blank_layout)


def add_bg(slide, color=LIGHT_BG):
    bg = slide.shapes.add_shape(1, 0, 0, prs.slide_width, prs.slide_height)
    bg.fill.solid()
    bg.fill.fore_color.rgb = color
    bg.line.fill.background()


def add_title_bar(slide, title_text):
    bar = slide.shapes.add_shape(1, 0, 0, prs.slide_width, Inches(1.1))
    bar.fill.solid()
    bar.fill.fore_color.rgb = NAVY
    bar.line.fill.background()
    tf = bar.text_frame
    tf.word_wrap = False
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.LEFT
    run = p.add_run()
    run.text = title_text
    run.font.bold = True
    run.font.size = Pt(28)
    run.font.color.rgb = WHITE
    tf.margin_left = Inches(0.3)
    tf.margin_top = Inches(0.15)


def add_textbox(slide, text, left, top, width, height,
                font_size=16, bold=False, color=DARK_GRAY,
                align=PP_ALIGN.LEFT, wrap=True):
    txBox = slide.shapes.add_textbox(left, top, width, height)
    tf = txBox.text_frame
    tf.word_wrap = wrap
    p = tf.paragraphs[0]
    p.alignment = align
    run = p.add_run()
    run.text = text
    run.font.size = Pt(font_size)
    run.font.bold = bold
    run.font.color.rgb = color
    return txBox


def add_bullets(slide, items, left, top, width, height, font_size=15):
    txBox = slide.shapes.add_textbox(left, top, width, height)
    tf = txBox.text_frame
    tf.word_wrap = True
    first = True
    for item in items:
        if first:
            p = tf.paragraphs[0]
            first = False
        else:
            p = tf.add_paragraph()
        p.level = item.get('level', 0)
        run = p.add_run()
        run.text = item['text']
        run.font.size = Pt(item.get('size', font_size))
        run.font.bold = item.get('bold', False)
        run.font.color.rgb = item.get('color', DARK_GRAY)
        p.space_after = Pt(4)


def add_table(slide, headers, rows, left, top, width, col_widths=None):
    rows_count = len(rows) + 1
    cols_count = len(headers)
    table = slide.shapes.add_table(rows_count, cols_count, left, top, width, Inches(0.35 * rows_count + 0.35)).table

    if col_widths:
        for i, w in enumerate(col_widths):
            table.columns[i].width = Inches(w)

    # Header row
    for i, h in enumerate(headers):
        cell = table.cell(0, i)
        cell.fill.solid()
        cell.fill.fore_color.rgb = NAVY
        p = cell.text_frame.paragraphs[0]
        run = p.add_run()
        run.text = h
        run.font.bold = True
        run.font.size = Pt(13)
        run.font.color.rgb = WHITE
        p.alignment = PP_ALIGN.CENTER

    # Data rows
    for ri, row in enumerate(rows):
        for ci, val in enumerate(row):
            cell = table.cell(ri + 1, ci)
            if (ri + 1) % 2 == 0:
                cell.fill.solid()
                cell.fill.fore_color.rgb = LIGHT_NAVY
            p = cell.text_frame.paragraphs[0]
            run = p.add_run()
            is_abnormal = val.get('abnormal', False) if isinstance(val, dict) else False
            text = val['text'] if isinstance(val, dict) else str(val)
            run.text = text
            run.font.size = Pt(13)
            run.font.color.rgb = RED if is_abnormal else DARK_GRAY
            run.font.bold = is_abnormal
            p.alignment = PP_ALIGN.CENTER


# ─────────────────────────────────────────────
# SLIDE 1: Title
# ─────────────────────────────────────────────
s = add_slide()
# Full navy background for title slide
bg = s.shapes.add_shape(1, 0, 0, prs.slide_width, prs.slide_height)
bg.fill.solid(); bg.fill.fore_color.rgb = NAVY; bg.line.fill.background()

# White accent bar
accent = s.shapes.add_shape(1, 0, Inches(3.0), prs.slide_width, Inches(0.08))
accent.fill.solid(); accent.fill.fore_color.rgb = WHITE; accent.line.fill.background()

add_textbox(s, "A Case of ST-Elevation Myocardial Infarction", Inches(0.5), Inches(1.5),
            Inches(12.3), Inches(1.2), font_size=36, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
add_textbox(s, "(STEMI — Anterior Wall, LAD Occlusion)", Inches(0.5), Inches(2.5),
            Inches(12.3), Inches(0.6), font_size=22, bold=False, color=LIGHT_NAVY, align=PP_ALIGN.CENTER)
add_textbox(s, "Department of Cardiology / Internal Medicine", Inches(0.5), Inches(3.3),
            Inches(12.3), Inches(0.5), font_size=18, color=WHITE, align=PP_ALIGN.CENTER)
add_textbox(s, "Medical Student Case Presentation  |  April 2026", Inches(0.5), Inches(3.9),
            Inches(12.3), Inches(0.5), font_size=16, color=LIGHT_NAVY, align=PP_ALIGN.CENTER)

# ─────────────────────────────────────────────
# SLIDE 2: Patient Information
# ─────────────────────────────────────────────
s = add_slide()
add_bg(s)
add_title_bar(s, "Patient Information")

add_table(s,
    ["Field", "Details"],
    [
        ["Age / Sex", "62 y/o Male"],
        ["Chief Complaint (CC)", "Sudden onset crushing chest pain — 2 hours"],
        ["Date of Visit", "Emergency admission via 119 ambulance"],
        ["Triage Level", {"text": "ESI Level 1 (Immediate)", "abnormal": True}],
        ["Vital on Arrival", {"text": "BP 158/96 | HR 102 | SpO2 94% (RA)", "abnormal": True}],
    ],
    Inches(0.5), Inches(1.3), Inches(12.3),
    col_widths=[3.5, 8.8]
)

# ─────────────────────────────────────────────
# SLIDE 3: HPI
# ─────────────────────────────────────────────
s = add_slide()
add_bg(s)
add_title_bar(s, "History of Present Illness (HPI)")

add_bullets(s, [
    {'text': 'Timeline', 'bold': True, 'size': 16, 'color': NAVY},
    {'text': '1 week prior: exertional chest discomfort (ignored)', 'level': 1},
    {'text': '2 hours prior to arrival: sudden onset substernal chest pain at rest', 'level': 1},
    {'text': 'Progressive worsening — not relieved by position or rest', 'level': 1},
    {'text': '', 'size': 8},
    {'text': 'OLDCARTS', 'bold': True, 'size': 16, 'color': NAVY},
], Inches(0.5), Inches(1.2), Inches(5.5), Inches(5.8))

add_table(s,
    ["Feature", "Description"],
    [
        ["Onset", "Sudden, at rest"],
        ["Location", "Substernal / precordial"],
        ["Duration", {"text": "~2 hours, persistent", "abnormal": True}],
        ["Character", {"text": "Crushing, pressure-like", "abnormal": True}],
        ["Radiation", {"text": "Left arm, jaw", "abnormal": True}],
        ["Severity", {"text": "9/10", "abnormal": True}],
        ["Associated Sx", "Diaphoresis, nausea, dyspnea, lightheadedness"],
    ],
    Inches(6.2), Inches(1.2), Inches(6.8),
    col_widths=[2.2, 4.6]
)

# ─────────────────────────────────────────────
# SLIDE 4: PMH / FH / SH
# ─────────────────────────────────────────────
s = add_slide()
add_bg(s)
add_title_bar(s, "Past Medical / Family / Social History")

add_bullets(s, [
    {'text': 'Past Medical History', 'bold': True, 'size': 16, 'color': NAVY},
    {'text': 'Hypertension (10 yrs) — Amlodipine 5mg QD', 'level': 1},
    {'text': 'T2DM (7 yrs) — Metformin 1000mg BID', 'level': 1},
    {'text': 'Hyperlipidemia (5 yrs) — Rosuvastatin 10mg (poor compliance)', 'level': 1},
    {'text': 'No prior cardiac Hx, no prior surgeries', 'level': 1},
    {'text': 'NKDA', 'level': 1},
    {'text': '', 'size': 6},
    {'text': 'Family History', 'bold': True, 'size': 16, 'color': NAVY},
    {'text': 'Father: MI at 55 y/o → deceased', 'level': 1, 'color': RED},
    {'text': 'Brother: CAD, s/p PCI at 58 y/o', 'level': 1, 'color': RED},
    {'text': '', 'size': 6},
    {'text': 'Social History', 'bold': True, 'size': 16, 'color': NAVY},
    {'text': 'Smoking: 30 pack-years (current)', 'level': 1, 'color': RED},
    {'text': 'Alcohol: 3–4 drinks/week', 'level': 1},
    {'text': 'Occupation: office worker; lives with wife', 'level': 1},
], Inches(0.5), Inches(1.2), Inches(12.5), Inches(6.0))

# ─────────────────────────────────────────────
# SLIDE 5: ROS
# ─────────────────────────────────────────────
s = add_slide()
add_bg(s)
add_title_bar(s, "Review of Systems (ROS)")

add_table(s,
    ["System", "Positive (+)", "Negative (−)"],
    [
        ["Constitutional", {"text": "Diaphoresis, fatigue (1 wk)", "abnormal": True}, "No fever, no weight loss"],
        ["HEENT", "—", "Unremarkable"],
        ["Cardiovascular", {"text": "Chest pain, exertional dyspnea", "abnormal": True}, "No palpitations, no syncope"],
        ["Pulmonary", {"text": "Dyspnea", "abnormal": True}, "No cough, no hemoptysis"],
        ["GI", {"text": "Nausea", "abnormal": True}, "No vomiting, no abd pain"],
        ["GU", "—", "Unremarkable"],
        ["MSK", "—", "Unremarkable"],
        ["Neuro", {"text": "Lightheadedness", "abnormal": True}, "No syncope, no focal deficit"],
        ["Skin", "—", "Unremarkable"],
    ],
    Inches(0.5), Inches(1.2), Inches(12.3),
    col_widths=[2.2, 4.5, 5.6]
)

# ─────────────────────────────────────────────
# SLIDE 6: Physical Exam
# ─────────────────────────────────────────────
s = add_slide()
add_bg(s)
add_title_bar(s, "Physical Examination")

add_table(s,
    ["BP", "HR", "RR", "Temp", "SpO2"],
    [[
        {"text": "158/96 mmHg", "abnormal": True},
        {"text": "102 bpm", "abnormal": True},
        {"text": "22/min", "abnormal": True},
        "36.8 °C",
        {"text": "94% (RA)", "abnormal": True},
    ]],
    Inches(0.5), Inches(1.2), Inches(12.3),
    col_widths=[2.8, 2.2, 2.2, 2.2, 2.9]
)

add_table(s,
    ["System", "Findings"],
    [
        ["General", {"text": "Acute distress, diaphoretic, pale, clutching chest", "abnormal": True}],
        ["HEENT / Neck", "No JVD, no carotid bruit"],
        ["Chest / Lungs", {"text": "Bilateral basal crackles (mild)", "abnormal": True}],
        ["Heart", {"text": "Tachycardic; S3 gallop; no murmur", "abnormal": True}],
        ["Abdomen", "Soft, non-tender, no organomegaly"],
        ["Extremities", "No edema; distal pulses 2+ bilaterally"],
        ["Neuro", "Alert & oriented ×3; no focal deficits"],
    ],
    Inches(0.5), Inches(2.45), Inches(12.3),
    col_widths=[2.8, 9.5]
)

# ─────────────────────────────────────────────
# SLIDE 7: Labs & Imaging
# ─────────────────────────────────────────────
s = add_slide()
add_bg(s)
add_title_bar(s, "Laboratory & Imaging Results")

add_table(s,
    ["Lab", "Result", "Ref", ""],
    [
        ["Troponin I", {"text": "18.4 ng/mL", "abnormal": True}, "<0.04", {"text": "↑↑↑", "abnormal": True}],
        ["CK-MB", {"text": "98 U/L", "abnormal": True}, "<25", {"text": "↑↑", "abnormal": True}],
        ["BNP", {"text": "420 pg/mL", "abnormal": True}, "<100", {"text": "↑", "abnormal": True}],
        ["WBC", {"text": "13.2 ×10³/μL", "abnormal": True}, "4–10", "↑"],
        ["Glucose", {"text": "198 mg/dL", "abnormal": True}, "70–100", "↑"],
        ["LDL", {"text": "168 mg/dL", "abnormal": True}, "<100", "↑"],
        ["HDL", {"text": "32 mg/dL", "abnormal": True}, ">40", "↓"],
        ["Cr", "1.1 mg/dL", "0.7–1.2", "WNL"],
    ],
    Inches(0.5), Inches(1.2), Inches(6.2),
    col_widths=[2.0, 2.0, 1.3, 0.9]
)

add_bullets(s, [
    {'text': '12-Lead ECG', 'bold': True, 'size': 15, 'color': NAVY},
    {'text': 'ST elevation 2–4mm in V1–V4', 'level': 1, 'color': RED, 'bold': True},
    {'text': 'Reciprocal ST depression in II, III, aVF', 'level': 1},
    {'text': 'Q waves developing in V1–V2', 'level': 1},
    {'text': '→ Anterior STEMI (LAD territory)', 'level': 1, 'color': RED, 'bold': True},
    {'text': '', 'size': 6},
    {'text': 'Chest X-Ray', 'bold': True, 'size': 15, 'color': NAVY},
    {'text': 'Mild cardiomegaly', 'level': 1},
    {'text': 'Pulmonary vascular congestion', 'level': 1, 'color': RED},
    {'text': 'Early interstitial edema', 'level': 1, 'color': RED},
    {'text': 'No PTX, no pleural effusion', 'level': 1},
], Inches(6.6), Inches(1.2), Inches(6.3), Inches(5.5))

# ─────────────────────────────────────────────
# SLIDE 8: Problem List & Assessment
# ─────────────────────────────────────────────
s = add_slide()
add_bg(s)
add_title_bar(s, "Problem List & Assessment")

add_bullets(s, [
    {'text': 'Problem List', 'bold': True, 'size': 17, 'color': NAVY},
    {'text': '1.  Anterior STEMI — LAD occlusion (PRIMARY)', 'level': 1, 'color': RED, 'bold': True, 'size': 15},
    {'text': '2.  Acute heart failure — Killip Class II', 'level': 1, 'color': RED, 'size': 15},
    {'text': '3.  Uncontrolled hypertension', 'level': 1, 'size': 15},
    {'text': '4.  Uncontrolled T2DM (glucose 198)', 'level': 1, 'size': 15},
    {'text': '5.  Hyperlipidemia (non-compliant)', 'level': 1, 'size': 15},
    {'text': '6.  Active smoker — 30 pack-years', 'level': 1, 'size': 15},
], Inches(0.5), Inches(1.2), Inches(12.3), Inches(3.2))

# Assessment box
box = s.shapes.add_shape(1, Inches(0.5), Inches(4.6), Inches(12.3), Inches(2.4))
box.fill.solid(); box.fill.fore_color.rgb = LIGHT_NAVY; box.line.color.rgb = NAVY

tf = box.text_frame; tf.word_wrap = True
tf.margin_left = Inches(0.15); tf.margin_top = Inches(0.1)
p = tf.paragraphs[0]
run = p.add_run(); run.text = "Assessment"
run.font.bold = True; run.font.size = Pt(15); run.font.color.rgb = NAVY

p2 = tf.add_paragraph()
run2 = p2.add_run()
run2.text = ("62 y/o male with HTN, T2DM, hyperlipidemia, 30 pack-year smoking history, and strong family "
             "history of CAD, presenting with 2-hour crushing substernal chest pain radiating to left arm with "
             "diaphoresis, ST elevation V1–V4, and markedly elevated troponin I (18.4 ng/mL), "
             "consistent with anterior STEMI secondary to acute LAD occlusion.")
run2.font.size = Pt(13); run2.font.color.rgb = DARK_GRAY

# ─────────────────────────────────────────────
# SLIDE 9: Differential Diagnosis
# ─────────────────────────────────────────────
s = add_slide()
add_bg(s)
add_title_bar(s, "Differential Diagnosis")

add_table(s,
    ["Diagnosis", "Supporting Evidence", "Against"],
    [
        [{"text": "Anterior STEMI ✓", "abnormal": True},
         "ST↑ V1–V4, Trop↑↑↑, crushing CP, diaphoresis, risk factors",
         "—"],
        ["Aortic Dissection",
         "Severe CP, hypertension",
         "No tearing quality, no pulse differential, normal mediastinum on CXR"],
        ["Pulmonary Embolism",
         "Dyspnea, tachycardia, SpO2↓",
         "No pleuritic pain, no DVT, ECG = ST↑ not S1Q3T3"],
        ["NSTEMI / UA",
         "Chest pain, troponin rise",
         "ST elevation present → rules out NSTEMI by definition"],
        ["Takotsubo CMP",
         "Anterior wall motion abnormality",
         "Male sex, no acute emotional stressor, classic risk factor profile"],
    ],
    Inches(0.5), Inches(1.2), Inches(12.3),
    col_widths=[2.8, 4.5, 5.0]
)

# ─────────────────────────────────────────────
# SLIDE 10: Final Diagnosis
# ─────────────────────────────────────────────
s = add_slide()
add_bg(s)
add_title_bar(s, "Final Diagnosis")

add_bullets(s, [
    {'text': 'Anterior ST-Elevation Myocardial Infarction (Anterior STEMI)', 'bold': True, 'size': 22, 'color': RED},
    {'text': 'Culprit Vessel: LAD (proximal occlusion)', 'bold': True, 'size': 17, 'color': NAVY},
    {'text': '', 'size': 8},
    {'text': 'Diagnostic Criteria Met (ACC/AHA Universal Definition of MI)', 'bold': True, 'size': 16, 'color': NAVY},
    {'text': '✅  Ischemic symptoms > 20 minutes', 'level': 1, 'size': 15},
    {'text': '✅  New ST elevation ≥ 2mm in V1–V4 (≥2 contiguous leads)', 'level': 1, 'size': 15},
    {'text': '✅  Troponin I 18.4 ng/mL (> 450× upper limit of normal)', 'level': 1, 'size': 15},
    {'text': '✅  Anterior wall hypokinesia on echocardiogram', 'level': 1, 'size': 15},
    {'text': '', 'size': 8},
    {'text': 'Classification', 'bold': True, 'size': 16, 'color': NAVY},
    {'text': 'Killip Class II  (S3 gallop + basal crackles)', 'level': 1, 'size': 15},
    {'text': 'TIMI Risk Score: 6/14  →  High Risk', 'level': 1, 'size': 15, 'color': RED},
    {'text': 'Type 1 MI (Spontaneous — atherosclerotic plaque rupture)', 'level': 1, 'size': 15},
], Inches(0.5), Inches(1.2), Inches(12.3), Inches(6.0))

# ─────────────────────────────────────────────
# SLIDE 11: Treatment Plan
# ─────────────────────────────────────────────
s = add_slide()
add_bg(s)
add_title_bar(s, "Treatment Plan")

add_bullets(s, [
    {'text': 'Acute / Emergency', 'bold': True, 'size': 15, 'color': RED},
    {'text': 'Primary PCI — LAD stent (DES)  |  Door-to-balloon target: < 90 min', 'level': 1, 'size': 13, 'bold': True},
    {'text': 'O2 supplementation (target SpO2 ≥ 95%)', 'level': 1, 'size': 13},
    {'text': 'IV access × 2, cardiac monitoring, 12-lead serial ECG', 'level': 1, 'size': 13},
], Inches(0.5), Inches(1.2), Inches(12.3), Inches(1.6))

add_table(s,
    ["Drug", "Dose", "Route", "Indication"],
    [
        [{"text": "Aspirin", "abnormal": False}, "300mg load → 100mg QD", "PO", "Antiplatelet"],
        ["Clopidogrel", "600mg load → 75mg QD", "PO", "DAPT (×12 mo)"],
        ["Heparin UFH", "60 U/kg bolus → infusion", "IV", "Anticoagulation"],
        ["Metoprolol succinate", "25mg QD → uptitrate", "PO", "Beta-blocker"],
        ["Ramipril", "2.5mg QD → uptitrate", "PO", "ACEi (EF↓, HTN)"],
        [{"text": "Rosuvastatin", "abnormal": False}, "20mg QD", "PO", "High-intensity statin"],
    ],
    Inches(0.5), Inches(2.85), Inches(12.3),
    col_widths=[2.8, 3.5, 1.5, 4.5]
)

add_bullets(s, [
    {'text': 'Non-pharm / Follow-up', 'bold': True, 'size': 14, 'color': NAVY},
    {'text': 'Low-Na/low-fat diet  |  Smoking cessation  |  Cardiac rehab referral', 'level': 1, 'size': 13},
    {'text': 'Echo at 4–6 wks  |  Outpatient cardiology at 2 wks  |  Lipid + HbA1c at 6 wks', 'level': 1, 'size': 13},
], Inches(0.5), Inches(6.2), Inches(12.3), Inches(1.1))

# ─────────────────────────────────────────────
# SLIDE 12: Discussion & Key Takeaways
# ─────────────────────────────────────────────
s = add_slide()
add_bg(s)
add_title_bar(s, "Discussion & Key Takeaways")

add_bullets(s, [
    {'text': '"Time is Muscle"', 'bold': True, 'size': 17, 'color': RED},
    {'text': 'Door-to-balloon < 90 min is the #1 determinant of outcome in STEMI', 'level': 1, 'size': 14},
    {'text': 'Every 30-min delay ≈ 7.5% increase in 1-year mortality', 'level': 1, 'size': 14},
    {'text': '', 'size': 6},
    {'text': 'Killip Classification guides acute HF management', 'bold': True, 'size': 17, 'color': NAVY},
    {'text': 'Class I: No HF  |  Class II: S3/crackles  |  Class III: Pulm edema  |  Class IV: Cardiogenic shock', 'level': 1, 'size': 13},
    {'text': '', 'size': 6},
    {'text': 'DAPT Duration Post-DES: 12 months minimum', 'bold': True, 'size': 17, 'color': NAVY},
    {'text': 'Aspirin + P2Y12 inhibitor (prefer ticagrelor > clopidogrel per guidelines)', 'level': 1, 'size': 13},
    {'text': '', 'size': 6},
    {'text': 'ACEi / ARB mandatory when EF < 40% post-MI', 'bold': True, 'size': 17, 'color': NAVY},
    {'text': 'Reduces ventricular remodeling and mortality (SAVE, AIRE trials)', 'level': 1, 'size': 13},
    {'text': '', 'size': 6},
    {'text': 'Secondary Prevention = as important as acute therapy', 'bold': True, 'size': 17, 'color': NAVY},
    {'text': 'Statin (LDL<70) + BP control + DM mgmt + smoking cessation + cardiac rehab → ↓50% recurrence', 'level': 1, 'size': 13},
], Inches(0.5), Inches(1.2), Inches(12.3), Inches(6.0))

# ─────────────────────────────────────────────
# Save
# ─────────────────────────────────────────────
output_path = "/home/user/endo/case_MI.pptx"
prs.save(output_path)
print(f"Saved: {output_path}")
