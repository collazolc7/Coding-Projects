#Luis Carlos Collazo 

#purpose of program
print()
print("This program can give you the price for entering the game rooms depending on the age and amount of the people in your group.")
print("The maximum amount of people in your party is 4 people.")
print()
#declare variables
number_of_customers = 0
age_of_cust1 = 0
age_of_cust2 = 0
age_of_cust3 = 0
age_of_cust4 = 0
#input

number_of_customers = int(input("How many people are in your group?: "))

#conditional statements
if number_of_customers > 4:
    print()
    print("The maximum amount of people in your party is 4 people. We cannot let your group in.")
    print()

elif number_of_customers == 1:
    print()
    age_of_cust1 = int(input("What is the age of the first person in your group?: "))
    print()
    if age_of_cust1 < 4:
        print("You do not need to pay to enter.")
    elif 4 <= age_of_cust1 <= 18:
        print("You need to pay $5 to enter.")
    elif age_of_cust1 > 18:
        print("You need to pay $10 to enter.")
    print()

elif number_of_customers == 2:
    print()
    age_of_cust1 = int(input("What is the age of the first person in your group?: "))
    age_of_cust2 = int(input("What is the age of the second person in your group?: "))
    print()
    if age_of_cust1 < 4:
        print("The first person does not need to pay to enter.")
    elif 4 <= age_of_cust1 <= 18:
        print("The first person needs to pay $5 to enter.")
    elif age_of_cust1 > 18:
        print("The first person needs to pay $10 to enter.")

    print()

    if age_of_cust2 < 4:
        print("The second person does not need to pay to enter.")
    elif 4 <= age_of_cust2 <= 18:
        print("The second person needs to pay $5 to enter.")
    elif age_of_cust2 > 18:
        print("The second person needs to pay $10 to enter.")
    print()

elif number_of_customers == 3:
    print()
    age_of_cust1 = int(input("What is the age of the first person in your group?: "))
    age_of_cust2 = int(input("What is the age of the second person in your group?: "))
    age_of_cust3 = int(input("What is the age of the third person in your group?: "))
    print()
    if age_of_cust1 < 4:
        print("The first person does not need to pay to enter.")
    elif 4 <= age_of_cust1 <= 18:
        print("The first person needs to pay $5 to enter.")
    elif age_of_cust1 > 18:
        print("The first person needs to pay $10 to enter.")

    print()

    if age_of_cust2 < 4:
        print("The second person does not need to pay to enter.")
    elif 4 <= age_of_cust2 <= 18:
        print("The second person needs to pay $5 to enter.")
    elif age_of_cust2 > 18:
        print("The second person needs to pay $10 to enter.")

    print()

    if age_of_cust3 < 4:
        print("The third person does not need to pay to enter.")
    elif 4 <= age_of_cust3 <= 18:
        print("The third person needs to pay $5 to enter.")
    elif age_of_cust3 > 18:
        print("The third person needs to pay $10 to enter.")

    print()
elif number_of_customers == 4:
    print()
    age_of_cust1 = int(input("What is the age of the first person in your group?: "))
    age_of_cust2 = int(input("What is the age of the second person in your group?: "))
    age_of_cust3 = int(input("What is the age of the third person in your group?: "))
    age_of_cust4 = int(input("What is the age of the fourth person in your group?: "))
    print()

    if age_of_cust1 < 4:
        print("The first person does not need to pay to enter.")
    elif 4 <= age_of_cust1 <= 18:
        print("The first person needs to pay $5 to enter.")
    elif age_of_cust1 > 18:
        print("The first person needs to pay $10 to enter.")

    print()

    if age_of_cust2 < 4:
        print("The second person does not need to pay to enter.")
    elif 4 <= age_of_cust2 <= 18:
        print("The second person needs to pay $5 to enter.")
    elif age_of_cust2 > 18:
        print("The second person needs to pay $10 to enter.")

    print()

    if age_of_cust3 < 4:
        print("The third person does not need to pay to enter.")
    elif 4 <= age_of_cust3 <= 18:
        print("The third person needs to pay $5 to enter.")
    elif age_of_cust3 > 18:
        print("The third person needs to pay $10 to enter.")

    print()

    if age_of_cust4 < 4:
        print("The fourth person does not need to pay to enter.")
    elif 4 <= age_of_cust4 <= 18:
        print("The fourth person needs to pay $5 to enter.")
    elif age_of_cust4 > 18:
        print("The fourth person needs to pay $10 to enter.")
    print()