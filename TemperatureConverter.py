#luiscarloscollazo
#mar142024

while True:
    #import tempconvertermodule
    import TempConverterModule

    #import colorama
    import colorama
    from colorama import Fore

    #clear console 
    import os
    os.system('clear')

    #declare variables 
    optionInput = 0

    #textplate
    print('\n')
    print("------------------------------------------")
    print("|         TEMPERATURE CONVERTER          |")
    print("|   Developed by: Luis Carlos Collazo    |")
    print("------------------------------------------")

    #purpose of program
    print('\nThis program can convert any temperature in a certain unit (Fahrenheit, Celsius, or Kelvin) to another unit.\n')

    #option menu
    print("-------------------")
    print("| MENU OF OPTIONS |")
    print("-------------------")

    print("\n")
    print("1. FAHRENHEIT TO CELSIUS")
    print("2. CELSIUS TO FAHRENHEIT")
    print("3. FAHRENHEIT TO KELVIN")
    print("4. KELVIN TO FAHRENHEIT")
    print("5. CELSIUS TO KELVIN")
    print("6. KELVIN TO CELSIUS")
    print("7. QUIT")
    print("\n")

    optionInput = int(input("Enter the number of the option you want to choose: "))

    #Show sub-program based on user input
    if optionInput == 1:
        os.system('clear')

        print("-----------------------------------")
        print("| FAHRENHEIT TO CELSIUS CONVERTER |")
        print("-----------------------------------")
        
        #input temperature
        print()
        tempinput = float(input("Enter the degree value in Fahrenheit that you would like to convert: "))
        result = TempConverterModule.fahrenheitToCelsius(tempinput)

        print(Fore.RED + f"\nThis temperature in Celsius is {result} degrees.\n" +Fore.RESET)

        input("Press any key and enter to return to the main menu.") 

        print("\n\n\n")

    elif optionInput == 2:
        os.system('clear')

        print("-----------------------------------")
        print("| CELSIUS TO FAHRENHEIT CONVERTER |")
        print("-----------------------------------")
        
        #input temperature
        print()
        tempinput = float(input("Enter the degree value in Celsius that you would like to convert: "))
        result = TempConverterModule.celsiusToFahrenheit(tempinput)

        print(Fore.CYAN + f"\nThis temperature in Fahrenheit is {result} degrees.\n" + Fore.RESET)

        input("Press any key and enter to return to the main menu.") 

        print("\n\n\n")

    elif optionInput == 3:
        os.system('clear')

        print("----------------------------------")
        print("| FAHRENHEIT TO KELVIN CONVERTER |")
        print("----------------------------------")
        
        #input temperature
        print()
        tempinput = float(input("Enter the degree value in Fahrenheit that you would like to convert: "))
        result = TempConverterModule.fahrenheitToKelvin(tempinput)

        print(Fore.MAGENTA + f"\nThis temperature in Kelvin is {result} degrees.\n" + Fore.RESET)

        input("Press any key and enter to return to the main menu.") 

        print("\n\n\n")
    
    elif optionInput == 4:
        os.system('clear')

        print("----------------------------------")
        print("| KELVIN TO FAHRENHEIT CONVERTER |")
        print("----------------------------------")
        
        #input temperature
        print()
        tempinput = float(input("Enter the degree value in Kelvin that you would like to convert: "))
        result = TempConverterModule.kelvinToFahrenheit(tempinput)

        print(Fore.GREEN + f"\nThis temperature in Fahrenheit is {result} degrees.\n" + Fore.RESET)

        input("Press any key and enter to return to the main menu.") 

        print("\n\n\n")

    elif optionInput == 5:
        os.system('clear')

        print("-------------------------------")
        print("| CELSIUS TO KELVIN CONVERTER |")
        print("-------------------------------")
        
        #input temperature
        print()
        tempinput = float(input("Enter the degree value in Celsius that you would like to convert: "))
        result = TempConverterModule.celsiusToKelvin(tempinput)

        print(Fore.BLUE + f"\nThis temperature in Kelvin is {result} degrees.\n" + Fore.RESET)

        input("Press any key and enter to return to the main menu.") 

        print("\n\n\n")

    elif optionInput == 6:
        os.system('clear')

        print("-------------------------------")
        print("| KELVIN TO CELSIUS CONVERTER |")
        print("-------------------------------")
        
        #input temperature
        print()
        tempinput = float(input("Enter the degree value in Kelvin that you would like to convert: "))
        result = TempConverterModule.kelvinToCelsius(tempinput)

        print(Fore.YELLOW + f"\nThis temperature in Celsius is {result} degrees.\n" + Fore.RESET)

        input("Press any key and enter to return to the main menu.") 

        print("\n\n\n")

    else:
        os.system('clear')

         #PROGRAM WILL QUIT at this point

        print("\n------ Have a good day! ------\n")

        break