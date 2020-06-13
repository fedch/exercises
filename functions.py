from itertools import product

# 1) Given an array of integers, find the sum of its elements.
# https://www.hackerrank.com/challenges/simple-array-sum/problem

def simpleArraySum():
    print("\nGiven an array of integers, find the sum of its elements.\n")
    ar_count = int(input("Denote the size of your array: "))
    ar = list(map(int, input(f"Enter {ar_count} numbers to calculate their sum: ").rstrip().split()))
    return sum(ar)

# 2) Compare two arrays
# https://www.hackerrank.com/challenges/compare-the-triplets/problem

def compareTriplets():
    print("\nGiven two arrays compare each pair of numbers and give a point to the array with a larger number\n")
    a = list(map(int, input("Enter 3 numbers separated by space: ").rstrip().split()))
    b = list(map(int, input("Enter another 3 numbers separated by space: ").rstrip().split()))
    apoints = 0
    bpoints = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            apoints += 1
        elif a[i] < b[i]:
            bpoints += 1
    return [apoints, bpoints]

# 3) Two cats and a mouse are at various positions on a line. You will be given their starting positions. Your task is to determine
# which cat will reach the mouse first, assuming the mouse doesn't move and the cats travel at equal speed. If the cats arrive at
# the same time, the mouse will be allowed to move and it will escape while they fight.
# https://www.hackerrank.com/challenges/cats-and-a-mouse/problem

def catAndMouse():
    print("\nCheck if either cat a or cat b will reach mouse c first, or it will escape\n")
    xyz = input("Respective values of x (cat a's location), y (cat b's location), and z (mouse c's location) separated by space\n").split()
    x = int(xyz[0])
    y = int(xyz[1])
    z = int(xyz[2])

    cat_a = abs(z - x)
    cat_b = abs(z - y)

    if cat_a < cat_b:
        return "Cat A"
    elif cat_a > cat_b:
        return "Cat B"
    else:
        return "Mouse C"

# 4) If two items are in the budget, return the amount of money spent. If not, return -1
# https://www.hackerrank.com/challenges/electronics-shop/problem

def getMoneySpent():
    bnm = input("Enter budget, the number of keyboard models and the number of USB drive models (e.g.: 10 2 3):\n").split()

    b = int(bnm[0])
    n = int(bnm[1])
    m = int(bnm[2])

    keyboards = list(map(int, input("Enter the prices of each keyboard model (e.g.: 3 1):\n").rstrip().split()))
    drives = list(map(int, input("Enter the prices of the USB drives.(e.g.: 5 2 8):\n").rstrip().split()))

    return max(m+n if m+n<=b else -1 for m, n in product(keyboards, drives))

# 5) Marie invented a Time Machine and wants to test it by time-traveling to visit Russia on the Day of the Programmer
#(the 256th day of the year) during a year in the inclusive range from 1700 to 2700.
# From 1700 to 1917, Russia's official calendar was the Julian calendar; since 1919 they used the Gregorian calendar system.
# https://www.hackerrank.com/challenges/day-of-the-programmer/problem

def dayOfProgrammer():
    year = int(input("""Choose a year to find the Day of the Programmer (the 256th day of the year) in Russia.
    Bear in mind that From 1700 to 1917, Russia's official calendar was the Julian calendar:\n""").strip())

    leap = 244
    non_leap = 243
    x = 256

    if year == 1918:
        return "26.09.1918"
    else:
        if year % 4 == 0 and (year < 1918 or year % 100 != 0 or year % 400 == 0):
            day = x - leap
            return f"{day}.09.{year}"
        else:
            day = x - non_leap
            return f"{day}.09.{year}"

# 6) Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.
# https://www.hackerrank.com/challenges/time-conversion/problem

def timeConversion():
    s = input("Choose a time in 12-hour AM/PM format to convert it to military (24-hour) time (e.g.: 07:05:45PM):\n")
    if s[8:] == "PM":
        if s[:2] == "12":
            y = int(s[:2])
        else:
            y = int(s[:2]) + 12

    elif s[8:] == "AM":
        if s[:2] == "12":
            y = int(s[:2]) - 12
            y = f"{y:02d}"
        else:
            y = s[:2]
    final = str(y) + s[2:8]
    return final

# 7) Round the grades according to the rules on:
# https://www.hackerrank.com/challenges/grading/problem

def gradingStudents():
    grades_count = int(input("Enter the number of students: ").strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input("Grade: ").strip())
        grades.append(grades_item)

    return [n if n < 38 or n % 5 < 3 else (n + 5 - (n % 5)) for n in grades]
