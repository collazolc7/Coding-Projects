#luiscarloscollazo
#jan13

#clear console 
import os
os.system('clear')

#YOUR CODE HERE FOR OPTION 4
print("-----------------------------------------------------")
print("|       AVERAGE HEIGHT OF FIVE INDIVIDUALS          |")
print("-----------------------------------------------------")
print("\n")

#purpose of program
print('This program can give you the average height of five different individuals.')
print()

#declare variables
ind1 = 0
ind2 = 0
ind3 = 0
ind4 = 0
ind5 = 0
sum = 0
averagelen = 0
indlist = 0

#lengthinput
ind1 = float(input("Enter the height of the first person in cm: "))
print()
ind2 = float(input("Enter the height of the second person in cm: "))
print()
ind3 = float(input("Enter the height of the third person in cm: "))
print()
ind4 = float(input("Enter the height of the fourth person in cm: "))
print()
ind5 = float(input("Enter the height of the fifth person in cm: "))
print("\n\n")

#average
indlist = [ind1, ind2, ind3, ind4, ind5]
sum = 0 
averagelen = 0

for ind in indlist:
    sum+= ind
        
averagelen = round(sum/len(indlist))

#results
print("The average length of the individuals is about", averagelen,"centimeters.\n\n")