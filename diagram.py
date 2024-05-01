import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("covid_19_clean_complete.csv")

# Convert 'Date' column to datetime object
df['Date'] = pd.to_datetime(df['Date'])

# Filter the dataframe to include only data from 2020
df_2020 = df[df['Date'].dt.year == 2020]

# Plotting confirmed cases over time for 2020
plt.figure(figsize=(12, 8))
sns.lineplot(x=df_2020['Date'], y=df_2020['Confirmed'])
plt.title('Trend of Confirmed COVID-19 Cases in 2020')
plt.xlabel('Date')
plt.ylabel('Confirmed Cases')
plt.xticks(rotation=45)
plt.show()


# Calculating correlation coefficient
correlation_matrix = df.select_dtypes(exclude='object').corr()
correlation_coefficient = correlation_matrix['Confirmed']['Deaths']
print(f"Correlation Coefficient between Confirmed Cases and Deaths: {correlation_coefficient}")

# Correlation matrix
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix')
plt.show()

# Aggregate the data by summing up confirmed cases for each country
country_cases = df.groupby('Country/Region')['Confirmed'].sum().reset_index()

# Sort the countries based on total confirmed cases
top_10_countries = country_cases.sort_values(by='Confirmed', ascending=False).head(10)

# Plotting distribution of confirmed cases by country
plt.figure(figsize=(12, 8))
sns.barplot(x='Confirmed', y='Country/Region', data=top_10_countries, palette='viridis')
plt.title('Top 10 Countries by Confirmed COVID-19 Cases')
plt.xlabel('Confirmed Cases')
plt.ylabel('Country')
plt.show()
