import pandas as pd

df = pd.read_csv(r"/Users/srijitdey/Documents/project_csvs/playlist_2010to2022.csv")

print(df['artist_name'].value_counts().head(30))