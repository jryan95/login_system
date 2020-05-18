import time
import os
import sys


class Login:

    def __init__(self):
        self._username = ""
        self._password = ""
        self._filename = "savedlogin.ini"
    
    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        while username == '':
            username = input("You must enter a username.")
        self._username = username
    
    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, password):
        while password == '':
            password = input("You must enter a password.")
        self._password = password
    
    def check_login_exists(self):
        with open(self._filename, 'r') as f:
            lines = f.readlines()
            for line in lines:
                info = line.rstrip("\n").split(':', 1)
                if info[1] != "":
                    return True
    
    # Fixed
    def check_login(self, username, password):
        with open(self._filename, 'r') as f:
            lines = f.readlines()
            # config = {}
            for line in lines:
                info = line.rstrip('\n').split(':', 1)
                if info[0] in 'Username':
                    if info[1] in username:
                        print("{} is the correct username.".format(username))
                        print("Checking password...")
                        for secondline in lines:
                            pw = secondline.rstrip('\n').split(":", 1)
                            if pw[0] in 'Password':
                                if pw[1] in password:
                                    return True
                                else:
                                    return False
                    else:
                        return False

    def create_login(self):
        with open(self._filename, 'w') as f:
            f.write("#Login info:\nUsername:{}\nPassword:{}\n".format(
                self._username, self._password))
            f.write("**" * 20)
            f.close
        
        self._username = ""
        self._password = ""


def main():
    filename = "savedlogin.ini"

    l = Login()
    if not l.check_login_exists():
        l.username = input("Enter a username: ")
        l.password = input("Enter a password: ")

        l.create_login()
    else:
        overwrite = input("There is already a login set for this file, would you like to overwrite? (y/n): ")
        if overwrite.lower() in 'y':
            os.remove(filename)

            l.username = input("Enter a new username: ")
            l.password = input("Enter a new password: ")

            l.create_login()

        elif overwrite.lower() in 'n':
            to_login = input("Would you like to login? (y/n): ")

            if to_login.lower() in 'y':

                l.username = input("Username: ")
                l.password = input("Password: ")

                print(l.username)
                print(l.password)

                if l.check_login(l.username, l.password):
                    print("You have successfully logged in! Welcome back.")
                else:
                    print("You have entered incorrect credential information.")
            
            elif to_login.lower() in 'n':
                print("Goodbye.")
            else:
                print("Goodbye.")
            
        elif overwrite.lower() in 'q':
            exit()
        else:
            print("Invalid option. Goodbye.")


if __name__ == "__main__":
    main()