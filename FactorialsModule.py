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
    
