You are assisting a Korean medical student (intern) who needs to prepare a virtual patient case presentation using **Canva**.

The department or disease to present is: **$ARGUMENTS**

Your job is to:
1. Design a realistic virtual patient case for **$ARGUMENTS**
2. Create a Canva presentation using the Canva MCP tools
3. Output the Korean presentation script as text
4. Output expected Q&A

---

## STEP 1: Design the Case

Internally plan a realistic, educational virtual patient case with:
- Realistic demographics (age, sex)
- Typical chief complaint for the disease
- Logical HPI → PE → Labs → Diagnosis → Treatment flow
- Common risk factors and comorbidities
- Representative lab values and imaging findings

---

## STEP 2: Create the Canva Presentation

### 2-A. Request Outline Review (MANDATORY FIRST STEP)

Call the `request-outline-review` MCP tool with the following parameters:

- **topic:** `"Virtual Patient Case: $ARGUMENTS — Medical Student Presentation"`
- **audience:** `"educational"`
- **style:** `"elegant"`
- **length:** `"comprehensive"`
- **pages:** an array of exactly 12 slide objects

The 12 slides must be:

1. **Title Slide**
   - Title: `"[Disease/Dept] — Virtual Patient Case"`
   - Description: Patient case overview with department, presentation type ("Medical Student Case Presentation"), and today's date. Introduce the case with a one-sentence clinical hook.

2. **Patient Information**
   - Title: `"Patient Overview"`
   - Description: Age, sex, chief complaint, date/mode of admission. Include occupation and relevant social context.

3. **History of Present Illness**
   - Title: `"History of Present Illness"`
   - Description: Chronological narrative using OLDCARTS framework: Onset, Location, Duration, Character, Aggravating/Alleviating factors, Radiation, Timing, Severity. Include relevant associated symptoms.

4. **Past Medical / Family / Social History**
   - Title: `"PMH / FH / SH"`
   - Description: Past medical and surgical history, current medications, allergies. Family history of related conditions. Social history: smoking, alcohol, occupation, exercise.

5. **Review of Systems**
   - Title: `"Review of Systems"`
   - Description: Systematic review organized by organ system. Clearly list pertinent positives and pertinent negatives for each system relevant to the case.

6. **Physical Examination**
   - Title: `"Physical Examination"`
   - Description: Vital signs (BP, HR, RR, Temp, SpO2, BMI). Systematic examination findings from head to toe. Highlight pertinent positives with clinical significance.

7. **Laboratory & Imaging Findings**
   - Title: `"Labs & Imaging"`
   - Description: Key laboratory values including CBC, BMP, and disease-specific markers. Clearly flag abnormal values. Imaging findings with interpretation (CXR, CT, US, or relevant modality).

8. **Problem List & Assessment**
   - Title: `"Problem List & Assessment"`
   - Description: Numbered active problem list. Clinical assessment paragraph synthesizing history, exam, and labs to explain why this presentation fits the working diagnosis.

9. **Differential Diagnosis**
   - Title: `"Differential Diagnosis"`
   - Description: Top 3–4 differential diagnoses. For each: supporting evidence from the case, and evidence against. Explain clinical reasoning for prioritization.

10. **Final Diagnosis**
    - Title: `"Final Diagnosis"`
    - Description: Confirmed diagnosis with full name. Diagnostic criteria met in this patient. Classification or staging if applicable (e.g., AHA/ACC staging, TNM, GOLD, etc.).

11. **Treatment Plan**
    - Title: `"Treatment Plan"`
    - Description: Non-pharmacological measures. Pharmacological treatment with drug names, doses, and rationale. Follow-up plan and monitoring parameters.

12. **Discussion & Key Takeaways**
    - Title: `"Discussion & Key Takeaways"`
    - Description: 3–5 clinical pearls specific to this case. Teaching points about pathophysiology, diagnostic approach, or management. One memorable summary sentence.

Wait for the user to review and approve the outline in the Canva widget before proceeding.

---

### 2-B. Generate the Design (ONLY after outline is approved)

After the user approves the outline, call `generate-design-structured` with:
- The exact same `topic`, `audience`, `style`, `length`, and `presentation_outlines` from the approved outline
- `design_type`: `"presentation"`

Then call `create-design-from-candidate` with the `job_id` and `candidate_id` from the generation result to convert it into an editable Canva design.

Present the resulting Canva design URL to the user so they can open and edit it directly.

---

### 2-C. Optional Export

Offer to export the design as PPTX using the `export-design` MCP tool with `format.type: "pptx"`, so the user has a local file as well.

---

## STEP 3: Output the Korean Presentation Script

After the design is created, output a Korean-language presentation script for each slide.

Format:
### [Slide N] 대본
[3–6 sentences in formal Korean (합쇼체)]

Guidelines:
- Natural transitions between slides
- Explain clinical reasoning (not just reading the slide)
- Highlight significance of key findings
- Use appropriate medical Korean terminology

---

## STEP 4: Output Expected Q&A

List 5 attending-physician questions with model answers in Korean.

**Q[N]: [Question]**
A: [Concise, clinically accurate answer in formal Korean]

---

Make the case representative of a typical teaching hospital presentation in Korea. Ensure clinical logic flows: history → exam → labs → diagnosis → treatment.
