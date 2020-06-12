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
