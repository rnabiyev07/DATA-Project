import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your dataset
df = pd.read_csv("covid_19_clean_complete.csv")

# Setting color palette for better distinction
custom_palette = sns.color_palette("pastel")

# Creating a box plot
plt.figure(figsize=(14, 8))  # Increase figure size for better readability
sns.boxplot(x='Province/State', y='Confirmed', data=df, palette=custom_palette)

# Customizing the plot
plt.title('Box Plot of Confirmed Cases Across Different Province/State')
plt.xlabel('Province/State')
plt.ylabel('Confirmed Cases')
plt.xticks(rotation=90)  # Rotate x-axis labels to 90 degrees for better visibility
plt.tight_layout()  # Adjust layout for better appearance
plt.show()
