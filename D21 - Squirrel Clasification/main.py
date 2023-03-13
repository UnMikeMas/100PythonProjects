# # with open("weather_data.csv") as file:
# #     data = file.readlines()
# #     print(data)"
#
# # import csv
# #
# # with open("weather_data.csv") as file:
# #     data = csv.reader(file)
# #     temperatures = []
# #     for row in data:
# #         if row[1]!="temp":
# #             temperatures.append(int(row[1]))
# #     print(temperatures)
#
# import pandas as pd
#
# data = pd.read_csv("weather_data.csv")
# temp_list = data["temp"]
# avg_temp = sum(temp_list)/len(temp_list)
# print(temp_list.max())
#
# # Get info from rows
#
# print(data[data.temp == temp_list.max()].temp)
#
# monday = data[data.day == "Monday"]
#
# print(int(monday.temp)*1.8+32)
#
# # Creating a DataFrame from scratch
#
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "grades": [76, 56, 65]
# }
#
# new_data = pd.DataFrame(data_dict)
#
# new_data.to_csv("new_data.csv")

import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
Fur_Color_Col = data["Primary Fur Color"]
total = []
x = 0
y = 0
z = 0
for i in Fur_Color_Col:
    if i == "Gray":
        x += 1
    elif i == "Cinnamon":
        y += 1
    elif i == "Black":
        z += 1
total.append(x)
total.append(y)
total.append(z)
print(total)

sq_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "count": total
}

new_file = pd.DataFrame(sq_dict)
new_file.to_csv("final.csv")