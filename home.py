# Created by: Agateeswaran K 
# Created on: 07:02:2023 
# Updated on: 14:02:2023 

from user import User
from serviceitems import Service
from dashboard import *


class Home:
    name = ""
    user_choice = 1

    @classmethod
    def signout(self):
        print("_"*100)
        flag = True
        while flag:
            try:
                userchoices = int(input("\nExit Application or not ?\n 1.Yes\t2.No\n"))
            except:
                print("Invalid entry!,Please Entry a valid entry")
            if userchoices == 1:
                print("\n\t\t\t\t-> Signed out Successfully! <- \n\n\t\t\t\tThanks for using this application!\n")
                quit()
            elif userchoices == 2:
                print("_"*100,"\nYour last Service details are")
                Customer().print_details(Home().name)

    def greeting( ):
        print("_" * 100)
        print("\t\t\t\t\t- > Welcome to the Application < -")
        print("_" * 100)
        while True:
            try:
                user_choice = int(input("\nExisting User ?\n\t1.Yes\t2.No\n"))
            except:
                print("Invalid entry !\nPlease try to enter a valid choice")
            else:
                break
        if user_choice == 1:
            name = User().signing_in()
        elif user_choice == 2:
            while True:
                try:
                    user_choice = int(
                        input("Want register as a user ? or exit the application.\n\t 1.Sign-up\t2.Exit\n"))
                except:
                    print("Invalid entry !\nPlease try to enter a valid choice")
                else:
                    break
            if user_choice == 1:
                name = User().register_user()
            elif user_choice == 2:
                quit()
            else:
                print("Invalid choice")
        else:
            print("Invalid choice")
        Service().rise_service_request()
        Customer().print_details(name)
        Payment().payment_methods()
        Home().signout()

Home.greeting()
