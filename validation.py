import re

from choosingtrain import choosingtrain


class New_Registration:
    passenger_name = []
    passenger_password = []
    passenger_phoneNumber = []
    passenger_emailId = []
    passenger_sex = []
    @classmethod
    def new_passenger(self):
        flag = True
        while flag:
            name = input("Enter your Name:")
            regex = ("(?=.*[a-z])(?=.*[A-Z]).+$")
            match = re.compile(regex)
            if (re.search(match, name)):
                self.passenger_name.append(name)
                flag = False
            else:
                print("Please, Enter the Valid User name:)")

        flag = True
        while flag:
            password = input("Enter your Password:")
            regex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?& ])[A-Za-z\d@$!#%*?&]{8,18}$"
            match = re.compile(regex)
            if (re.search(match, password)):
                self.passenger_password.append(password)
                flag = False
            else:
                print("Please, Enter the valid password:)")
        flag = True
        while flag:
            try:
                number = int(input("Enter your Contact number:"))
                if number > 6000000000 and number < 10000000000:
                    pass
                else:
                    print("Enter the valid one:")
            except:
                print("you have entered a Invalid mobile number please try with valid one:)")
            else:
                if number > 6000000000 and number < 10000000000:
                 self.passenger_phoneNumber.append(number)
                flag = False

        flag = True
        while flag:
             Email = input("Enter your Email address:")
             regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
             match = re.compile(regex)
             if (re.search(match, Email)):
                self.passenger_emailId.append(Email)
                flag = False
             else:
              print("Please, Enter your Valid Email Address:")
        flag = True
        while flag:
              Sex = input("Enter your Sex:")
              self.passenger_sex.append(Sex)
              flag = False


    @classmethod
    def display(self):
        print(self.passenger_name)
        print(self.passenger_emailId)
        print(self.passenger_sex)



class login(New_Registration):


    def __init__(self):
            self.name = ""
            self.password = ""

    @classmethod
    def Login(self):
            self.name = input("Enter user name:")
            self.password = input("Enter user password:")
            # print(self.passenger_name)
            for i in range(len(self.passenger_name)):
                if self.passenger_name[i] == self.name:
                    if self.passenger_password[i] == self.password:
                        print("You have been logged in successfully")
                        print("choose 1 for Train Details")
                        print("choose 2 to display the user details")
                        print("Choose 3 for Log out from the account")
                        flag = True
                        while flag:
                            try:
                                choice = int(input("Enter your Choice:"))
                            except:
                                print("Enter the valid choice")
                            else:
                                # print("choice")
                                flag = False
                        if choice == 1:
                                print("Checking.... train details")
                                choosingtrain.detailsview()
                                choosingtrain.passengerdetails(self)
                               # choosingtrain.detailschoosing(self)
                               # choosingtrain.classtype(self)
                                flag = False
                        elif choice == 2:
                                New_Registration.display()
                        elif choice == 3:
                                # print("Log out from the account")
                            print("Logging out..........")
                            print("Logged out from the account")
                else:
                    print("You have entered the wrong user name and password")

