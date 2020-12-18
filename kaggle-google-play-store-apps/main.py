import numpy as np
import pandas as pd

stats_dir = './data/googleplaystore.csv'
reviews_dir = './data/googleplaystore_user_reviews.csv'

stats_data = pd.read_csv(stats_dir)
reviews_data = pd.read_csv(reviews_dir)

print(stats_data.head())

#Get list of all categories
Cat = list(stats_data["Category"].unique())

#sum amount of apps per
dict_cat = {}
for i in Cat:
    num = stats_data["Category"] == i
    dict_cat[i] = num.sum()
dict_cat = sorted(dict_cat.items(), key=lambda x: x[1],reverse=True)

print(f"Most popular category is {dict_cat[0][0]} with {dict_cat[0][1]} apps")

dict_sizes = {}

#remove all that aren't floats

#not ideal as this would be slow on large datasets
# for i in stats_data.itertuples():
#         if i[5][-1] == "M":
#                 size_clean = i[5][:-1] * 1000000
#         elif i[5][-1] == "k":
#                 size_clean = i[5][:-1] * 1000
#         else:
#                 print("Error 001")
#                 print(i)

#         dict_sizes[i[1]] = size_clean
