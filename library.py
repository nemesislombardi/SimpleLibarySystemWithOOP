from book import *
from student import *


class Libary:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.students = []


    def addBooks(self,book):
        self.books.append(book)

    def addStudent(self,student):
        self.addStudent(student)

    def showBooks(self):
        if not self.books:
            print("Book data empty")
            return

        for x in self.books:
            x.showBook()
            print("-" *30)
            

    def showStudent(self):
        if not self.students:
            print("Student data empty")
            return

        for x in self.students:
            x.showStudent()
            print("-" *30)
            

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
                print(f"Status: {'Available' if x.isAvaible else 'Borrowed'}")
                print("-" * 30)
                return

        print("Book not found.")



    def searchStudent(self,studentID):
        if not self.students:
            print("Student data empty")
            return

        for x in self.students:
            if x['id'] == studentID:
                print(f"ID: {x[self.studentID]}")
                print(f"Name: {x[self.Name]}")
                print(f"Borrowed Books: {x[len(self.borrowedBooks)]}")
                print("-" *30)
                return
            
        print("Student not found.")

    def borrowBook(self,studentID,bookID):
        if not self.students:
            print("Student data empty")
            return

        if not self.books:
            print("Book data empty")
            return

        student = None
        for s in self.students:
            if s.studentID == studentID:
                student = s
                break

        if student is None:
            print("Student not found.")
            return

        book = None
        for b in self.books:
            if b.bookID == bookID:
                book = b
                break

        if book is None:
            print("Book not found.")
            return

        student.borrowBook(book)

    def returnBook(self,studentID,bookID):
        if not self.students:
            print("Student data empty")
            return

        if not self.books:
            print("Book data empty")
            return

        student = None
        for s in self.students:
            if s.studentID == studentID:
                student = s
                break

        if student is None:
            print("Student not found.")
            return

        book = None
        for b in self.books:
            if b.bookID == bookID:
                book = b
                break

        if book is None:
            print("Book not found.")
            return

        student.returnBookS(book)