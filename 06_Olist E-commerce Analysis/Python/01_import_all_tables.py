import os
import pandas as pd
from sqlalchemy import create_engine

# -------------------------------
# MySQL Connection
# -------------------------------
username = "root"
password = "2005anu"
host = "localhost"
port = "3306"
database = "olist"

engine = create_engine(
    f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"
)

# -------------------------------
# Folder containing CSV files
# -------------------------------
folder_path = r"E:\Data Analyst\DataAnalystProjects\Olist Project\archive"

# -------------------------------
# Import all CSV files
# -------------------------------
for file in os.listdir(folder_path):

    if file.endswith(".csv"):

        table_name = file.replace(".csv", "")

        file_path = os.path.join(folder_path, file)

        print(f"\nImporting {table_name}...")

        df = pd.read_csv(file_path)

        df.to_sql(
            name=table_name,
            con=engine,
            if_exists="replace",
            index=False
        )

        print(f"✅ {table_name} imported successfully.")
        print(f"Rows : {len(df)}")

print("\n🎉 All Tables Imported Successfully!")