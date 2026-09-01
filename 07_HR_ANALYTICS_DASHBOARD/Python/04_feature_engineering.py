import pandas as pd

# Load Clean Data
employees = pd.read_csv(
    "../Data/clean/clean_employees.csv"
)

print("Original Shape:", employees.shape)

# Age Group
employees["Age_Group"] = pd.cut(
    employees["Age"],
    bins=[0, 25, 35, 45, 55, 100],
    labels=[
        "Under 25",
        "25-35",
        "36-45",
        "46-55",
        "55+"
    ]
)

# Salary Band
employees["Salary_Band"] = pd.cut(
    employees["Monthly_Income"],
    bins=[0, 3000, 6000, 10000, 15000, float("inf")],
    labels=[
        "Low",
        "Medium",
        "High",
        "Very High",
        "Executive"
    ]
)

# Experience Level
employees["Experience_Level"] = pd.cut(
    employees["Years_At_Company"],
    bins=[-1, 2, 5, 10, float("inf")],
    labels=[
        "Entry Level",
        "Mid Level",
        "Experienced",
        "Senior"
    ]
)

# Attrition Flag
employees["Attrition_Flag"] = (
    employees["Attrition"]
    .map({
        "Yes": 1,
        "No": 0
    })
)

# Check New Features
print("\nFeature Engineering Result:")

print(
    employees[
        [
            "Age",
            "Age_Group",
            "Monthly_Income",
            "Salary_Band",
            "Years_At_Company",
            "Experience_Level",
            "Attrition",
            "Attrition_Flag"
        ]
    ].head(10)
)

# Check Missing Values
print("\nNew Feature Missing Values:")

print(
    employees[
        [
            "Age_Group",
            "Salary_Band",
            "Experience_Level",
            "Attrition_Flag"
        ]
    ].isnull().sum()
)

# Save
employees.to_csv(
    "../Data/clean/clean_employees.csv",
    index=False
)

print("\n✅ Feature engineering completed!")
print("Final Shape:", employees.shape)
print("✅ Clean dataset updated successfully!")