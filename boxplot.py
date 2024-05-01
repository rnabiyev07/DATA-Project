import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_boxplot(column):
    # Creating a box plot
    plt.figure(figsize=(14, 8))  # Increase figure size for better readability
    sns.boxplot(x='Province/State', y=column, data=df, palette=custom_palette)

    # Customizing the plot
    plt.title(f'Box Plot of {column} Cases Across Different Province/State')
    plt.xlabel('Province/State')
    plt.ylabel(f'{column} Cases')
    plt.xticks(rotation=90)  # Rotate x-axis labels to 90 degrees for better visibility
    plt.tight_layout()  # Adjust layout for better appearance
    plt.show()

# Load dataset
df = pd.read_csv("covid_19_clean_complete.csv")

# Setting color palette for better distinction
custom_palette = sns.color_palette("pastel")

# Call the method for each column
columns_to_plot = ['Confirmed', 'Deaths', 'Recovered', 'Active']
for column in columns_to_plot:
    plot_boxplot(column)
