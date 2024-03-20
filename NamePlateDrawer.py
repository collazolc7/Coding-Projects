#luiscarloscollazo
#feb292024

#declarefunctions
def printCustomPlate(name, grade, hometown):
    print("")
    print(" ========================================================")
    print(" == NAME:", name)
    print(" == GRADE:", grade)
    print(" == HOMETOWN:", hometown)
    print(" ========================================================")
    print("")

#clearconsole 
import os
os.system('clear')

#purposeofprogram
print()
print("This program can receive the name of a person, their grade, and their hometown to create a custom name plate made for them.")
print()

#declarevariables
name = input("Enter the name of the person you want to create the name plate for: ")
print()
grade = input("Enter the person's grade: ")
print()
hometown = input("Enter the person's hometown: ")
print()

#result
printCustomPlate(name, grade, hometown)
