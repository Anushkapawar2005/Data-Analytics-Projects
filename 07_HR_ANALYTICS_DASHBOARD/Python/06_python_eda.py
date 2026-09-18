import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

engine = create_engine(
    "mysql+pymysql://root:2005anu@localhost:3306/hr_analytics"
)

employees = pd.read_sql(
    "SELECT * FROM clean_employees",
    engine
)

print(employees.head())
print("Shape:", employees.shape)

# Analysis 1 — Attrition Distribution

attrition = employees["Attrition"].value_counts()
print(attrition)

attrition.plot(kind="bar")
plt.title("Employee Attrition Distribution")
plt.xlabel("Attrition")
plt.ylabel("Number of Employees")

plt.show()


# Analysis 2 — Department-wise Attrition

department_attrition = (
    employees.groupby("Department")["Attrition_Flag"]
    .sum()
    .sort_values(ascending=False)
)

print(department_attrition)

department_attrition.plot(kind="bar")

plt.title("Attrition by Department")
plt.xlabel("Department")
plt.ylabel("Attrition Count")
plt.show()



# Analysis 3 — Job Role-wise Attrition

role_attrition = (
    employees.groupby("Job_Role")["Attrition_Flag"]
    .sum()
    .sort_values(ascending=False)
)

print(role_attrition)

role_attrition.plot(kind="bar")

plt.title("Attrition by Job Role")
plt.xlabel("Job Role")
plt.ylabel("Attrition Count")
plt.xticks(rotation=45)
plt.show()

# Analysis 4 — Overtime vs Attrition

overtime_attrition = (
    employees.groupby("Overtime")["Attrition_Flag"]
    .sum()
)

print(overtime_attrition)

overtime_attrition.plot(kind="bar")

plt.title("Attrition by Overtime")
plt.xlabel("Overtime")
plt.ylabel("Attrition Count")

plt.show()



# Analysis 5 — Age Group Distribution

age_group = (
    employees["Age_Group"]
    .value_counts()
    .sort_index()
)

print(age_group)

age_group.plot(kind="bar")

plt.title("Employee Distribution by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Employees")

plt.show()



# Analysis 6 — Salary Band Distribution
salary_band = (
    employees["Salary_Band"]
    .value_counts()
)

print(salary_band)

salary_band.plot(kind="bar")

plt.title("Employee Distribution by Salary Band")
plt.xlabel("Salary Band")
plt.ylabel("Employees")

plt.show()




# Analysis 7 — Experience Level
experience = (
    employees["Experience_Level"]
    .value_counts()
)

print(experience)

experience.plot(kind="bar")

plt.title("Employee Distribution by Experience Level")
plt.xlabel("Experience Level")
plt.ylabel("Employees")

plt.show()



# Analysis 8 — Monthly Income Distribution
employees["Monthly_Income"].plot(
    kind="hist",
    bins=20
)

plt.title("Monthly Income Distribution")
plt.xlabel("Monthly Income")
plt.ylabel("Number of Employees")

plt.show()

# Analysis 9 — Attrition Rate by Department
department_rate = (
    employees.groupby("Department")["Attrition_Flag"]
    .mean()
    .mul(100)
    .round(2)
    .sort_values(ascending=False)
)

print(department_rate)

department_rate.plot(kind="bar")

plt.title("Attrition Rate by Department")
plt.xlabel("Department")
plt.ylabel("Attrition Rate (%)")

plt.show()



# Analysis 10 — Attrition Rate by Overtime
overtime_rate = (
    employees.groupby("Overtime")["Attrition_Flag"]
    .mean()
    .mul(100)
    .round(2)
)

print(overtime_rate)
overtime_rate.plot(kind="bar")

plt.title("Attrition Rate by Overtime")
plt.xlabel("Overtime")
plt.ylabel("Attrition Rate (%)")

plt.show()


department_rate.to_csv(
    "../Output/department_attrition_rate.csv"
)


role_attrition.to_csv(
    "../Output/role_attrition.csv"
)


overtime_rate.to_csv(
    "../Output/overtime_attrition_rate.csv"
)