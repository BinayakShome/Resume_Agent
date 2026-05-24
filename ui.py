from flask import Flask, render_template, request, jsonify
from google.genai import types
import json
import app  # Your app.py handling extraction
import prompt  # Your prompt.py containing the prompt

flask_app = Flask(__name__)


@flask_app.route('/')
def home():
    return render_template('index.html')


@flask_app.route('/analyze', methods=['POST'])
def analyze():
    role = request.form.get('role')
    uploaded_file = request.files.get('resume')

    # Check extension and extract text using your app.py functions
    if uploaded_file.filename.endswith('.pdf'):
        text = app.extract_text(uploaded_file)
    else:
        text = app.extract_text_from_docx(uploaded_file)

    # Compile template and request content from Gemini
    full_prompt = prompt.PROMPT_TEMPLATE.format(JOB_ROLE=role, resume_text=text)

    response = app.client.models.generate_content(
        model="gemini-2.5-flash",
        contents=full_prompt,
        config=types.GenerateContentConfig(response_mime_type="application/json")
    )

    # Parse and safely return json directly to the webpage view
    try:
        data = json.loads(response.text)
    except json.JSONDecodeError:
        data = {"ats_score": 0, "overall_summary": "Error parsing output", "critical_missing_skills": [],
                "suggested_bullet_point_improvements": []}

    return jsonify(data)


if __name__ == '__main__':
    flask_app.run(debug=True)