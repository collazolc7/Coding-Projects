#luiscarloscollazo
#mar62024

#clearconsole
import os
os.system('clear')

#define functions
def getFactorial(num):

    fact = 1
    for ind in range(1, num + 1):
        fact *= ind
    

    print(f"\nThe factorial of {num} is {fact}.\n") 

def printFactorial(num, fact):
    fact = 1
    for ind in range(1, num + 1):
        fact *= ind
    
    numList = []
    for i in range(num, 0, -1):
        numList.append(i)
    for eachind in numList:
        if eachind == 1:
            print(eachind, "=", fact)
        else:
            print(eachind, "x ", end=(""))
    


    
#purpose of program
print("\nThis program can find the factorial of any number.\n")

#declare variables
num = int(input("Enter the number you want to find the factorial of: "))
fact = 1

#result
getFactorial(num)
printFactorial(num, fact)
print()

