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
            bookID = getInt("Enter Book ID: ")
            title = input("Enter Title: ")
            author = input("Enter Author: ")
            pageCount = getInt("Enter Page Count: ")
            lib.addBooks(Book(bookID, title, author, pageCount))
            print("Book added.")

        elif choice == 2:
            studentID = getInt("Enter Student ID: ")
            name = input("Enter Student Name: ")
            lib.addStudent(Student(studentID, name))
            print("Student added.")
            input("\nPress ENTER to continue...")

        elif choice == 3:
            lib.showBooks()
            input("\nPress ENTER to continue...")

        elif choice == 4:
            lib.showStudent()
            input("\nPress ENTER to continue...")

        elif choice == 5:
            getID = getInt("Enter Book ID:")
            lib.searchBook(getID)
            input("\nPress ENTER to continue...")

        elif choice == 6:
            getID = getInt("Enter Student ID:")
            lib.searchStudent(getID)
            input("\nPress ENTER to continue...")

        elif choice == 7:
            getID = getInt("Enter Student ID:")
            getID2 = getInt("Enter Book ID:")
            lib.borrowBook(getID, getID2)
            input("\nPress ENTER to continue...")

        elif choice == 8:
            getID = getInt("Enter Student ID:")
            getID2 = getInt("Enter Book ID:")
            lib.returnBook(getID, getID2)
            input("\nPress ENTER to continue...")

        elif choice == 0:
            print("Closing..")
            break

        else:
            print("Something went wrong..")

main()


    

    