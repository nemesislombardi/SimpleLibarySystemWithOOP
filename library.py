from book import *
from student import *


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.students = []

    def addBooks(self, book):
        self.books.append(book)

    def addStudent(self, student):
        self.students.append(student)

    def showBooks(self):
        if not self.books:
            print("Book data empty")
            return

        for x in self.books:
            x.showBook()
            print("-" * 30)

    def showStudent(self):
        if not self.students:
            print("Student data empty")
            return

        for x in self.students:
            x.showStudent()
            print("-" * 30)

    def searchBook(self, bookID):
        if not self.books:
            print("Book data empty")
            return

        for x in self.books:
            if x.bookID == bookID:
                print(f"ID: {x.bookID}")
                print(f"Title: {x.title}")
                print(f"Author: {x.author}")
                print(f"Page Count: {x.pageCount}")
                print(f"Status: {'Available' if x.isAvailable else 'Borrowed'}")
                print("-" * 30)
                return

        print("Book not found.")

    def searchStudent(self, studentID):
        if not self.students:
            print("Student data empty")
            return

        for x in self.students:
            if x.studentID == studentID:
                print(f"ID: {x.studentID}")
                print(f"Name: {x.Name}")
                print(f"Borrowed Books: {len(x.borrowedBooks)}")
                print("-" * 30)
                return

        print("Student not found.")

    def borrowBook(self, studentID, bookID):
        if not self.students:
            print("Student data empty")
            return

        if not self.books:
            print("Book data empty")
            return

        student = None
        for x in self.students:
            if x.studentID == studentID:
                student = x
                break

        if student is None:
            print("Student not found.")
            return

        book = None
        for x in self.books:
            if x.bookID == bookID:
                book = x
                break

        if book is None:
            print("Book not found.")
            return

        student.borrowBook1(book)

    def returnBook(self, studentID, bookID):
        if not self.students:
            print("Student data empty")
            return

        if not self.books:
            print("Book data empty")
            return

        student = None
        for x in self.students:
            if x.studentID == studentID:
                student = x
                break

        if student is None:
            print("Student not found.")
            return

        book = None
        for x in self.books:
            if x.bookID == bookID:
                book = x
                break

        if book is None:
            print("Book not found.")
            return

        student.returnBookS(book)