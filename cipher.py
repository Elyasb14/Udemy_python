
from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# while loop that breaks when user doesn't want to continue 

while True:
    # user inputs
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = (int(input("Type the shift number:\n")) % 26)
    # main function
    def main(direction):
        if direction == 'encode':
            encrypt2(text, shift)
        elif direction == "decode":
            decrypt2(text, shift)
    # does user want to go again?
    choice = input('Do you want to go again? ')
    if choice == 'no':
        break




# function to encrypt version 2

def encrypt2(text, shift):
    # making a list of all the letters and symbols in text
    letters = list(text)
    # list to store shifted text
    shifted_text = []
    # loop thru letters list
    for letter in letters:
        # shift letters
        if letter in alphabet:
            letter_index = alphabet.index(letter)
            if letter_index + shift < 26:
                shifted_letter = alphabet[letter_index + shift]
                shifted_text.append(shifted_letter)
            # if index is out of range
            else:
                difference = 26 - letter_index
                shifted_letter = alphabet[shift - difference]
                shifted_text.append(shifted_letter)
        # leave symbols still
        else:
            shifted_text.append(letter)
    # print shifted_letters as string
    print(''.join(shifted_text))


# function to decrypt version 2

def decrypt2(text, shift):
    # making a list of all the letters and symbols in text
    letters = list(text)
    # list to store shifted text
    shifted_text = []
    # loop thru letters list
    for letter in letters:
        # shift letters
        if letter in alphabet:
            letter_index = alphabet.index(letter)
            if 26 - letter_index > 0:
                shifted_text.append(alphabet[letter_index - shift])
            # if index is out of range
            else:
                difference = letter_index - 26
                shifted_text.append(alphabet[difference - shift])
        # leave symbols still
        else:
            shifted_text.append(letter)
    # print shifted_letters as string
    print(''.join(shifted_text))



'''
LEGACY CODE

def encrypt(text, shift):
    # list to store shifted letters
    shifted_text = []
    # loop over all letters in the text
    for letter in text:
        # obtain letter index
        letter_index = alphabet.index(letter)
        # if letter's index is in rane
        if letter_index + shift < 26:
            shifted_letter = alphabet[letter_index + shift]
            shifted_text.append(shifted_letter)
        # if letter's index is out of range
        else:
            difference = 26 - letter_index
            shifted_letter = alphabet[shift - difference]
            shifted_text.append(shifted_letter)
    print(shifted_text)
    print(''.join(shifted_text))

# function to decrypt text

def decrypt(text, shift):
    # list to store shifted letters
    shifted_text = []
    # loop over all letters in the text
    for letter in text:
        # obtain letter index
        letter_index = alphabet.index(letter)
        # if index is in range
        if 26 - letter_index > 0:
            shifted_text.append(alphabet[letter_index - shift])
        # if index is out of range
        else:
            difference = letter_index - 26
            shifted_text.append(alphabet[difference - shift])
    print(''.join(shifted_text))'''
