#This program is quite simple. What it does is:
#1. Ask for a password
#2. Ask if you need help
#3. Ask for a name to be added
#4. Add that name
#5. Print all the names.
#I'm faily certain all of this code can be tweaked to your needs. 

#Made by Jake Zaleski

import sys

MainLine = ("People in the database: ")

#if you wish to change the password, change 'admin' to the new password.
#Be sure to leave the quotation marks in, or else it won't work.
#
#If you wish to completely remove the password, delete everything from HERE:
password = "admin" 
print ("Please type in the password to begin. This is case sensitive.\n")

PossiblePass = input()

if PossiblePass == ("admin"):

    print("\nWelcome!\n\nFor help, please consult the guide on GitHub or the README.txt.")

else:

    print ("Incorrect.")

    sys.exit()

#To HERE.

while(1 == 1):

    newPerson = input("\nPlease enter a name or a command (Commands: search, end).\n\n")    

    if newPerson == ("end"):

        break

    if newPerson == ("search"):

        searchName = input("\nWhat is their first name?\n")

        if searchName in MainLine: 

            print ("True.")

        else:

            print ("False.")

    else:

        MainLine = "\n" + MainLine + "\n" + newPerson

        print (MainLine)
