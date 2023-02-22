# Created by: Agateeswaran K 
# Created on: 07:02:2023 
# Updated on: 14:02:2023 

class Service:
    __service_price = [1000]
    __service = ["Nominal service Charges"]

    @classmethod
    def add_service(self):
        user_choice = 1

        try:
            user_choice = int(input(
                "Enter the service you need...\n1.Hardware Service\tRs 5000\n2.Software Serice\tRs 1500\n3.General "
                "Service\tRs 3000\n"))
        except:
            print("Invalid entry !\nPlease try to enter a valid choice\n")
        if user_choice == 1:
            Service.__service.append("Hardware Service")
            Service.__service_price.append(5000)
        elif user_choice == 2:
            Service.__service.append("Software Serice")
            Service.__service_price.append(1500)
        elif user_choice == 3:
            Service.__service.append("General Service")
            Service.__service_price.append(3000)
        else:
            print("Invalid choice !\nPlease try to enter a valid choice\n")
        flag = False

    def rise_service_request(self):
        print("_" * 100)
        print("\t\t\t\t\t- > Service initiation < -")
        print("_" * 100)
        Service.add_service()
        while True:
            try:
                user_choice = int(
                    input("Want to add another service \n 1.Yes or 2.No\n"))
            except:
                print("Invalid Entry !\nPlease try to enter a valid choice\n")
            if user_choice == 1:
                Service.add_service()
            elif user_choice == 2:
                break
        # print(service.__service)

    def give_service_list(self):
        return Service.__service

    def give_service_price(self):
        return Service.__service_price
