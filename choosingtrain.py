import random

import ticketcancel
from Payment import Payment
from ticketcancel import Ticketcancel


class choosingtrain:
    choice = 0
    @classmethod
    def detailsview(self):
        train_from = ['salem', 'chennai', 'coimbatore', 'erode']
        train_destination = ['erode', 'coimbatore', 'chennai', 'salem']
        print("1.Salem to Erode\n2.Chennai to Coimbatore\n3.Coimbatore to Chennai\n4.Erode to Salem")

        flag = True
        while flag:
            try:
                choice = int(input("Enter your choice"))
            except:
                print("Enter the valid choice:")
            else:
                # print("Choice")
                flag = False



        if choice == 1:
            print("The first train details")
            choosingtrain.traindetailsfor1(self)
        elif choice == 2:
            print("The second train details")
            choosingtrain.traindetailsfor2(self)
        elif choice == 3:
            print("The third train details")
            choosingtrain.traindetailsfor3(self)
        elif choice == 4:
            print("The fourth train details")
            choosingtrain.traindetailsfor4(self)

    def traindetailsfor1(self):

        train1 = ["Sabari Express","Salem","Erode","5.00 PM","7.00 PM",1145,695,510,200]
        print(train1)


    def traindetailsfor2(self):

        train2 = ["Shaam Express","Chennai","Coimbatore","5.00 PM","2.00 AM",1145,695,510,200]
        print(train2)

    def traindetailsfor3(self):

        train3 = ["Sabari Express","Erode","Salem","5.00 PM","7.00 PM",1145,695,510,200]
        print(train3)


    def traindetailsfor4(self):

        train4 =["Shaam Express","Coimbatore","Chennai","5.00 PM","2.00 AM",1145,695,510,200]
        print(train4)

    def passengerdetails(self):
        flag = True
        while flag:
            try:
                passenger_number = int(input("Enter the total number of passengers: "))
            except:
                print("Enter the valid passenger_number")
            else:
                flag = False

        choosingtrain.detailschoosing(self)
        choosingtrain.classtype(passenger_number)
    def detailschoosing(self):
        print("1. For one passenger\n2. For two passenger\n3. For Three Passengers\n4. For Four Passengers")
        
        flag = True
        while flag:
            try:
                option = int(input("Enter the Choice:"))
            except:
                print("Enter the valid one")
            else:
                # print("option")
                flag = False



        if option == 1:
            print("the details for one passenger")
            choosingtrain.one_passenger(self)
        elif option == 2:
            print("the details for two passengers")
            choosingtrain.two_passengers(self)
        elif option ==3:
            print("details for three passengers")
            choosingtrain.three_passengers(self)
        elif option ==4:
            print("details for four passengers")
            choosingtrain.four_passengers(self)


    def one_passenger(self):
        passenger1_name = input("Enter the Passenger1 Name:")
        passenger1_age = int(input("Enter the Passenger1 Age"))
        passenger1_sex = input("Enter the Passenger1_sex:")
        PNR_number = (random.randint(1000000000, 9999999999))
        print("The PNR Number for Passenger 1 :", PNR_number)


    def two_passengers(self):
        passenger1_name = input("Enter the Passenger1 Name:")
        passenger1_age = int(input("Enter the Passenger1 Age"))
        passenger1_sex = input("Enter the Passenger1_sex:")
        PNR_number = ( random.randint(1000000000, 9999999999))
        print("The PNR Number for Passenger 1 :",PNR_number)

        passenger2_name = input("Enter the Passenger2 Name:")
        passenger2_age = int(input("Enter the Passenger2 Age"))
        passenger2_sex = input("Enter the Passenger2_sex:")
        PNR_number2 = (PNR_number+1)
        print("The PNR Number for Passenegr 2 : ",PNR_number2)

    def three_passengers(self):
        passenger1_name = input("Enter the Passenger1 Name:")
        passenger1_age = int(input("Enter the Passenger1 Age"))
        passenger1_sex = input("Enter the Passenger1_sex:")
        PNR_number = (random.randint(1000000000, 9999999999))
        print("The PNR Number for Passenger 1 :", PNR_number)

        passenger2_name = input("Enter the Passenger2 Name:")
        passenger2_age = int(input("Enter the Passenger2 Age"))
        passenger2_sex = input("Enter the Passenger2_sex:")
        PNR_number2 = (PNR_number + 1)
        print("The PNR Number for Passenger 2 : ", PNR_number2)

        passenger3_name = input("Enter the Passenger3 Name:")
        passenger3_age = int(input("Enter the Passenger3 Age"))
        passenger3_sex = input("Enter the Passenger3_sex:")
        PNR_number3 = (PNR_number + 2)
        print("The PNR Number for Passenger 3 : ", PNR_number3)
    def four_passengers(self):
        passenger1_name = input("Enter the Passenger1 Name:")
        passenger1_age = int(input("Enter the Passenger1 Age"))
        passenger1_sex = input("Enter the Passenger1_sex:")
        PNR_number = (random.randint(1000000000, 9999999999))
        print("The PNR Number for Passenger 1 :", PNR_number)

        passenger2_name = input("Enter the Passenger2 Name:")
        passenger2_age = int(input("Enter the Passenger2 Age"))
        passenger2_sex = input("Enter the Passenger2_sex:")
        PNR_number2 = (PNR_number + 1)
        print("The PNR Number for Passenger 2 : ", PNR_number2)

        passenger3_name = input("Enter the Passenger3 Name:")
        passenger3_age = int(input("Enter the Passenger3 Age"))
        passenger3_sex = input("Enter the Passenger3_sex:")
        PNR_number3 = (PNR_number + 2)
        print("The PNR Number for Passenger 3 : ", PNR_number3)

        passenger4_name = input("Enter the Passenger4 Name:")
        passenger4_age = int(input("Enter the Passenger4 Age:"))
        passenger4_sex = input("Enter the Passenger4_sex:")
        PNR_number4 = (PNR_number + 3)
        print("The PNR Number for Passenger 4 : ", PNR_number4)

    def classtype(passenger_number):
        print("1. 1st class")
        print("2. 2nd class")
        print("3. 3rd class")
        print("4. general class")
        fee = [1145,695,510,200]
        flag = True
        while flag:
            try:
                value = int(input("The choice is: "))
            except:
                print("Enter the valid Choice:")
            else:
                flag = False


        if value == 1:
            payment = fee[0] * passenger_number
            print("The payment for 1st class is : ",payment)
            print("The payment amount is: ", payment)
            print("If you want t0 cancel the tickets means choose")
            choice = int(input("Enter the choice:"))
            if choice == 1:
                Ticketcancel.cancel()
            else:
                print("Log out")
        elif value == 2:
             payment = fee[1] * passenger_number
             print(payment)
             print("The payment for 2nd class is : ", payment)
             print("The payment amount is: ", payment)
             print("If you want t0 cancel the tickets means choose")
             choice = int(input("Enter the choice:"))
             if choice == 1:
                Ticketcancel.cancel()
             else:
                print("Log out")
        elif value == 3:
             payment = fee[2] * passenger_number
             print("The payment amount is: ", payment)
             print("The payment for 3rd class is : ", payment)
             Payment.payment()
             print("If you want t0 cancel the tickets means choose")
             choice = int(input("Enter the choice:"))
             if choice == 1:
                Ticketcancel.cancel()
             else:
                print("Log out")
        elif value == 4:
            payment = fee[3] * passenger_number
            print("The payment amount is: ",payment)
            print("The payment for 4th class is : ", payment)
            Payment.payment()
            print("If you want t0 cancel the tickets means choose")
            choice = int(input("Enter the choice:"))
            if choice == 1:
                Ticketcancel.cancel()
            else:
                print("Log out")






