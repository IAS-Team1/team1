import ticketcancel
from ticketcancel import Ticketcancel
from validation import New_Registration, login


class Userchoice():
    @classmethod
    def userChoice(self):
        flag = True
        while flag:
            print("..........Welcome to Indian Railways..........")
            print("1.for new registration\n2.for Login\n3.to display the details of user\n4. exit the application")

            choice = int(input())
            if choice == 1:
                New_Registration.new_passenger()
            elif choice == 2:
                login.Login()
            elif choice == 3:
                New_Registration.display()
            elif choice == 4:
                flag = False
            else:
             print("Please enter the Choice Correctly")




