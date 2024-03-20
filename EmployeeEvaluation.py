#luis carlos collazo

#purpose of program
print()
print("This program can read your evaluation score and can indicate your level of performance and how much money you make.")
print()

#declare variables
level_of_performance = 0
user_performance_score = 0
money_earned = 0

#input

user_performance_score = float(input("What is your user score?: "))

#conditional statements
print()
if user_performance_score == 0.0:
    print("Your level of performance is unacceptable and you did not earn any money.")

elif user_performance_score == 0.4:
    print("Your level of performance is acceptable and you earned 960 dollars.")

elif user_performance_score >= 0.6:
    print("Your level of performance is meritorious and you earned", user_performance_score * 2400, "dollars.")

else:
    print("This is not a correct user score.")

print()