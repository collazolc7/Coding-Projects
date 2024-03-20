# define variables
fahrenheit = 0
celsius = 0
# print purpose of program
print()
print("This program can convert any temperature given in Fahrenheit to Celsius.")
print()
# declare the temperature in fahrenheit
fahrenheit = int(input("Enter the temperature value in degrees Fahrenheit: "))
# compute temp in celsius using: C = (F-32) * 5/9
celsius = (fahrenheit - 32) * 5/9
# results are printed to user
print("This temperature in Celsius is:", celsius)
print()