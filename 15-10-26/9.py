# Write a python program that creates a ParkingTicket class for calculating the parking fee for one vehicle.
# The program must:
# 1.Ask the user to enter the vehicle number and parking duration in hours.The duration may include a fraction,such as 2.5 hours
# 2.Calculate the fee using the billable hours.
# - Each started hour counts as one full hour.For example,2.1 hour is billed as 3hours.
# - Charge rupees 30 per billable hour for the first two hours.
# - Charge rupees 20 for each billable hour after the first two hours
# 3.Display the vehicle number,actual parking duration,and total fee.
# 4. If the duration is zero or negative,display an error message and do not calculate a fee .
# Example: A vehicle parked for 2.5 hours is billed for 3 hours.The fee is rupees 30 + rupees30 + rupees 20 = rupees 80


import math

class ParkingTicket:
    def __init__(self):
        self.vehicle = ""
        self.hours = 0

    def calculate_fee(self, vehicle, hours):
        self.vehicle = vehicle
        self.hours = hours

        if hours <= 0:
            print("Parking duration must be greater than zero")
        else:
            bill_hours = math.ceil(hours)

            if bill_hours <= 2:
                fee = bill_hours * 30
            else:
                fee = 2 * 30 + (bill_hours - 2) * 20

            print("\nVehicle Number:", self.vehicle)
            print("Parking Duration:", self.hours, "hours")
            print("Total Fee: Rs.", fee)


ticket = ParkingTicket()

vehicle = input("Enter vehicle number: ")
hours = float(input("Enter parking duration in hours: "))

ticket.calculate_fee(vehicle, hours)
