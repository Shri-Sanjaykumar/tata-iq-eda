import pandas as pd
import numpy as np

# Load the dataset
file_path = r"C:\Users\Priya\OneDrive\Documents\tata\Delinquency_prediction_dataset.xlsx"
df = pd.read_excel(file_path)

print("Dataset Info:")
print(df.info())
print("\n---")

print("\nMissing Values:")
print(df.isnull().sum())
print("\n---")

print("\nSummary Statistics:")
print(df.describe(include='all'))
print("\n---")

print("\nFirst 5 rows:")
print(df.head())
print("\n---")

# Look at target variable distribution
if 'delinquency' in df.columns.str.lower():
    target_col = [col for col in df.columns if col.lower() == 'delinquency'][0]
    print(f"\nTarget Variable ({target_col}) Distribution:")
    print(df[target_col].value_counts(dropna=False))
elif 'target' in df.columns.str.lower():
    target_col = [col for col in df.columns if col.lower() == 'target'][0]
    print(f"\nTarget Variable ({target_col}) Distribution:")
    print(df[target_col].value_counts(dropna=False))
else:
    print("\nColumns available:")
    print(df.columns)
