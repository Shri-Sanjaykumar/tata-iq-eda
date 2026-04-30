import docx

docx_path = r"C:\Users\Priya\OneDrive\Documents\tata\Task 2_ModelPlan_Template.docx"

doc = docx.Document(docx_path)
for para in doc.paragraphs:
    if para.text.strip():
        print(para.text)
