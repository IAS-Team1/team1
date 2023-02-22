import random
class Ticketcancel:
    @classmethod
    def cancel(self):
        on = 0
        ont = (random.randint(1000, 9999))
        print(ont)
        flag = True
        while flag:
            try:
                on = int(input("Enter on number:"))
            except:
                print("you have entered a Invalid on number please try with valid one:")
            else:
                print(on)
                flag = False

        if on == ont:
            print("your ticket has been cancelled")
        else:
            print("enter the valid on number:")

