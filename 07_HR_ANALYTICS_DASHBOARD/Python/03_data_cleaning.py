gimport pandas as pd
from sqlalchemy import create_engine

# MySQL Connection
engine = create_engine(
    "mysql+pymysql://root:2005anu@localhost:3306/hr_analytics"
)

# Load Raw Data
employees = pd.read_sql(
    "SELECT * FROM `wa_fn-usec_-hr-employee-attrition`",
    engine
)

# Duplicate Check
print("Duplicate Rows:", employees.duplicated().sum())

# Remove duplicates only if present
employees = employees.drop_duplicates()

# Missing Values
print("\nMissing Values:")
print(employees.isnull().sum())

# Rename Columns
employees.rename(columns={
    "EmployeeNumber": "Employee_ID",
    "MonthlyIncome": "Monthly_Income",
    "DailyRate": "Daily_Rate",
    "HourlyRate": "Hourly_Rate",
    "MonthlyRate": "Monthly_Rate",
    "JobRole": "Job_Role",
    "JobSatisfaction": "Job_Satisfaction",
    "YearsAtCompany": "Years_At_Company",
    "YearsInCurrentRole": "Years_In_Current_Role",
    "YearsSinceLastPromotion": "Years_Since_Last_Promotion",
    "WorkLifeBalance": "Work_Life_Balance",
    "PerformanceRating": "Performance_Rating",
    "OverTime": "Overtime",
    "BusinessTravel": "Business_Travel",
    "DistanceFromHome": "Distance_From_Home"
}, inplace=True)

# Negative Value Checks
print("\nNegative Age:",
      (employees["Age"] < 0).sum())

print("Negative Monthly Income:",
      (employees["Monthly_Income"] < 0).sum())

print("Negative Years At Company:",
      (employees["Years_At_Company"] < 0).sum())

# Final Checks
print("\nFinal Shape:")
print(employees.shape)

print("\nFinal Missing Values:")
print(employees.isnull().sum())

print("\nFinal Duplicates:")
print(employees.duplicated().sum())

# Save Clean Data
employees.to_csv(
    "../Data/clean/clean_employees.csv",
    index=False
)

print("\n✅ Clean data saved successfully!")