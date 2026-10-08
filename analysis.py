import pandas as pd

# Load dataset
file_path = r"C:\Users\DELL\Downloads\archive\SuperStoreOrders.csv"

df = pd.read_csv(file_path, encoding="utf-8-sig")

# Clean Sales column
df["sales"] = pd.to_numeric(
    df["sales"].astype(str).str.replace(",", "", regex=False)
)

# Convert Profit to numeric
df["profit"] = pd.to_numeric(df["profit"], errors="coerce")

# Convert date columns
df["order_date"] = pd.to_datetime(
    df["order_date"], format="mixed", dayfirst=False
)

df["ship_date"] = pd.to_datetime(
    df["ship_date"], format="mixed", dayfirst=False
)

print("Data loaded successfully!")
print("Rows:", len(df))
print("Columns:", len(df.columns))
print(df.head())


# Overall KPIs
total_orders = df["order_id"].nunique()
total_sales = df["sales"].sum()
total_profit = df["profit"].sum()
average_profit = df["profit"].mean()
profit_margin = (total_profit / total_sales) * 100

print("\n--- Overall KPIs ---")
print("Total Orders:", total_orders)
print("Total Sales:", round(total_sales, 2))
print("Total Profit:", round(total_profit, 2))
print("Average Profit:", round(average_profit, 2))
print("Profit Margin:", round(profit_margin, 2), "%")

# Year-wise Sales and Profit
year_analysis = (
    df.groupby("year")
    .agg(
        total_sales=("sales", "sum"),
        total_profit=("profit", "sum")
    )
    .round(2)
)

print("\n--- Year-wise Sales & Profit ---")
print(year_analysis)

# Category-wise Sales and Profit
category_analysis = (
    df.groupby("category")
    .agg(
        total_sales=("sales", "sum"),
        total_profit=("profit", "sum")
    )
    .sort_values("total_sales", ascending=False)
    .round(2)
)

print("\n--- Category-wise Sales & Profit ---")
print(category_analysis)

# Region-wise Sales and Profit
region_analysis = (
    df.groupby("region")
    .agg(
        total_sales=("sales", "sum"),
        total_profit=("profit", "sum")
    )
    .sort_values("total_sales", ascending=False)
    .round(2)
)

print("\n--- Region-wise Sales & Profit ---")
print(region_analysis)

# Top 10 Customers by Sales
top_customers = (
    df.groupby("customer_name")
    .agg(
        total_sales=("sales", "sum"),
        total_profit=("profit", "sum")
    )
    .sort_values("total_sales", ascending=False)
    .head(10)
    .round(2)
)

print("\n--- Top 10 Customers ---")
print(top_customers)

# Discount vs Profit Analysis
discount_analysis = (
    df.groupby("discount")
    .agg(
        records=("discount", "size"),
        total_sales=("sales", "sum"),
        total_profit=("profit", "sum"),
        average_profit=("profit", "mean")
    )
    .round(2)
)

print("\n--- Discount vs Profit ---")
print(discount_analysis)

# Top 10 Products by Sales
top_products = (
    df.groupby("product_name")
    .agg(
        total_sales=("sales", "sum"),
        total_profit=("profit", "sum")
    )
    .sort_values("total_sales", ascending=False)
    .head(10)
    .round(2)
)

print("\n--- Top 10 Products ---")
print(top_products)

# Export cleaned dataset for Power BI
output_file = r"C:\Users\DELL\SalesAnalytics\SuperStoreOrders_Cleaned.csv"

df.to_csv(output_file, index=False)

print("\n--- Export Complete ---")
print("Cleaned dataset saved at:")
print(output_file)