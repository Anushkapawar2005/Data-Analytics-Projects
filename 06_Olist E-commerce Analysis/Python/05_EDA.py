# Exploratory Data Analysis (EDA)
import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

engine = create_engine(
    "mysql+pymysql://root:2005anu@localhost:3306/olist"
)

query = """
SELECT *
FROM olist_orders_dataset
"""

orders = pd.read_sql(query, engine)

date_columns = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date"
]

for col in date_columns:
    orders[col] = pd.to_datetime(orders[col])


orders["Purchase_Year"] = orders["order_purchase_timestamp"].dt.year
orders["Purchase_Month"] = orders["order_purchase_timestamp"].dt.month
orders["Weekday"] = orders["order_purchase_timestamp"].dt.day_name()

orders["Delivery_Days"] = (
    orders["order_delivered_customer_date"] -
    orders["order_purchase_timestamp"]
).dt.days

status = orders["order_status"].value_counts()

print(status)

status.plot(kind="bar")

plt.title("Order Status Distribution")
plt.xlabel("Order Status")
plt.ylabel("Number of Orders")

plt.show()