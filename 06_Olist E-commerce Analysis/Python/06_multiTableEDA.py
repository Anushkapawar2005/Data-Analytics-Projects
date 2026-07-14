import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

engine = create_engine(
    "mysql+pymysql://root:2005anu@localhost:3306/olist"
)

orders = pd.read_sql("SELECT * FROM olist_orders_dataset", engine)

customers = pd.read_sql("SELECT * FROM olist_customers_dataset", engine)

order_items = pd.read_sql("SELECT * FROM olist_order_items_dataset", engine)

products = pd.read_sql("SELECT * FROM olist_products_dataset", engine)

payments = pd.read_sql("SELECT * FROM olist_order_payments_dataset", engine)

reviews = pd.read_sql("SELECT * FROM olist_order_reviews_dataset", engine)

translation = pd.read_sql(
    "SELECT * FROM product_category_name_translation",
    engine
)


# Analysis 1 – Revenue by State
orders_customers = pd.merge(
    orders,
    customers,
    on="customer_id"
)

full_data = pd.merge(
    orders_customers,
    order_items,
    on="order_id"
)

state_revenue = (
    full_data
    .groupby("customer_state")["price"]
    .sum()
    .sort_values(ascending=False)
)

# print(state_revenue.head(10))

# state_revenue.head(10).plot(kind="bar")

# plt.title("Top 10 States by Revenue")

# plt.xlabel("State")

# plt.ylabel("Revenue")

# # plt.show()



# Analysis 2 – Top Product Categories
product_sales = pd.merge(
    order_items,
    products,
    on="product_id"
)

product_sales = pd.merge(
    product_sales,
    translation,
    on="product_category_name",
    how="left"
)
top_categories = (
    product_sales
    .groupby("product_category_name_english")["price"]
    .sum()
    .sort_values(ascending=False)
)

print(top_categories.head(10))
# top_categories.head(10).plot(kind="bar")

# plt.title("Top Product Categories")

# plt.xlabel("Category")

# plt.ylabel("Revenue")

# plt.show()



# Analysis 3 – Payment Method
payment_counts = (
    payments["payment_type"]
    .value_counts()
)

print(payment_counts)

# payment_counts.plot(kind="bar")

# plt.title("Payment Methods")
# plt.xlabel("Payment Type")
# plt.ylabel("Orders")

# plt.show()





# Analysis 4 – Review Score
rating = (
    reviews["review_score"]
    .value_counts()
    .sort_index()
)

print(rating)
# rating.plot(kind="bar")

# plt.title("Review Score")

# plt.xlabel("Rating")

# plt.ylabel("Count")

# plt.show()




# Analysis 5 – Top 10 Cities
city_orders = (
    customers["customer_city"]
    .value_counts()
    .head(10)
)

print(city_orders)

city_orders.plot(kind="bar")

plt.title("Top 10 Customer Cities")

plt.xlabel("City")

plt.ylabel("Customers")

plt.show()




# Analysis 6 – Average Payment Value

print(
    payments["payment_value"].describe()
)
print(
    "Average Payment:",
    round(
        payments["payment_value"].mean(),
        2
    )
)


state_revenue.to_csv(
    "output/state_revenue.csv"
)

top_categories.to_csv(
    "output/top_categories.csv"
)