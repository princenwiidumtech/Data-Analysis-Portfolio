import pandas as pd
import matplotlib.pyplot as plt

pd.set_option("display.max_columns", None)
pd.set_option("display.max_row", None)

df = pd.read_csv("/storage/emulated/0/Download/supermarket_sales_1000.csv")


#Data Exploration

print(df.info())
print(df.head())
print(df.shape)
print(df.columns)
print(df.describe())
print(df.isnull().sum())
print(df.tail())
print(df["Branch"].nunique())
print(df["City"].nunique())
print(df["Product line"].nunique())
print(df["Payment"].nunique())

print(df.groupby("Branch")["Total"].sum().sort_values(ascending=False))

print(df.groupby("City")["Total"].sum().sort_values(ascending=False))

print(df.groupby("Product line")["Total"].sum().sort_values(ascending=False))

print(df.groupby("Payment")["Total"].sum().sort_values(ascending=False))

print(df.groupby("Gender")["Total"].sum().sort_values(ascending=False))

#customer analysis

print(df.groupby("Customer type")["Total"].sum().sort_values(ascending=False))

print(df["Customer type"].value_counts())

print(df.groupby("Product line")["Rating"].mean().sort_values(ascending=False))

print(df.groupby("Branch")["Rating"].mean().sort_values(ascending=False))

#Finding the "Best" and "Worst"

print(df.groupby("Product line")["Quantity"].sum().sort_values())

print(df["Payment"].value_counts())

print(df.groupby("Gender")["Quantity"].sum().sort_values(ascending=False))

print(
    df[df["Gender"] == "Male"]
    .groupby("Product line")["Total"]
    .sum()
    .sort_values(ascending=False)
)

print(df.groupby("Branch")["Quantity"].sum().sort_values(ascending=False))

print(df.groupby("Payment")["Total"].mean().sort_values(ascending=False))

print(df.groupby("City")["Rating"].mean().sort_values(ascending=False))

print(
    df.groupby("Branch")["gross income"]
    .sum()
    .sort_values(ascending=False)
)

print(
    df.groupby("Product line")["Unit price"]
    .mean()
    .sort_values(ascending=False)
)

#Visualization of chart

#branch_sales = df.groupby("Branch")["Total"].sum()

#branch_sales.plot(kind="bar")

#plt.title("Total Sales by Branch")
#plt.xlabel("Branch")
#plt.ylabel("Total Sales")
#plt.show()

#Kind Pie

#percentage_sales = df.groupby("Payment")["Total"].sum()

#percentage_sales.plot(
    #kind="pie",
    #autopct="%1.1f%%",
    #figsize=(6,6)
#)

#plt.title("Percentage of Sales by Payment Method")
#plt.ylabel("")   # Pie charts usually don't need a y-label
#plt.show()

#Kind Line

#sales = df.groupby("Product line")["Total"].sum().sort_values()

#sales.plot(
    #kind="line",
    #marker="o",
    #figsize=(10,5)
#)

#plt.title("Total Sales by Product Line")
#plt.xlabel("Product Line")
#plt.ylabel("Total Sales")
#plt.xticks(rotation=45)
#plt.grid(True)

#plt.show()

#Kind Hist

#df["Rating"].plot(
    #kind="hist",
    #bins=10,
    #figsize=(8,5)
#)

#plt.title("Distrution by Customer Rating")
#plt.xlabel("Rating")
#plt.ylabel("Frequency")

#plt.show()

#Kind Box

#df.boxplot(column="Total", figsize=(6,6))

#plt.title("Box Plot of Total Sales")

#plt.show()

#Numeric Corr

print(df.corr(numeric_only=True))

corr = df.corr(numeric_only=True)

plt.figure(figsize=(8,6))
plt.imshow(corr, cmap="coolwarm", interpolation="nearest")
plt.colorbar()

plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)
plt.yticks(range(len(corr.columns)), corr.columns)

plt.title("Coleration Matrix")

plt.show()