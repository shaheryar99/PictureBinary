#CPSC Assignment 3
#Shaheryar Syed
#UCID: 30052162

import sys

checksum = 0
#Check to see if an actual input was put
if len(sys.argv) == 2:
    #Recieve the command given by the user
    command = sys.argv[1]
    #Introducing the human readable file
    intro = "CPSC Assignment 3, Shaheryar Syed - UCID 30052162"
    print(intro)
    #Reading the length of intro string
    introlen = len(intro)
    #Defining the section numbers
    #Reading Section
    section = input()
    #Reading image dimensions
    dimensions = input()
    #Splitting Dimensions into single lists
    dimsplit = dimensions.split(" ")
    dimlen = len(dimensions) - 1
    #Checking for the section
    #Reading all commands
    if command == "217":
        #Getting some housework commands like dimensions and sections in
        print(*dimsplit, sep="\n")
        numbersection = "1"
        print(numbersection)
        if section == "P1":
            print("image")
        #While loop is running
        while True:
            try:
                #Read all data, split it and check the length.
                charcheck = 0
                data = input()
                data1 = data.strip()
                datasplit = data1.split(" ")
                charcheck = len(datasplit)
                checksum = charcheck + checksum
                print(*datasplit, sep="\n")
            #Check for an EOF Error
            except EOFError:
                print("END")
                print(checksum + dimlen)
                break
    elif command == "Invert" or command == "invert":
        n = 0
        #Again some more housework commands
        print("P1")
        print(*dimsplit)
        while True:
            try:
                #Input the data, remove all whitespace and seperate each 0,1
                data = input()
                data1 = data.strip()
                datasplit = data1.split(" ")
                #Run through a loop where we look for values in the list and change them accordingly
                #Thank you stackoverflow (https://stackoverflow.com/questions/2582138/finding-and-replacing-elements-in-a-list)
                for number, i in enumerate(datasplit):
                    if i == "0":
                        datasplit[number] = "1"
                    if i == "1":
                        datasplit[number] = "0"
                #Print the list without brackets or quotes
                print(*datasplit)
            except EOFError:
                break
    #If an invalid command was entered
    else:
        print("The command ", sys.argv[1:], "is invalid. Please enter one of the following: Invert, or 217.")
#If no command was entered
elif len(sys.argv) == 3:
    print("Too many commands were entered at once. Please either only one of Invert or 217.")
else:
    print("You did not enter a command. Please enter either Invert, or 217.")