import os
import pdfplumber
from docx import Document

def extract_text_from_file(file_path):
    """
    Detects file extension and extracts plain text from PDF or DOCX files.
    """
    ext = os.path.splitext(file_path)[1].lower()
    text = ""
    
    try:
        if ext == '.pdf':
            with pdfplumber.open(file_path) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"
        elif ext in ['.docx', '.doc']:
            doc = Document(file_path)
            for para in doc.paragraphs:
                if para.text.strip():
                    text += para.text + "\n"
    except Exception as e:
        print(f"Error parsing file: {e}")
        
    return text.strip()