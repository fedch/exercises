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
