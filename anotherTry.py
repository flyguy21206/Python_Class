#This is Improved ATM project for Reskill Americans-FINAL

#Welcome customer

#Login with Account Number and Password
    #---If not current user, Register for access

#register
# - supply first name, last name, email address, and password
# - generate user account
#login with new credentials to confirm successful registration

#login
# - enter account number and password

#bank operations
#Once logged in, choose option to Withdraw, Deposit, Check Balance
    #---confirm if done with transactions and exit when completed

#initializing the system

import random

accountInformation = {} 

def init():

    
    print("Welcome to Your Favorite Bank")
    
    haveAccount = int(input("Do you have an account with us? 1 (yes) 2 (no) \n"))
         
    if(haveAccount == 1):

        login()
    elif(haveAccount == 2):
            
        register()
    else:
        print("You have selected an invalid option")
        init()

#login
# - enter account number and password
def login():


    print("Please login to your account")

    accountNumberFromUser = int(input("What is your account number? \n"))
    password = input("What is your password? \n")

    for accountNumber,userDetails in accountInformation.items():
        if(accountNumber == accountNumberFromUser):
            if(userDetails[3] == password):
                bankOperation(userDetails)


    else:
        print("Invalid account number or password")
        init()
    

#register
# - supply first name, last name, email address, and password
# - generate user account
#login with new credentials to confirm successful registration
def register():

    print("****Register*****")

    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = input("Please create a password \n")

    accountNumber = generateAccountNumber()

    accountInformation[accountNumber] = [ first_name, last_name, email, password ]

    print("Your Account has been created")
    print(" == ==== ===== ===== ===")
    print("Your account number is: %d" % accountNumber)
    print("Make sure you keep it safe")
    print(" == ==== ====== ===== ===")
    #login with new credentials to confirm successful registration
    login()

def bankOperation(user):
    
    print("Welcome %s %s" % ( user [0], user[1] ) )
    mainMenu()

def mainMenu():
    selectedOption = int(input("What would you like to do? (1) Deposit (2) Withdrawal (3) Logout  \n"))

    if(selectedOption == 1):

        depositOperation()
    elif(selectedOption == 2):

        withdrawalOperation()
    elif(selectedOption == 3):

        logout()
    else:

        print("Invalid option selected")
        mainMenu()


def depositOperation():
    print("Deposit Operations")
    depositAmount = input("How much would you like to deposit? \n")
    print("Your Deposit has been completed")
    print("Your new balance is $2030. Please take your receipt")
    mainMenu()

def withdrawalOperation():
    withdrawalAmount = input("How much would you like to withdraw? \n")
    print("Please take your cash")
    print("Your new balance is $2030. Please take your receipt")
    mainMenu()

def logout():
    print("Have a nice day!")
    init()



def generateAccountNumber():

    return random.randrange(111111111,999999999)




init()

