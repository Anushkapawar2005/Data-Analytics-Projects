import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "mysql+pymysql://root:2005anu@localhost:3306/hr_analytics"
)

employees = pd.read_sql(
    "SELECT * FROM clean_employees",
    engine
)

print("Data Loaded Successfully")
print("Shape:", employees.shape)

total_employees = len(employees)

attrition_count = employees["Attrition_Flag"].sum()

attrition_rate = (
    employees["Attrition_Flag"].mean() * 100
)

average_age = employees["Age"].mean()

average_income = employees["Monthly_Income"].mean()

average_experience = employees["Years_At_Company"].mean()

print("\n===== HR KPI SUMMARY =====")

print("Total Employees:", total_employees)
print("Attrition Count:", attrition_count)
print("Attrition Rate:", round(attrition_rate, 2), "%")
print("Average Age:", round(average_age, 2))
print("Average Monthly Income:", round(average_income, 2))
print("Average Years at Company:", round(average_experience, 2))

salary_attrition = (
    employees.groupby("Salary_Band")["Attrition_Flag"]
    .mean()
    .mul(100)
    .round(2)
)

print("\n===== SALARY BAND VS ATTRITION =====")
print(salary_attrition)


satisfaction_attrition = (
    employees.groupby("Job_Satisfaction")["Attrition_Flag"]
    .mean()
    .mul(100)
    .round(2)
)

print("\n===== JOB SATISFACTION VS ATTRITION =====")
print(satisfaction_attrition)


worklife_attrition = (
    employees.groupby("Work_Life_Balance")["Attrition_Flag"]
    .mean()
    .mul(100)
    .round(2)
)

print("\n===== WORK LIFE BALANCE VS ATTRITION =====")
print(worklife_attrition)

experience_attrition = (
    employees.groupby("Experience_Level")["Attrition_Flag"]
    .mean()
    .mul(100)
    .round(2)
)

print("\n===== EXPERIENCE LEVEL VS ATTRITION =====")
print(experience_attrition)


distance_attrition = (
    employees.groupby("Distance_From_Home")["Attrition_Flag"]
    .mean()
    .mul(100)
    .round(2)
)

print("\n===== DISTANCE FROM HOME VS ATTRITION =====")
print(distance_attrition.head(15))


department_analysis = (
    employees.groupby("Department")
    .agg(
        Total_Employees=("Employee_ID", "count"),
        Attrition_Count=("Attrition_Flag", "sum"),
        Average_Income=("Monthly_Income", "mean"),
        Average_Age=("Age", "mean")
    )
)

department_analysis["Attrition_Rate"] = (
    department_analysis["Attrition_Count"]
    / department_analysis["Total_Employees"]
    * 100
).round(2)

print("\n===== DEPARTMENT ANALYSIS =====")
print(department_analysis)


department_analysis.to_csv(
    "../Output/department_business_analysis.csv"
)

salary_attrition.to_csv(
    "../Output/salary_attrition_rate.csv"
)

satisfaction_attrition.to_csv(
    "../Output/job_satisfaction_attrition_rate.csv"
)

worklife_attrition.to_csv(
    "../Output/worklife_balance_attrition_rate.csv"
)

experience_attrition.to_csv(
    "../Output/experience_attrition_rate.csv"
)

distance_attrition.to_csv(
    "../Output/distance_attrition_rate.csv"
)

print("\nBusiness analysis files saved successfully.")

active_employees = total_employees - attrition_count

print("Active Employees:", active_employees)