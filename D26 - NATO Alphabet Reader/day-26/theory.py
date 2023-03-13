# numbers = [1, 2, 3]
# # new_list = [new_item for item in list if test]
#
# new_list = [n+1 for n in numbers]
# print(new_list)
#
# a = range(1, 5)
#
# list_1 = [n*2 for n in a]
#
# print(list_1)
#
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# short_names = [name for name in names if len(name) < 5]
# long_capital_names = [name.upper() for name in names if len(name) > 5]
# print(long_capital_names)
#
# list_txt1 = open("file1.txt", "r").readlines()
# list_txt2 = open("file2.txt", "r").readlines()
# result = [int(num.strip("\n")) for num in list_txt1 if num in list_txt2]
# # Write your code above 👆
#
# print(result)


# DICTIONARY COMPREHENSION

# new_dict = {new_key:new_value for item or (key,value) in list or in dict.items() if test}
# import random
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# student_score = {name: random.randint(1, 100) for name in names}
# print(student_score)
# passed_students = {name: score for (name, score) in student_score.items() if score >= 60}
# print(passed_students)

# looping through a Pandas DataFrame

import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}
student_data_frame = pandas.DataFrame(student_dict)

# for (key, value) in student_data_frame.items()
#     print(key or value)

for (index, row) in student_data_frame.iterrows():
    print(row)
