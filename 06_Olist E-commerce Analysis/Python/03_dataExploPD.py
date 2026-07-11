import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "mysql+pymysql://root:2005anu@localhost:3306/olist"
)

query = """
SELECT *
FROM olist_orders_dataset
"""

orders = pd.read_sql(query, engine)

print(orders.head())
print(orders.shape)
print(orders.info())
print(orders.isnull().sum())

print(orders.duplicated().sum())

print(orders["order_status"].unique())

print(orders["order_status"].value_counts())