# Created by: Agateeswaran K 
# Created on: 07:02:2023 
# Updated on: 14:02:2023 

import time
from serviceitems import Service
from user import User
import datetime


class Payment:
    def payment_methods(self):
        # print("_" * 100, "\n","-"*25,"> Services done <","-"*25)
        # print("_" * 100)
        print("_" * 100)
        print("\t\t\t\t\t- > Payment < -")
        print("_" * 100)
        print("1. Net Banking")
        print("2. Credit / Debit card")
        print("3. Cash on delivery")
        print("4. UPI Payment")
        try:
            userchoices = int(input("Enter your choice:\n"))
        except:
            print("Invalid entry !\nPlease try to enter a valid choice")
        if userchoices == 1:

            bank_name = input("Type your Bank name")
            time.sleep(5)
            print("Please wait we are redirecting your bank server")
            pin = int(input("Enter your Transaction pin"))
            if pin == 1234:
                time.sleep(10)
                print("Thank you For your purchase, visit again")
            else:
                print("You have entered An incorrect pin\nWill restart your payment")
                Payment.payment_methods()

        elif userchoices == 2:
            try:
                card_number = int(input("Enter your card number"))
            except:
                print("Invalid entry !\nPlease try to enter a valid choice")
            if card_number > 1000000000000000 and card_number < 9999999999999999:
                time.sleep(5)
                try:
                    pin = int(input("Enter your pin"))
                except:
                    print("Invalid entry !\nPlease try to enter a valid choice")
                if pin == 1234:
                    time.sleep(10)
                    print("Thank you For your purchase, visit again")
                else:
                    print("You have entered An incorrect pin \nWill restart your payment")
                    Payment.payment_methods()
        elif userchoices == 3:
            print("Your Order will be Arriving Soon")
            print("Thank you For your purchase, visit again")
        elif userchoices == 4:
            upi_id = input("enter your upi-id")
            try:
                pin = int(input("Enter your transaction pin"))
            except:
                print("Invalid entry !\nPlease try to enter a valid choice")
            if pin == 1234:
                print("Please wait we are redirecting your bank server")
                time.sleep(5)
                print("Thank you For your purchase, visit again")
            else:
                print("You have entered An incorrect pin/upi_id\nWill restart your payment")
                Payment.payment_methods()
        else:
            print("Please select valid payment method")


class Customer(Payment):
    # total = service().print_data()
    __services = Service().give_service_list()
    __service_cost = Service().give_service_price()

    @classmethod
    def print_service_details(cls):
        total = 0
        for i in range(len(Customer.__services)):
            print(i + 1, ".", Customer.__services[i], "\t", "Rs", Customer.__service_cost[i])
            total += Customer.__service_cost[i]
        # print(service.__service_price)
        print("\nYour total service charge is \tRs", total)

    def print_details(self, name):
        # print(customer.total)
        # print(service.__service)
        total = 0
        print("_" * 100, "\n\t\t\t\t\t","> Services done <")
        print("_" * 100)
        print("Name: ", name, "\n")
        x = datetime.datetime.now()
        print("Date: ",x.strftime("%c"))
        print("")
        print("_" * 40, "\n")
        Customer.print_service_details()
        # Payment().payment_methods()
        # return total
        # print(customer.__services)
        # print(customer.__service_cost)
        
            
