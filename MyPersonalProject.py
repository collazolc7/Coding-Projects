#luiscarloscollazo

import os
os.system('clear')
#declare variables

choose_option = 0

#displaymenu

print("=============================================")
print("==           My Personal Program           ==")
print("=============================================")
print()
print()
print()
print("Menu of options:")
print()
print()
print("1. My Name Plate")
print()
print("2. My Job Interests")
print()
print("3. My Python Art")
print()
print("4. My Personal Project")
print()
print()
print()
print("---------------------------------------------")
print()
print()
print()
choose_option = int(input("Choose the option you want to enter: "))

#conditional statements
if choose_option == 1:
    os.system('clear')
    print("")
    print(" ========================================================")
    print(" == NAME: Luis Carlos Collazo Carrión                  ==")
    print(" == GRADE: 8th Grade                                   ==")
    print(" == HOBBIES: Basketball, Volleyball, Running, and Math ==")
    print(" ========================================================")
    print("")



elif choose_option == 2:
    os.system('clear')
    print("")
    print("When I grow up, I want to become an electrical engineer specializing in wireless telecommunications.")
    print("Also, I want to go to a good engineering program like MIT, Duke, Harvard, and Stanford, among others.")
    print("")



elif choose_option == 3:
    os.system('clear')
    print("My first drawing:")
    print("")
    print("")
    print("@-----------*")
    print("   |     |    ")
    print("   |     |       **")
    print("")
    print("")
    print("My bonus drawing:")
    print("")
    print("")
    print("         /\            ")
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

elif choose_option == 4:
    os.system('clear')
    #Define Variables
    length = 0
    width = 0 
    result = 0
    #Purpose of Program
    print()
    print("This program can find the perimeter of any rectangle with the length and with that you choose.")

    #Read first value: length
    print()
    length = int(input ("Insert the length of the rectangle: "))
    print()

    #Read second value: width
    width= int(input("Insert the width of the rectangle: "))
    print()

    #Compute the perimeter

    if length == width:
        print ("This figure is a square, this program cannot calculate its area.")
        print()
    else:
        result = 2 * (length + width)
        print()

    #Result
    if length == width:
        print()

    else:
        print("The perimeter of the rectangle with length", length,"and width", width, "is",result, "units.")
        print()
    
else:
    print()
    print("This is not a correct option.")
    print()