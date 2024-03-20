#luiscarloscollazo
#mar62024

#clear console
import os
os.system('clear')

#define functions
def findEvenNumbers(listNum):
    print("\nThe even numbers in this list are: \n")

    for num in listNum:
        if num % 2 == 0:
            print(num)

#purpose of program
print("\nThis program can find all of the even numbers in a set of numbers.\n")

#declare variables
inputList = input("Enter the list of numbers you want to find the even numbers of (Please separate the numbers with commas): ")

listNum = inputList.split(",")

#convert ind strings into integers
listNum = {int(x) for x in listNum}

#result
findEvenNumbers(listNum)
print()