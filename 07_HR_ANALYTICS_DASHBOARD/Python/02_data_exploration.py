import pandas as pd
from sqlalchemy import create_engine

# MySQL Connection
engine = create_engine(
    "mysql+pymysql://root:2005anu@localhost:3306/hr_analytics"
)

# Load Data
employees = pd.read_sql(
    "SELECT * FROM `wa_fn-usec_-hr-employee-attrition`",
    engine
)

# First 5 Rows
print(employees.head())

# Last 5 Rows
print(employees.tail())

# Shape
print("Shape:", employees.shape)

# Columns
print(employees.columns)

# Data Types
print(employees.dtypes)

# Basic Information
employees.info()

# Statistical Summary
print(employees.describe())

# Missing Values
print("\nMissing Values:")
print(employees.isnull().sum())

# Duplicate Rows
print(
    "\nDuplicate Rows:",
    employees.duplicated().sum()
)

# Unique Values
print("\nAttrition:")
print(employees["Attrition"].unique())

print("\nDepartment:")
print(employees["Department"].unique())

print("\nJob Roles:")
print(employees["JobRole"].unique())

# Value Counts
print("\nAttrition Count:")
print(employees["Attrition"].value_counts())

print("\nDepartment Count:")
print(employees["Department"].value_counts())

print("\nJob Role Count:")
print(employees["JobRole"].value_counts())

# Important HR Columns
print(
    employees[
        [
            "Age",
            "Attrition",
            "Department",
            "JobRole",
            "MonthlyIncome",
            "OverTime",
            "JobSatisfaction",
            "YearsAtCompany",
            "PerformanceRating"
        ]
    ].head(10)
)