# Customer Churn Analysis & BI Dashboard

### End-to-End SaaS Customer Retention, MRR & Churn Analytics

![Power BI Dashboard](screenshots/executive_dashboard.png)

##  Project Overview

This project analyzes customer churn and subscription revenue for a simulated SaaS business.

The objective is to identify customer retention patterns, understand revenue trends, measure churn, analyze customer cohorts, and identify high-value customers who may be at risk of churn.

The project follows an end-to-end analytics workflow using Python, MySQL, and Power BI.

##  Business Problem

Customer churn directly impacts recurring revenue and long-term customer value.

The business needs to understand:

- How many customers are churning?
- What is the overall churn rate?
- Which subscription plans have the highest churn?
- Which customer segments are most at risk?
- How does customer retention change over time?
- How is Monthly Recurring Revenue (MRR) changing?
- Which high-value customers should be prioritized for retention?

##  Project Objectives

1. Clean and prepare customer subscription data using Python and Pandas.
2. Store and analyze structured data using MySQL.
3. Apply SQL joins, CTEs, and window functions for business analysis.
4. Build a star-schema data model for BI reporting.
5. Calculate customer churn, retention, MRR, and customer lifetime value metrics.
6. Perform cohort retention analysis.
7. Identify high-risk and high-value customers.
8. Build interactive Power BI dashboards.
9. Generate actionable business recommendations from the analysis.

##  Tools & Technologies

| Tool | Purpose |
|---|---|
| Python | Data cleaning and transformation |
| Pandas | Data manipulation |
| NumPy | Numerical operations |
| MySQL | Data storage and SQL analysis |
| SQL | Business analysis and KPI calculations |
| Power BI | Interactive dashboards |
| DAX | BI measures and advanced calculations |
| Git | Version control |
| GitHub | Project documentation and portfolio |
| VS Code | Development environment |

## 🔄 End-to-End Workflow

Raw CSV Data
↓
Python / Pandas
↓
Data Cleaning & Transformation
↓
Clean CSV Data
↓
MySQL Database
↓
SQL Analysis
↓
Star Schema
↓
Power BI Data Model
↓
DAX Calculations
↓
Interactive Dashboards
↓
Business Insights & Recommendations

##  Python Data Cleaning

Python and Pandas were used to prepare the raw customer dataset for analysis.

The cleaning process included:

- Loading raw CSV data
- Inspecting dataset structure
- Checking data types
- Identifying missing values
- Detecting duplicate records
- Validating numerical fields
- Standardizing relevant columns
- Creating derived analytical fields
- Exporting the cleaned dataset

### Example Python Workflow

```python
import pandas as pd

df = pd.read_csv("../data/customers_raw.csv")

print(df.head())
print(df.info())
print(df.isnull().sum())
print(df.duplicated().sum())

df = df.drop_duplicates()

df.to_csv(
    "../data/customers_clean.csv",
    index=False
)

##  MySQL Analysis

The cleaned dataset was loaded into MySQL for structured analysis.

SQL was used to calculate and investigate:

- Total customers
- Active customers
- Churned customers
- Churn rate
- Monthly recurring revenue
- Revenue at risk
- Customer lifetime value
- Customer segmentation
- Cohort metrics
- Plan-level performance
- Contract-level churn

### SQL Techniques Used

- SELECT
- WHERE
- GROUP BY
- HAVING
- JOIN
- CASE WHEN
- Common Table Expressions (CTEs)
- Window Functions
- Aggregations
- Date Functions
- Ranking

## ⭐ Data Model

A star-schema structure was used to organize the analytical model.

The central fact table contains subscription-level business data, while dimension tables provide descriptive attributes.

### Conceptual Model

                    dim_date
                       |
                       |
dim_customer --- fact_subscription --- dim_plan
                       |
                       |
                  dim_contract

### Benefits

- Simplifies reporting relationships
- Improves filtering and aggregation
- Separates transactional and descriptive data
- Makes Power BI calculations easier to manage
- Improves model clarity and maintainability

##  Power BI Dashboard

The Power BI report contains multiple analytical pages designed for different business questions.

### 1. Executive Dashboard

Provides a high-level overview of:

- Total customers
- Active customers
- Churn rate
- Current MRR
- Revenue at risk
- Customer risk distribution
- MRR trend
- Churn trend

### 2. MRR Analysis

The MRR page analyzes recurring subscription revenue.

Key metrics include:

- Current MRR
- Previous-period MRR
- MRR change
- MRR growth %
- Monthly MRR trend
- MRR waterfall
- New MRR
- Churned MRR

### 3. Churn Analysis

The churn dashboard examines customer loss across different dimensions.

Analysis includes:

- Overall churn rate
- Churned customers
- Churned revenue
- Revenue at risk
- Churn by subscription plan
- Churn by contract type
- Churn by customer tenure
- Customer risk distribution

### 4. Cohort Retention Analysis

Customers are grouped according to their acquisition month and tracked across subsequent months.

The cohort analysis includes:

- Cohort size
- Month since cohort
- Retained customers
- Retention percentage
- Cohort retention heatmap
- Retention curve
- Cohort revenue

### 5. Customer Details

The customer-level analysis helps identify customers requiring retention attention.

The analysis includes:

- Customer ID
- Subscription plan
- Contract type
- Monthly fee
- Customer lifetime value
- Tenure
- Risk score
- Risk category
- Retention priority

screenshots
│
├── executive_dashboard.png
├── mrr_analysis.png
├── churn_analysis.png
├── cohort_retention.png
└── customer_details.png


## 📈 Key KPIs

| KPI | Result |
|---|---:|
| Total Customers | TBD |
| Active Customers | TBD |
| Churned Customers | TBD |
| Churn Rate | TBD |
| Current MRR | TBD |
| MRR Growth | TBD |
| Revenue at Risk | TBD |
| Average CLV | TBD |


## 🔍 Key Business Insights

### Customer Churn

- TBD based on final analysis.

### Subscription Plan

- TBD based on final churn comparison.

### Customer Tenure

- TBD based on tenure analysis.

### Cohort Retention

- TBD based on cohort retention analysis.

### Revenue Risk

- TBD based on revenue-at-risk analysis.


## 💼 Business Recommendations

Based on the final analytical findings, recommendations will focus on:

1. Prioritizing high-value customers with elevated churn risk.
2. Improving onboarding during the early customer lifecycle.
3. Investigating subscription plans with above-average churn.
4. Developing targeted retention campaigns.
5. Prioritizing retention efforts based on revenue at risk rather than customer count alone.
6. Monitoring cohort retention to identify changes in customer behavior.


## 📁 Project Structure

Customer-Churn-Analysis/
│
├── data/
│   ├── customers_raw.csv
│   └── customers_clean.csv
│
├── python/
│   └── data_cleaning.py
│
├── sql/
│   └── churn_analysis.sql
│
├── powerbi/
│   └── Customer_Churn_Analysis.pbix
│
├── screenshots/
│   ├── executive_dashboard.png
│   ├── mrr_analysis.png
│   ├── churn_analysis.png
│   ├── cohort_retention.png
│   └── customer_details.png
│
├── README.md
├── requirements.txt
└── .gitignore


## ▶️ How to Run

### 1. Clone the repository

```bash
git clone <https://github.com/mvinodreddyvkr-hub/customer-churn-analysis>


##  Author

**Vinod Reddy**

Data Analyst | SQL | Python | Power BI

This project was developed as part of a data analytics portfolio demonstrating end-to-end data preparation, SQL analysis, BI modeling, dashboard development, and business insight generation.