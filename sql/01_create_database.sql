CREATE DATABASE IF NOT EXISTS saas_churn;

USE saas_churn;

CREATE TABLE stg_customers (
    customer_id VARCHAR(20),
    signup_date DATE,
    churn_date DATE,
    plan VARCHAR(50),
    country VARCHAR(100),
    age INT,
    monthly_fee DECIMAL(10,2),
    payment_method VARCHAR(50),
    acquisition_channel VARCHAR(100),
    contract_type VARCHAR(50),
    support_tickets INT,
    login_frequency DECIMAL(10,2),
    days_since_last_login INT,
    churn_flag TINYINT,
    status VARCHAR(20),
    annual_revenue DECIMAL(12,2),
    tenure_days INT,
    tenure_months DECIMAL(10,1),
    estimated_clv DECIMAL(12,2),
    risk_score INT,
    risk_category VARCHAR(20)
);