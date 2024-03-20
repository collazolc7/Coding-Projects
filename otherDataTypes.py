#luiscarloscollazo
#nov8

import os
os.system ('clear')

#purposeofprogram
print()
print("---This program is meant to show the different features of the List data type--- \n")
print()

#creatingalistinpython

#numbers
numlist = [1, 2, 3, 4, 5]

#mixedvalues
mixedlist = ["Colegio", "San", 'Ignacio']

#printalist
print("Here is our first list: ")
print(numlist, '\n')

#printtwolists
print('Here are two lists: ')
print(numlist, mixedlist, '\n')

#modifying the values of a list 
mixedlist[0] = 'Luis'
mixedlist[1] = 'Carlos'
mixedlist[2] = 'Collazo'
print('Here is a modified list:')
print(mixedlist)


#-------------Operation with Variable-------------

#length
print('\nThe length of our latest list is:', len(mixedlist))
print("\n")

#Concatenete 
biggerlist = mixedlist + numlist
print("A bigger list is:")

print(biggerlist, "\n")