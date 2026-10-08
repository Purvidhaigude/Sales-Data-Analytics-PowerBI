# Sales & Profit Analytics Dashboard

An interactive Sales & Profit Analytics Dashboard built using **Python, Pandas, SQL, and Power BI** to analyze sales performance, profitability, customers, products, regions, categories, and discount impact.

## 📊 Project Overview

This project analyzes the Superstore sales dataset to identify important business trends and performance indicators.

The workflow includes:

- Data cleaning and preprocessing using Python and Pandas
- Sales and profit analysis using SQL
- Exploratory data analysis
- Customer and product performance analysis
- Discount vs. profit analysis
- Interactive dashboard development using Power BI

## 🛠️ Technologies Used

- Python
- Pandas
- SQL / MySQL
- Power BI
- Git & GitHub

## 📌 Key KPIs

| KPI | Value |
|---|---:|
| Total Sales | 12,642,905 |
| Total Profit | 1,469,035 |
| Total Orders | 25,035 |
| Profit Margin | 11.62% |

## 📈 Dashboard Analysis

The Power BI dashboard includes:

- Year-wise Sales and Profit
- Category-wise Sales
- Region-wise Sales
- Average Profit by Discount
- Top 10 Customers by Sales
- Top 10 Products by Sales
- Year, Category, and Region filters

## 🔍 Key Insights

- Sales increased consistently from 2011 to 2014.
- Technology generated the highest sales and profit among the three major categories.
- Central region recorded the highest sales among the analyzed regions.
- Higher discount levels were generally associated with lower or negative profit in the dataset.
- A small group of customers and products contributed significantly to overall sales.
- The overall profit margin was approximately 11.62%.

## 🧹 Data Preparation

The dataset was cleaned using Python and Pandas.

Major preprocessing steps included:

- Handling mixed date formats
- Converting sales values into numeric format
- Removing comma separators from sales values
- Converting date columns to proper date types
- Checking missing values
- Checking duplicate records
- Exporting the cleaned dataset for Power BI analysis

## 📂 Project Structure

```text
Sales-Data-Analytics-PowerBI/
│
├── analysis.py
├── SuperStoreOrders_Cleaned.csv
├── sales analysis.pbix
└── README.md
