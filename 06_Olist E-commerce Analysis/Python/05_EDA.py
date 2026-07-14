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



# Analysis 1 – Order Status Distribution
status = orders["order_status"].value_counts()
print(status)

# status.plot(kind="bar")

# plt.title("Order Status Distribution")
# plt.xlabel("Order Status")
# plt.ylabel("Number of Orders")

# plt.show()


# Analysis 2 – Monthly Orders
monthly_orders = (
    orders.groupby("Purchase_Month")
    .size()
)
# print(monthly_orders)

# monthly_orders.plot(kind="line")

# plt.title("Monthly Orders")

# plt.xlabel("Month")

# plt.ylabel("Orders")

# plt.show()



# Analysis 3 – Weekday Orders
weekday_orders = (
    orders["Weekday"]
    .value_counts()
)
print(weekday_orders)

# weekday_orders.plot(kind="bar")
# plt.title("Orders by Weekday")
# plt.xlabel("Weekday")
# plt.ylabel("Orders")
# plt.show()



# Analysis 4 – Delivery Days
# print(orders["Delivery_Days"].describe())
# orders["Delivery_Days"].plot(kind="hist", bins=20)

# plt.title("Delivery Days Distribution")

# plt.xlabel("Days")

# plt.show()



# Analysis 5 – Orders Per Year
year_orders = (
    orders.groupby("Purchase_Year")
    .size()
)

print(year_orders)

# year_orders.plot(kind="bar")

# plt.title("Orders Per Year")

# plt.xlabel("Year")

# plt.ylabel("Orders")

# plt.show()



# Analysis 6 – Delivery Delay
orders["Delivery_Delay"] = (
    orders["order_delivered_customer_date"] -
    orders["order_estimated_delivery_date"]
).dt.days

print(
    orders["Delivery_Delay"].describe()
)

monthly_orders.to_csv(
    "output/monthly_orders.csv"
)

weekday_orders.to_csv(
    "output/weekday_orders.csv"
)