from functions import *

def menu():
    while True:
        option = input("""\nChoose the excercise:
                        1) Simple Array Sum
                        2) Compare triplets
                        3) Cats and a mouse
                        4) Electronics Shop
                        5) Day of the Programmer
                        6) Time Conversion
                        7) Grading students

                        x to quit\n""")

        if option == "1":
            print(simpleArraySum())

        if option == "2":
            print(compareTriplets())

        if option == "3":
            print(catAndMouse())

        if option == "4":
            print(getMoneySpent())

        if option == "5":
            print(dayOfProgrammer())

        if option == "6":
            print(timeConversion())

        if option == "7":
            print(gradingStudents())

        if option == "x":
            break


if __name__ == "__main__":
    menu()
