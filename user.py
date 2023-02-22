# Created by: Agateeswaran K 
# Created on: 07:02:2023 
# Updated on: 14:02:2023 

import re
from getpass import getpass

class User:
    __username = ["Adminroot"]
    __password = ["Aspire@123"]
    __phone = [9865743120]
    __emailid = ["Admin@aspiresys.com"]

    @classmethod
    def signing_in(cls):
        user_choice = 1
        flag = True
        name = ""
        print("_" * 100)
        print("\t\t\t\t\t- > Sign-in < -")
        print("_" * 100)
        # print(User.__username)
        # print(User.__password)
        while flag:
            # print("Enter your username:")
            temp_username = input("Enter your username:\n")
            # print("Enter your password:")
            temp_password = getpass(prompt="Enter your password:\n")

            for i in range(len(User.__username)):
                if temp_username == User.__username[i]:
                    if temp_password == User.__password[i]:
                        print("\t\t\t\t- > logged-in successfully! < -")
                        flag = False
                        name = User.__username[i]
                    else:
                        print("Error!, invalid credentials")
                        try:
                            userchoices = int(input("\nWant retry to signing-in ? or exit the "
                                                "application.\n\t 1.Sign-in\t2.Exit\n"))
                        except:
                            print("Invalid entry !\nPlease try to enter a valid choice")
                        if userchoices == 1:
                            flag = True
                        elif userchoices == 2:
                            quit()
        return name

    def register_user(self):
        name = ""
        print("_" * 100)
        print("\t\t\t\t\t- > Sign-up < -")
        print("_" * 100)
        flag = True
        regex = ("(?=.*[a-z])(?=.*[A-Z]).+$")
        rule = re.compile(regex)
        while flag:
            temp_username = input("Enter the Username:\n")
            if re.search(rule, temp_username):

                User.__username.append(temp_username)
                # print(User.__username)
                flag = False
            else:
                print("Invalid Username!\nPlease try to enter a valid username!")
        flag = True
        regex = (
            "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$")
        rule = re.compile(regex)
        while flag:
            temp_password = input("Enter the password:\n")
            if re.search(rule, temp_password):
                User.__password.append(temp_password)
                flag = False
            else:
                print("Invalid password!\nPlease try  to enter a valid password")
        flag = True
        while flag:
            try:
                temp_phone = int(input("Enter your Mobile number:\n"))
            except:
                print("Invalid entry !\nPlease try  to enter a valid Mobile number")
            else:
                if 6000000000 < temp_phone and 10000000000 > temp_phone:
                    flag = False
                else:
                    print("Invalid Mobile number!\nPlease try  to enter a valid Mobile number")
        flag = True
        regex = ("^[A-Za-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$")
        rule = re.compile(regex)
        while flag:
            temp_email = input("Enter the email:\n")
            if re.search(rule, temp_email):
                User.__emailid.append(temp_email)
                flag = False
            else:
                print("Invalid Email Id!\nPlease try  to enter a valid email")
        print("\n","-"*25,">Successfully registered as the User<","-"*25)
        name = User.signing_in()
        return name
