# Library management system - Book, library and user management classes (Object Oriented Programming)
import tkinter as tk # Importing tkinter for GUI elements
from tkinter import simpledialog # Importing simpledialog for user input dialogs
from tkinter import messagebox # Importing messagebox for displaying messages

# Creation of main window for the library management system
root =tk.Tk() # Create the main window
root.title("Library Management System") # Set the title of the window
root.geometry("400x400") # Set the size of the window

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
        window_book =tk.Toplevel(root) # Create a new window for adding a book
        window_book.title("Add Book") # Set the title of the window
        window_book.geometry("320x300") # Set the size of the window

        tk.Label(window_book, text = "Title:").pack() # Label for book title input
        title_entry = tk.Entry(window_book) # Entry field for book title
        title_entry.pack() # Pack the title entry field
        tk.Label(window_book, text = "Author:").pack() # Label for book author input
        author_entry = tk.Entry(window_book) # Entry field for book author
        author_entry.pack() # Pack the author entry field
        tk.Label(window_book, text = "Year:").pack() # Label for book year input
        year_entry = tk.Entry(window_book) # Entry field for book year
        year_entry.pack() # Pack the year entry field
        tk.Label(window_book, text = "ISBN:").pack() # Label for book ISBN input
        isbn_entry = tk.Entry(window_book) # Entry field for book ISBN
        isbn_entry.pack() # Pack the ISBN entry field

        messagebox.showinfo("Add Book", f"Adding book: {book.title}") # Show message box with book title
        if any(b.title == book.title for b in self.books): # Check if the book already exists in the library
            print(f"The book '{book.title}' already exists in the library.")
            return # Exit the method if the book is already in the library
        if not isinstance(book, Book): # Check if the book is an instance of the Book class
            print("Invalid book object. Please provide a valid Book instance.")
            return # Exit the method if the book is not valid
        # If the book is valid and does not exist in the library
        self.books.append(book) # Add book to the library's book list
        print(f"The book '{book.title}' has been added to the library.")
    def remove_book(self, book_title): # Method to remove a book from the library
        """Remove a book from the library."""
        book = next((b for b in self.books if b.title == book_title), None) # Find the book by title
        if not book: # Check if the book exists in the library
            messagebox.showerror("ERROR", f"The book '{book_title}' does not exist in the library.")
            return # Exit the method if the book is not found
        # Check if the book is borrowed
        if book.is_borrowed: # If the book is borrowed
            messagebox.showwarning("WARNING",f"The book '{book.title}' is currently borrowed and cannot be removed.")
            return # Exit the method if the book is borrowed
        # If the book is not borrowed, it can be removed
        self.books.remove(book) # Remove book from the library's book list
        messagebox.showinfo(f"Removing book: {book.title}", f"The book has been removed successfully from the library.") # Show message box with book title
    def add_user(self, user): # Method to add a user to the library
        """Add a user to the library."""
        self.users.append(user) # Add user to the library's user list
        print(f"User {user.name} registered successfully.")
        messagebox.showinfo("Add User", f"User {user.name} registered successfully.") # Show message box with user name
        # Check if the user already exists in the library
        if any(u.user_id == user.user_id for u in self.users): # Check if the user ID already exists
            print(f"The user with ID '{user.user_id}' already exists in the library.")
            return # Exit the method if the user already exists
        if not isinstance(user, User): # Check if the user is an instance of the User class
            print("Invalid user object. Please provide a valid User instance.")
            return
    def remove_user(self, user_id): # Method to remove a user from the library
        """Remove a user from the library."""
        user = next((u for u in self.users if u.user_id == user_id), None) # Find the user by ID
        if not user: # Check if the user exists in the library
            messagebox.showerror("ERROR", f"The user {user.name} with ID '{user_id}' does not exist in the library.")
            return # Exit the method if the user is not found
        # Check if the user has borrowed books
        if user.borrowed_books: # If the user has borrowed books
            messagebox.showwarning("WARNING", f"The user {user.name} with ID '{user_id}' has borrowed books and cannot be removed.")
            return # Exit the method if the user has borrowed books
        # If the user has no borrowed books, they can be removed
        self.users.remove(user) # Remove user from the library's user list
        messagebox.showinfo(f"Removing user: {user.name}", "The user has been removed successfully from the library.") # Show message box with user name
    def show_books(self): # Method to display all books in the library
        """Display all books in the library."""
        # Iterate through the books and display their information
        if not self.books: # Check if there are no books in the library
            print("\nNo books available in the library.")
        else:
            print("\nBooks in the library:")
            for book in self.books:
                book.show_book_info() # Display book information
        messagebox.showinfo("Show Books", "Displaying all books in the library.") # Show message box indicating books are displayed
    def show_users(self): # Method to display all users in the library
        """Display all users in the library."""
        print("\nRegistered users:")
        for user in self.users:
            print(f"    - {user.name} (ID: {user.user_id})")
        messagebox.showinfo("Show Users", "Displaying all registered users in the library.") # Show message box indicating users are displayed
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
            messagebox.showinfo("Lend Book", f"Lending book: {book.title} to {user.name}") # Show message box with book title and user name
            # Update the library's book inventory
            self.books.remove(book) # Remove book from the library's book list
            print(f"The book '{book.title}' has been removed from the library's inventory.")
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
        messagebox.showinfo("Return Book", f"Returning book: {book.title}") # Message box to return a book
        # Update the library's book inventory
        self.books.append(book)

def open_form_add_book():
    window = tk.Toplevel(root)
    window.title = tk.Entry(window)
    window.geometry("300x230")

    tk.Label(window, text = "Title:").pack_slaves
    title_entry = tk.Entry(window)
    title_entry.pack()
    tk.Label(window, text = "Author:").pack()
    author_entry = tk.Entry(window)
    author_entry.pack()
    tk.Label(window, text = "Year:").pack()
    year_entry = tk.Entry(window)
    year_entry.pack()
    tk.Label(window, text = "ISBN:").pack()
    isbn_entry = tk.Entry(window)
    isbn_entry.pack()

    def save():
        title = title_entry.get()
        author = author_entry.get()
        year = year_entry.get()
        isbn = isbn_entry.get()
        if not title or not author or not year.isdigit() or not isbn:
            messagebox.showerror("Error", "Please fill in all fields.")
            return
        new_book = Book(title, author, year, isbn)
        library.add_book(new_book)
        messagebox.showinfo("Success", f"Book '{title}' added successfully.")
        window.destroy()

    tk.Button(window, text = "Save", command = save).pack(pady = 5)
    tk.Button(window, text = "Cancel", command = window.destroy).pack(pady = 5)

def open_form_add_user():
    window = tk.Toplevel(root)
    window.title = tk.Entry(window)
    window.geometry("300x230")

    tk.Label(window, text = "ID:").pack_slaves
    user_id_entry = tk.Entry(window)
    user_id_entry.pack()
    tk.Label(window, text = "Name:").pack()
    name_entry = tk.Entry(window)
    name_entry.pack()
    tk.Label(window, text = "Email:").pack()
    email_entry = tk.Entry(window)
    email_entry.pack()

    def save():
        user_id = user_id_entry.get()
        name = name_entry.get()
        email = email_entry.get()
        if not user_id.isdigit() or not name or not email:
            messagebox.showerror("Error", "Please fill in all fields.")
            return
        new_user = User(user_id, name, email)
        library.add_user(new_user)
        messagebox.showinfo("Success", f"User '{name}' added successfully.")
        window.destroy()

    tk.Button(window, text = "Save", command = save).pack(pady = 5)
    tk.Button(window, text = "Cancel", command = window.destroy).pack(pady = 5)

def open_form_remove_book():
    window = tk.Toplevel(root)
    window.title = tk.Entry(window)
    window.geometry("300x230")

    tk.Label(window, text = "Title:").pack_slaves
    title_entry = tk.Entry(window)
    title_entry.pack()
    tk.Label(window, text = "Author:").pack()
    author_entry = tk.Entry(window)
    author_entry.pack()
    tk.Label(window, text = "Year:").pack()
    year_entry = tk.Entry(window)
    year_entry.pack()
    tk.Label(window, text = "ISBN:").pack()
    isbn_entry = tk.Entry(window)
    isbn_entry.pack()

    def save():
        title = title_entry.get()
        author = author.get()
        year = year_entry.get()
        isbn = isbn_entry.get()
        if not title or not author or not year.isdigit() or not isbn:
            messagebox.showerror("Error", "Please fill in all fields.")
            return
          
    tk.Button(window, text = "Save", command = save).pack(pady = 5)
    tk.Button(window, text = "Cancel", command = window.destroy).pack(pady = 5)

def open_form_remove_user():
    window = tk.Toplevel(root)
    window.title = tk.Entry(window)
    window.geometry("300x230")

    tk.Label(window, text = "ID:").pack_slaves
    user_id_entry = tk.Entry(window)
    user_id_entry.pack()
    tk.Label(window, text = "Name:").pack()
    name_entry = tk.Entry(window)
    name_entry.pack()
    tk.Label(window, text = "Email:").pack()
    email_entry = tk.Entry(window)
    email_entry.pack()

    def save():
        user_id = user_id_entry.get()
        name = name_entry.get()
        email = email_entry.get()
        if not user_id.isdigit() or not name or not email:
            messagebox.showerror("Error", "Please fill in all fields.")
            return
        new_user = User(user_id, name, email)
        library.add_user(new_user)
        messagebox.showinfo("Success", f"User '{name}' added successfully.")
        window.destroy()

    tk.Button(window, text = "Save", command = save).pack(pady = 5)
    tk.Button(window, text = "Cancel", command = window.destroy).pack(pady = 5)

def open_form_lend_book():
    window = tk.Toplevel(root)
    window.title = tk.Entry(window)
    window.geometry("300x230")

    tk.Label(window, text = "Title:").pack_slaves
    title_entry = tk.Entry(window)
    title_entry.pack()
    tk.Label(window, text = "Author:").pack()
    author_entry = tk.Entry(window)
    author_entry.pack()
    tk.Label(window, text = "Year:").pack()
    year_entry = tk.Entry(window)
    year_entry.pack()
    tk.Label(window, text = "ISBN:").pack()
    isbn_entry = tk.Entry(window)
    isbn_entry.pack()

    def save():
        title = title_entry.get()
        author = author.get()
        year = year_entry.get()
        isbn = isbn_entry.get()
        if not title or not author or not year.isdigit() or not isbn:
            messagebox.showerror("Error", "Please fill in all fields.")
            return
          
    tk.Button(window, text = "Save", command = save).pack(pady = 5)
    tk.Button(window, text = "Cancel", command = window.destroy).pack(pady = 5)

def open_form_return_book():
    window = tk.Toplevel(root)
    window.title = tk.Entry(window)
    window.geometry("300x230")

    tk.Label(window, text = "Title:").pack_slaves
    title_entry = tk.Entry(window)
    title_entry.pack()
    tk.Label(window, text = "Author:").pack()
    author_entry = tk.Entry(window)
    author_entry.pack()
    tk.Label(window, text = "Year:").pack()
    year_entry = tk.Entry(window)
    year_entry.pack()
    tk.Label(window, text = "ISBN:").pack()
    isbn_entry = tk.Entry(window)
    isbn_entry.pack()

    def save():
        title = title_entry.get()
        author = author.get()
        year = year_entry.get()
        isbn = isbn_entry.get()
        if not title or not author or not year.isdigit() or not isbn:
            messagebox.showerror("Error", "Please fill in all fields.")
            return
          
    tk.Button(window, text = "Save", command = save).pack(pady = 5)
    tk.Button(window, text = "Cancel", command = window.destroy).pack(pady = 5)

def show_books():
    window = tk.Toplevel(root)
    window.title("Books in Library")
    window.geometry("300x230")
    
    text = tk.Text(window)
    text.pack(expand = True, fill = "both")
    if not Library.books:
        text.insert(tk.END, "There are no books available in library.\n")
    else:
        for book in Library.books:
            state = "Borrowed" if book.is_borrowed else "Available"
            text.insert(tk.END, f"{book.title} by {book.author} ({book.year}) - {state}\n")
            text.config(state = "Disabled")

def show_users():
    window = tk.Toplevel(root)
    window.title("Library Users")
    window.geometry("300x230")

    text = tk.Text(window)
    text.pack(expand = True, fill = "both")
    if not Library.users:
        text.insert(tk.END, "There are no registered users in library.\n")
    else:
        for user in Library.show_users:
            text.insert(tk.END, f"{user.name} (ID: {user.user_id})")
            text.config(state = "Disabled")
                        


library = Library() # Create an instance of the Library class
tk.Button(root, text="Add Book", command = open_form_add_book, width=30).pack(pady=5)
tk.Button(root, text="Remove Book", command = open_form_remove_book, width=30).pack(pady=5)
tk.Button(root, text="Add User", command = open_form_add_user, width=30).pack(pady=5)
tk.Button(root, text="Remove User", command = open_form_remove_user, width=30).pack(pady=5)
tk.Button(root, text="Lend Book", command = open_form_lend_book, width=30).pack(pady=5)
tk.Button(root, text="Return Book", command = open_form_return_book, width=30).pack(pady=5)
tk.Button(root, text="Show Books", command = show_books, width=30).pack(pady=5)
tk.Button(root, text="Show Users", command = show_users, width=30).pack(pady=5)
root.mainloop() # Start the main event loop of the GUI

# Example usage of user classes and library management:
#user1 = User(1, "Ana García", "ana@email.com") # Create an instance of the User class
#user2 = User(2, "Luis Pérez", "luis@email.com")
#user3 = User(3, "María López", "maria@email.com")
#library = Library() # Create an instance of the Library class
#library.add_user(user1) # Add users to the library
#library.add_user(user2)
#library.add_user(user3)
#print()
# Example usage of book classes and library management:
#book1 = Book("1984", "George Orwell", 1949, "1234567890") # Create an instance of the Book class
#book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960, "0987654321")
#book3 = Book("El Principito", "Antoine de Saint-Exupéry", 1943, "1122334455")
#library.add_book(book1) # Add books to the library
#ibrary.add_book(book2)
#library.add_book(book3)
#print()
# Display all books and users in the library
#library.show_books() # Show all books in the library
#print()
#library.show_users() # Show all users in the library
# Example of borrowing and returning books
#print()
#library.lend_book("1984", 1) # User 1 borrows "1984"
#ibrary.lend_book("1984", 2) # User 2 tries to borrow "1984" (already borrowed)
#library.return_book("1984", 1) # User 1 returns "1984"
#library.lend_book("1984", 2) # User 2 borrows "1984" after it has been returned