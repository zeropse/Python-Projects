import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data_frame = pd.read_csv(r"/Users/srijitdey/Documents/project_csvs/Sample - Superstore.csv", encoding="windows-1252")
df = data_frame
# print(df.head())
# print(df.index)
# print(df.info())
# print(df.describe())

df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])
df["Order Month"] = df["Order Date"].dt.month
df["Order Year"] = df["Order Date"].dt.year
df["Order Day of the Week"] = df["Order Date"].dt.dayofweek
# print(df)
df.query("`Order Month`==11")
# Calculating Monthly Sales
Monthly_Sales = df.groupby("Order Month")["Sales"].sum().reset_index()
# print(Monthly_Sales)

plt.figure(figsize=(7,7))
plt.xlabel("Order Month")
plt.ylabel("Sales")
plt.title("Monthly Sales")
plt.plot(Monthly_Sales,linestyle='-.',color='red')
plt.xticks(np.arange(1,13,))
plt.yticks(np.arange(40000,350000,50000))
plt.show()

# Calculating Monthly Profits
Monthly_Profits = df.groupby("Order Month")["Profit"].sum().reset_index()
# print(Monthly_Profits)

plt.figure(figsize=(7,7))
plt.xlabel("Order Month")
plt.ylabel("Profits")
plt.title("Monthly Profits")
plt.plot(Monthly_Profits,linestyle='-.',color='k')
plt.xticks(np.arange(1,13,))
plt.yticks(np.arange(5000,50000,10000))
plt.show()

