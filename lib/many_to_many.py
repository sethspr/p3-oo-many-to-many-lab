class Author:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<Author Name: {self.name})>"


    def contracts(self):
        results = []
        for contract in Contract.all:
            if contract.author is self:
                results.append(contract)
        return results

class Book:
    def __init__(self, title):
        self.title = title
    
    def __repr__(self):
        return f"<Book Title: {self.title})>"


class Contract:
    all = []
    def __init__(self, author, book, date=0, royalties=0):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

    def __repr__(self):
        return f"<Contract Author: {self.author.name}, Book: {self.book.title}, Date: {self.date}, Royalties: {self.royalties})>"
    
    

auth_1 = Author("Seth")
auth_2 = Author("Sammy")
book_1 = Book("Pythons are Snakes")
book_2 = Book("Just Say No to JSON")
contract_1 = Contract(auth_1, book_1)

print(contract_1)