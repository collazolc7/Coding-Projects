#luiscarloscollazo
#mar12024

#import colors
import colorama
from colorama import Fore

#declare functions
def printArt(num):
    if num == 1:
        print()
        print()
        print("My first drawing (a dog): ")
        print("")
        print("")
        print(Fore.GREEN + "@-----------*")
        print("   |     |    ")
        print("   |     |       **")
        print("")
        print("")

    elif num == 2:
        print("")
        print("")
        print("My second drawing (a star): ")
        print("")
        print("")
        print(Fore.YELLOW + "         /\            ")
        print("        /  \           ")
        print(" _ _ _ /    \ _ _ _    ")
        print(" \                /    ")
        print("  \              /     ")
        print("  /              \     ")
        print(" /_ _ _      _ _ _\    ") 
        print("       \    /          ")
        print("        \  /           ")
        print("         \/            ")
        print("")
        print("")
    
    elif num == 3: 
        print("")
        print("")
        print("My third drawing (some mountains): ")
        print("")
        print("")
        print(Fore.RED + "|\    /\    /\    /|")
        print("| \  /  \  /  \  / |")
        print("|  \/    \/    \/  |")
        print("|  /      \     \  |")
        print("| /        \     \ |")
        print("|/          \     \| ")
        print()
        print()

    elif num == 4:
        print()
        print()
        print("My final drawing (a rocket with PR written on it): ")
        print()
        print()
        print(Fore.BLUE + "               /\                ")
        print("              /  \               ")
        print("             /____\              ")
        print("             ||||||              ")
        print("             |    |              ")
        print("             | || |              ")
        print("             | ___|              ")
        print("             |_||||              ")
        print("             ||||||              ")
        print("             |    |              ")
        print("             | || |              ")
        print("             | __ |              ")
        print("             |_|\_|              ")
        print("             ||||||              ")
        print("                                 ")
        print("             ||||||              ")
        print("            /||||||\             ")
        print("           /||||||||\            ")
        print("           -,-,-,-,-,-           ")
        print()
        print()
    
    else:
        print()
        print("This is not an option.")


#clearconsole
import os
os.system('clear')

#purposeofprogram
print()
print("This program is an ASCII Art Displayer. All of these drawings were made by Luis Carlos Collazo, the creator of this program. There are four drawings to choose from.")
print()

#declare variables
num = int(input("Enter the number of the option you want to view: "))

#result
printArt(num)

