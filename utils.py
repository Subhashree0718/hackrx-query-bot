import os
import pdfplumber

def load_documents():
    texts = []
    folder = "data"
    for filename in os.listdir(folder):
        if filename.endswith(".pdf"):
            with pdfplumber.open(os.path.join(folder, filename)) as pdf:
                full_text = "\n".join(page.extract_text() or "" for page in pdf.pages)
                texts.append(full_text)
    return texts
