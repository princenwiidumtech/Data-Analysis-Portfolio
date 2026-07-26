import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("/storage/emulated/0/Download/gym_data.csv")

pd.set_option("display.max_columns", None)

#Data Exploration

print(df.info())
print(df.head(10))
print(df.tail(10))
print(df.shape)
print(df.columns)
print(df.describe())
print(df.isnull().sum())

#Data Analysis

print("Average Age:", df["Age"].mean())

print("Average Duration:", df["Duration"].mean())

print("Average Calories:", df["Calories"].mean())

print("Highest Calories:", (m := df["Calories"].max()), "| Member(s):", df[df["Calories"] == m])

print("Lowest Calories:", (m := df["Calories"].min()), "| Member(s):", df[df["Calories"] == m])

print("Highest Pulse:", df["Pulse"].max(), 
      "| Member(s):", df[df["Pulse"] == df["Pulse"].max()][["Name", "Age", "Gender"]])
      
print("Lowest Pulse:", df["Pulse"].min(), 
      "| Member(s):", df[df["Pulse"] == df["Pulse"].min()][["Name", "Age", "Gender"]])
      
print(df[df["Age"] == df["Age"].max()])

print(df[df["Age"] == df["Age"].min()])

#Filtering Data

print(df[df["Age"] > 30])

print(df[df["Age"] < 25])

print(df[df["Gender"] == "Female"])

print(df[df["Gender"] == "Male"])

print(df[df["Calories"] > 400])

print(df[df["Pulse"] > 120])

#Sorting & Ranking

print(df.sort_values("Age"))

print(df.sort_values("Age", ascending=False))

print(df.sort_values("Calories", ascending=False))

print(df.sort_values("Calories"))

print(df.sort_values("Duration", ascending=False))

#Grouping Data

print(df["Gender"].value_counts())

print(df.groupby("Gender")["Age"].mean())

print(df.groupby("Gender")["Calories"].mean())

print(df.groupby("Gender")["Duration"].mean())

print(df.groupby("Gender")["Calories"].max())

print(df.groupby("Gender")["Pulse"].mean())

#Bar Chart

#df.plot(
    #x="Name",
    #y="Calories",
    #kind="bar",
    #figsize=(10,5),
    #title="Calories Burned by Gym Members"
#)

#plt.xlabel("Members")
#plt.ylabel("Calories Burned")
#plt.tight_layout()
#plt.show()

#df.plot(
    #x="Name",
    #y="Pulse",
    #kind="line",
    #figsize=(10,5),
    #title="Pulse Rate of Gym Members",
    #marker="o",
    #color="red"
#)

#plt.xlabel("Members")
#plt.ylabel("Pulse (BPM)")
#plt.tight_layout()
#plt.show()

#gender_count = df["Gender"].value_counts()

#gender_count.plot(
    #kind="pie",
    #autopct="%1.1f%%",
    #figsize=(6,6),
    #title="Gender Distrubution of Gym Members"
#)

#plt.xlabel("")
#plt.show()

#df["Age"].plot(
    #kind="hist",
    #bins=6,
    #figsize=(8,5),
    #color="skyblue",
    #edgecolor="black",
    #title="Distrubution of Gym Members Ages"
#)

#plt.xlabel("Age")
#plt.ylabel("Numbers of Members")
#plt.tight_layout()
#plt.show()

#df.plot(
    #x="Duration",
    #y="Calories",
    #kind="scatter",
    #figsize=(8,5),
    #color="green",
    #title="Workout Duration vs Calories Burned"
#)

#plt.xlabel("Workout Duration (Minutes)")
#plt.ylabel("Calories Burned")
#plt.tight_layout()
#plt.show()

df["Calories"].plot(
    kind="box",
    figsize=(5,6),
    title="Box Plot of Calories Burned"
)

plt.ylabel("Calories")
plt.tight_layout()
plt.show()