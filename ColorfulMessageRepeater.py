#luiscarloscollazo
#mar12024

#import time, colors, and random packages
import time
import random
import colorama
from colorama import Fore

#declare functions
def printColorfulMessage(message, reps):
    for ind in range(1, reps + 1):
        colorSelect = random.randint(1,5)
        if colorSelect == 1:
            print()
            print(Fore.LIGHTMAGENTA_EX + message)
            print()
            time.sleep(1)
        elif colorSelect == 2:
            print()
            print(Fore.GREEN + message)
            print()
            time.sleep(1)
        elif colorSelect == 3:
            print()
            print(Fore.RED + message)
            print()
            time.sleep(1)
        elif colorSelect == 4:
            print()
            print(Fore.BLUE + message)
            print()
            time.sleep(1)
        elif colorSelect == 5:
            print()
            print(Fore.YELLOW + message)
            print()
            time.sleep(1)

#clear console
import os
os.system ('clear')
#purpose of program
print()
print("This program can print any message you want any amount of times you want it to repeat. The repetitions will be printed in random colors.")
print("\n\n")

#declarevariables
message = input("Enter the message you want to print: ")
print()
reps = int(input("Enter the amount of times you want this message to be repeated: "))

#result
printColorfulMessage(message, reps)




