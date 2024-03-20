#luiscarloscollazo
#nov22


#creating menus in our Python console programs 

#library for accessing operating system's features (like clearing console) and time
import os
import time

#colors input
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

while True:

    #define variables
    optionInput = 0

    #clear console
    os.system('clear')
    print("\n")




    #program title and introduction
    print("---------------------------------------------------------")
    print("--------- BONAVILLE UNIVERSITY SOFTWARE TOOLKIT ---------")
    print("---------------------------------------------------------")
    print("\n")

    #purpose of program
    print("This is a software toolkit for faculty and staff at Bonaville University.")
    print("\n")

    #request option from user
    print("-------------------")
    print("| MENU OF OPTIONS |")
    print("-------------------")

    print("\n")
    print("1. SCHOLARSHIP REQUEST VALIDATION")
    print("2. CHARACTER COUNTER")
    print("3. STUDENT ID VERIFIER")
    print("4. AVERAGE HEIGHT OF LEAVES FROM OAK TREE")
    print("5. CREDITS")
    print("6. QUIT")
    print("\n")


    optionInput = int(input("Choose option: "))

    #Show sub-program based on user input
    if optionInput == 1:
        #clear console
        os.system('clear')


        #YOUR CODE HERE FOR OPTION 1
        print("----------------------------------")
        print("| SCHOLARSHIP REQUEST VALIDATION |")
        print("----------------------------------")
        print("\n")

        #purpose of program
        print("This program can tell you if a student qualifies for a scholarship depending on their grades.")
        print()

        #declare variables
        phys = 0
        math = 0
        sci = 0
        eng = 0
        spa = 0
        hist = 0

        #grade input by user
        phys = int(input("Enter the student's physics grade: "))
        print("\n")
        math = int(input("Enter the student's mathematics grade: "))
        print("\n")
        sci = int(input("Enter the student's science grade: "))
        print("\n")
        eng = int(input("Enter the student's english grade: "))
        print("\n")
        spa = int(input("Enter the student's spanish grade: "))
        print("\n")
        hist = int(input("Enter the student's history grade: "))
        print("\n\n")

        #averagegrade
        gradelist = [phys, math, sci, eng, spa, hist]
        averagegrade = 0
        sum = 0
        
        for individualgrade in gradelist:
            sum += individualgrade
        
        #division
        averagegrade = round(sum/len(gradelist))

        #print results
        if averagegrade > 80:
            print("The student's average grade is: ", averagegrade)
            print()
            print("They can qualify for a scholarship.")
        
        else:
            print("The student's average grade is: ", averagegrade)
            print()
            print("They cannot qualify for a scholarship.\n\n")

            
        input("Press any key to return to the menu.") 

        print("\n\n\n")
    
    elif optionInput == 2:
        #clear console
        os.system('clear')

        #YOUR CODE HERE FOR OPTION 2
        print("----------------------------------")
        print("|        CHARACTER COUNTER       |")
        print("----------------------------------")
        print("\n")

        #purpose of program
        print("This program can tell you if the number of characters a sentence has and if it is too long (more than 45 characters).")
        print()

        #declare variables
        inputstr = 0

        #string input by user
        inputstr = str(input("Enter the text sentence you want to use: "))
        print("\n")

        #conditionalresults
        if len(inputstr) <= 45:
            print("This sentence contains ", len(inputstr), "characters.")
            print("It has a normal amount of characters.\n\n\n")

        else:
            print("This sentence contains ", len(inputstr), "characters.")
            print("It is too long.\n\n\n")

        input("Press any key to return to the menu.") 

    elif optionInput == 3:

        #clear console
        os.system('clear')

        #YOUR CODE HERE FOR OPTION 3
        print("----------------------------------")
        print("|       STUDENT ID VERIFIER      |")
        print("----------------------------------")
        print("\n")

        #purpose of program
        print("This program can verify if a student ID is valid or invalid. A student ID is valid when the sum of its digits is greater than or equal to 20.")
        print()

        #declare variables
        studentID = 0 

        #input student ID
        studentID = str(input("Enter the eight digits of the student's ID: "))
        print("\n")

        #sum of digits
        digitlist = [int(studentID[0]),int(studentID[1]), int(studentID[2]), int(studentID[3]), int(studentID[4]), int(studentID[5]), int(studentID[6]), int(studentID[7])]
        sum = 0 

        for individualdigit in digitlist:
            sum += individualdigit

        #conditionalresults
        if sum >= 20:
            print("The sum of this student ID's digits is", sum,".")
            print()
            print("This is a valid ID.\n\n\n")

        else:
            print("The sum of this student ID's digits is", sum,".")
            print()
            print("This is a not a valid ID.\n\n\n")
        
        input("Press any key to return to the menu.")

    elif optionInput == 4:

    #clear console
        os.system('clear')

        #YOUR CODE HERE FOR OPTION 4
        print("-----------------------------------------------------")
        print("|       AVERAGE HEIGHT OF LEAVES FROM OAK TREE      |")
        print("-----------------------------------------------------")
        print("\n")

        #purpose of program
        print('This program can give you the average height of five different leaves from an oak tree.')
        print()

        #declare variables
        leaf1 = 0
        leaf2 = 0
        leaf3 = 0
        leaf4 = 0
        leaf5 = 0

        #lengthinput
        leaf1 = float(input("Enter the length of the first leaf: "))
        print()
        leaf2 = float(input("Enter the length of the second leaf: "))
        print()
        leaf3 = float(input("Enter the length of the third leaf: "))
        print()
        leaf4 = float(input("Enter the length of the fourth leaf: "))
        print()
        leaf5 = float(input("Enter the length of the fifth leaf: "))
        print("\n\n")

        #average
        leaflist = [leaf1, leaf2, leaf3, leaf4, leaf5]
        sum = 0 
        averagelen = 0

        for leaf in leaflist:
            sum += leaf
        
        averagelen = round(sum/len(leaflist))

        #results
        print("The average length of the leaves is: ", averagelen,"\n\n")

        input("Press any key to return to the menu.")

    elif optionInput == 5:

        #clear console
        os.system('clear')

        #YOUR CODE HERE FOR OPTION 5
        print(bcolors.OKCYAN + "----------------------" + bcolors.ENDC)
        print(bcolors.OKCYAN + "|       CREDITS      |" + bcolors.ENDC)
        print(bcolors.OKCYAN + "----------------------" + bcolors.ENDC)
        print("\n")


        #nameplate

    

        print("This program was made by:\n")

        

        print("-------------------------------------")
        time.sleep(1)
        print(bcolors.OKGREEN + "| NAME: LUIS CARLOS COLLAZO CARRIÓN |" + bcolors.ENDC)
        time.sleep(1)
        print(bcolors.OKGREEN + "| STUDENT NUMBER: 28-008            |" + bcolors.ENDC)
        time.sleep(1)
        print(bcolors.OKGREEN + "| CURRENT HOME LOCATION: SAN JUAN   |" + bcolors.ENDC)
        time.sleep(1)
        print("-------------------------------------\n")
        
        input("Press any key to return to the menu.")

    else:

        #PROGRAM WILL QUIT at this point

        print("\n------ Have a good day! ------\n")

        input("Press any key to return to the menu.")
        break
        

#END
