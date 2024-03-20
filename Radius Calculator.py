#Luis Carlos Collazo


#intro
print()
print("                                  --- Radius Calculator ---                                       ")
print()
print("This calculator can give you the circumference and area of a circle with any radius that you want.")
print()



#variables
radius = float(input("Enter the radius of the circle: "))
pi = 3.14
units = (input("Enter the units of the radius: "))
diameter = 2 * radius
print()
print()

#equations
print("The area of the circle with radius",radius,"is approximately", pi * radius * radius,units,"squared.")
print()
print("The circumference of the circle with radius",radius,"is approximately", pi * (diameter), units,".")
print()