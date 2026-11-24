from library import *


def getInt(text):
    while True:
        try:
            return int(input(text))
        except ValueError:
            print("Please enter a valid number.")

def getText(message):
    while True:
        value = input(message).strip()

        if value:
            return value

        print("Not be empty")


def showMenu():
    print("""
    
    ===== LIBRARY MENU =====
    1 - Add book
    2 - Add student
    3 - Show books
    4 - Show students
    5 - Search book
    6 - Search student
    7 - Borrow book
    8 - Return book
    0 - Exit

    """)

def main():
    lib = Library("My Library")

    while True:
        showMenu()

        choice = getInt("Enter choice; ")

        if choice == 1:
            bookID = getInt("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            pageCount = getInt("Page count: ")
            lib.addBooks(Book(bookID, title, author, pageCount))
            print("Book added.")

        elif choice == 2:
            studentID = getInt("Student ID: ")
            name = input("Enter Student Name: ")
            lib.addStudent(Student(studentID, name))


    

    