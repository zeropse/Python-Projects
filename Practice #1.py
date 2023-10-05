import pandas as pd

df = pd.read_csv(r"C:\Users\deysr\OneDrive\Documents\Github\Python-Projects\csv\playlist_2010to2022.csv")
print(df['artist_name'].value_counts().head(30))