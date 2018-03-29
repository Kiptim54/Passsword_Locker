#!/usr/bin/env python3.6
from creddata import Credentials
from userdata import User

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

def main():
    # Dealing user class first
    print("Hello! Welcome to Password Locker! Please Key in your name:  ")
    name = input ()
    print(f"Hey, {name} would you like to create an account or login in?")
    print('\n')
    print("*" * 20)
    while True:
        print("Reply with these short codes : lg - to login cc - create a new account,  ex -exit ")
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

        elif short_code =='lg':



        elif short_code == 'ex':
            print("*"*30)
            print("logging out...")
            print('\n')
            print('\n')
            print("logged out")
            print("*"*30)
            break


        else:
            print("Invalid, please use the short_codes")
if __name__ == '__main__':
    main()  