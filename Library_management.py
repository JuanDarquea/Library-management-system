# Library management system - Book, library and user management classes (Object Oriented Programming)

class Book:
    def __init__(self, Title, Author, Year, ISBN): # Constructor to initialize book attributes
        self.title = Title        # Title atribute
        self.author = Author      # Author atribute
        self.year = Year          # publication date
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

book1 = Book("1984", "George Orwell", 1949, "1234567890") # First book instance
book1.show_book_info()                                    # Display book information

