import pandas as pd
import matplotlib.pyplot as plt

# Create DataFrames
df1 = pd.DataFrame({
    'Student': ['A', 'B', 'C', 'D'],
    'Math': [85, 92, 88, 75],
    'Science': [90, 80, 78, 88]
})

df2 = pd.DataFrame({
    'Student': ['A', 'B', 'C', 'D'],
    'English': [78, 85, 89, 82],
    'History': [80, 75, 85, 90]
})

# Merge DataFrames
df = pd.merge(df1, df2, on='Student')
print("Merged DataFrame:\n", df)

# Descriptive Statistics
print("\nDescriptive Analysis:\n", df.describe())

# Pivot Table (Average Scores Per Subject)
pivot = pd.melt(df, id_vars=["Student"], var_name="Subject", value_name="Marks")
pivot_table = pivot.pivot_table(index="Subject", values="Marks", aggfunc=["mean", "max", "min"])
print("\nPivot Table (Aggregated):\n", pivot_table)

# Prepare data for plotting
x = df['Student']
y_math = df['Math']
y_science = df['Science']

# Line Plot
plt.figure(figsize=(10, 6))
plt.plot(x, y_math, marker='o', label='Math')
plt.plot(x, y_science, marker='s', label='Science')
plt.title("Line Plot - Subject Scores")
plt.xlabel("Student")
plt.ylabel("Marks")
plt.legend()
plt.grid(True)
plt.show()

# Bar Plot
plt.figure(figsize=(8, 5))
plt.bar(x, y_math, color='skyblue')
plt.title("Bar Plot - Math Scores")
plt.xlabel("Student")
plt.ylabel("Marks")
plt.show()

# Scatter Plot
plt.figure(figsize=(6, 6))
plt.scatter(y_math, y_science, color='green')
plt.title("Scatter Plot - Math vs Science")
plt.xlabel("Math Marks")
plt.ylabel("Science Marks")
plt.grid(True)
plt.show()

# Pie Chart
plt.figure(figsize=(6, 6))
plt.pie(y_math, labels=x, autopct='%1.1f%%', startangle=90)
plt.title("Pie Chart - Math Score Distribution")
plt.show()