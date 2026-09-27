# Customer Churn Analysis

## Internship Project

**Name:** Nitin Baburao Davhare  
**Project:** Customer Churn & Retention Analysis  
**Dataset:** Telco Customer Churn Dataset  
**Tools:** Python, Pandas, Matplotlib

---

## 1. Project Overview

This project analyzes customer churn and retention patterns using the Telco Customer Churn dataset.

The main objective is to identify customer groups with higher churn rates and understand the factors associated with customer churn.

---

## 2. Objectives

- Calculate overall customer churn and retention rates
- Analyze churn by contract type
- Analyze churn by customer tenure
- Analyze churn by internet service
- Analyze churn by payment method
- Analyze churn by monthly charges
- Identify important churn-associated patterns
- Provide business recommendations for improving customer retention

---

## 3. Dataset

The dataset contains **7,043 customer records** and **21 columns**.

Important fields include:

- Customer ID
- Tenure
- Internet Service
- Contract
- Payment Method
- Monthly Charges
- Total Charges
- Churn

---

## 4. Data Cleaning

The following preprocessing steps were performed:

- Checked dataset shape and columns
- Checked missing values
- Checked duplicate records
- Converted `TotalCharges` into numeric format
- Handled 11 missing `TotalCharges` values
- Saved the cleaned dataset as `cleaned_customer_churn.csv`

---

## 5. Key Findings

### Overall Churn

- Total Customers: **7,043**
- Churned Customers: **1,869**
- Retained Customers: **5,174**
- Churn Rate: **26.54%**
- Retention Rate: **73.46%**

### Churn by Contract

- Month-to-month: **42.71%**
- One year: **11.27%**
- Two year: **2.83%**

### Churn by Tenure

- 0–6 Months: **52.94%**
- 7–12 Months: **35.89%**
- 13–24 Months: **28.71%**
- 25–48 Months: **20.39%**
- 49–60 Months: **14.42%**
- 61–72 Months: **6.61%**

### Churn by Internet Service

- DSL: **18.96%**
- Fiber optic: **41.89%**
- No Internet: **7.40%**

### Churn by Payment Method

- Electronic check: **45.29%**
- Mailed check: **19.11%**
- Bank transfer: **16.71%**
- Credit card: **15.24%**

### Churn by Monthly Charges

- 0–30: **9.80%**
- 31–60: **25.93%**
- 61–90: **33.91%**
- 91–120: **32.78%**

---

## 6. Business Recommendations

Based on the analysis:

1. Focus on retaining month-to-month customers.
2. Provide onboarding and engagement support during the first few months.
3. Investigate customer experience and pricing factors affecting fiber-optic customers.
4. Encourage customers to use automatic payment methods.
5. Monitor customers with higher monthly charges.
6. Develop targeted retention offers for high-risk customer segments.

---

## 7. Visualizations

The project includes the following charts:

- Churn Rate by Contract Type
- Churn Rate by Tenure Group
- Churn Rate by Internet Service
- Churn Rate by Payment Method
- Churn Rate by Monthly Charges

All visualizations are available in the `charts` folder.

---

## 8. Project Files

```text
Customer-Churn-Analysis/
│
├── data_cleaning.py
├── WA_Fn-UseC_-Telco-Customer-Churn.csv
├── cleaned_customer_churn.csv
├── README.md
│
└── charts/
    ├── contract_churn.png
    ├── tenure_churn.png
    ├── internet_service_churn.png
    ├── payment_method_churn.png
    └── monthly_charges_churn.png