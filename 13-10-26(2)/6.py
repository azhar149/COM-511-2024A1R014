# Create an electricity bill class that stores a customer's name and electrcity units used.Calculate the bill using these rates rupees 3 per unit for the first 100 units,rupees 5 per unit for the next 100 units and rupees 7 per unit for units above 200.Add a fixed charge of rupees 50.Display the customer's name,units used and ctotal bill.If the entered units are negative,display an error message

class ElectricityBill:
    def __init__(self, name, units):
        self.name = name
        self.units = units

    def calculate_bill(self):
        if self.units < 0:
            print("Invalid units")
        else:
            if self.units <= 100:
                bill = self.units * 3
            elif self.units <= 200:
                bill = 100 * 3 + (self.units - 100) * 5
            else:
                bill = 100 * 3 + 100 * 5 + (self.units - 200) * 7

            bill = bill + 50

            print("Customer Name:", self.name)
            print("Units Used:", self.units)
            print("Total Bill: Rs.", bill)


name = input("Enter customer name: ")
units = int(input("Enter units used: "))

obj = ElectricityBill(name, units)
obj.calculate_bill()
