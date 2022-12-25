import pandas as pd
'''
data = pd.read_csv("weather_data.csv")

average_temp = data["temp"].mean()
max_temp = data["temp"].max()


# print(data[data.day == "Monday"])
# print(data[data.temp == max_temp])

monday = data[data.day == "Monday"]
# print(int(monday.temp) * 1.8 + 32)
'''
# create a dataframe

data_dict = {
    "students": ["elyas", "lucy"],
    "scores": [76, 86]
}

data = pd.DataFrame(data_dict)
data.to_csv("new_data.csv")
print(data)


