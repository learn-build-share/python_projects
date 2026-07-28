import pdfplumber
from docx import Document

def extract_pdf(file):
    """
    Parameter
        file

    Argument
        uploaded pdf
    """

    text = ""

    with pdfplumber.open(file) as pdf:

        for page in pdf.pages:

            text += page.extract_text()

    return text

def extract_docx(file):

    document = Document(file)

    text = ""

    for para in document.paragraphs:

        text += para.text

    return text

def extract_text(file):

    if file.name.endswith(".pdf"):

        return extract_pdf(file)

    else:

        return extract_docx(file)