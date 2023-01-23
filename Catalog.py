from Book import Book
#firts Book is file name & Second Book is class name
class Catalog:
    def __init__(self):
        self.defferent_book_count = 0
        self.total_book_count = 0
        self.books = []

#only availabe to admin
    def addBook(self,name,author,publish_date,pages):
        b = Book(name,author,publish_date,pages)
        self.defferent_book_count += 1
        self.books.append(b)
        return b

    def addBookItem(self,book,isbn,rack):
        book.addBookItem(isbn, rack)

#availabe to user
    def searchByname(self,name):
        for bookname in self.books:
            if bookname.name == name:
                print("book is present by name")
            else:
                print("book not present by name")

    def searchByAuthor(self,author):
        for by_author in self.books:
            if by_author.author == author:
                return "book is present by author"
            else:
                return "book not present by author"

    def displayAllBooks(self):
        print('Different book count',self.defferent_book_count)
        c = 0
        for book in self.books:
            c += book.total_count
            book.printBook()
        
        print("Total Book Count",c)