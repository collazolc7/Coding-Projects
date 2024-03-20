#luiscarloscollazo
#mar62024

#clearconsole
import os
os.system('clear')

#define functions
def generateOddNumbers(start, finish):
    print(f"\nThe odd numbers from {start} to {finish} are: \n")

    for num in range(start, finish + 1):
        if num % 2 == 1:
            print(num)

#purpose of program
print("\nThis program can generate all of the odd numbers in the range of two numbers.\n")

#declare variables
start = int(input("Enter the number you want to start counting at: "))
print()
finish = int(input("Enter the number you want to stop counting at: "))
print()

#result
generateOddNumbers(start, finish)