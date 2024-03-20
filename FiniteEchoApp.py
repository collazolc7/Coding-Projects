#luiscarloscollazo
#feb22024

#clear console
import os
os.system ('clear')

#colors
import colorama

#title
print()
print('---------------------------------------------------')
print('|                 Finite Echo App                 |')
print('---------------------------------------------------')

#purpose of program
print('\n')
print('In this program, you can enter whatever you want, and the same message you wrote will be sent to you. You will have ten attempts to enter text.')
print()

#declarevariables
att = 0
count = 0
#att1input
while count < 10:
    from colorama import Fore
    count += 1
    if count == 10:
        break
    print("Attempt", count,":")
    att = input("Type your message: ")
    print()
    print("Your message:", Fore.CYAN + att + Fore.RESET)
    print("\n\n\n")
    
if count == 10:
    print("Attempt", count,":")
    att = input("Type your message: ")
    print()
    print("Your message:", Fore.CYAN + att + Fore.RESET)
    print("\n")
    print("Goodbye!\n\n\n")





