with open("./Input/Letters/starting_letter.txt") as letter:
    content = letter.read()
with open("./Input/Names/invited_names.txt") as list:
    list_of_names = list.readlines()
    for name in list_of_names:
        new_letter = content.replace("[name]", name.strip())
        with open(f"./Output/ReadyToSend/letter_{name}.txt", mode="w") as file:
            file.write(new_letter)
