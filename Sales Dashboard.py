import pandas as pd
import matplotlib.pyplot as plt

pd.set_option("display.max_columns", None)
pd.set_option("display.max_row", None)

df = pd.read_csv("/storage/emulated/0/Download/Project_5_Sales_Dataset_1500_Rows.csv")

print(df.info())
print(df.head())
print(df.tail())
print(df.shape)
print(df.describe())
print(df.isnull().sum())
print(df.describe())

print(df["Sales"].sum())
print(df["Profit"].sum())
print(df["Sales"].mean())
print(df["Order ID"].nunique())

print(df.groupby("Category")["Sales"].sum().sort_values(ascending=False))

print(df.groupby("Region")["Profit"].sum().sort_values(ascending=False))

print(df.groupby("Segment")["Profit"].sum().sort_values(ascending=False))

print(df.groupby("Category")["Customer Rating"].sum().sort_values(ascending=False))

#Visualization

#Bar Chart

#Category = df.groupby("Category")["Sales"].sum().plot(
    #kind="bar",
    #figsize=(8,5)
#)

#plt.title("Total Sales by Category")
#plt.xlabel("Category")
#plt.ylabel("Sales")

#plt.show()

#Pie Chart

#df.groupby("Region")["Profit"].sum().plot(
    #kind="pie",
    #autopct="1%.1f%%",
    #figsize=(6,6)
#)

#plt.title("Profit by Region")
#plt.ylabel("")

#plt.show()

#df["Customer Rating"].plot(
    #kind="hist",
    #bins=8,
    #figsize=(8,5)
#)

#plt.title("Customer Rating Distribution")
#plt.xlabel("Rating")
#plt.ylabel("Frequency")

#plt.show()

df["Sales"].plot(
    kind="box",
    figsize=(5,6)
)

plt.title("Sales Distribution")

plt.show()