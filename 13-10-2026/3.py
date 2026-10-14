class product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total(self):
        return self.price * self.quantity
    name = input("Enter product name: ")
    price = float(input("enter price: "))
    quantity = int(input("enter quantity: "))

    product1 = product(name, price, quantity)

print("product:", product1.name)
print("total cost:", product1.calculate_total())