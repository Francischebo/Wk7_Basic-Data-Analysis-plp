import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Task 1: Load and Explore the Dataset
# Load the dataset
file_path = 'Churn_Modelling.csv'  # Update the path if necessary
data = pd.read_csv(file_path)

# Display the first few rows
print("Dataset Preview:")
print(data.head())

# Explore the structure of the dataset
print("\nDataset Information:")
data.info()

# Check for missing values
missing_values = data.isnull().sum()
print("\nMissing Values:")
print(missing_values)

# Task 2: Basic Data Analysis
# Basic statistics for numerical columns
print("\nBasic Statistics:")
print(data.describe())

# Grouping by a categorical column and computing mean of a numerical column
grouped_means = data.groupby('Geography')['Balance'].mean()
print("\nAverage Balance by Geography:")
print(grouped_means)

# Task 3: Data Visualization
# Set the theme for plots
sns.set_theme(style="whitegrid")

# Line Chart: Trends in CreditScore vs. Age
plt.figure(figsize=(10, 6))
sns.lineplot(data=data, x="Age", y="CreditScore", label="CreditScore by Age")
plt.title("CreditScore Trends by Age")
plt.xlabel("Age")
plt.ylabel("CreditScore")
plt.legend()
plt.show()

# Bar Chart: Average Balance by Geography
plt.figure(figsize=(8, 5))
sns.barplot(data=data, x="Geography", y="Balance", ci=None, palette="viridis")
plt.title("Average Balance by Geography")
plt.xlabel("Geography")
plt.ylabel("Average Balance ($)")
plt.show()

# Histogram: Distribution of Age
plt.figure(figsize=(8, 5))
sns.histplot(data=data, x="Age", bins=20, kde=True, color="blue")
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

# Scatter Plot: Balance vs. EstimatedSalary
plt.figure(figsize=(8, 6))
sns.scatterplot(data=data, x="Balance", y="EstimatedSalary", hue="Exited", palette="coolwarm", alpha=0.7)
plt.title("Balance vs. Estimated Salary (Colored by Churn)")
plt.xlabel("Balance ($)")
plt.ylabel("Estimated Salary ($)")
plt.legend(title="Churned")
plt.show()
