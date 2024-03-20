#luiscarloscollazo
#jan31

#import random
import random

#clear console
import os
os.system('clear')

#declare variables
num = random.randint(1,9)

#purpose of program 
print()
print('This is a guessing game! Try to see if you can know what number I am thinking of. (Hint: It is between 1 and 9, inclusive.)\n')

#input
usernum = int(input("Enter the number you think I chose: "))

#conditional statements

if num == usernum:
    print ("Well done! You guessed my number!\n")

elif num > usernum: 
    print("You guessed a bit low. Try higher!\n")

else:
    print("You guessed a bit high. Try lower!\n")
