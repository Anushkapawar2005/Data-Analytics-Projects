import pandas as pd
from sqlalchemy import create_engine

# -------------------------------
# MySQL Connection
# -------------------------------
username = "root"
password = "2005anu"      # XAMPP default password is blank
host = "localhost"
port = "3306"
database = "olist"

engine = create_engine(
    f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"
)

# -------------------------------
# CSV File Path
# -------------------------------
csv_path = r"E:\Data Analyst\DataAnalystProjects\Olist Project\archive\olist_customers_dataset.csv"

# -------------------------------
# Read CSV
# -------------------------------
df = pd.read_csv(csv_path)

# Show first 5 rows
print(df.head())

# Total Rows
print("\nTotal Rows:", len(df))

# -------------------------------
# Import into MySQL
# -------------------------------
df.to_sql(
    name="olist_customers_dataset",
    con=engine,
    if_exists="replace",   # Replace if table already exists
    index=False
)

print("\n✅ Customers table imported successfully!")