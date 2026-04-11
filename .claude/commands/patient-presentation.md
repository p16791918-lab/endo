You are assisting a Korean medical student (intern) who needs to prepare a virtual patient case presentation.

The department or disease to present is: **$ARGUMENTS**

Your job is to:
1. Design a realistic virtual patient case for **$ARGUMENTS**
2. Write a Python script using `python-pptx` to generate an actual `.pptx` PowerPoint file
3. Execute the script using the Bash tool to create the file
4. Output the Korean presentation script as text

---

## STEP 1: Design the Case

Internally plan a realistic, educational virtual patient case with:
- Realistic demographics (age, sex)
- Typical chief complaint for the disease
- Logical HPI → PE → Labs → Diagnosis → Treatment flow
- Common risk factors and comorbidities
- Representative lab values and imaging findings

---

## STEP 2: Generate the PowerPoint File

Write and execute a Python script that creates a `.pptx` file with **12 slides** using `python-pptx`.

**File output path:** `/home/user/endo/case_$ARGUMENTS.pptx`
(Replace spaces in $ARGUMENTS with underscores)

### Slide Design Requirements:
- Use a clean, professional medical presentation style
- Background: white or very light gray (RGB 245, 245, 245)
- Title text: dark navy (RGB 31, 73, 125) — bold, 28–32pt
- Body text: dark gray (RGB 50, 50, 50) — 16–20pt
- Accent color for important values: red (RGB 192, 0, 0)
- Slide size: widescreen 16:9 (13.33 × 7.5 inches)
- Each slide must have: a colored title bar at top, content area below

### 12 Required Slides:

1. **Title Slide** — Case title, department, "Medical Student Case Presentation", date
2. **Patient Information** — Age, sex, CC, date of admission
3. **History of Present Illness** — OLDCARTS table or timeline bullets
4. **PMH / FH / SH** — Three columns or sections
5. **Review of Systems** — Table: System | Positive | Negative
6. **Physical Examination** — Vital signs table + systematic exam findings
7. **Laboratory & Imaging** — Key lab values in table (highlight abnormals in red), imaging findings
8. **Problem List & Assessment** — Numbered list + assessment paragraph
9. **Differential Diagnosis** — Table: Diagnosis | For | Against
10. **Final Diagnosis** — Confirmed diagnosis + criteria met + classification/staging
11. **Treatment Plan** — Non-pharm / Pharm table + follow-up
12. **Discussion & Key Takeaways** — 3–5 bullet points with clinical pearls

### Python Script Guidelines:
- Use `python-pptx` library
- For each slide: add a filled rectangle as title bar (navy, top strip), add title text, add body content
- Use `add_textbox` for flexible layout
- For tables: use `add_table` with proper column widths
- Bold abnormal lab values; use red font for critical values
- Keep bullet points concise — keywords and numbers only, not full sentences
- All slide content in **English**

After writing the script, execute it with the Bash tool and confirm the file was created.

---

## STEP 3: Output the Korean Presentation Script

After the file is created, output a Korean-language presentation script for each slide.

Format:
### [Slide N] 대본
[3–6 sentences in formal Korean (합쇼체)]

Guidelines:
- Natural transitions between slides
- Explain clinical reasoning (not just reading the slide)
- Highlight significance of key findings

---

## STEP 4: Output Expected Q&A

List 5 attending-physician questions with model answers in Korean.

**Q[N]: [Question]**
A: [Concise, clinically accurate answer]

---

Make the case representative of a typical teaching hospital presentation in Korea. Ensure clinical logic flows: history → exam → labs → diagnosis → treatment.
