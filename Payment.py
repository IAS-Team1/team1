import time
class Payment:
    @classmethod
    def payment(self):
        print("1 for Card/Debit Card")
        print("2 for UPI Payment")
        print("3 for Cash on Delivery")
        print("4 for Net Banking")
        flag = True
        while flag:
            try:
                choice = int(input("Enter your Choice: "))
            except:
                print("enter the valid one:")
            else:
                print("choice")
                flag = False
        if choice == 1:
            card_number = int(input("Enter your Card Number:"))
            pin = int(input("Enter your pin:"))
            if pin == 1098:
                print("Your Tickets has been booked and it will be sent to your Registered mail and phone number")
            else:
                print("Enter the correct pin")
            flag = False
        elif choice ==2:
            upi = input("Enter your UPI Id:")
            pin = int(input("Enter your Pin:"))
            if pin == 1098:
                print("Your Tickets has been booked and it will be sent to your Registered mail and phone number")
            else:
                print("Enter your valid pin")
            flag = False
        elif choice == 3:
            print("Your Tickets has been booked and it will be sent to your Registered mail and phone number")
            flag = False
        elif choice == 4:
            print("Enter your bank name:")
            input("Your Bank Name")
            pin = int(input("Enter your pin number:"))
            if pin == 1098:
                print("Your Tickets has been booked and it will be sent to your Registered mail and phone number")
            else:
                print("Enter your valid pin")
                flag = False

        else:
            print("Select valid payment method")
