#luiscarloscollazo
#feb142024

#clear console
import os
os.system ('clear')

#purpose of program
print()
print("This program can count to any number you want in increments of 10.\n")

#declare variables
userinput = 0

#input
userinput = int(input("Enter the number you want to count to in increments of 10: "))
print()

#result
for i in range(0,userinput + 1, 10):
    print(i)
    print()
