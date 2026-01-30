import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("superstore.csv")

print("First 5 rows:")
print(df.head())

print("\nColumns:")
print(df.columns)

print("\nTotal sales by category:")
print(df.groupby("Category")["Sales"].sum())

print("\nTotal sales by region:")
print(df.groupby("Region")["Sales"].sum())

print("\nTop 5 states by sales:")
print(df.groupby("State")["Sales"].sum().sort_values(ascending=False).head())

print("\nTop 5 sub-categories:")
print(df.groupby("Sub-Category")["Sales"].sum().sort_values(ascending=False).head())

df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True)
df["Month"] = df["Order Date"].dt.month

monthly = df.groupby("Month")["Sales"].sum()
print("\nMonthly sales:")
print(monthly)

monthly.plot()
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()