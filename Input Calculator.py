#Luis Carlos Collazo

#intro
print("")
print("                                         ---- Python Calculator ----                                       ")
print("")
print("This program gives you some mathematical equations that can be made for any two integers that you want.")
print("")



#variables
n1 = int(input("Enter your first number: "))

print()

n2 = int(input("Enter your second number: "))

print()

#equations
print("The possible equations made with", n1 ,"and",n2,"are:")
print("")
print(n1, "+", n2, "=", n1 + n2)
print("")

if n2 > n1:
    print( n2, "-", n1, "=", n2 - n1)

elif n1 > n2:
    print(n1, "-", n2, "=", n1 - n2)

else:
    print(n1, "-", n2, "=", 0)


print("")
print(n1, "x", n2, "=", n1 * n2)
print("")
print(n1, "/", n2, "=", n1 / n2)
print("")
print(n1, "mod", n2, "=", n1 % n2)
print()






