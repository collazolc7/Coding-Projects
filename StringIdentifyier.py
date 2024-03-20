#luiscarloscollazo
#nov8

import os
os.system ('clear')

#declarevariables
string1 = 0
string2 = 0

#purposeofprogram
print()
print("This program can tell you if two different strings of text of 3 or more characters are identical or if they have the same amount of characters.\n ")

#input 
string1 = str(input("Enter your first string of text: "))
string2 = str(input("Enter your second string of text: "))
print("\n")

#conditionalstatements
if len(string1) < 3 and len(string2) < 3:
    print('Both of these strings are less than three characters.')

elif len(string1) < 3:
    print("The first string of text is not 3 or more characters.")
    print()

elif len(string2) < 3:
    print('The second string of text is not 3 or more characters.')
    print()



else: 
    if string1 == string2:
        print("These two strings are identical.")
        print()

    elif len(string1) == len(string2):
        print('These two strings of text have the same amount of characters.')
        print()

    else:
        print("These strings do not have any of these properties.")
        print()



