from functions import *

def menu():
    options = int(input("""Choose the excercise:
                    1) Simple Array Sum
                    2) Compare triplets\n"""))

    if options == 1:
        print(simpleArraySum())

    if options == 2:
        print(compareTriplets())


if __name__ == "__main__":
    menu()
