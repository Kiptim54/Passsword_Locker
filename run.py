#!/usr/bin/env python3.6
from creddata import Credentials
from userdata import User

#userdata

def create_useraccount(username, password):
    '''
    Function creates a user account
    '''
    new_user = User(username, password)
    return new_user
def save_user(user):
    '''
    function save user account
    '''
    user.save_user()

def find_user(username):
    '''
    find user using username
    '''
    return User.find_user(username)

#creddata
def create_credentials(account, email, passlock):
    '''
    create credentials details
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
    print(f"Hey, {name} would you like to create an account or login in?")
    print('\n')
    print("*" * 20)
    print("Reply with these short codes : lg - to login cc - create a new account,  ex -exit ")
    while True:
        short_code = input().lower()

        if short_code == 'cc':
            print("Creating account...")
            print("Username ")
            username = input()

            print("password")
            password = input()

            save_user(create_useraccount(username, password))
            print("*" * 20)
            print("Account information: ")
            print(f"Username: {username} , Password:{password}")
            print("*" * 20)
            print(f"Remember this information, now login")
            print(f"Logged in. Welcome {username}!")
            print("*" * 50)
            #working with creddata now
            print("Use these short codes : ca - create a new account, da - display accounts, fa -find an account, gp - generate a random password , ex -exit the contact list ")

        elif short_code == "ca":
            print("Enter account details: ")
            print("Account Company: ")
            account = input()
            print("Email: ")
            email = input()
            print("Password: ")
            passlock = input()

            save_cred(create_credentials(account, email, passlock))
            print("Credentials saved!")
            print("Use these short codes : ca - create a new account, da - display accounts, fa -find an account, gp - generate a random password , ex -exit the contact list ")

        elif short_code == "da":
            print(f"These are your accounts {username}")
            for cred in display_cred():
                print(f"{cred.account} {cred.email} {cred.passlock}")
            else:
                print("If empty, you do not have any accounts saved")

        elif short_code == "fa":
            print("Key in  the account you are searching for (ie.'Facebook': " )
            search_cred= input()
            if find_account(search_cred):
                search_acc = find_account(search_cred)
                print(f"{search_acc.account} {search_acc.email} { search_acc.passlock}")
            else: print("This account does not exist")
            
        elif short_code == "de":
            print("Key in account you want to delete: ")
            

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