#luiscarloscollazo
#feb 23 2024

#declare functions
def printRepeat(message, repeatNumber):
    print("\n")
    print("Result:\n")
    print(message * repeatNumber)
    print("\n")

    for i in range(repeatNumber):
        print(message)
        print()
    
#clearconsole
import os
os.system ('clear')

#purposeofprogram
print()
print("This program can receive any message you want and it will print your message back to you any amount of times you want.")
print()

#declare variables
message = input("Enter the message you want to repeat: ")
print()
repeatNumber = int(input("Enter the number of times you want to repeat this message: "))
print()

#result
printRepeat(message, repeatNumber)
