# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

# import pandas
# student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
import pandas as pd
file = pd.read_csv("nato_phonetic_alphabet.csv")
data = pd.DataFrame(file)
new_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# {"A": "Alfa", "B": "Bravo"}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

no_input = True
while no_input:
    user_word = input("Enter the word to translate: ")
    try:
        word_list = [letter.upper() for letter in user_word]
        code_list = [new_dict[item] for item in word_list]
    except KeyError:
        print("Only letters in the alphabet please.")
    else:
        no_input = False
print(code_list)
# code_list = [value for value in new_dict if test]
