#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
with open('./Input/Letters/starting_letter.txt') as file:
    letter_lines = file.readlines()

with open('./Input/Names/invited_names.txt') as file:
    names = file.readlines()

for name in names:
    name = name.strip()  # Remove newline character from name
    modified_lines = []
    for line in letter_lines:
        modified_line = line.replace('[name]', name)
        modified_lines.append(modified_line)

    modified_letter = ''.join(modified_lines)
    with open(f'./Output/ReadyToSend/{name}_letter.txt', mode='w') as file:
        file.write(modified_letter)
