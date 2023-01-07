
try:
    file = open("afile.txt")
    a_dict = {"key": "value"}
    print(a_dict["fdsf"])
except FileNotFoundError:
    file = open("afile.txt", "w")
    file.write("something")
except KeyError as error_message:
    print(f"the key {error_message} does not exist")
else:
    content = file.read()
    print(content)
finally:
    raise TypeError("This is an error I made up")


height = float(input("Height: "))
weight = int(input("weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters")

bmi = weight / height ** 2
print(bmi)