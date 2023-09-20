#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def borrow(self):
        if self.available:
            self.available = False
            print(f"Book '{self.title}' by {self.author} is borrowed.")
        else:
            print(f"Book '{self.title}' by {self.author} is not available.")

    def return_book(self):
        if not self.available:
            self.available = True
            print(f"Book '{self.title}' by {self.author}' has returned.")
        else:
            print(f"Book '{self.title}' by {self.author}' is available.")

    def display_details(self):
        availability = "Available" if self.available else "Not Available"
        print("Title:", self.title)
        print("Author:", self.author)
        print("Availability:", availability)


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully.")

    def display_books(self):
        print("Library Books:")
        if self.books:
            for book in self.books:
                book.display_details()
                print()
        else:
            print("Book Not available in the library.")

library = Library()

while True:
    print("Library Management System")
    print("1. Add a book")
    print("2. Borrow a book")
    print("3. Return a book")
    print("4. Display available books")
    print("5. Quit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        title = input("Enter the book title: ")
        author = input("Enter the author name: ")
        book = Book(title, author)
        library.add_book(book)

    elif choice == "2":
        title = input("Enter the book title to borrow: ")
        for book in library.books:
            if book.title.lower() == title.lower():
                book.borrow()
                break
        else:
            print("Book not found in the library.")

    elif choice == "3":
        title = input("Enter the book title to return: ")
        for book in library.books:
            if book.title.lower() == title.lower():
                book.return_book()
                break
        else:
            print("Book not found in the library.")

    elif choice == "4":
        library.display_books()

    elif choice == "5":
        print("Thank you for using the Library Management System.")
        break

    else:
        print("Invalid choice. Please try again.")

