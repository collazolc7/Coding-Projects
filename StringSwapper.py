#luiscarloscollazo
#nov6

import os
os.system ('clear')
#declarevariables
string1 = 0
string2 = 0
result = 0

#purposeofprogram
print()
print("This program can swap the places of two strings that are entered by the user and separates them with a space.")
print()

#input
string1 = str(input("Enter your first string: "))
string2 = str(input("Enter your second string: "))

#result
result = string2 + " " + string1
#output
print()
print("The output of strings is:", result)