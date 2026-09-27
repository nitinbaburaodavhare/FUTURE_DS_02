import pandas as pd

# Load dataset
df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")

# Basic information
print("Dataset Shape:", df.shape)
print("\nColumns:")
print(df.columns.tolist())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check duplicate rows
print("\nDuplicate Rows:", df.duplicated().sum())

# Convert TotalCharges to numeric
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

# Check missing values again
print("\nMissing TotalCharges:", df["TotalCharges"].isnull().sum())

# Display rows where TotalCharges is missing
print("\nRows with missing TotalCharges:")
print(df[df["TotalCharges"].isnull()][["customerID", "tenure", "TotalCharges"]])
# Fill missing TotalCharges for new customers
df["TotalCharges"] = df["TotalCharges"].fillna(0)

# Save cleaned dataset
df.to_csv("cleaned_customer_churn.csv", index=False)

print("\nCleaning completed successfully!")
print("Cleaned dataset saved as: cleaned_customer_churn.csv")
# Churn Analysis

total_customers = len(df)

churned_customers = (df["Churn"] == "Yes").sum()

churn_rate = (churned_customers / total_customers) * 100

retained_customers = (df["Churn"] == "No").sum()

retention_rate = (retained_customers / total_customers) * 100

print("\n--- Churn Analysis ---")
print("Total Customers:", total_customers)
print("Churned Customers:", churned_customers)
print("Retained Customers:", retained_customers)
print("Churn Rate:", round(churn_rate, 2), "%")
print("Retention Rate:", round(retention_rate, 2), "%")
# Churn Analysis

total_customers = len(df)

churned_customers = (df["Churn"] == "Yes").sum()

churn_rate = (churned_customers / total_customers) * 100

retained_customers = (df["Churn"] == "No").sum()

retention_rate = (retained_customers / total_customers) * 100

print("\n--- Churn Analysis ---")
print("Total Customers:", total_customers)
print("Churned Customers:", churned_customers)
print("Retained Customers:", retained_customers)
print("Churn Rate:", round(churn_rate, 2), "%")
print("Retention Rate:", round(retention_rate, 2), "%")
# Churn Rate by Contract Type

contract_churn = df.groupby("Contract")["Churn"].apply(
    lambda x: (x == "Yes").mean() * 100
)

print("\n--- Churn Rate by Contract Type ---")
print(contract_churn.round(2))
# Churn Rate by Contract Type

contract_churn = df.groupby("Contract")["Churn"].apply(
    lambda x: (x == "Yes").mean() * 100
)

print("\n--- Churn Rate by Contract Type ---")
print(contract_churn.round(2))
# Churn Rate by Tenure Group

df["TenureGroup"] = pd.cut(
    df["tenure"],
    bins=[0, 6, 12, 24, 48, 60, 72],
    labels=["0-6 Months", "7-12 Months", "13-24 Months",
            "25-48 Months", "49-60 Months", "61-72 Months"],
    include_lowest=True
)

tenure_churn = df.groupby("TenureGroup", observed=False)["Churn"].apply(
    lambda x: (x == "Yes").mean() * 100
)

print("\n--- Churn Rate by Tenure Group ---")
print(tenure_churn.round(2))
# Churn Rate by Internet Service

internet_churn = df.groupby("InternetService")["Churn"].apply(
    lambda x: (x == "Yes").mean() * 100
)

print("\n--- Churn Rate by Internet Service ---")
print(internet_churn.round(2))
# Churn Rate by Internet Service

internet_churn = df.groupby("InternetService")["Churn"].apply(
    lambda x: (x == "Yes").mean() * 100
)

print("\n--- Churn Rate by Internet Service ---")
print(internet_churn.round(2))
# Churn Rate by Internet Service

internet_churn = df.groupby("InternetService")["Churn"].apply(
    lambda x: (x == "Yes").mean() * 100
)

print("\n--- Churn Rate by Internet Service ---")
print(internet_churn.round(2))
# Churn Rate by Payment Method

payment_churn = df.groupby("PaymentMethod")["Churn"].apply(
    lambda x: (x == "Yes").mean() * 100
)

print("\n--- Churn Rate by Payment Method ---")
print(payment_churn.round(2))
# Churn Rate by Monthly Charges Group

df["MonthlyChargesGroup"] = pd.cut(
    df["MonthlyCharges"],
    bins=[0, 30, 60, 90, 120, 150],
    labels=["0-30", "31-60", "61-90", "91-120", "121-150"],
    include_lowest=True
)

monthly_charges_churn = df.groupby(
    "MonthlyChargesGroup", observed=False
)["Churn"].apply(
    lambda x: (x == "Yes").mean() * 100
)

print("\n--- Churn Rate by Monthly Charges Group ---")
print(monthly_charges_churn.round(2))
import matplotlib.pyplot as plt

# Create charts folder
import os
os.makedirs("charts", exist_ok=True)

# 1. Contract Churn
contract_churn.plot(kind="bar")
plt.title("Churn Rate by Contract Type")
plt.ylabel("Churn Rate (%)")
plt.xlabel("Contract Type")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("charts/contract_churn.png")
plt.close()

# 2. Tenure Churn
tenure_churn.plot(kind="bar")
plt.title("Churn Rate by Tenure Group")
plt.ylabel("Churn Rate (%)")
plt.xlabel("Tenure Group")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("charts/tenure_churn.png")
plt.close()

# 3. Internet Service Churn
internet_churn.plot(kind="bar")
plt.title("Churn Rate by Internet Service")
plt.ylabel("Churn Rate (%)")
plt.xlabel("Internet Service")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("charts/internet_service_churn.png")
plt.close()

# 4. Payment Method Churn
payment_churn.plot(kind="bar")
plt.title("Churn Rate by Payment Method")
plt.ylabel("Churn Rate (%)")
plt.xlabel("Payment Method")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.savefig("charts/payment_method_churn.png")
plt.close()

# 5. Monthly Charges Churn
monthly_charges_churn.dropna().plot(kind="bar")
plt.title("Churn Rate by Monthly Charges")
plt.ylabel("Churn Rate (%)")
plt.xlabel("Monthly Charges Group")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("charts/monthly_charges_churn.png")
plt.close()

print("\nAll charts saved successfully in the 'charts' folder!")