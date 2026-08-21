import pandas as pd
import numpy as np
from faker import Faker
from pathlib import Path


# ============================================
# 1. INITIAL SETUP
# ============================================

fake = Faker()

np.random.seed(42)


# ============================================
# 2. CREATE OUTPUT FOLDER
# ============================================

OUTPUT_DIR = Path("data/raw")

OUTPUT_DIR.mkdir(
    parents=True,
    exist_ok=True
)


# ============================================
# 3. NUMBER OF CUSTOMERS
# ============================================

NUM_CUSTOMERS = 5000


# ============================================
# 4. BUSINESS SETTINGS
# ============================================

plans = {
    "Basic": 19,
    "Standard": 49,
    "Premium": 99
}


countries = [
    "India",
    "United States",
    "United Kingdom",
    "Canada",
    "Australia",
    "Germany"
]


payment_methods = [
    "Credit Card",
    "Debit Card",
    "UPI",
    "PayPal"
]


acquisition_channels = [
    "Organic Search",
    "Paid Search",
    "Referral",
    "Social Media",
    "Email",
    "Partner"
]


contract_types = [
    "Monthly",
    "Annual"
]


# ============================================
# 5. CREATE EMPTY LIST
# ============================================

rows = []


# ============================================
# 6. GENERATE CUSTOMER DATA
# ============================================

for i in range(
    1,
    NUM_CUSTOMERS + 1
):

    # Customer ID
    customer_id = f"C{i:05d}"


    # Signup date
    signup_date = pd.Timestamp(
        fake.date_between(
            start_date="-30M",
            end_date="-2M"
        )
    )


    # Subscription plan
    plan = np.random.choice(
        list(plans.keys()),
        p=[
            0.45,
            0.35,
            0.20
        ]
    )


    # Country
    country = np.random.choice(
        countries
    )


    # Age
    age = np.random.randint(
        18,
        65
    )


    # Payment method
    payment_method = np.random.choice(
        payment_methods
    )


    # Acquisition channel
    acquisition_channel = np.random.choice(
        acquisition_channels
    )


    # Contract type
    contract_type = np.random.choice(
        contract_types,
        p=[
            0.70,
            0.30
        ]
    )


    # Monthly subscription price
    monthly_fee = plans[plan]


    # Calculate tenure
    tenure_months = max(
        1,
        int(
            (
                pd.Timestamp("2025-12-31")
                - signup_date
            ).days / 30
        )
    )


    # ========================================
    # CHURN PROBABILITY
    # ========================================

    churn_probability = 0.10


    # Monthly contracts have higher churn
    if contract_type == "Monthly":

        churn_probability += 0.10


    # Basic plan has slightly higher churn
    if plan == "Basic":

        churn_probability += 0.05


    # Premium has slightly lower churn
    if plan == "Premium":

        churn_probability -= 0.03


    # Keep probability within range
    churn_probability = min(
        max(
            churn_probability,
            0.03
        ),
        0.40
    )


    # Determine churn
    churn_flag = np.random.binomial(
        1,
        churn_probability
    )


    # ========================================
    # CHURN DATE
    # ========================================

    churn_date = None


    if churn_flag == 1:

        churn_offset = np.random.randint(
            30,
            max(
                31,
                tenure_months * 30
            )
        )

        churn_date = (
            signup_date
            + pd.Timedelta(
                days=int(churn_offset)
            )
        )


        if (
            churn_date
            > pd.Timestamp("2025-12-31")
        ):

            churn_date = pd.Timestamp(
                "2025-12-31"
            )


    # ========================================
    # CUSTOMER BEHAVIOR
    # ========================================

    support_tickets = np.random.poisson(
        2
    )


    login_frequency = max(
        0,
        np.random.normal(
            12,
            5
        )
    )


    days_since_last_login = max(
        1,
        int(
            np.random.normal(
                15,
                10
            )
        )
    )


    # ========================================
    # STORE RECORD
    # ========================================

    rows.append({

        "customer_id":
            customer_id,

        "signup_date":
            signup_date,

        "churn_date":
            churn_date,

        "plan":
            plan,

        "country":
            country,

        "age":
            age,

        "monthly_fee":
            monthly_fee,

        "payment_method":
            payment_method,

        "acquisition_channel":
            acquisition_channel,

        "contract_type":
            contract_type,

        "support_tickets":
            support_tickets,

        "login_frequency":
            round(
                login_frequency,
                2
            ),

        "days_since_last_login":
            days_since_last_login,

        "churn_flag":
            churn_flag
    })


# ============================================
# 7. CREATE DATAFRAME
# ============================================

df = pd.DataFrame(rows)


# ============================================
# 8. CREATE STATUS
# ============================================

df["status"] = np.where(
    df["churn_flag"] == 1,
    "Churned",
    "Active"
)


# ============================================
# 9. ANNUAL REVENUE
# ============================================

df["annual_revenue"] = (
    df["monthly_fee"] * 12
)


# ============================================
# 10. SAVE CSV
# ============================================

output_file = (
    OUTPUT_DIR
    / "customers_raw.csv"
)


df.to_csv(
    output_file,
    index=False
)

print(
    "===================================="
)

print(
    "CUSTOMER DATA GENERATION COMPLETE"
)

print(
    "===================================="
)

print(
    f"Customers created: {len(df):,}"
)

print(
    f"File created: {output_file}"
)

print(
    "\nCustomer status:"
)

print(
    df["status"].value_counts()
)