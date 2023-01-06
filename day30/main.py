# file not found
try:
    file = open("afile.txt")
    a_dict = {"key": "value"}
    print(a_dict["fdsf"])
except FileNotFoundError():
    file = open("afile.txt", "w")
    file.write("something")

