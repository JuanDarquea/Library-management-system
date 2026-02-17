# Library Management System
A Python-based desktop application designed to manage a library's inventory and user database using Object-Oriented Programming (OOP) principles and the Tkinter library for the graphical interface.

## Features
#### Book Management: 
- Add new books with details (Title, Author, Year, ISBN) or remove them from the collection.

#### User Management: 
- Register new library members or remove existing ones using unique IDs.

#### Lending System: 
- Efficiently track which books are lent to which users.

#### Inventory Tracking: 
- Check the status of any book (Available vs. Borrowed) and see a list of books currently held by any user.

### Interactive GUI: 
- User-friendly forms and scrollable lists to view the entire database.

## Technical Architecture
The system is built on three core classes that interact with one another:

#### Book: 
- Handles individual book data and its availability status.

#### User: 
- Manages member information and a personal list of borrowed book objects.

#### Library: 
- The central controller that manages the logic for adding/removing items and processing the lending/returning transactions.

## Requirements
To run this application, you need:
- Python 3.x
- Tkinter (usually included in standard Python installations)

## Installation & Usage
Clone or Copy the Code: 
- Save the provided script as library_system.py.

Run the Application:
```
Bash

python library_system.py
```

#### Navigating the Interface: 
- Add Book/User: 
  - Opens a new window with a form. Ensure all fields are filled (Year and ID must be numeric).
- Lend Book:
  - Requires the exact Book Title and User ID.
- Show Books/Users:
  - Opens a scrollable window displaying the current state of the library.

## Data Validation Rules
#### To prevent data corruption, the system includes several built-in checks:
- No Duplicates: 
  - You cannot add a book title or a User ID that already exists.
- Borrowing Logic:
  - A book cannot be lent if it is already borrowed.
- Removal Safety:
  - A book cannot be removed from the system if it is currently borrowed.
  - A user cannot be removed if they still have books in their possession.
- Input Validation:
  - ID and Year fields strictly require numerical input.

## Future Enhancements
1. Data Persistence: Integrate a database (like SQLite) or JSON file to save data between sessions (currently, data is lost when the app closes).
2. Search Functionality: Add a search bar to find books by ISBN or Author.
3. Due Dates: Implement a system to track return deadlines and late fees.
