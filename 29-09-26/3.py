# Write a Python program to manage a small library using a dictionary. The program must repeнабу allow the user to add books, issue books, return books, and display the current book record
# Conditions:
# -Store book title as the key and available copies as the value.# -A book can be issued only if it exists and at least one copy is avaliable
# -Return a book only if it already exists in the library record.
# -Book names should work regardless of uppercase or lowercase letters.
library = {}

while True:
    print("\n--- Library Menu ---")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Display Books")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book = input("Enter book name: ").lower()
        copies = int(input("Enter number of copies: "))

        if book in library:
            library[book] = library[book] + copies
        else:
            library[book] = copies

        print("Book added successfully.")

    elif choice == "2":
        book = input("Enter book name: ").lower()

        if book in library:
            if library[book] > 0:
                library[book] = library[book] - 1
                print("Book issued successfully.")
            else:
                print("Book is not available.")
        else:
            print("Book does not exist.")

    elif choice == "3":
        book = input("Enter book name: ").lower()

        if book in library:
            library[book] = library[book] + 1
            print("Book returned successfully.")
        else:
            print("Book does not exist in the library.")

    elif choice == "4":
        print("\nCurrent Library Record:")

        if len(library) == 0:
            print("Library is empty.")
        else:
            for book in library:
                print(book, ":", library[book], "copies")

    elif choice == "5":
        print("Exiting library...")
        break

    else:
        print("Invalid choice.")