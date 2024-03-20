#luiscarloscollazo
#nov2

#declarevariables
chem = 0
math = 0
phys = 0

#purposeofprogram
print()
print("-------------------------------------------")
print("-        University of Lakefield          -")
print("-           Lakefield, U.S.A.             -")
print("-------------------------------------------")
print()
print("This program can tell you if you are eligible for admission at the University of Lakefield.")

#input
print()
chem = int(input("What is your chemistry grade?: "))
math = int(input("What is your mathematics grade?:"))
phys = int(input("What is your physics grade?:"))
print()

#conditionalstatements
if chem > 50 and math > 65 and phys > 55:
    print("You are eligible to admit at the University of Lakefield!")
    print()
else:
    print("We regret to inform you, you are not eligible for admission at the University of Lakefield.")
    print()

