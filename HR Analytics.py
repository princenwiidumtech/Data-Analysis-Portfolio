import pandas as pd
import matplotlib.pyplot as plt

pd.set_option("display.max_columns", None)
pd.set_option("display.max_row", None)

import pandas as pd

df = pd.read_csv("/storage/emulated/0/Download/Project_4_HR_Analytics_Dataset_1001_Rows.csv")

print(df.info())
print(df.head(10))
print(df.tail())
print(df.shape)
print(df.columns)
print(df.describe())
print(df.isnull().sum())
print(df.duplicated().sum())

print(df["Department"].value_counts())
print(df["Gender"].value_counts())
print(df["Job Role"].value_counts())
print(df["Promotion"].value_counts())
print(df["Attrition"].value_counts())

print(df.groupby("Department")["Monthly Salary"].mean().sort_values(ascending=False))

print(df.groupby("Job Role")["Performance Score"].mean().sort_values(ascending=False))

print(df.groupby("Department")["Performance Score"].mean().sort_values(ascending=False))

print(
    df[df["Attrition"] == "Yes"]
      .groupby("Department")
      .size()
      .sort_values(ascending=False)
)

print(
    df.groupby("Gender")["Overtime Hours"]
      .mean()
      .sort_values(ascending=False)
)

print(
    df.groupby("Job Role")["Monthly Salary"].mean().sort_values(ascending=False)
)

print(
    df.groupby("Department")["Training Hours"].mean().sort_values(ascending=False)
)

print(
    df.groupby("Gender")["Performance Score"].mean().sort_values(ascending=False)
)

print(
    df.groupby("Department")["Projects Completed"]
      .mean()
      .sort_values(ascending=False)
)

print(
    df.groupby("Department")["Age"].mean().sort_values(ascending=False)
)

#Visualisation

#Bar Chart

#Salary = df.groupby("Department")["Monthly Salary"].mean().sort_values(ascending=False)

#Salary.plot(
    #kind="bar",
    #figsize=(8,5)
#)

#plt.title("Average Monthly Salary by Department")
#plt.xlabel("Department")
#plt.ylabel("Average Monthly Salary")

#plt.show()

#Pie Chart

#department = df["Department"].value_counts()

#department.plot(
    #kind="pie",
    #autopct="%1.1f%%",
    #figsize=(6,6)
#)

#plt.title("Employee Distribution by Department")
#plt.ylabel("")

#plt.show()

#Hist Chart

df["Age"].plot(
    kind="hist",
    bins=10,
    figsize=(8,5)
)

plt.title("Distrubution by Employee Ages")
plt.xlabel("Age")
plt.ylabel("Frequency")

plt.show()