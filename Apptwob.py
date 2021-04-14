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

databaseUser = {
  '1111122222':'ABCD',
  '1111112223':'EFGH',
  '2222222222':'IJKL'
} 

#Login with Account Number and Password
def init():
    print("Welcome to Your Money Bank")
    
    haveAccount = int(input("Do you have an account with us? 1 (yes) 2 (no) \n"))
         
    if(haveAccount == 1):

        login1()
    #---If not current user, Register for access, then login
    elif(haveAccount == 2):
            
        register()
        login1()
    else:
        print("You have selected an invalid option")
        init()

#login
def login1():
    print("****Login****")
    # - enter account number and password
    accountNumberFromUser = input("Please enter your 10 digit account number \n") 
    password = str(input("Please enter your 4 digit password \n"))
    
    for accountNumberFromUser,userDetails in databaseUser.items():
        if(accountNumberFromUser in databaseUser and password == databaseUser[accountNumberFromUser]):
            print("Welcome " + accountNumberFromUser)
            from datetime import datetime
            now = datetime.now()
            dt_string = now.strftime("%m/%d/%Y %H:%M")
            print("date and time =", dt_string)
        
        #running bank operation after successful login
            bankOperation()
    
    else:
        print("You have entered an invalid Account number or password. Please try again")
        init()
   

#register
def register():
    print("Please Register for access")
    # - supply first name, last name, email address, and password
    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = input("Please create a 4 digit password \n")

# - generate user account
    accountNumberFromUser = generateAccountNumber()

    print("Your Account has been created")
    print(" == ==== ===== ===== ===")
    print("Your account number is: %d" % accountNumberFromUser)
    print("Make sure you keep it safe")
    print(" == ==== ====== ===== ===")
    #login with new credentials to confirm successful registration
    bankOperation()

#Once logged in, choose option to Withdraw, Deposit, Check Balance
    #---confirm if done with transactions and exit when completed
def bankOperation():
    print('These are the available options:')
    print('1. Withdrawal')
    print('2. Cash Deposit')
    print('3. Complaint')
    print('4. Logout')

    selectedOption = (int(input('Please select an option:')))
    print(selectedOption)
        #These are the steps for Withdrawal
    if(selectedOption == 1):
        print('You have selected Withdrawal.')
        Withdrawal=input('How much would you like to withdraw? \n')
        print('Please take your cash and receipt')
        print('Your balance is $5000')
        print('Would you like to perform another transaction?')
        bankOperation()
        

    elif(selectedOption == 2):
        print('You have selected Deposit')
        Deposit=input('How much money would you like to deposit? \n')
        print('Please take your cash and receipt')
        print('Your balance is $5000')
        print('Would you like to perform another transaction?')
        bankOperation()
                
    elif(selectedOption == 3):
        print('You have selected Complaint')
        Complaint=input('What issue would you like to report? \n')
        print('Thank you for contacting us with your issue!')
        print('Would you like to perform another transaction?')
        bankOperation()

    elif(selectedOption == 4):
        print('You have selected Logout. Have a Great Day!')
        init()
    
    else:
        print("You have selected an invalid option. Please try again.")
        bankOperation()
def generateAccountNumber():

    return random.randrange(1111111111,9999999999)


init()