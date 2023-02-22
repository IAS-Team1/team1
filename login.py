#created by Dharun M
#created on 13.02.2023
#modified on 21.02.2023
import time
from getpass import getpass
from ticketAvailablity import ticketavailablity

class login:
    def __init__(self):
        self.name=input("ENTER UR NAME")
        self.phonenumber=input("ENTER UR PHONE NUMBER")
        self.password=getpass()   
    def details(self):              
        print(self.name)
        print(self.phonenumber)
        #print(self.password)
        time.sleep(3)
        print("SUCESSFULLY LOGGED IN")
        ticketavailablity.info()

class register:
    def __init__(self):
        self.name=input("ENTER UR NAME")
        self.phonenumber=input("ENTER UR PHONE NUMBER")
        self.password=getpass()
    def details(self):
        print(self.name)
        print(self.phonenumber)
        #print(self.password) 
        time.sleep(3)
        print("REGISTERED SUCESSFULLY")
        ticketavailablity.info()


print("WELCOME TO RESEREVE_MY_TICKET")
print("ENTER 1 TO LOGIN FOR EXISTING USER:\nENTER 2 TO REGISTER FOR NEW USER  :")
flag=True
while flag:
    try:
        choice=int(input())
    except:
        print("Invalid Input")
        
    else:
        flag=False
        if choice==1:
            obj=login()
            obj.details()
        if choice ==2:
            obj1=register()
            obj1.details()
        else:
            print("Invalid Input and Enter 1 or 2")
            flag=True
print("ENSURE THE PROVIDED DETAILS ARE CORRECT")
print("THANKS FOR BOOKING\nENJOY THE EXPERIENCE\nTHEATRE VIBES STARTED!!")
