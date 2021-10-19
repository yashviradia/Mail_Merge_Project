invited_names = open("./Input/Names/invited_names.txt")
starting_letter = open("./Input/Letters/starting_letter.txt", mode="r")

names = invited_names.readlines()
contents = starting_letter.readlines()

for invitees in names:
    for lines in contents:
        new_lines = lines.replace("[name]", f"{invitees.strip()}")

        # create a new file using naming "letter_for_{invitees}"
        with open(f"./Output/ReadyToSend/letter_for_{invitees.strip()}", mode="a+") as new_file:
            new_file.write(new_lines)

invited_names.close()
starting_letter.close()
