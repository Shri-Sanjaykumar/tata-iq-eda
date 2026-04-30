import docx

docx_path = r"C:\Users\Priya\Downloads\Updated_Business_Summary_Report_Template.docx"

doc = docx.Document(docx_path)
for para in doc.paragraphs:
    if para.text.strip():
        print(para.text)
