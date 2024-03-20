#luiscarloscollazo
#feb62024

#clearconsole
import os
os.system ('clear')

#colors 
import colorama

#title
print()
print('---------------------------------------------------')
print('|                Infinite Echo App                |')
print('---------------------------------------------------')

#purposeofprogram
print('\n')
print('In this program, you can enter whatever you want, and the same message you wrote will be sent back to you in color. If you enter exit, the program will end.')
print()

#declarevariables
input1 = 0
#att1input
while True:
    from colorama import Fore
    input1 = input("Type your message: ")
    if input1 == "exit" or "EXIT":
        break
    
else:
        print()
        print("Your message:", Fore.CYAN + input1 + Fore.RESET)
        print("\n\n\n")
    
if input1 == "exit" or "EXIT":
    print()
    print("Goodbye!\n")

