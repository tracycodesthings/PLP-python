import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Load dataset (Iris dataset from sklearn for simplicity)
try:
    iris = load_iris(as_frame=True)  # Load as a pandas-friendly dataframe
    df = iris.frame
    df['species'] = df['target'].map(dict(enumerate(iris.target_names)))  # Map numeric target to species names
    print("✅ Dataset loaded successfully!")
except Exception as e:
    print("❌ Error loading dataset:", e)

# Display first 5 rows
print("\n🔹 First 5 rows of dataset:")
print(df.head())

# Inspect structure
print("\n🔹 Dataset info:")
df.info()

# Check missing values
print("\n🔹 Missing values per column:")
print(df.isnull().sum())

# Clean dataset (Iris dataset has no missing values, but here’s how you’d handle it)
df = df.dropna()  # Drop rows with missing values

# -----------------------------
# 📊 Task 2: Basic Data Analysis
# -----------------------------

# Compute basic statistics
print("\n🔹 Basic statistics:")
print(df.describe())

# Group by categorical column (species) and compute mean of numerical columns
print("\n🔹 Mean values by species:")
group_means = df.groupby('species').mean()
print(group_means)

# Interesting findings
print("\n🔹 Insights:")
print("Setosa flowers have smaller petal length & width compared to Versicolor and Virginica.")
print("Virginica generally has the largest measurements in all dimensions.")

# -----------------------------
# 📊 Task 3: Data Visualization
# -----------------------------

# 1️⃣ Line Chart - simulate a trend (cumulative sepal length per row index)
plt.figure(figsize=(8,5))
df['sepal length (cm)'].cumsum().plot(kind='line')
plt.title("Cumulative Sepal Length over Samples")
plt.xlabel("Sample Index")
plt.ylabel("Cumulative Sepal Length (cm)")
plt.grid(True)
plt.show()

# 2️⃣ Bar Chart - average petal length per species
plt.figure(figsize=(8,5))
sns.barplot(x="species", y="petal length (cm)", data=df)
plt.title("Average Petal Length by Species")
plt.xlabel("Species")
plt.ylabel("Petal Length (cm)")
plt.show()

# 3️⃣ Histogram - distribution of sepal length
plt.figure(figsize=(8,5))
plt.hist(df['sepal length (cm)'], bins=15, color='skyblue', edgecolor='black')
plt.title("Distribution of Sepal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Frequency")
plt.show()

# 4️⃣ Scatter Plot - sepal length vs petal length
plt.figure(figsize=(8,5))
sns.scatterplot(x="sepal length (cm)", y="petal length (cm)", hue="species", data=df)
plt.title("Sepal Length vs Petal Length by Species")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.show()