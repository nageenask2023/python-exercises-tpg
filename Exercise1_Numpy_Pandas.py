import pandas as pd
import numpy as np

# Set seed for reproducibility
np.random.seed(42)

# Generate 170 rows of simulated data
n = 170

data = {
    'Duration': np.random.choice([30, 45, 60, 75, 90, 120], size=n, p=[0.1, 0.2, 0.4, 0.2, 0.05, 0.05]),
    'Pulse': np.random.randint(80, 130, size=n),
    'Maxpulse': np.random.randint(120, 180, size=n),
    'Calories': np.round(np.random.normal(loc=350, scale=80, size=n), 1)  # Normally distributed around 350
}

# Create the DataFrame
df = pd.DataFrame(data)

# Introduce a few NaN values for practice
for _ in range(5):
    idx = np.random.randint(0, n)
    df.loc[idx, 'Calories'] = np.nan

#  DATA CLEANING 
# Check missing values
print("Missing values:\n", df.isnull().sum())

# Fill missing Calories with mean
df['Calories'].fillna(df['Calories'].mean(), inplace=True)

# Basic statistics
print("\nData description:\n", df.describe())

# Save cleaned DataFrame
df.to_csv('data/Exercise1_Cleaned.csv', index=False)
print("\nCleaned DataFrame saved to data/Exercise1_Cleaned.csv")
