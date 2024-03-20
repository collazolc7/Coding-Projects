#luiscarloscollazo
#mar122024

#clear console
import os 
os.system ('clear')

#import from getFactorial module
import FactorialsModule

#purpose of program
print("\nHello! This program will show you the factorial of any number and the process of finding it.\n")

#declare the variables
num = int(input("Enter the number you want to find the factorial of: "))
fact = 1

#result
FactorialsModule.getFactorial(num)
FactorialsModule.printFactorial(num, fact)
print()


