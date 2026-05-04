# TASK 5
# Load Dataset
import pandas as pd
df = pd.read_csv(r"D:\Prodigy Data Science\US_Accidents_March23.csv", nrows=50000)
df.head()

# Select Important Columns
df = df[['Severity', 'Start_Time', 'Weather_Condition', 'Visibility(mi)', 'Temperature(F)', 'Start_Lat', 'Start_Lng']]

# Convert Time
df['Start_Time'] = pd.to_datetime(df['Start_Time'])
df['Hour'] = df['Start_Time'].dt.hour

# Check Missing Values
df.isnull().sum()

# Handle Weather
df['Weather_Condition'].fillna(df['Weather_Condition'].mode()[0], inplace=True)

# Handle Numerical Columns
df['Visibility(mi)'].fillna(df['Visibility(mi)'].mean(), inplace=True)
df['Temperature(F)'].fillna(df['Temperature(F)'].mean(), inplace=True)

# Verify Cleaning
df.isnull().sum()

# Accidents by Time
import seaborn as sns
import matplotlib.pyplot as plt
sns.histplot(df['Hour'], bins=24)
plt.title("Accidents by Time of Day")
plt.show()

# Accidents by Weather
top_weather = df['Weather_Condition'].value_counts().head(10)
sns.barplot(x=top_weather.values, y=top_weather.index)
plt.title("Top Weather Conditions")
plt.show()

# Accident Hotspots
plt.figure(figsize=(8,6))
plt.scatter(df['Start_Lng'], df['Start_Lat'], alpha=0.1)
plt.title("Accident Hotspots")
plt.show()

# Severity Analysis
sns.countplot(x='Severity', data=df)
plt.title("Accident Severity")
plt.show()