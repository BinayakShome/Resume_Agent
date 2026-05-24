# 🚀 Resume Checker (ATS Optimization Agent)

A full-stack, automated AI agent that acts as an expert applicant tracking system (ATS). Users can upload their resumes in PDF or DOCX format, select a target industry, and receive an instantaneous ATS score breakdown along with clear, context-aware suggestions to improve their bullet points.

**🔗 Live Demo:** [Resume agent on Render](https://resume-checker-fshg.onrender.com)

---

## 🛠️ Tech Stack & Architecture

The system is split cleanly into a lightweight, non-blocking asynchronous frontend and an event-driven Python backend:

* **Frontend:** Pure HTML5, Modern Semantic CSS3 (Dark Mode Theme), and Vanilla JavaScript (`Fetch API` for asynchronous background processing).
* **Backend Framework:** Flask (WSGI Web Server Application).
* **AI Engine:** Google Gemini 2.5 Flash API via the official `google-genai` SDK.
* **Data Parsing:** `PyMuPDF (fitz)` for robust layout text extraction from PDFs and `python-docx` for parsing Microsoft Word files.
* **Production Deployment:** Gunicorn HTTP Server hosted on Render with Automated Continuous Deployment (CD).

---

## ✨ Features

* **Zero-Page-Reload Experience:** The frontend communicates with the Flask server natively using JSON payloads, providing a smooth user experience while the AI evaluates data.
* **Strict Structural Intelligence:** Leverages Gemini's structured output capabilities (`response_mime_type="application/json"`) to securely feed structural dictionaries straight to client-side renders without crashing.
* **Contextual Semantic Analysis:** Instead of matching primitive keywords, the AI agent interprets high-level technical concepts, action-verb impacts, and metric-driven points.

---

## 🚀 Getting Started Locally

Follow these steps to spin up the project on your local environment.

### 1. Clone the Repository
```bash
git clone [https://github.com/BinayakShome/Resume_Agent.git](https://github.com/BinayakShome/Resume_Agent.git)
cd Resume_Agent
