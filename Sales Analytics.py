import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)

df = pd.read_csv("/storage/emulated/0/Download/company_sales.csv")

#Data Exploration

print(df.info())
print(df.head())
print(df.tail())
print(df.describe())
print(df.shape)
print(df.columns)

print(len(df))
print(df["Product"].nunique())
print(df["City"].nunique())
print(df["Salesperson"].nunique())
print(df["Category"].nunique())

print(df.groupby("Product")["Revenue"].sum().sort_values(ascending=False))

print(df.groupby("City")["Revenue"].sum().sort_values(ascending=False))

print(df.groupby("Salesperson")["Revenue"].sum().sort_values(ascending=False))

print(df.groupby("Month")["Revenue"].sum().sort_values(ascending=False))

print("Average Revenue:", df["Revenue"].mean())

#Filtering Data

print(len(df[df["City"] == "Lagos"]))

print(df[df["City"] == "Lagos"]["Product"].unique())

print(len(df[df["Category"] == "Electronics"]))

print(len(df[df["Revenue"] > 1500]))

print(df[df["Revenue"] > 2000])

#Value Count

print(df["City"].value_counts())

print(df["Product"].value_counts())

print(df["Salesperson"].value_counts())

print(df["Month"].value_counts())

print(df["Category"].value_counts())

#Sort Value

print(df.sort_values("Revenue", ascending=False))

print(df.sort_values("Revenue", ascending=True))

print(df.sort_values("Revenue", ascending=False).head())

print(df.sort_values("Revenue").head())

print(df.groupby("City")["Revenue"].mean().sort_values(ascending=False))

print(len(df[(df["City"] == "Lagos") & (df["Category"] == "Electronics")]))

print(len(df[(df["City"] == "Lagos") | (df["City"] == "Abuja")]))

print(len(df[(df["Category"] == "Electronics") & (df["Revenue"] > 1000 )]))

print(df[(df["Category"] == "Furniture") | (df["Revenue"] > 2000)])

print(df[df["Category"] == "Electronics"].groupby("Salesperson")["Revenue"].sum().sort_values(ascending=False))