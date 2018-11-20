"""Input a name and print alternate character"""

name = input("Enter name: ")

while len(name) <= 1:
    print("Invalid")
    name = input("Enter long name: ")

print(name[::2])