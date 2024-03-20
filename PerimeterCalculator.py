#luiscarloscollazo
#feb82024

while True:
    #clear console
    import os
    os.system ('clear')

    #title
    print("-----------------------------")
    print("---- Perimeter Calculator ---")
    print("-----------------------------")
    print()

    #purpose of program
    print("This program can calculate the perimeters of a square, a rectangle, or a hexagon.")
    print()

    #declare variables
    optioninput = 0
    sqsidelength = 0
    rectlength = 0 
    rectwidth = 0
    hexs1 = 0
    hexs2 = 0
    hexs3 = 0
    hexs4 = 0
    hexs5 = 0
    hexs6 = 0


    #options
    print("OPTIONS:\n")
    print("1. SQUARE\n")
    print('2. RECTANGLE\n')
    print("3. HEXAGON\n")
    print("4. QUIT\n")

    #userinput
    optioninput = int(input("Enter the number of the option you want: "))
    print()

    if optioninput == 1:
        os.system  ('clear')
        sqsidelength = int(input("Enter the length of the side of the square you want to find the perimeter of: "))
        print("\n")
        print("The perimeter of this square is:", 4 * sqsidelength, "units long.\n")
        input("Press any key and enter to return to the menu: ")


    elif optioninput == 2:
        os.system  ('clear')
        rectlength = int(input("Enter the length of the rectangle you want to find the perimeter of: "))
        rectwidth = int(input("Enter the width of this rectangle: "))
        print("\n")
        print("The perimeter of this rectangle is:", (rectlength * 2) + (rectwidth * 2), "units long.\n")
        input("Press any key and enter to return to the menu: ")

    elif optioninput == 3:
        os.system  ('clear')
        hexs1 = int(input("Enter the length of the first side of the hexagon you want to find the perimeter of: "))
        hexs2 = int(input("Enter the length of the second side: "))
        hexs3 = int(input("Enter the length of the third side: "))
        hexs4 = int(input("Enter the length of the fourth side: "))
        hexs5 = int(input("Enter the length of the fifth side: "))
        hexs6 = int(input("Enter the length of the sixth side: "))
        print("\n")
        print("The perimeter of this hexagon is:", hexs1 + hexs2 + hexs3 + hexs4 + hexs5 + hexs6, "units long.\n")
        input("Press any key and enter to return to the menu: ")

    else:
        os.system  ('clear')
        print("Goodbye!\n")
        break
        


            
        

