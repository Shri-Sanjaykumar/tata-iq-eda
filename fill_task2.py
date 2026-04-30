import docx

docx_path = r"C:\Users\Priya\OneDrive\Documents\tata\Task 2_ModelPlan_Template.docx"
out_path = r"C:\Users\Priya\.gemini\antigravity\scratch\tata_iq_eda\Task2_Predictive_Model_Plan.docx"

doc = docx.Document(docx_path)

logic_text = """[Insert GenAI model logic here]"""
justification_text = """[Insert your justification here]"""
evaluation_text = """[Insert your evaluation plan here]"""

new_logic = """Model Selected: Random Forest Classifier
Top 5 Input Features: Credit_Utilization, Missed_Payments, Payment_History (Months 1-6), Debt_to_Income_Ratio, and Loan_Balance.

Workflow / Pseudo-code:
1. Data Preprocessing: Impute missing Income and Loan_Balance using median values. Encode categorical features (Month_1 to Month_6 payment statuses).
2. Feature Selection: Focus on top behavioral indicators (Credit_Utilization, Debt_to_Income_Ratio, Missed_Payments).
3. Model Training: Train a Random Forest Classifier on historical data to learn patterns of default.
4. Prediction: The model outputs a probability score (0.0 to 1.0) for each customer. If the probability exceeds the risk threshold, the customer is flagged as "High Risk".

Summary: The model utilizes a Random Forest Classifier to ingest customer behavioral and financial data, processing it through an ensemble of decision trees to predict the likelihood of credit delinquency. It effectively transforms raw inputs into an actionable risk probability score."""

new_justification = """A Random Forest Classifier was selected because it balances high predictive accuracy with necessary model explainability, which is vital in financial services. While simple logistic regression may miss complex, non-linear relationships, Random Forests capture these patterns effectively while still allowing us to extract feature importance. This means Geldium’s Risk Team can understand exactly why a customer was flagged (e.g., "high credit utilization" + "recent missed payment"). This level of transparency ensures regulatory compliance, avoids the "black box" problem of neural networks, and empowers the Collections team to tailor their interventions effectively based on actionable insights."""

new_evaluation = """Metrics and Interpretation:
- Recall: This is our primary metric, as the cost of failing to identify a delinquent customer (False Negative) is high. We want to capture as many at-risk customers as possible.
- Precision: Important to monitor so the Collections team isn't overwhelmed by false alarms (False Positives).
- F1 Score & AUC-ROC: Used to balance Precision and Recall, and to evaluate the model's overall discriminative ability across different probability thresholds.

Bias & Fairness Strategy:
To ensure the model is ethical and fair, we will perform Disparate Impact Analysis across demographic groups (e.g., Age, Location) before deployment. If the model is found to unfairly penalize certain groups, we will apply bias mitigation techniques, such as re-weighting the training data distributions or adjusting classification thresholds for specific cohorts, ensuring all customers are assessed strictly on their financial behavior rather than demographic proxy variables."""

for para in doc.paragraphs:
    if logic_text in para.text:
        para.text = para.text.replace(logic_text, new_logic)
    elif justification_text in para.text:
        para.text = para.text.replace(justification_text, new_justification)
    elif evaluation_text in para.text:
        para.text = para.text.replace(evaluation_text, new_evaluation)

doc.save(out_path)
print("Saved filled docx to:", out_path)
