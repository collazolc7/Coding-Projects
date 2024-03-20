#luiscarloscollazo
#feb82024

while True:
    #clear console
    import os
    os.system ('clear')

    #import time
    import time

    #title
    print("------------")
    print("-   TIMER  -")
    print("------------")
    #purpose of program
    print()
    print("This program is a timer app. You can enter the amount of seconds you want this timer to be.\n")

    #declarevariables
    inputtime = 0

    #userinput
    inputtime = int(input("Enter the amount of seconds you want this timer to be: "))
    print()

    #timeroutput
    while inputtime > 0:
        print(inputtime, "seconds left\n")
        time.sleep(1)
        inputtime -= 1

    if inputtime == 0:
        print("0 seconds left.\n\n")
        print("Your timer has finished.\n")
        input("Press any key and then enter to make a new timer.")
    

        







