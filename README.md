# Tata iQ & Geldium Delinquency Risk Assessment - EDA

This repository contains the Exploratory Data Analysis (EDA) process and findings for the Geldium Delinquency Risk Assessment project. The goal of this phase is to assess dataset completeness, identify patterns, and flag potential gaps that could impact delinquency predictions for Geldium's credit card operations.

## Repository Contents

* `eda.py`: A Python script that loads the dataset, checks for missing values, and calculates basic summary statistics.
* `EDA_Report.md`: The complete Exploratory Data Analysis (EDA) report summarizing key insights, data quality observations, missing data treatments, and high-risk indicators of delinquency.
* `eda_output.txt`: The output of running `eda.py` on the `Delinquency_prediction_dataset.xlsx` file.

## Project Background

Geldium’s current risk assessment relies on historical trends and broad segmentation models, lacking precision for proactive intervention. The leadership aims to leverage AI-driven insights, requiring a solid foundation of clean, reliable data. This EDA forms the first step in ensuring data integrity before predictive modeling.

## Key Steps Performed

1. **Dataset Review**: Summarized key features and missing values using Python (pandas).
2. **Missing Data Analysis**: Evaluated missing elements in `Income`, `Loan_Balance`, and `Credit_Score` and defined statistical imputation strategies.
3. **Pattern Detection**: Analyzed risk factors such as `Credit_Utilization`, recent `Missed_Payments`, and `Debt_to_Income_Ratio` as strong behavioral indicators for predicting delinquency.

## Instructions to Run

1. Ensure Python is installed.
2. Create and activate a virtual environment.
3. Install required libraries: `pip install pandas numpy openpyxl`.
4. Run the EDA script: `python eda.py` (assuming the dataset path is updated).
