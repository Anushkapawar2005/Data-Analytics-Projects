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