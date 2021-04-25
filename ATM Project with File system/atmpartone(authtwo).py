# This is Improved ATM project for Re-skill Americans-FINAL

# Welcome customer

# Login with Account Number and Password
# ---If not current user, Register for access

# register
# - supply first name, last name, email address, and password
# - generate user account
# login with new credentials to confirm successful registration

# login
# - enter account number and password

# bank operations
# Once logged in, choose option to Withdraw, Deposit, Check Balance, logout
# ---confirm if done with transactions after every action is completed and exit when completed

# initializing the system

# create database to store account numbers
# Update database with new account numbers from register
# read account number when validating login, account balance after withdrawal and deposit
# delete file from bank system when logged out(will stay in database)
# create separate code for validation and use module to import info
# create separate code for adding account info to database once created
# add password validation
# add try except onto init for do you have an account with us to prevent error when
# --something other than an integer is added(like a letter)
# add try except onto main_menu for select option to prevent error when
# --something other than an integer is added(like a letter)
# add date and time to welcome
# obfuscate password it should not show on screen when entered for registration or login

import random
import validation_user_account_number
import database
from getpass import getpass


def init():
    print("Welcome to Your Favorite Bank")

    have_account = int(input("Do you have an account with us? 1 (yes) 2 (no) \n"))

    if have_account == 1:

        login()

    elif have_account == 2:

        register()

    else:
        print('Invalid option, Please try again')
        init()


def login():

    print("Please login to your account")

    account_number_from_user = input("What is your account number? \n")

    is_valid_account_number = validation_user_account_number.account_number_validation(account_number_from_user)

    if is_valid_account_number:

        password = getpass("Please enter your password? \n")

        user = database.authenticated_user(account_number_from_user, password)

        if user:
            main_menu(user)

        else:
            print("Login failed")
            print("Please check your account number and password and try again")
            init()


# register
# - supply first name, last name, email address, and password
# - generate user account
# login with new credentials to confirm successful registration
def register():
    print("****Register*****")

    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = getpass("Please create a password \n")

    account_number = generate_account_number()

    is_new_user_created = database.create(account_number, first_name, last_name, email, password)

    if is_new_user_created:
        # using database module to create and store user record
        print("Your Account has been created")
        print(" == ==== ===== ===== ===")
        print("Your account number is: %d" % account_number)
        print("Make sure you keep it safe")
        print(" == ==== ====== ===== ===")

        login()

    else:
        print("Something went wrong. Please try again")
        register()


def deposit_operation(user):
    current_user_balance = user[4]
    deposit_amount = float(input("How much would you like to deposit? \n"))
    mew_user_balance=float(current_user_balance + deposit_amount)
    
    
    
    f = open(user_db_path + str(account_number_from_user) + ".txt", "r")
    f.write(str(updated_user_details))
    f.close()
    print("Your new balance is " + str(current_balance_displayed(4)))
    main_menu(user)


def withdrawal_operation(user):
    current_user_balance = float(user[4])
    withdrawal_amount = float(input("How much would you like to withdraw? \n"))

    if current_user_balance < withdrawal_amount:

        print("Insufficient funds")
        print("Please choose another option")
        return False
       
    else:
    
        new_user_balance = current_user_balance - withdrawal_amount
        print("Your new balance is ", new_user_balance)
        print("Please take your cash and receipt")
    user_db_path = "C:/Users/flygu/Python_Class/ATM Project with File system/data/user_records/"
    updated_user_details = user[0] + "," + user[1] + "," + user[2] + "," + user[3] + "," + str(user[4])
    f = open(user_db_path + str(account_number_from_user) + ".txt", "r")
    f.write(str(updated_user_details))
    f.close()
            
    main_menu(user)
            

def current_balance_displayed(user):

    print("Your current balance is " + user[4])
    
    main_menu(user)


def main_menu(user):
    print("Hello %s %s" % (user[0], user[1]))
    selected_option = int(input("What would you like to do? (1) Deposit (2) Withdrawal (3) Balance (4) Logout  \n"))

    if selected_option == 1:

        deposit_operation(user)
    elif selected_option == 2:

        withdrawal_operation(user)
    elif selected_option == 3:

        current_balance_displayed(user)
    elif selected_option == 4:

        logout()
    else:

        print("Invalid option selected")
        main_menu(user)


# login
# - enter account number and password
def generate_account_number():
    return random.randrange(1111111111, 9999999999)


def bank_operation(user):
    main_menu(user)


def logout():
    print("Have a nice day!")


init()
