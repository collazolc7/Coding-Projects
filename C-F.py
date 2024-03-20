# define variables
fahrenheit = 0 
celsius = 0
# print purpose of program
print()
print("This program can convert any temperature given in Fahrenheit to Celsius.")
print()
# declare the temperature in celsius
celsius = int(input("Enter the temperature value in degrees Celsius: "))
# compute temp in fahrenheit using: F = C * 9/5 + 32
fahrenheit = celsius * 9/5 + 32
# results are printed to user
print("This temperature in Fahrenheit is:", fahrenheit)