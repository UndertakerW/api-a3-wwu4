class BookClass:
    isbn = ''
    title = ''
    author = ''
    genre = 0
    year = 0

b1 = BookClass()
b1.isbn = '978–0–07–340320–5'
b1.title = 'Leadership Communication'
b1.author = 'Deborah J. Barrett'
b1.genre = 1
b1.year = 2014

b2 = BookClass()
b2.isbn = '978-0-470-01270-3'
b2.title = 'Requirements Engineering'
b2.author = 'Axel van Lamsweerde'
b2.genre = 2
b2.year = 2009

b3 = BookClass()
b3.isbn = '978-1783299607'
b3.title = 'Warcraft: Durotan'
b3.author = 'Christie Golden, Chris Metzen'
b3.genre = 3
b3.year = 2016

b4 = BookClass()
b4.isbn = '978-1594631931'
b4.title = 'The Kite Runner'
b4.author = 'Khaled Hosseini'
b4.genre = 4
b4.year = 2013

books = {
    b1.isbn: b1,
    b2.isbn: b2,
    b3.isbn: b3,
    b4.isbn: b4
}