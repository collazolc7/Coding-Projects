#luiscarloscollazo
#feb 23 2024

#declare functions
def testNumericRange(number):
    if 1000 <= number <= 2000 or 5000 <= number <= 5500:
        print()
        print("The number IS between 1000 and 2000 or between 5000 and 5500.\n")
    else:
        print()
        print("The number IS NOT between 1000 and 2000 or between 5000 and 5500.\n")

#clear console
import os
os.system ('clear')

#purpose of program
print()
print('This program can receive any number that you enter and determine if it is between 1000 and 2000 or between 5000 and 5500 or if it is not between any of these numbers.')
print()

#declarevariables
number = float(input("Enter the number you want to be evaluated: "))
print()

#result
testNumericRange(number)
