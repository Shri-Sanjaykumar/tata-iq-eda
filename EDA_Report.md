# Exploratory Data Analysis (EDA) Report
**Project:** Geldium Delinquency Risk Assessment
**Prepared for:** Tata iQ Analytics Team & Geldium Decision-Makers

## Step 1: Key Insights & Initial Observations

### Notable Missing or Inconsistent Data
* **Income:** 39 missing entries out of 500 (~7.8%). This is a critical field for predicting repayment capability.
* **Loan_Balance:** 29 missing entries out of 500 (~5.8%). Without this, debt-to-income ratio estimations could be skewed.
* **Credit_Score:** 2 missing entries out of 500 (~0.4%). Missing values here are minimal but essential for risk evaluation.

### Key Anomalies
* **Credit Score:** The minimum is 398 and max is 500, which suggests it might be a normalized scale or specific internal score rather than standard FICO (typically 300-850).
* **Payment History (Month 1-6):** Values are categorical ("Late", "Missed", "On-time"), which will require encoding (e.g., ordinal or one-hot) before modeling.

### Early Indicators of Delinquency Risk
* **Credit_Utilization:** High utilization is consistently linked to missing payments.
* **Missed_Payments & Month 1-6 Status:** Customers who have "Missed" or "Late" statuses in recent months represent an immediate higher risk for continued delinquency.
* **Debt_to_Income_Ratio:** High debt loads relative to income correlate with financial stress and delinquency.

### Initial Data Quality Summary
Overall, the dataset has a reasonable level of completeness with only three columns showing missing values. The features are highly relevant to predicting credit default, but we must impute the missing `Income` and `Loan_Balance` values without introducing bias. Payment statuses over the last six months require numerical encoding, and the internal scaling for `Credit_Score` needs to be accounted for when building predictive models.

---

## Step 2: Addressing Missing Data

| Feature | Missing Values | Handling Method | Justification |
| :--- | :--- | :--- | :--- |
| **Income** | 39 | Impute with Median / Regression Imputation | Median is robust to outliers compared to the mean; alternatively, regression imputation based on Age and Employment_Status can yield a more precise estimate. |
| **Loan_Balance** | 29 | Impute using Predictive Model or Median | `Loan_Balance` can often be inferred based on `Credit_Utilization` and other credit features. If not, median imputation is a safe baseline. |
| **Credit_Score** | 2 | Impute with Median or Exclude | Given the very low missing count (0.4%), imputing with the median introduces negligible bias, or dropping those 2 rows entirely will not impact the dataset size significantly. |

---

## Step 3: Detecting Patterns and Risk Factors

### High-Risk Indicators
1. **High Credit Utilization Rate**
   * *Explanation:* Customers maxing out their available credit are often facing cash flow issues, making them highly susceptible to missing upcoming payments.
2. **Recent Missed Payments (Month_1 to Month_6)**
   * *Explanation:* A history of late or missed payments in the immediate past is the strongest behavioral predictor of future delinquency.
3. **High Debt-to-Income (DTI) Ratio**
   * *Explanation:* Customers whose debt payments consume a large portion of their income have less financial flexibility and are at higher risk of defaulting.

### Key Insights for Predictive Modeling
* **Behavioral vs. Demographic:** Behavioral features like `Credit_Utilization` and `Missed_Payments` are likely to carry more predictive weight than demographic features like `Age` or `Location`.
* **Sequential Patterns:** The sequential nature of `Month_1` to `Month_6` could be leveraged using time-series features or by counting the total number of consecutive missed payments. A customer going from "On-time" to "Late" to "Missed" indicates a deteriorating financial situation that the model should prioritize.
