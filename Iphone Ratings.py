import pandas as pd
import numpy as np
import plotly.express as px


iphone_data = pd.read_csv(r"C:\Users\deysr\OneDrive\Documents\Github\Python-Projects\csv\apple_products.csv")
# print(iphone_data.head())
# print(iphone_data.describe())

highest_rated = iphone_data.sort_values(by = ["Star Rating"], ascending= False)
highest_rated = highest_rated.head(10)
print(highest_rated["Product Name"])

#Highest Ratings of Iphone
iphones = highest_rated["Product Name"].value_counts()
label = iphones.index
counts = highest_rated["Number Of Ratings"]
figure = px.bar(highest_rated, x=label,
                y=counts,
                title="Ratings of Iphone")
figure.show()

# Reviews Of Highest Rated Phones

iphones = highest_rated["Product Name"].value_counts()
label = iphones.index
counts = highest_rated["Number Of Reviews"]
figure = px.bar(highest_rated, x=label,
                y = counts,
            title="Reviews of Highest Rated iPhones")
figure.show()

