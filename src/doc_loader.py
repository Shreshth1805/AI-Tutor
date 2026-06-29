from pypdf import PdfReader
import docx2txt

def load_file(file_path):
    if file_path.endswith(".pdf"):
        pdf=PdfReader(file_path)
        text=""
        for page in pdf.pages:
            text+=page.extract_text()
        return text
    elif file_path.endswith(".docx"):
        return docx2txt.process(file_path)
    elif file_path.endswith(".txt"):
        with open(file_path,'r',encoding='utf-8') as file:
            return file.read()
    return ""
            