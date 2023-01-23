class BookItem:
    def __init__(self,book,isbn,rack):
        self.book = book
        self.isbn = isbn
        self.rack = rack

class Book:
    def __init__(self, name,author,publish_date,pages,):
        self.name = name
        self.author = author
        self.publish_date = publish_date
        self.pages = pages
        self.total_count = 0 
        self.book_item = []

    def addBookItem(self,isbn,rack):
        b = BookItem(self, isbn, rack)
        self.book_item.append(b)
        self.total_count +=1

    def printBook(self):
        print(self.name,self.author)
        for book_item in self.book_item:
            print(book_item.isbn)
            print(book_item.rack)

b1 = Book('Shoe Dog','Phil Knight','2015', 300)
b2 = Book('Shivaji', 'fule', '2001', 405)
b3 = Book('sham chi aai','sane guruji','2013',500)

b1.addBookItem('123hg', 'H1B2')
b1.addBookItem('124hg', 'H1B3')
b2.addBookItem('125hg', 'H1B4')
b3.addBookItem('126hg', 'H1B5')

print(b1.__dict__['book_item'][0].isbn)
b1.printBook()
b2.printBook()
b3.printBook()