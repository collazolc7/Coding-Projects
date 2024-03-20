#luiscarloscollazo
#jan13

#clear console 
import os
os.system('clear')


print("-----------------------------------------------------")
print("|                AVERAGE CALCULATOR                 |")
print("-----------------------------------------------------")
print("\n")

#purpose of program
print('This program can give you the average of any numbers that you want. Please enter the string of numbers with a comma separating them.')
print()

#declare variables
inputList = input("Enter the numbers you want to find the average of: ")
print()

#create list
inputList = inputList.split(",")

newList = []

for num in inputList:
    newList.append(int(num))



#average
sum = 0 
average = 0

for ind in newList:
    sum+= ind
        
average = round(sum/len(newList))

#results
print("The average of the numbers is about", average,".\n\n")