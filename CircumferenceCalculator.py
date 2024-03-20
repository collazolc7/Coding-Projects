#luiscarloscollazo
#jan13

#clear console
import os
os.system('clear')

#intro and purpose of program
print()
print("                                  --- Circumference Calculator ---                                       ")
print()
print("This calculator can give you the circumference of a circle with any radius that you want.")
print()



# declare variables
radius = float(input("Enter the radius of the circle in centimeters: "))
pi = 3.14159
diameter = 2 * radius
print()
print()

#equations
print("The circumference of the circle with radius",radius,"cm is approximately", pi * (diameter),"centimeters.")
print()