# write a menu-drive python program where the user can add items,remove items ,view cart ,and exit
cart = []
while True:
    print("1. Add item to cart")
    print("2. Remove item from cart")
    print("3. View cart")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        item = input("Enter item name: ")
        cart.append(item)
    elif choice == '2':
        item = input("Enter item to remove: ")
        if item in cart:
            cart.remove(item)
        else:
            print("Item not found in cart")
    elif choice == '3':
        print("Cart items:", cart)
    elif choice == '4':
        break
    else:
        print("Invalid Choice.")
