#luiscarloscollazo
#nov6

import os
os.system ('clear')
#declare variables
string1 = 0
string2 = 0
newstring = 0 

#purposeofprogram
print()
print("This program will combine two different strings of text of 3 or more characters into a new string with the first two letters of each string.\n")

#input 
string1 = str(input("Enter your first string of text: "))
string2 = str(input("Enter your second string of text: "))
print("\n")

#result


if len(string1) <= 3 and len(string2) < 3:
    print('Both strings are three or less characters long.\n')
    
elif len(string1) < 3:
    print('The first string is three or less characters long.\n')

elif len(string2) < 3:
    print('The second string is three or less characters long.\n')

else:
    newstring = string2[0:2] + string1[2:] + (string1[0:2]) + string2[2:]

    print("The new string is: ", newstring)
    print()




