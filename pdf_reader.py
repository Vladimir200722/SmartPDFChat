import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_file) -> str:
    """
    Liest ein PDF (File-Like-Objekt) und gibt den gesamten Text zurück.
    """
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    full_text = ""
    for page in doc:
        full_text += page.get_text()
    return full_text
