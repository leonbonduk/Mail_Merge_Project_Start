#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
with open("./Input/Names/invited_names.txt") as names:
    name_list = names.readlines()

#Replace the [name] placeholder with the actual name.
with open("./Input/Letters/starting_letter.txt") as letter:
    letter_contents = letter.read()

#Save the letters in the folder "ReadyToSend".
for name in name_list:
    formatted_name = name.strip('\n')

    with open("./Output/ReadyToSend/"+formatted_name+".txt",mode="w") as output:
        output_text = letter_contents.replace("[name]", formatted_name)
        output.write(output_text)





#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp


#Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp