class Student:
    def __init__(self, studentID, Name):
        self.studentID = studentID
        self.Name = Name
        self.borrowedBooks = []

    def showInfo(self):
        print(f"""
        
        ID: {self.studentID}
        Name: {self.studentID}
        Borrowed Books: {len(self.borrowedBooks)}

        """)

    def borrowBook(self,book):
        if book.isAvaliable:
            book.borrow()
            self.borrowedBooks.append(book)
            print("Book Borrowed.")
        else:
            print("Book is not avaible.")

    def returnBook(self,book):
        if book in self.borrowedBooks:
            book.returnBook()
            self.borrowedBooks.remove(book)
            print("Book returned.")
        else:
            print("Book is not avaible")

s1 = Student(1, "Mustafa")
s2 = Student(2, "Resul")
s3 = Student(3, "Ayxan")