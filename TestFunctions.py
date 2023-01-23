from Book import Book
from Catalog import Catalog
from User import Member, Librarian

#b1 = Book('Shoe Dog','Phil Knight','2015', 300)
#b2 = Book('Shivaji', 'fule', '2001', 405)

#b1.addBookItem('123hg', 'H1B2')
#b1.addBookItem('124hg', 'H1B3')
catalog = Catalog()
b = catalog.addBook('Shoe Dog','Phil Knight','2015', 300)
catalog.addBookItem(b,'123hg', 'H1B2')
catalog.addBookItem(b,'124hg', 'H1B3')
catalog.addBookItem(b,'125hg', 'H1B4')

b = catalog.addBook('sham chi aai','sane guruji','2017', 500)
catalog.addBookItem(b,'400hg', 'K1B1')

b = catalog.addBook('The arabian night','Bloomsbury','1994',205)
catalog.addBookItem(b, '401hg', 'K1B2')
catalog.addBookItem(b, '402hg', 'K1B3')
catalog.addBookItem(b, '403hg', 'K1B4')
catalog.addBookItem(b, '404hg', 'K1B5')

catalog.searchByname('sham chi aai')
print(catalog.searchByAuthor('sane guruji'))
#catalog.displayAllBooks()

m = Member("Harsh","Nagpur",21,'123456',"std123")
L = Librarian("Anupam", "Pune", 32, '133456', 'emp22')

print(m)
print(L)
