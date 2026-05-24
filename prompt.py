# prompt.py

PROMPT_TEMPLATE = """
Role: You are an expert ATS (Applicant Tracking System) with 20 years of HR experience.
Task: Analyze the provided RESUME text against general industry standards for a {JOB_ROLE} position.

General Standards to Check:
1. Quantifiable Achievements: Did they use metrics (%, $, numbers)?
2. Action Verbs: Did they start bullets with "Developed", "Managed", "Optimized"?
3. Formatting: Is the structure logical (Summary -> Experience -> Skills -> Education)?
4. Keyword Density: Are core skills for {JOB_ROLE} present?

Return the response in this EXACT JSON structure:
{{
  "ats_score": 85,
  "critical_missing_skills": [],
  "formatting_critique": "",
  "suggested_bullet_point_improvements": [
      {{"original": "...", "improved": "..."}}
  ],
  "overall_summary": ""
}}

RESUME TEXT:
{resume_text}
"""