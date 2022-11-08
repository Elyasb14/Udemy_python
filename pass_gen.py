#Password Generator Project


# import modules and initial option variables
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# initialize password generator, prompt for choices
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))




# random letter, number, and symbol variables for storage
ran_letters = []
ran_numbers = []
ran_symbols = []

# random letter generator
for i in range(0,nr_letters):
    random_letter = random.choice(letters)
    ran_letters.append(random_letter)

# random number generator
for j in range(0,nr_numbers):
    random_number = random.choice(numbers)
    ran_numbers.append(random_number)

#random symbol generator
for k in range(0,nr_symbols):
    random_symbol = random.choice(symbols)
    ran_symbols.append(random_symbol)

# password in list form
password = ran_letters + ran_numbers + ran_symbols

# print the contents of the password list with no spaces, i.e. print weak password
print(f"Weak password: {''.join(password)}")

# shuffle password list
random.shuffle(password)

# print the contents of the shuffles password list with no spaces, i.e. print strong password

print(f"Strong password: {''.join(password)}")
