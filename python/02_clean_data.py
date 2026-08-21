import pandas as pd

df = pd.read_csv("data/raw/customers_raw.csv")

print("DATA LOADED SUCCESSFULLY")
print("=" * 50)

print(df.head())


print("\nDATASET SHAPE")
print(df.shape)

print("\nCOLUMN NAMES")
print(df.columns.tolist())
print("\nDATA TYPES")
print(df.dtypes)


df["signup_date"] = pd.to_datetime(
    df["signup_date"],
    errors="coerce"
)

df["churn_date"] = pd.to_datetime(
    df["churn_date"],
    errors="coerce"
)

print("\nMISSING VALUES")
print(df.isnull().sum())

print("\nDUPLICATE ROWS")
print(df.duplicated().sum())

print("\nDUPLICATE ROWS")
print(df['customer_id'].duplicated().sum())

print("\nUNIQUE CUSTOMERS")
print(df["customer_id"].nunique())

print("\nPLAN VALUES")
print(df["plan"].value_counts())

print("\nCUSTOMER STATUS")
print(df["status"].value_counts())

print("\nCHURN FLAG")
print(df["churn_flag"].value_counts())

print("\nAGE RANGE")
print(df["age"].min())
print(df["age"].max())


print("\nMONTHLY FEE VALUES")
print(df["monthly_fee"].value_counts())

invalid_age = df[
    (df["age"] < 18) |
    (df["age"] > 100)
]

print("\nINVALID AGES")
print(len(invalid_age))

valid_fees = [19, 49, 99]

invalid_fees = df[
    ~df["monthly_fee"].isin(valid_fees)
]

print("\nINVALID MONTHLY FEES")
print(len(invalid_fees))

invalid_churn = df[
    (df["churn_flag"] == 1) &
    (df["churn_date"].isnull())
]

print("\nCHURNED CUSTOMERS WITHOUT CHURN DATE")
print(len(invalid_churn))

invalid_active = df[
    (df["churn_flag"] == 0) &
    (df["churn_date"].notnull())
]

print("\nACTIVE CUSTOMERS WITH CHURN DATE")
print(len(invalid_active))

df["tenure_days"] = (
    pd.Timestamp("2025-12-31")
    - df["signup_date"]
).dt.days

df["tenure_months"] = (
    df["tenure_days"] / 30
).round(1)

df["estimated_clv"] = (
    df["monthly_fee"]
    * df["tenure_months"]
).round(2)

print(df[["signup_date", "tenure_days", "tenure_months", "monthly_fee", "estimated_clv"]].head())


df["risk_score"] = 0


df.loc[
    df["days_since_last_login"] > 30,
    "risk_score"
] += 1

df.loc[
    df["support_tickets"] >= 5,
    "risk_score"
] += 1

df.loc[
    df["contract_type"] == "Monthly",
    "risk_score"
] += 1


print("\n" + "=" * 40)
print("RISK SCORE DISTRIBUTION")
print("=" * 40)

print(df["risk_score"].value_counts().sort_index())

print("\nSAMPLE RESULTS (First 5 Rows):")
print(
    df[[
        "days_since_last_login", 
        "support_tickets", 
        "contract_type", 
        "risk_score"
    ]].head()
)

df["risk_category"] = pd.cut(
    df["risk_score"],
    bins=[-1, 0, 1, 3],
    labels=[
        "Low Risk",
        "Medium Risk",
        "High Risk"
    ]
)

print("\n" + "=" * 40)
print("RISK CATEGORY DISTRIBUTION")
print("=" * 40)


print(df["risk_category"].value_counts())


print("\nPERCENTAGE BREAKDOWN:")
print(df["risk_category"].value_counts(normalize=True) * 100)

print("\nSAMPLE RESULTS (First 5 Rows):")
print(df[["risk_score", "risk_category"]].head())

output_file = "data/processed/customers_clean.csv"

df.to_csv(
    output_file,
    index=False
)

print("\n" + "=" * 50)
print("DATA CLEANING COMPLETE")
print("=" * 50)

print(f"Rows: {len(df):,}")
print(f"Columns: {len(df.columns):,}")
print(f"Output: {output_file}")