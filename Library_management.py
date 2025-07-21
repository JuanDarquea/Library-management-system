# Library management system - Book, library and user management classes (Object Oriented Programming)

class Book:
    def __init__(self, Title, Author, Year, ISBN): # Constructor to initialize book attributes
        self.title = Title        # Title atribute
        self.author = Author      # Author atribute
        self.year = Year          # Publication date
        self.isbn = ISBN          # ISBN code
        self.is_borrowed = False  # Initial book status, not borrowed
    def show_book_info(self):                                    # Method to display book information
        """Display book information."""
        status = "Borrowed" if self.is_borrowed else "Available" # Check if the book is borrowed
                                                                 # Print book details
        print(f"Title: {self.title}", f"\nAuthor: {self.author}", f"\nYear: {self.year}", f"\nISBN: {self.isbn}", f"\nStatus: {status}")
        print("-" * 40)  # Separator line for better readability
    def borrow(self):                               # Method to borrow a book
        """Borrow the book if it is available."""
        if self.is_borrowed:                        # Check if the book is already borrowed
            print("The book is borrowed and cannot be borrowed again.")
        else:                                       # If the book is available
            self.is_borrowed = True                 # Set book status to borrowed
            print("Book borrowed successfully.")
    def return_book(self):                           # Method to return a borrowed book
        """Return the borrowed book."""
        if not self.is_borrowed:                     # Check if the book is not borrowed
            print("The book is already available in the library.")
        else:                                        # If the book is borrowed
            self.is_borrowed = False                 # Set book status to available
            print("Book returned successfully.")

class User:
    def __init__(self, User_id, Name, Email):
        self.user_id = User_id
        self.name = Name
        self.email = Email
        self.borrowed_books = []  # List of borrowed books
    def show_user_info(self):     # Function to display user information
        """Display user information."""
        print(f"\nUser: {self.name}", f"\nUser ID: {self.user_id}", f"\nEmail: {self.email}")
        if self.borrowed_books:                                # Check if the user has borrowed books
            print("\nBorrowed books:")
            for book in self.borrowed_books:                   # Iterate through borrowed books
                print(f"    - {book.title} by {book.author}")  # Display borrowed book details
        else:
            print("No borrowed books at the moment.")
    """Methods to (intention) request and return books, simulating user actions."""
    def request_book(self, book_title): # Method to request a book(intention to borrow)
        print(f"\n{self.name} requests the book '{book_title}'.")
        return book_title
    def return_book(self, book_title): # Method to return a book(intention to return)
        print(f"\n{self.name} returns the book '{book_title}'.")
        return book_title

# Creation of Library class to manage books and users
class Library: 
    def __init__(self):
        self.books = [] # List to store book instances
        self.users = [] # List to store user instances
    def add_book(self, book): # Method to add a book to the library
        """Add a book to the library."""
        self.books.append(book) # Add book to the library's book list
        print(f"The book '{book.title}' has been added to the library.")
    def add_user(self, user): # Method to add a user to the library
        """Add a user to the library."""
        self.users.append(user) # Add user to the library's user list
        print(f"User {user.name} registered successfully.")
    def show_books(self): # Method to display all books in the library
        """Display all books in the library."""
        if not self.books: # Check if there are no books in the library
            print("\nNo books available in the library.")
        else:
            print("\nBooks in the library:")
            for book in self.books:
                book.show_book_info() # Display book information
    def show_users(self): # Method to display all users in the library
        """Display all users in the library."""
        print("\nRegistered users:")
        for user in self.users:
            print(f"    - {user.name} (ID: {user.user_id})")
    def lend_book(self, book_title, user_id): # Method to lend a book to a user
        """Lend a book to a user."""
        book = next((b for b in self.books if b.title == book_title), None) # Find the book by title
        if not book: # Check if the book exists in the library
            print(f"The book '{book_title}' is not available in the library.")
            return # Exit the method if the book is not found
        user = next((u for u in self.users if u.user_id == user_id), None) # Find the user by ID
        if not user: # Check if the user exists in the library
            print(f"The user with ID '{user_id}' is not registered in the library.")
            return # Exit the method if the user is not found
        # Check if the book is already borrowed
        if book.is_borrowed: 
            print(f"The book '{book_title}' is already borrowed.")
        else: # If the book is available
            book.is_borrowed = True # Set book status to borrowed
            user.borrowed_books.append(book) # Add book to the user's borrowed books list
            print(f"The book '{book_title}' has been lent to {user.name}.")
    def return_book(self, book_title, user_id): # Method to return a borrowed book
        """Return a borrowed book."""
        user = next((u for u in self.users if u.user_id == user_id), None) # Find the user by ID
        if not user: # Check if the user exists in the library
            print(f"The user with ID '{user_id}' is not registered in the library.")
            return
        book = next((b for b in user.borrowed_books if b.title == book_title), None) # Find the book in the user's borrowed books
        if not book: # Check if the book is borrowed by the user
            print(f"The book '{book_title}' is not borrowed by {user.name}.")
            return
        book.is_borrowed = False # Set book status to not borrowed
        user.borrowed_books.remove(book) # Remove book from the user's borrowed books list
        print(f"The book '{book_title}' has been returned by {user.name}.")

# Example usage of user classes and library management:
user1 = User(1, "Ana García", "ana@email.com") # Create an instance of the User class
user2 = User(2, "Luis Pérez", "luis@email.com")
user3 = User(3, "María López", "maria@email.com")
library = Library() # Create an instance of the Library class
library.add_user(user1) # Add users to the library
library.add_user(user2)
library.add_user(user3)
print()
# Example usage of book classes and library management:
book1 = Book("1984", "George Orwell", 1949, "1234567890") # Create an instance of the Book class
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960, "0987654321")
book3 = Book("El Principito", "Antoine de Saint-Exupéry", 1943, "1122334455")
library.add_book(book1) # Add books to the library
library.add_book(book2)
library.add_book(book3)
print()
# Display all books and users in the library
library.show_books() # Show all books in the library
print()
library.show_users() # Show all users in the library
# Example of borrowing and returning books
print()
library.lend_book("1984", 1) # User 1 borrows "1984"
library.lend_book("1984", 2) # User 2 tries to borrow "1984" (already borrowed)
library.return_book("1984", 1) # User 1 returns "1984"
library.lend_book("1984", 2) # User 2 borrows "1984" after it has been returned