You are assisting a Korean medical student (intern) who needs to prepare a virtual patient case presentation.

The department or disease to present is: **$ARGUMENTS**

Your job is to:
1. Design a realistic virtual patient case for **$ARGUMENTS**
2. Write a Python script using `python-pptx` to generate a `.pptx` file, then execute it
3. Output the Korean presentation script as text
4. Output expected Q&A

---

## STEP 1: Design the Case

Internally plan a realistic, educational virtual patient case with:
- Realistic demographics (age, sex, Korean name)
- Typical chief complaint for the disease
- Logical HPI → PE → Labs → Diagnosis → Treatment flow
- Common risk factors and comorbidities
- Representative lab values and imaging findings

---

## STEP 2: Generate the PowerPoint File

Write a complete Python script and execute it with the Bash tool.

**File output path:** `/home/user/endo/case_$ARGUMENTS.pptx`
(Replace spaces in $ARGUMENTS with underscores)

First check/install python-pptx:
```bash
python3 -c "from pptx import Presentation" 2>/dev/null || pip install python-pptx -q
```

### Design Style (Canva-inspired, elegant medical):
- Slide size: 13.33 × 7.5 inches (16:9)
- Background: light gray RGB(245,245,245)
- Title bar: full-width navy rectangle RGB(31,73,125) at top, height ~1.1 in
- Title text: white, bold, 28–30pt, inside the title bar
- Body text: dark gray RGB(50,50,50), 14–16pt
- Abnormal lab values: red RGB(192,0,0), bold
- Tables: navy header row (white bold text), alternating row colors

### Helper functions to define once and reuse:
```python
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN

NAVY  = RGBColor(31,73,125)
WHITE = RGBColor(255,255,255)
DARK  = RGBColor(50,50,50)
RED   = RGBColor(192,0,0)
LGRAY = RGBColor(245,245,245)

def add_slide(prs): return prs.slides.add_slide(prs.slide_layouts[6])
def bg(slide, prs, color=LGRAY): ...   # full-slide background rectangle
def title_bar(slide, prs, text): ...   # navy bar + white title text
def body_box(slide, text, left, top, width, height, size=15, bold=False, color=DARK): ...
def add_table(slide, headers, rows, left, top, width, height, col_widths=None): ...
```

### 12 Required Slides:

1. **Title Slide** — Large navy band in center; disease name 40–44pt white bold; subtitle "Virtual Patient Case"; department + date; patient one-liner
2. **Patient Overview** — 2-column table: Item | Detail (name, age/sex, occupation, CC, admission date, referral reason)
3. **History of Present Illness** — OLDCARTS table: column 1 = framework item, column 2 = patient findings; include associated symptoms row
4. **PMH / FH / SH** — Three side-by-side columns with navy header bars: Past Medical Hx | Family Hx | Social Hx
5. **Review of Systems** — 3-column table: System | Pertinent Positives | Pertinent Negatives (7–8 systems)
6. **Physical Examination** — Top half: 4-column vitals table (Parameter|Value|Parameter|Value); Bottom half: System|Findings table
7. **Labs & Imaging** — Table: Test | Result | Reference | Interpretation; red+bold for abnormals; imaging summary below
8. **Problem List & Assessment** — Numbered problem table (#|Problem|Details) + shaded assessment paragraph box
9. **Differential Diagnosis** — Table: Diagnosis | Evidence FOR | Evidence AGAINST (4 diagnoses; top one marked ★)
10. **Final Diagnosis** — Central navy diagnosis banner; criteria table (#|Criterion|Patient Findings); severity classification row
11. **Treatment Plan** — Table: Category | Details (Non-Pharm, Drug 1, Drug 2, Definitive option 1, Definitive option 2, Follow-Up)
12. **Discussion & Key Takeaways** — Table: Pearl # | Clinical Pearl (5 pearls); navy summary banner at bottom

### Script rules:
- All content in **English**
- Write the entire script as one block; execute with Bash tool
- Bold + red font for any value containing ↑ ↓ HIGH LOW CRIT or known abnormal patterns
- Delete the script file after successful execution
- Print confirmation: `Saved: /home/user/endo/case_$ARGUMENTS.pptx`

After execution confirm the file exists with `ls -lh`.

---

## STEP 3: Output the Korean Presentation Script

After the file is created, output a Korean-language script for each slide.

Format:
### [Slide N] 대본
[3–6 sentences in formal Korean (합쇼체)]

Guidelines:
- Natural transitions between slides
- Explain clinical reasoning, not just reading slides
- Highlight significance of key findings
- Use proper medical Korean terminology

---

## STEP 4: Output Expected Q&A

List 5 attending-physician questions with model answers in Korean.

**Q[N]: [Question]**
A: [Concise, clinically accurate answer in formal Korean]

---

> **Canva import tip:** The generated `.pptx` can be imported directly into Canva via canva.com → Create a design → Import file. Canva will convert all slides automatically.

Make the case representative of a typical Korean teaching hospital presentation. Ensure clinical logic flows: history → exam → labs → diagnosis → treatment.
