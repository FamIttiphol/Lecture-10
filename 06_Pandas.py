import pandas as pd

data = {
    "Name": ["NongFamINE", "John", "Alice"],
    "Age": [18, 25, 30],
    "City": ["New York", "London", "Tokyo"]
    }
df = pd.DataFrame(data)
print("DataFrame:\n", df)

average_age = df["Age"].mean()
print("\nAverage Age: {average_age}")

filtered_df = df[df["Age"] > 20]
print("\nFiltered DataFrame (Age > 20):\n", filtered_df)

df["Salary"] = [50000, 60000, 70000]
print("\nDataFrame with Salary Column:\n", df)