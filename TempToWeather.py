#luiscarloscollazo
#nov2

#declarevariables
temp = 0

#purpose of program
print()
print("This program can tell you the intensity of the weather based on the temperature in Celsius.")
print()

#input
temp = float(input("Enter the temperature in Celsius: "))

#conditional statements
print()
if temp < 0:
    print("The weather is freezing.")
elif 0 <= temp <= 10:
    print("The temperature is very cold.")
elif 10 <= temp <= 20:
    print("The temperature is cold.")
elif 20 <= temp <= 30:
    print("The temperature is normal.")
elif 30 <= temp <= 40:
    print("The temperature is hot.")
elif 40 <= temp:
    print("The temperature is very hot.")
print()
