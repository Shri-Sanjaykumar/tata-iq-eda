import docx
from PyPDF2 import PdfReader

docx_path = r"C:\Users\Priya\OneDrive\Documents\tata\EDA_SummaryReport_Template.docx"
pdf_path = r"C:\Users\Priya\OneDrive\Documents\tata\Updated_Dataset_Description_Guide.pdf"

print("DOCX Content:\n")
doc = docx.Document(docx_path)
for para in doc.paragraphs:
    if para.text.strip():
        print(para.text)

print("\n----------------------\n")

print("PDF Content:\n")
reader = PdfReader(pdf_path)
for page in reader.pages:
    print(page.extract_text())
