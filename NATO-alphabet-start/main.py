student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas as pd
student_data_frame = pd.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
alphabet_df = pd.read_csv("nato_phonetic_alphabet.csv")

# print(alphabet_df)
alphabet_dict = {code.letter: code.code for (letter, code) in alphabet_df.iterrows()}
# print(alphabet_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Input a word mate: ").upper()
phonetic_word = [alphabet_dict[letter] for letter in user_input]
print(phonetic_word)

