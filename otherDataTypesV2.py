#luiscarloscollazo
#nov8

import os
os.system ('clear')

#purposeofprogram
print()
print("---Learning about Lists v2--- \n")

#creatingalistinpython

mixedlist = ["Colegio", "San", 'Ignacio', 'Luis Carlos',
              'Collazo', 'Carrion']

print('Current list: \n', mixedlist)
print()


#Append various items in a list and print on screen
mixedlist.append('celular')
mixedlist.append('tareas')
mixedlist.append(3.14159)

print("List with additional items:\n", mixedlist)
print()
print("------------------------------------------------------------------------------------------------------------")
print()


#Remove (pops) items from a list and print on screen
mixedlist.pop()
print('Updated list: \n ', mixedlist)
print()

#Lets use pop() on an empty list - ERROR
    # emptylist = []
    # emptylist.pop()


#Remove more elements from our list
mixedlist.pop()
mixedlist.pop()
mixedlist.pop()

print("Updated list: \n", mixedlist)
print()

#Remove specific items using index value
mixedlist.pop(2)

print("Updated list: \n", mixedlist)
print()




#-------------Operation with Variable------------
#Write a Python program that prints a list of six numbers
#and then prints the square of those same numbers

print('-----List of numbers squared-----')
print()

numberlist =[2, 3, 4, 5, 6, 7]

numberlist[0] = numberlist[0] ** 2
numberlist[1] = numberlist[1] ** 2
numberlist[2] = numberlist[2] ** 2
numberlist[3] = numberlist[3] ** 2
numberlist[4] = numberlist[4] ** 2
numberlist[5] = numberlist[5] ** 2

print("List of numbers, SQUARED \n", numberlist)
print()

numberlist2 = [3, 4, 5, 6, 7]

print('Another list of numbers: \n', numberlist2)

