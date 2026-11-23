class Book:
    def __init__(self,bookID,title,author,pageCount):
        self.bookID = bookID
        self.title = title
        self.author = author
        self.pageCount = pageCount
        self.isAvaible = True

    def showBook(self):
        print(f"""
        Tittle: {self.title}
        Author: {self.author}
        Page Count: {self.pageCount}
        """)

        if self.isAvaible:
            print("Status: Avaible.")
        else:
            print("Status: Borrowed.")

    def borrow(self):
        if self.isAvaible:
            self.isAvaible = False
            print(f"{self.title} Borrowed.")
        else:
            print("Print This Book Already Borrowed.")

    def returnBook(self):
        if not self.isAvaible:
            self.isAvaible = True
            print(f"{self.title} Returned.")
        else:
            print("This book already Returned.")

book1 = Book(1, "Laylay", "Duben", 30)
book2 = Book(2, "Clean Code", "Marc", 222)
book3 = Book(3, "Dream", "Jason", 80)

for x in book1,book2,book3:
    x.showBook()