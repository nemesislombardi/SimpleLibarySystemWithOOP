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
        if not self.books:
            print("Book data empty")
            return

        for x in self.books:
            if x['id'] == bookID:
                print(f"ID: {x[self.bookID]}")
                print(f"Tittle: {x[self.title]}")
                print(f"Author: {x[self.author]}")
                print(f"Page Count: {x[self.pageCount]}")
                print("-" *30)
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
                print(f"Borrowed Books:: {x[len(self.borrowedBooks)]}")
                print("-" *30)
                return
            
        print("Student not found.")

    def borrowBook(self,studentID,bookID):
        pass

    def returnBook(self,studentID,bookID):
        pass