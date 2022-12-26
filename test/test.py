import pandas as pd

'''
sentence = "What is the Airspeed velocity of an anladen swallow"

result = {word:len(word) for word in sentence.split()}

print(result)
'''
'''
weather_c = {
    "monday": 12,
    "tuesday": 14,
    "wednesday": 15,
    "thursday": 14,
    "friday": 21,
    "saturday": 22,
    "sunday": 24,
}

weather_f = {day:(temp * 1.8 + 32) for (day, temp) in weather_c.items()}

print(weather_f)
'''

student_dic = {
    "student": ["angela", "james", "lily"],
    "Score": [56, 76, 98]
}

# make student_dic into dataframe
student_df = pd.DataFrame(student_dic)

# loop thru each of the rows of a data frame
for (index, row) in student_df.iterrows():
    if row.student == "angela":
        print(row.Score)
