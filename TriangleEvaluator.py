#luis carlos collazo
#october31
import os
os.system('clear')
#declarevariables
angle1 = 0
angle2 = 0
angle3 = 0


#purpose
print()
print("This program can tell you if a triangle is scalene, isosceles, and equilateral.")
print()

#input
angle1 = float(input("What is the first angle of your triangle in degrees?: "))
angle2 = float(input("What is the second angle of your triangle in degrees?: "))
angle3 = float(input("What is the third angle of your triangle in degrees?: "))

#conditionalstatements
if angle1== angle2 == angle3:
    print("The triangle is equilateral.")
elif angle1 == angle2 or angle1 == angle3 or angle2 == angle3:
    print("The triangle is isosceles.")
else:
    print("The triangle is scalene.")

