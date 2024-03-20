#luiscarloscollazo
#mar42024

#clearconsole
import os
os.system ('clear')

#declarefunctions
def multiplyList(numList):
    
    total = 1
    for num in numList:
        total *= num
    
    print(f"The product is {total}.")

#purpose of program
print("\nHello! This program can give you the product of any list of integers.\n")

#declare variables

inputList = input("Enter the list of numbers you want to multiply separated by a comma: ")
print()
numList = inputList.split(",")

#convert individual strings into numbers
numList = [int(x) for x in numList]


#result
multiplyList(numList)
print()