import pandas as pd

# turn data into dataframe
data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
'''
grey_squirells = data[data["Primary Fur Color"] == "Gray"]
black_squirells = data[data["Primary Fur Color"] == "Black"]
cinnamon_squirells = data[data["Primary Fur Color"] == "Cinnamon"]


print(len(grey_squirells))
print(len(cinnamon_squirells))
print(len(black_squirells))
'''

# get counts of all items in primary color column
fur_counts = data["Primary Fur Color"].value_counts()
print(fur_counts)

# write fur_counts into a csv
fur_counts.to_csv("fur_counts.csv")

