import pandas as pd
from sqlalchemy import create_engine

# MySQL Connection
engine = create_engine(
    "mysql+pymysql://root:2005anu@localhost:3306/hr_analytics"
)

# Load Clean Data
employees = pd.read_csv(
    "../Data/clean/clean_employees.csv"
)

# Check Data
print(employees.head())

print("\nShape:", employees.shape)

# Validation
print("\nTotal Missing Values:")
print(employees.isnull().sum().sum())

print("\nDuplicate Rows:")
print(employees.duplicated().sum())

# Load into MySQL
employees.to_sql(
    name="clean_employees",
    con=engine,
    if_exists="replace",
    index=False
)

# Success
print("\n✅ Clean employees table imported successfully!")
print("Rows:", len(employees))
print("Columns:", len(employees.columns))