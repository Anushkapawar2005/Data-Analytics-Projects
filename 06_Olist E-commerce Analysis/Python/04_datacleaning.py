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
print(orders.dtypes)

#date convert
date_columns = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date"
]

for col in date_columns:
    orders[col] = pd.to_datetime(orders[col])

print(orders.dtypes)

#missing values
print(orders.isnull().sum())

#check duplicate rows
print(orders.duplicated().sum())

#Rename columns
orders.rename(columns={
    "order_purchase_timestamp": "purchase_date",
    "order_approved_at": "approved_date",
    "order_delivered_carrier_date": "carrier_delivery_date",
    "order_delivered_customer_date": "delivery_date",
    "order_estimated_delivery_date": "estimated_delivery"
}, inplace=True)

print(orders.columns)

orders["Purchase_Year"] = orders["purchase_date"].dt.year

orders["Purchase_Month"] = orders["purchase_date"].dt.month

orders["Purchase_Day"] = orders["purchase_date"].dt.day

orders["Weekday"] = orders["purchase_date"].dt.day_name()

print(
    orders[
        [
            "purchase_date",
            "Purchase_Year",
            "Purchase_Month",
            "Purchase_Day",
            "Weekday"
        ]
    ].head(10)
)

#Delivery Time
orders["Delivery_Days"] = (
    orders["delivery_date"] -
    orders["purchase_date"]
).dt.days

#Average Delivery Time
print("Average Delivery Days:", round(orders["Delivery_Days"].mean(), 2))

#Orders per Month
print("\nOrders Per Month:")
print(orders.groupby("Purchase_Month").size())

print(
    orders[
        [
            "purchase_date",
            "delivery_date",
            "Delivery_Days"
        ]
    ].head(10)
)

# Save Clean Dataset
orders.to_csv("Output/clean_orders.csv", index=False)

print("\n✅ Clean dataset saved successfully!")