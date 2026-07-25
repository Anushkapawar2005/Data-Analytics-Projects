import pandas as pd
from sqlalchemy import create_engine
import os

engine = create_engine(
    "mysql+pymysql://root:2005anu@localhost:3306/hr_analytics"
)

folder_path = r"E:\Data Analyst\DataAnalystProjects\07_HR_ANALYTICS_DASHBOARD\Data\raw"

for file in os.listdir(folder_path):

    if file.endswith(".csv"):

        table_name = file.replace(".csv", "").lower()

        file_path = os.path.join(folder_path, file)

        df = pd.read_csv(file_path)

        print(f"\nImporting {table_name}...")

        df.to_sql(
            name=table_name,
            con=engine,
            if_exists="replace",
            index=False
        )

        print(f"✅ Imported Successfully")

        print(f"Rows : {len(df)}")

print("\n🎉 All Tables Imported Successfully!")