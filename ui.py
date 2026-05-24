import streamlit as st
from google.genai import types
import json
import app
import prompt

st.title("AI Resume Agent")
role = st.selectbox("Select Target Industry",
                    ["Software Engineer", "Data Scientist", "Product Manager", "Backend Developer", "Android Developer",
                     "ML engineer", "Fintech", "Edtech", "Sales(Non - tech)"])
uploaded_file = st.file_uploader("Upload your Resume", type=["pdf", "docx"])

if uploaded_file and st.button("Analyze Resume"):
    with st.spinner("Agent is analyzing..."):
        # 1. Extraction
        if uploaded_file.type == "application/pdf":
            text = app.extract_text(uploaded_file)
        else:
            # Assuming you named your docx function extract_text_from_docx in app.py
            text = app.extract_text_from_docx(uploaded_file)

        # 2. AI Reasoning
        full_prompt = prompt.PROMPT_TEMPLATE.format(JOB_ROLE=role, resume_text=text)
        response = app.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=full_prompt,
            config=types.GenerateContentConfig(response_mime_type="application/json")
        )

        # 3. Display Results safely using json.loads()
        try:
            data = json.loads(response.text)

            # Display Score Metric
            st.metric("ATS Match Score", f"{data.get('ats_score', 0)}%")

            # Display Summary & Missing Skills
            st.subheader("Overall Summary")
            st.write(data.get('overall_summary', 'No summary provided.'))

            st.subheader("Critical Missing Skills")
            missing_skills = data.get('critical_missing_skills', [])
            if missing_skills:
                st.write(", ".join(missing_skills))
            else:
                st.success("No glaring skill gaps found!")

            # Display Suggested Changes
            st.subheader("Suggested Changes")
            suggestions = data.get('suggested_bullet_point_improvements', [])
            if suggestions:
                for suggestion in suggestions:
                    st.write(f"**Original:** {suggestion.get('original')}")
                    st.success(f"**Improved:** {suggestion.get('improved')}")
                    st.markdown("---")
            else:
                st.info("No explicit bullet point edits suggested.")

        except json.JSONDecodeError:
            st.error("Failed to parse the AI response into clean JSON data.")
            st.text("Raw Response from AI:")
            st.text(response.text)
