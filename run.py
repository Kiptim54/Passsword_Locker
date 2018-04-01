#!/usr/bin/env python3.6
from creddata import Credentials
from userdata import User
import random

#userdata 

def create_useraccount(username, password):
    ''"
    method creates a user account
    '''
    new_user = User(username, password)
    return new_user
def save_user(user):
    '''
    method save user  account
    '''
    user.save_user()

def find_user(username):
    ''
    method for find user using username
    '''
    return User.find_user(username)

#creddata
def create_credentials(account, email, passlock):
    '''
    method credentials details
    '''
    new_cred = Credentials(account, email, passlock)
    return new_cred

def save_cred(cred):
    '''
    save credentials
    '''
    cred.save_cred()

def display_cred():
    '''
    method to display all the saved credentials
    '''
    return Credentials.display_cred()

def find_account(account):
    '''
    method to search for an account
    '''
    return Credentials.find_account(account)
def delete_cred(account):
    '''
    method to delete account
    '''
    account.delete_cred()



def main():
    # Dealing user class first
    print("Hello! Welcome to Password Locker! Please Key in your name:  ")
    name = input ()
    print(f"Hey {name}, please create an account to access Password Locker")
    print('\n')
    print("*" * 80)
    print("Reply with these short codes : cc - create a new account,  ex -exit ")
    print("*" * 80)

    while True:
        short_code = input().lower()

        if short_code == 'cc':
            print("Creating account...")
            print("Key in these details:")
            print("Username: ")
            username = input()

            print("Password: ")
            password = input()

            save_user(create_useraccount(username, password))
            print('\n')
            print(f"{name}'s Account information: ")
            print(f"Username: {username} , Password:{password}")
            print('\n')
            print(f"Logged in. Welcome {username}!")
            print("*" * 80)
            #working with creddata now
            print("Use these short codes : ca - create a new account, da - display accounts, fa -find an account, gp - generate a random password , ex -exit the contact list ")
            print("*" * 80)

        elif short_code == "ca":
            print("Enter account details: ")
            print("Account Company(e.g:Facebook): ")
            account = input()
            print("Email: ")
            email = input()
            print("Password: ")
            passlock = input()

            save_cred(create_credentials(account, email, passlock))
            print("Credentials saved! Enter 'da' to see account")
            print("*" * 80)
            print("Use these short codes : ca - create a new account, da - display accounts, fa -find an account, gp - generate a random password , ex -exit the contact list ")
            print("*" * 80)

        elif short_code == "da":
            print(f"These are your accounts {username}:")
            print("*" * 30)
            for cred in display_cred():
                print(f"{cred.account} {cred.email} {cred.passlock}")
            else:
                print("*" * 30)
                print("If empty, you do not have any accounts saved")

        elif short_code == "fa":
            print("Key in  the account you are searching for (ie.'Facebook'): " )
            search_cred= input()
            if find_account(search_cred):
                search_acc = find_account(search_cred)
                print(f"{search_acc.account} {search_acc.email} { search_acc.passlock}")
            else: print("This account does not exist")
            
        elif short_code == "gp":
                letters= "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
                how_many = len(letters)
                print("How long would you like your password to be? ")
                print(f"p.s: Maximum length of password is {how_many}")
                lent = int(input())
                password = "".join(random.sample(letters, lent))
                print(f"Your password has {lent} characters ")
                print(password)
                
            

        elif short_code == 'ex':
            print("*"*30)
            print("logging out...")
            print('\n')
            print('\n')
            print("logged out")
            print("*"*30)
            break


        else:
            print("Invalid, please  use these short codes : ca - create a new account, da - display accounts, fa -find an account, de- delete account , gp - generate a random password , ex -logout")
if __name__ == '__main__':
    main()  