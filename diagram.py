import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def analyze_covid_data(column, df):
    # Convert 'Date' column to datetime object
    df['Date'] = pd.to_datetime(df['Date'])

    # Filter the dataframe to include only data from 2020
    df_2020 = df[df['Date'].dt.year == 2020]

    # Plotting confirmed cases over time for 2020
    plt.figure(figsize=(12, 8))
    sns.lineplot(x=df_2020['Date'], y=df_2020[column])
    plt.title(f'Trend of {column} COVID-19 Cases in 2020')
    plt.xlabel('Date')
    plt.ylabel(f'{column} Cases')
    plt.xticks(rotation=45)
    plt.show()

    # Calculating correlation coefficient
    correlation_matrix = df.select_dtypes(exclude='object').corr()
    correlation_coefficient = correlation_matrix['Confirmed'][column]
    print(f"Correlation Coefficient between Confirmed Cases and {column}: {correlation_coefficient}")

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
    plt.title(f'Top 10 Countries by {column} COVID-19 Cases')
    plt.xlabel(f'{column} Cases')
    plt.ylabel('Country')
    plt.show()


# Load the dataset
df = pd.read_csv("covid_19_clean_complete.csv")
# Call the method for each column
columns_to_analyze = ['Deaths', 'Recovered', 'Active', 'Confirmed']
for column in columns_to_analyze:
    analyze_covid_data(column, df)
