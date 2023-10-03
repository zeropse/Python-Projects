import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv(r"/Users/srijitdey/Documents/project_csvs/bestsellers with categories.csv")
# print(df.head())
# print(df.shape)

df = df.rename(columns={"Name": "Book Title"})
data_frame = df
# print(df.info())
# print(df.isnull().sum())
# print(df.describe())

years = np.array([2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019])
ratings = np.array([3, 4, 2, 5, 1, 4, 3, 5, 2, 4, 3])

plt.figure(figsize=(10,10))
plt.plot(years, ratings, marker='D', color="red", linestyle='-')
plt.xlabel("Year")
plt.xticks(years)
plt.ylabel("Rating")
plt.title("Most Rated Book of each Year")
plt.grid(True)
plt.show()
