# item in starting_letter.txt that we want to replace
PLACEHOLDER = "[name]"

# pure names as strings with no new lines
stripped_names = []

# open the file with names
with open("/Users/ebianchi/Documents/programs/Udemy_python/Mail_Merge/Input/Names/invited_names.txt") as names_file:
    # obtain names
    names = names_file.readlines()
    # loop thru names and strip new line and add to stripped names list
    for name in names:
        stripped_name = name.strip()
        stripped_names.append(stripped_name)
    

# open starting_letter.txt
with open("/Users/ebianchi/Documents/programs/Udemy_python/Mail_Merge/Input/Letters/starting_letter.txt") as letter_file:
    # get the contents of the file 
    letter_contents = letter_file.read()
    # loop over names and write new file with PLACEHOLDER replaced with name 
    for name in stripped_names:
        new_letter = letter_contents.replace(PLACEHOLDER, name)
        with open(f"/Users/ebianchi/Documents/programs/Udemy_python/Mail_Merge/Output/ReadyToSend/letter_for_{name}", 'w') as completed_letter:
            completed_letter.write(new_letter)

