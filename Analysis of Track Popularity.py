import pandas as pd
import matplotlib.pyplot as plt

path = pd.read_csv(r"/Users/srijitdey/Documents/project_csvs/playlist_2010to2022.csv")

playlist_data = path
missing_values = playlist_data.isnull().sum()

playlist_data_cleaned = playlist_data.dropna()

# print(playlist_data_cleaned)

plt.figure(figsize=(9, 7))
plt.hist(playlist_data_cleaned["track_popularity"], bins=20, color="yellow", edgecolor="black")
plt.title("Analysis of Track Popularity")
plt.xlabel('Track Popularity')
plt.ylabel('Frequency')
plt.grid(axis='y')
plt.tight_layout()
plt.show()
