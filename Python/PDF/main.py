import os

from PyPDF2 import PdfFileReader

def extract_information(path:str):
    if not os.path.exists(path):
        raise FileNotFoundError
    if not os.path.isfile(path):
        raise FileExistsError

    with open(path, "rb") as f:
        pdf = PdfFileReader(f)
        info = pdf.getDocumentInfo()
    print(info)
    return info
)