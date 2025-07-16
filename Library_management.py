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

    def borrow(self):                               # Method to borrow a book
        """Borrow the book if it is available."""
        if self.is_borrowed:                        # Check if the book is already borrowed
            print("El libro ya está prestado.")
        else:                                       # If the book is available
            self.is_borrowed = True                 # Set book status to borrowed
            print("Libro prestado correctamente.")

    def return_book(self):                           # Method to return a borrowed book
        """Return the borrowed book."""
        if not self.is_borrowed:                     # Check if the book is not borrowed
            print("El libro ya está disponible en la biblioteca.")
        else:                                        # If the book is borrowed
            self.is_borrowed = False                 # Set book status to available
            print("Libro devuelto correctamente.")

class User:
    def __init__(self, User_id, Name, Email):
        self.user_id = User_id
        self.name = Name
        self.email = Email
        self.borrowed_books = []  # List of borrowed books
    def show_user_info(self):     # Function to display user information
        """Display user information."""
        print(f"Usuario: {self.name}", f"\nID usuario: {self.user_id}", f"\nCorreo: {self.email}")
        if self.borrowed_books:                                # Check if the user has borrowed books
            print("Libros prestados:")
            for book in self.borrowed_books:                   # Iterate through borrowed books
                print(f"    - {book.title} de {book.author}")  # Display borrowed book details
        else:
            print("No tiene libros prestados actualmente")
    """Methods to (intention) request and return books, simulating user actions."""
    def request_book(self, book_title): # Method to request a book(intention to borrow)
        print(f"{self.name} solicita el libro '{book_title}'.")
        return book_title
    def return_book(self, book_title): # Method to return a book(intention to return)
        print(f"{self.name} devuelve el libro '{book_title}'.")
        return book_title

book1 = Book("1984", "George Orwell", 1949, "1234567890") # First book instance
book1.show_book_info()                                    # Display book information

