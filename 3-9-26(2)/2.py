# WAP to simulate a digital lock system.

# The Lock should ask the user to enter a 4-digit PIN. 
# If the PIN entered does not contain exactly 4 digits, 
# the program should display an error message and ask again.
# If the entered PIN is correct, the lock should open. 
# Otherwise, the program should ask the user to try again.

correct_pin = "6969"

while 1:
    pin = input("Enter your 4-Digit Pin : ")

    if len(pin) != 4 or not pin.isdigit():
        print("Error: PIN must contain exactly 4 digits. Please try again.")
        continue

    if pin == correct_pin:
        print("Correct PIN! The lock is now open.")
        break
    else:
        print("Incorrect PIN. Please try again.")