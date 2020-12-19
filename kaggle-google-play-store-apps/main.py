import numpy as np
import pandas as pd

stats_dir = './data/googleplaystore.csv'
reviews_dir = './data/googleplaystore_user_reviews.csv'

stats_data = pd.read_csv(stats_dir)
reviews_data = pd.read_csv(reviews_dir)

print(stats_data.head())


###Most popular category###
#Get list of all categories
Cat = list(stats_data["Category"].unique())

#sum amount of apps per cat
dict_cat = {}
for i in Cat:
    num = stats_data["Category"] == i
    dict_cat[i] = num.sum()
dict_cat = sorted(dict_cat.items(), key=lambda x: x[1],reverse=True)

print(f"Most popular category is {dict_cat[0][0]} with {dict_cat[0][1]} apps")

###App with the largest size###
dict_sizes = {}

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

###Apps with largest num of install###
unique_installs = stats_data["Installs"].unique()
clean_installs = stats_data
#print(stats_data.groupby(["Installs"]).count()["App"])
# ['10,000+' '500,000+' '5,000,000+' '50,000,000+' '100,000+' '50,000+'
#  '1,000,000+' '10,000,000+' '5,000+' '100,000,000+' '1,000,000,000+'
#  '1,000+' '500,000,000+' '50+' '100+' '500+' '10+' '1+' '5+' '0+' '0'
#  'Free']
#remove + and replace , with nothing
clean_installs["Installs"] = clean_installs["Installs"].str.replace("+","").str.replace(",","")[~clean_installs["Installs"].str.contains("Free")].astype(int)
sorted_installs = clean_installs.groupby("App")["Installs"].sum().reset_index().sort_values(by= "Installs" , ascending = False).head(5)

print("The top 5 Apps with the most downloads are " + str(list(sorted_installs["App"])))
