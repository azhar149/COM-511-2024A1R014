# write a python program that allows a librarian to add several books to a library.For each book,ask the user to enter its title and the number of copies.Store each book and it's available copy count in a dictionary.
# After the books has been added ,display a menu that lets the user issue a book ,return book ,display all books or exit the program.
# Apply these conditions:
# - Book title should be compared without distinguishing uppercase and lowercase letters.
# - A book can be issued only if it exists in the library and has at least one copy available.
# - Issuing a book decreases it's available copy count by one.
# - A book can be returned only if it exists in the library and has at least one copy issued.
# - Returning a book increases it's available copy count by one.
# - Display all appropriate message for an unavailable book,an invalid choice or an invalid number of copies.



class Library:
    def __init__(self):
        self.books = {}

    def add_books(self, title, copies):
        key=title.lower()
        self.books[key]=[title,copies]
    def issue_book(self,title):
        key=title.lower()

        if key not in self.books:
            print("Book not found")
        elif self.books[key][1] == 0:
            print("No copies are available")
        else:
            self.books[key][1] -= 1
            print("Book issued successfully")

    def return_book(self,title):
        key=title.lower()

        if key not in self.books:
            print("Book not found")
        elif self.books[key][1] == 0:
            print("No book to return")
        else:
            self.books[key][1] += 1
            print("Book returned successfully")

    def display_books(self):
        print("\nlibrary books:")
        for details in self.books.values():
            title=details[0]
            available_copies=details[1]
            print(f"{title}: {available_copies} copies available")


library = Library()
number_of_books = int(input("Enter number of books to add: "))
for i in range(number_of_books):
    title = input("Enter book title: ")
    copies = int(input("Enter number of copies: "))
    library.add_books(title, copies)
if copies < 0:
    print("Number of copies must be greater than zero")
else:
    library.add_books(title, copies)
    print("Book added successfully")
while True:
    print("\n1. Issue a Book")
    print("2. Return a Book")
    print("3. Display all Books")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        title=input("Enter the title of book to issue: ").strip()
        library.issue_book(title)
    elif choice == "2":
        title=input("Enter the title of book to return: ").strip()
        library.return_book(title)
    elif choice == "3":

        library.display_books()
    elif choice == "4":
        break
    else:
        print("Invalid choice.Please enter 1,2,3 or 4")

