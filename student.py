class Student:
    def __init__(self, studentID, Name):
        self.studentID = studentID
        self.Name = Name
        self.borrowedBooks = []

    def showStudent(self):
        print(f"""
        ID: {self.studentID}
        Name: {self.Name}
        Borrowed Books: {len(self.borrowedBooks)}
        """)

    def borrowBook1(self, book):
        if book.isAvailable:
            book.borrow()
            self.borrowedBooks.append(book)
        else:
            print("Book is not available.")

    def returnBookS(self, book):
        if book in self.borrowedBooks:
            book.returnBook()
            self.borrowedBooks.remove(book)
        else:
            print("This student has not borrowed this book.")