#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Names/invited_names.txt", "r") as invited_names_file:
    with open("./Input/Letters/starting_letter.txt", "r") as letter_in_file:

        letter_string = letter_in_file.read()
        invited_names_array = invited_names_file.readlines()

        formated_letters = []
        for invited_name in invited_names_array:
            formated_letter = letter_string.replace("[name]", invited_name.removesuffix("\n"))
            formated_letters.append(formated_letter)


            with open(f"./Output/ReadyToSend/letter_to_{invited_name.removesuffix("\n")}.txt", "w") as letter_out_file:
                letter_out_file.write(formated_letter)

