#luiscarloscollazo
#nov8

import os
os.system ('clear')

#-------------Operation with Variable------------
#Write a Python program that prints a list of six numbers
#and then prints the square of those same numbers

print('-----List of numbers squared-----')
print()

numberlist =[2, 3, 4, 5, 6, 7]

print(numberlist, "\n")

numberlist[0] = numberlist[0] ** 2
numberlist[1] = numberlist[1] ** 2
numberlist[2] = numberlist[2] ** 2
numberlist[3] = numberlist[3] ** 2
numberlist[4] = numberlist[4] ** 2
numberlist[5] = numberlist[5] ** 2


print("List of numbers, SQUARED")
print()
print(numberlist)
print()

numberlist2 = [3, 4, 5, 6, 7]

print('Another list of numbers:')
print()
print(numberlist2)

#calculate the square of each element and store in a separate list

#create a second list of numbers 
numlist2 = [10, 11, 12, 13, 14]

#create an empty list where we will store results
resultList = []

for numberElement in numlist2:
    exponentResult = numberElement ** 2
    resultList.append(exponentResult)
#print the results
print()
print("Original list: ", numlist2)
print()
print("Same list but squared: ", resultList)
print("\n")

#exercise: take the average of a list of numbers (cm)
personheight = [142, 189, 155]
averagenum = 0
sum = 0

for individualheight in personheight:
    sum += individualheight

#divide the heights by the amount of persons
averagenum = sum / len(personheight)

#print results
print("Average height = ", averagenum)
print()

