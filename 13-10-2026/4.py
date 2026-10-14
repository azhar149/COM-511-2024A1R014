class bankaccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def depposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("withdrawal successful.")
        else:
            print("insufficient balance.")

    def show_balance(self):
        print("Account holder:", self.name)
        print("Current balance:", self.balance)
        name = input("Enter account holder name: ")
        balance = float(input("Enter initial balance: "))

        account1 = bankaccount(name, balance)

        deposit_amount = float(input("Enter amount to deposit: "))
        account1.depposit(deposit_amount)
        withdraw_amount = float(input("Enter amount to withdraw: "))
        account1.withdraw(withdraw_amount)

        account1.show_balance()    