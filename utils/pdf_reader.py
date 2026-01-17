import pdfplumber


def extract_text_from_pdf(file):
    """
    Extracts text from an uploaded PDF file.

    Parameters:
    file : file-like object (UploadedFile from Streamlit or file path)

    Returns:
    str : extracted text
    """
    text = ""

    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

    return text
