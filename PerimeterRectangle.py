#Luis Carlos Collazo

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