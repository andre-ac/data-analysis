import numpy as np
import pandas as pd

stats_dir = './data/googleplaystore.csv'
reviews_dir = './data/googleplaystore_user_reviews.csv' 

stats_data = pd.read_csv(stats_dir)
reviews_data = pd.read_csv(reviews_dir)

#Get list of all categories
Cat = list(stats_data["Category"].unique())

#sum amount of apps per
dict_cat = {}
for i in Cat:
        num = stats_data["Category"] == i
        dict_cat[i] = num.sum()
dict_cat = sorted(dict_cat.items(), key=lambda x: x[1],reverse=True)

print(f"Most popular category is {dict_cat[0][0]} with {dict_cat[0][1]} apps" )

