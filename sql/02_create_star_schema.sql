CREATE TABLE dim_customer (
    customer_key INT IDENTITY(1,1) PRIMARY KEY,
    customer_id VARCHAR(20) NOT NULL UNIQUE,
    country VARCHAR(100),
    age INT,
    payment_method VARCHAR(50),
    acquisition_channel VARCHAR(100)
);

CREATE TABLE dim_plan (
    plan_key INT IDENTITY(1,1) PRIMARY KEY,
    [plan] VARCHAR(50) NOT NULL UNIQUE,
    monthly_fee DECIMAL(10,2)
);

CREATE TABLE dim_contract (
    contract_key INT IDENTITY(1,1) PRIMARY KEY,
    contract_type VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE dim_date (
    date_key INT PRIMARY KEY,
    full_date DATE NOT NULL UNIQUE,
    year INT,
    quarter INT,
    month INT,
    month_name VARCHAR(20),
    year_month VARCHAR(7)
);

CREATE TABLE fact_subscription (
    subscription_key INT IDENTITY(1,1) PRIMARY KEY,

    customer_key INT NOT NULL,

    plan_key INT NOT NULL,

    contract_key INT NOT NULL,

    signup_date_key INT,

    churn_date_key INT,

    monthly_fee DECIMAL(10,2),

    annual_revenue DECIMAL(12,2),

    churn_flag TINYINT,

    tenure_days INT,

    tenure_months DECIMAL(10,1),

    estimated_clv DECIMAL(12,2),

    support_tickets INT,

    login_frequency DECIMAL(10,2),

    days_since_last_login INT,

    risk_score INT,

    risk_category VARCHAR(20),

    FOREIGN KEY (customer_key)
        REFERENCES dim_customer(customer_key),

    FOREIGN KEY (plan_key)
        REFERENCES dim_plan(plan_key),

    FOREIGN KEY (contract_key)
        REFERENCES dim_contract(contract_key),

    FOREIGN KEY (signup_date_key)
        REFERENCES dim_date(date_key),

    FOREIGN KEY (churn_date_key)
        REFERENCES dim_date(date_key)
);