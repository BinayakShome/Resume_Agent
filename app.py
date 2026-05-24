from google import genai
import fitz
import docx
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

client = genai.Client(api_key= API_KEY)

def extract_text(uploaded_file):
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def extract_text_from_docx(uploaded_file):
    doc = docx.Document(uploaded_file)
    return "\n".join([para.text for para in doc.paragraphs])