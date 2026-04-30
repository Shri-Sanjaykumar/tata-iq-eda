import docx

def replace_text_in_paragraph(paragraph, old_text, new_text):
    if old_text in paragraph.text:
        # Simplest way: replace the whole text of the paragraph if we don't care about formatting too much
        # But to keep some formatting we can replace within runs if possible
        # However, for simplicity, we'll just rewrite the paragraph text if a placeholder is found
        paragraph.text = paragraph.text.replace(old_text, new_text)

docx_path = r"C:\Users\Priya\OneDrive\Documents\tata\EDA_SummaryReport_Template.docx"
out_path = r"C:\Users\Priya\.gemini\antigravity\scratch\tata_iq_eda\EDA_SummaryReport.docx"

doc = docx.Document(docx_path)

replacements = {
    "[Insert purpose and goal(s) of the report.]": "The purpose of this report is to conduct an Exploratory Data Analysis (EDA) on Geldium's dataset to assess its structure, completeness, and key attributes. The goal is to identify missing values and risk indicators to ensure the data is reliable for predictive modeling of delinquency.",
    "[Insert count]": "500",
    "[List key columns and descriptions]": "Customer_ID, Age, Income, Credit_Score, Credit_Utilization, Missed_Payments, Delinquent_Account, Loan_Balance, Debt_to_Income_Ratio, Employment_Status, Account_Tenure, Credit_Card_Type, Location, Month_1 to Month_6.",
    "[Categorical, Numerical, etc.]": "Numerical (Age, Income, Credit_Score, Credit_Utilization, Missed_Payments, Loan_Balance, Debt_to_Income_Ratio, Account_Tenure), Categorical (Customer_ID, Delinquent_Account, Employment_Status, Credit_Card_Type, Location, Month_1 to Month_6)",
    "[List affected columns]": "Income (39 missing), Loan_Balance (29 missing), Credit_Score (2 missing)",
    "[Deletion, Imputation, Synthetic Data, etc.]": "Imputation: Median imputation will be used for Income and Loan_Balance to minimize the effect of outliers. For Credit_Score, median imputation is also applied since the missing volume is extremely low (0.4%).",
    "[Summarize findings]": "High Credit Utilization is strongly linked to missed payments. Furthermore, recent late or missed payments in Month 1 to Month 6 represent a significant behavioral indicator of future delinquency.",
    "[Highlight data points requiring further investigation]": "The Credit_Score column ranges from 398 to 500, indicating an internal or normalized scoring system rather than a standard FICO score. Additionally, Month_1 to Month_6 values are categorical and will require numeric encoding.",
    "[Summarize key findings and outline the recommended next steps.]": "The dataset is of relatively high quality with minimal missing values. After imputing the missing Income and Loan_Balance fields, and encoding the categorical payment history columns, the dataset will be well-prepared for training predictive models. The next step is to engineer sequential features from the 6-month payment history and proceed to model selection."
}

for para in doc.paragraphs:
    for old, new in replacements.items():
        if old in para.text:
            para.text = para.text.replace(old, new)

doc.save(out_path)
print("Saved filled docx to:", out_path)
