"""Input a name and print alternate character"""


def main():
    name = input("Enter name: ")

    while len(name) <= 1:
        print("Invalid")
        name = input("Enter long name: ")

    print(name[::2])


main()