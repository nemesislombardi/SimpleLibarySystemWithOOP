from book import *


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
            

    def searchBook(self,bookID):
        pass

    def searchStudent(self,studentID):
        pass

    def borrowBook(self,studentID,bookID):
        pass

    def returnBook(self,studentID,bookID):
        pass