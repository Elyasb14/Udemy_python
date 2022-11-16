# dumb prime number calculator
def prime_checker(number):
    remainder_list = []
    for i in range(2, number-1):
        remainder_list.append(number % i)
    if 0 in remainder_list:
        print("It's not a prime number")
    if 0 not in remainder_list:
        print("It's a prime number")


# calling the function
n = int(input("Check this number: "))
prime_checker(number=n)
