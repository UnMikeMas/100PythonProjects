# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("The file was closed")
#
# raise TypeError("Made up TypeError")

height = float(input("Give me your height: "))
weight = int(input("Give me your weight: "))

if height>3:
    raise ValueError("Human height shouldn't be that much, monster")

bmi = weight/(height**2)
print(bmi)