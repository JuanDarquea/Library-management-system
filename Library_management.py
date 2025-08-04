# Library management system - Book, library and user management classes (Object Oriented Programming)
import tkinter as tk # Importing tkinter for GUI elements
from tkinter import simpledialog # Importing simpledialog for user input dialogs
from tkinter import messagebox # Importing messagebox for displaying messages

# Creation of main window for the library management system
root =tk.Tk() # Create the main window
root.title("Library Management System") # Set the title of the window
root.geometry("400x400") # Set the size of the window
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
        # Check if the book already exists in the library
        if any(b.title == book.title and b.author == book.author for b in self.books):
            # Exit the method if the book is already in the library
            return False, "The book already exists in the library." 
        
        if not isinstance(book, Book): # Check if the book is an instance of the Book class
            # Exit the method if the book is not a valid instance
            return False, "Invalid book object. Please provide a valid Book instance."
        
        # If the book is valid, add it to the library's book list
        # Check if the book already exists in the library
        if any(b.title == book.title for b in self.books):
            # Exit the method if the book is already in the library
            return False, "The book already exists in the library." 
        
        if not isinstance(book, Book): # Check if the book is an instance of the Book class
            # Exit the method if the book is not a valid instance
            return False, "Invalid book object. Please provide a valid Book instance."
        
        # If the book is valid, add it to the library's book list
        self.books.append(book) # Add book to the library's book list
        print(f"DEBUG: Book '{book.title}' added to library. Total books in library: {len(self.books)}") # Debug message to confirm book addition
        # Show success message with book title
        return True, f"The Book '{book.title}' was added successfully to the library."

    def remove_book(self, book_title): # Method to remove a book from the library
        """Remove a book from the library."""
        # Find the book by title
        book = next((b for b in self.books if b.title == book_title), None)
        if not book: # Check if the book exists in the library
            # Exit the method if the book is not found
            return False, "The book is not found in the library."
        
        # Check if the book is borrowed
        if book.is_borrowed: # If the book is borrowed
            # Exit the method if the book is borrowed
            return False, "The book is borrowed already and cannot be removed." 
        
        # If the book is not borrowed, it can be removed
        self.books.remove(book) # Remove book from the library's book list
        # Show success message
        return True, f"The book has been removed successfully from the library." 

    def add_user(self, user): # Method to add a user to the library
        """Add a user to the library."""
        # Check if the user already exists in the library
        if any(u.user_id == user.user_id for u in self.users):
            # Exit the method if the user already exists
            return False, f"The user with ID '{user.user_id}' already exists in the library." 
        
        # Check if the user is an instance of the User class
        if not isinstance(user, User): 
            # Exit the method if the user is not a valid instance
            return False, "Invalid user object. Please provide a valid User instance."
        
        # Check if the user already exists in the library
        if any(u.user_id == user.user_id for u in self.users):
            # Exit the method if the user already exists
            return False, f"The user with ID '{user.user_id}' already exists in the library." 
        
        # Check if the user is an instance of the User class
        if not isinstance(user, User): 
            # Exit the method if the user is not a valid instance
            return False, "Invalid user object. Please provide a valid User instance."
        
        self.users.append(user) # Add user to the library's user list
        print(f"DEBUG: User '{user.name}' added to library. Total users in library: {len(self.users)}") # Debug message to confirm user addition
        # Show success message with users name and ID
        return True, f"User '{user.name}' with ID '{user.user_id}' registered successfully."

    def remove_user(self, user_id): # Method to remove a user from the library
        """Remove a user from the library."""
        # Find the user by ID
        user = next((u for u in self.users if str(u.user_id) == str(user_id)), None)
        if not user: # Check if the user exists in the library
            # Exit the method if the user is not found
            return False, f"The user with ID '{user_id}' does not exist in the library." 
        
        # Check if the user has borrowed books
        if user.borrowed_books: # If the user has borrowed books
            # Exit the method if the user has borrowed books
            return False, f"The user with ID '{user_id}' has borrowed books and cannot be removed."
        
        # If the user has no borrowed books, they can be removed
        self.users.remove(user) # Remove user from the library's user list
        # Show success message with user name
        return True, f"The user {user.name} with ID '{user_id}' has been removed successfully from the library."

#    def show_books(self): # Method to display all books in the library
#        """Display all books in the library."""
        # Iterate through the books and display their information
#        if not self.books: # Check if there are no books in the library
#            return False, "No books available in the library."
#        else:
#            for book in self.books:
#                book.show_book_info()
#            return True, f"Displayed {len(self.books)} books."  # Display book information

#    def show_users(self): # Method to display all users in the library
#        """Display all users in the library."""
#        if not self.users: # Check if there are no users in the library
#            return False, "No registered users in the library."
#        else:
#            for user in self.users:
#                user.show_user_info()
#            return True, f"Displayed {len(self.users)} users."  # Display user information

    def lend_book(self, book_title, user_id): # Method to lend a book to a user
        """Lend a book to a user."""
        # Find the book by title
        book = next((b for b in self.books if b.title == book_title), None) 
        # Find the book by title
        book = next((b for b in self.books if b.title == book_title), None) 
        if not book: # Check if the book exists in the library
            # Exit the method if the book is not found
            return False, f"The book '{book_title}' is not available in the library."
        
        # Find the user by ID
        user = next((u for u in self.users if str(u.user_id) == str(user_id)), None)
            # Exit the method if the book is not found
        return False, f"The book '{book_title}' is not available in the library."
        
        # Find the user by ID
        user = next((u for u in self.users if str(u.user_id) == str(user_id)), None)
        if not user: # Check if the user exists in the library
            # Exit the method if the user is not found
            return False, f"The user with ID '{user_id}' is not registered in the library."
        
            # Exit the method if the user is not found
            return False, f"The user with ID '{user_id}' is not registered in the library."
        
        # Check if the book is already borrowed
        if book.is_borrowed: 
            return False, f"The book '{book_title}' is already borrowed."
            return False, f"The book '{book_title}' is already borrowed."
        else: # If the book is available
            book.is_borrowed = True # Set book status to borrowed
            # Add book to the user's borrowed books list
            user.borrowed_books.append(book) 
            # Show success message with book title and user name
            return True, f"The book '{book.title}' has been borrowed to {user.name}"

            # Add book to the user's borrowed books list
            user.borrowed_books.append(book) 
            # Show success message with book title and user name
            return True, f"The book '{book.title}' has been borrowed to {user.name}"

    def return_book(self, book_title, user_id): # Method to return a borrowed book
        """Return a borrowed book."""
        # Find the user by ID
        user = next((u for u in self.users if str(u.user_id) == str(user_id)), None)
        # Find the user by ID
        user = next((u for u in self.users if str(u.user_id) == str(user_id)), None)
        if not user: # Check if the user exists in the library
            # Show message with error if user doesn't exist
            return False, f"The user with ID '{user_id}' is not registered in the library."
        
        # Find the book in the user's borrowed books
        book = next((b for b in user.borrowed_books if b.title == book_title), None) 
            # Show message with error if user doesn't exist
        return False, f"The user with ID '{user_id}' is not registered in the library."
        
        # Find the book in the user's borrowed books
        book = next((b for b in user.borrowed_books if b.title == book_title), None) 
        if not book: # Check if the book is borrowed by the user
            # Show message with error if book is not borrowed by the user
            return False, f"The book '{book_title}' is not borrowed by the user."
        
            # Show message with error if book is not borrowed by the user
            return False, f"The book '{book_title}' is not borrowed by the user."
        
        book.is_borrowed = False # Set book status to not borrowed
        # Remove book from the user's borrowed books list
        user.borrowed_books.remove(book)
        # Message box to return a book
        return True, f"The book '{book_title}' has been returned by the user '{user.name}'."

def open_form_add_book():
    window = tk.Toplevel(root)
    window.title("Add Book")
    window.geometry("300x230")

    tk.Label(window, text = "Title:").pack()
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
        title = title_entry.get().strip()
        author = author_entry.get().strip()
        year = year_entry.get().strip()
        isbn = isbn_entry.get().strip()

        if not title or not author or not year.isdigit() or not isbn:
            messagebox.showerror("Error", "Please fill in all fields.")
            return
        # Create a new book instance with the provided details
        new_book = Book(title, author, year, isbn)
        success, msg = library.add_book(new_book)
        if success:
            messagebox.showinfo("Success", f"Book '{title}' added successfully.")
        else:
            messagebox.showwarning("Warning", f"Book '{title}' already exists in the library.")
        window.destroy()

    tk.Button(window, text = "Save", command = save).pack(pady = 5)
    tk.Button(window, text = "Cancel", command = window.destroy).pack(pady = 5)

def open_form_add_user():
    window = tk.Toplevel(root)
    window.title("Add User")
    window.geometry("300x230")

    tk.Label(window, text = "ID:").pack()
    user_id_entry = tk.Entry(window)
    user_id_entry.pack()
    tk.Label(window, text = "Name:").pack()
    name_entry = tk.Entry(window)
    name_entry.pack()
    tk.Label(window, text = "Email:").pack()
    email_entry = tk.Entry(window)
    email_entry.pack()

    def save():
        user_id = user_id_entry.get().strip()
        name = name_entry.get().strip()
        email = email_entry.get().strip()

        if not user_id.isdigit() or not name or not email:
            messagebox.showerror("Error", "Please fill in all fields.")
            return
        # Create a new user instance with the provided details
        new_user = User(user_id, name, email)
        library.add_user(new_user)
        messagebox.showinfo("Success", f"User '{name}' added successfully.")
        window.destroy()

    tk.Button(window, text = "Save", command = save).pack(pady = 5)
    tk.Button(window, text = "Cancel", command = window.destroy).pack(pady = 5)

def open_form_remove_book():
    window = tk.Toplevel(root)
    window.title("Remove Book")
    window.geometry("300x120")

    tk.Label(window, text = "Title:").pack()
    title_entry = tk.Entry(window)
    title_entry.pack()


    def remove_book():
        title = title_entry.get().strip()
        if not title:
            messagebox.showerror("Error", "Please enter the book title.")
            return
        success, msg = library.remove_book(title)
        # Check if the book was removed successfully
        if success:
            messagebox.showinfo("Success", msg)
        else:
            messagebox.showerror("Error", msg)
        window.destroy()    
          
    tk.Button(window, text = "Remove", command = remove_book).pack(pady = 5)
    tk.Button(window, text = "Cancel", command = window.destroy).pack(pady = 5)

def open_form_remove_user():
    window = tk.Toplevel(root)
    window.title("Remove User")
    window.geometry("300x120")

    tk.Label(window, text = "User ID:").pack()
    user_id_entry = tk.Entry(window)
    user_id_entry.pack()


    def remove_user():        
        """Function to remove a user from the library."""
        user_id = user_id_entry.get().strip()
        if not user_id.isdigit():
            messagebox.showerror("Error", "Please enter a valid User ID.")
            return
        success, msg = library.remove_user(user_id)
        # Check if the user was removed successfully
        if success:
            messagebox.showinfo("Success", msg)
        else:
            messagebox.showerror("Error", msg)
        window.destroy()

    tk.Button(window, text = "Remove", command = remove_user).pack(pady = 5)
    tk.Button(window, text = "Cancel", command = window.destroy).pack(pady = 5)

def open_form_lend_book():
    window = tk.Toplevel(root)
    window.title("Lend Book")
    window.geometry("300x150")

    tk.Label(window, text = "Book Title:").pack()
    title_entry = tk.Entry(window)
    title_entry.pack()
    tk.Label(window, text = "User ID:").pack()
    user_id_entry = tk.Entry(window)
    user_id_entry.pack()

    def lend():
        title = title_entry.get().strip()
        user_id = user_id_entry.get().strip()
        if not title or not user_id.isdigit():
            messagebox.showerror("Error", "Please fill in all fields correctly.")
            return
        success, msg = library.lend_book(title, str(user_id))
        if success:
            messagebox.showinfo("Success", msg)
        else:
            messagebox.showerror("Error", msg)
        window.destroy()
          
    tk.Button(window, text = "Lend", command = lend).pack(pady = 5)
    tk.Button(window, text = "Cancel", command = window.destroy).pack(pady = 5)

def open_form_return_book():
    window = tk.Toplevel(root)
    window.title("Return Book")
    window.geometry("300x150")

    tk.Label(window, text = "Book Title:").pack()
    title_entry = tk.Entry(window)
    title_entry.pack()
    tk.Label(window, text = "User ID:").pack()
    user_id_entry = tk.Entry(window)
    user_id_entry.pack()

    def return_book():
        title = title_entry.get().strip()
        user_id = user_id_entry.get().strip()
        if not title or not user_id.isdigit():
            messagebox.showerror("Error", "Please fill in all fields.")
           # window.destroy()
            return
        # Return the borrowed book
        success, msg = library.return_book(title, str(user_id))
        if success:
            messagebox.showinfo("Success", msg)
        else:
            messagebox.showerror("Error", msg)
        window.destroy()
          
    tk.Button(window, text = "Return Book", command = return_book).pack(pady = 5)
    tk.Button(window, text = "Cancel", command = window.destroy).pack(pady = 5)

def show_books():
    """Function to display all books in the library."""
    print(f"DEBUG: Total books in library: {len(library.books)}")
    window = tk.Toplevel(root)
    window.title("Books in Library")
    window.geometry("500x400")
    
    frame = tk.Frame(window)
    frame.pack(fill = tk.BOTH, expand = True, padx = 10, pady = 10)
    text = tk.Text(frame, wrap = tk.WORD)
    scrollbar = tk.Scrollbar(frame, orient = tk.VERTICAL, command = text.yview)
    text.configure(yscrollcommand = scrollbar.set)

    text.pack(side = tk.LEFT, fill = tk.BOTH, expand = True)
    scrollbar.pack(side = tk.RIGHT, fill = tk.Y)

    if not library.books:
        text.insert(tk.END, "There are no books available in library.\n")
    else:
        text.insert(tk.END, f"Total books in library: {len(library.books)}\n")
        text.insert(tk.END, "=" * 50 + "\n\n")
        for i, book in enumerate(library.books, start = 1):
            print(f"DEBUG: Book {i + 1}: {book.title}")
            status = "Borrowed" if book.is_borrowed else "Available"
            text.insert(tk.END, f"{i}. \"Title\": {book.title}\n")
            text.insert(tk.END, f"   \"Author\": {book.author}\n")
            text.insert(tk.END, f"   \"Year\": {book.year}\n")
            text.insert(tk.END, f"   \"ISBN\": {book.isbn}\n")
            text.insert(tk.END, f"   \"Status\": {status}\n")
            text.insert(tk.END, "-" * 30 + "\n\n")
    text.config(state = "disabled")

def show_users():
    """Function to display all users in the library."""
    print(f"DEBUG: Total users in library: {len(library.users)}")
    window = tk.Toplevel(root)
    window.title("Library Users")
    window.geometry("500x400")

    frame = tk.Frame(window)
    frame.pack(fill = tk.BOTH, expand = True, padx = 10, pady = 10)
    text = tk.Text(frame, wrap = tk.WORD)
    scrollbar = tk.Scrollbar(frame, orient = tk.VERTICAL, command = text.yview)
    text.configure(yscrollcommand = scrollbar.set)

    text.pack(side = tk.LEFT, fill = tk.BOTH, expand = True)
    scrollbar.pack(side = tk.RIGHT, fill = tk.Y)

    if not library.users:
        text.insert(tk.END, "There are no registered users in library.\n")
    else:
        text.insert(tk.END, f"Total users in library: {len(library.users)}\n")
        text.insert(tk.END, "=" * 50 + "\n\n")
        for i, user in enumerate(library.users, start = 1):
            print(f"DEBUG: User {i + 1}: {user.name}")
            text.insert(tk.END, f"{i}. \"Name\": {user.name}\n")
            text.insert(tk.END, f"   \"User ID\": {user.user_id}\n")
            text.insert(tk.END, f"   \"Email\": {user.email}\n")
            if user.borrowed_books:
                text.insert(tk.END, f"  Borrowed books({len(user.borrowed_books)}):\n")
                for book in user.borrowed_books:
                    text.insert(tk.END, f"    - {book.title} by {book.author}\n")
            else:
                text.insert(tk.END, "  No borrowed books at the moment.\n")
            text.insert(tk.END, "-" * 30 + "\n\n")
    text.config(state = "disabled")
                        


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
