#luiscarloscollazo
#jan31

#clear console
import os
os.system('clear')

#declare variables
myList = 0

#purposeofprogram
print()
print("This program can accept a sequence of comma-separated numbers and make a list of these numbers.\n")

#userinput
myList = str(input('Enter your sequence of comma-separated numbers: '))

#results
print("\n")
print("The final list of numbers is the following:", myList.split(","),"\n")
