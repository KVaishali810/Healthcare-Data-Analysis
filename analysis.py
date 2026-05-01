import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load Data
df = pd.read_csv('data/healthcare_data.csv')

# 2. Data Cleaning
df.dropna(inplace=True) # Removing null values
df['Date'] = pd.to_datetime(df['Date']) # Ensure dates are correct

# 3. Exploratory Data Analysis (EDA)
print(df.describe())
print(df['Disease_Type'].value_counts())

# 4. Visualization: Disease Prevalence
plt.figure(figsize=(10, 6))
sns.countplot(x='Disease_Type', data=df)
plt.title('Prevalence of Diseases')
plt.savefig('disease_trend.png') # Save for GitHub README
plt.show()

# 5. Correlation Heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Risk Factor Correlation')
plt.show()
