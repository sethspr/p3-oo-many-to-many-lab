class Author: #Class attribute to store all Author instances
    all = [] #Class attribute to store all Author instances
    def __init__(self, name): #Constructor
        self.name = name #instance attribute to store author's name
        Author.all.append(self) #Add the Author instance ot he list of all authors

    def __repr__(self):
        return f"<Author Name: {self.name})>"


    def contracts(self):
        results = [] #List of all contract instances
        for contract in Contract.all: #Get all contract
            if contract.author is self: #Find contracst associated with this author
                results.append(contract) # Add the contract to the list of results
        return results # Return a list of all contracts associated with this author
    
    def books(self):
        results = [] #List of all book instances
        for contract in self.contracts(): #Get all book
            results.append(contract.book) # Add the book to the list of results
        return results # Return a list of all books associated with this author
    
    def sign_contract(self, book, date, royalties): 
        return Contract(self, book, date, royalties) # Create a new contract for this author instance
    
    def total_royalties(self):
        results = [] #List of all royalties for all contracts
        for contract in self.contracts(): #Get all royalties
            results.append(contract.royalties) # Add the royalties to the list of results
        return sum(results) # Return the sum of all royalties for all contracts

class Book: #Class attribute to store all Book instances
    all = [] #Class attribute to store all Book instances
    def __init__(self, title): #Constructor
        self.title = title # instance attribute to store book's title
        Book.all.append(self) # Add the Book instance ot he list of all books
    
    def contracts(self): #Get all contracts
        results = [] # List of all contract instances
        for contract in Contract.all: # Get all contract associated with this book instance 
            if contract.book is self: # Find contracst associated with this book
                results.append(contract) # Add the contract to the list of results
        return results # Return a list of all contracts associated with this book
    
    def authors(self): #Get all authors
        results = [] # List of all author instances
        for contract in self.contracts(): # Get all author associated with this book instance 
            results.append(contract.author) # Add the author instance to the list of results
        return results # Return a list of all authors associated with this book
    def __repr__(self):
        return f"<Book Title: {self.title})>"


class Contract: #Class attribute to store all Contract instances
    all = [] # Class attribute to store all Contract instances
    def __init__(self, author, book, date=0, royalties=0): #Constructor
        self.author = author # instance attribute to store contract's author
        self.book = book # instance attribute to store contract's book
        self.date = date # instance attribute to store contract's date
        self.royalties = royalties # instance attribute to store contract's royalties
        Contract.all.append(self) # Add the Contract instance to the list of all contracts

    @property #getter method to return the author of the contract
    def author(self): #Get the author of the contract
        return self._author # update the author of the contract with the new author instance
    
    @author.setter #setter method to update the author of the contract
    def author(self, new_author): #Update the author of the contract with the new author instance
        if not isinstance(new_author, Author): # Check if the new author is an instance of Author or not
            raise Exception("Author must be an instance of Author") # Raise an exception if not
        self._author = new_author # Update the author of the contract with the new author instance

    @property #getter method to return the book of the contract
    def book(self): #Get the book of the contract
        return self._book # update the book of the contract with the new book instance
    
    @book.setter #setter method to update the book of the contract with the new book instance
    def book(self, new_book): # Update the book of the contract with the new book instance
        if not isinstance(new_book, Book): # Check if the new book is an instance of Book or not 
            raise Exception("Book must be an instance of Book") # Raise an exception if not
        self._book = new_book # Update the book of the contract with the new book instance

    @property #getter method to return the date of the contract
    def date(self): #Get the date of the contract
        return self._date # update the date of the contract with the new date instance
    
    @date.setter #setter method to update the date of the contract with the new date instance
    def date(self, new_date): # Update the date of the contract with the new date instance
        if not isinstance(new_date, str): # Check if the new date is an instance of string or not
            raise Exception("Date must be an integer") # Raise an exception if not 
        self._date = new_date # Update the date of the contract with the new date instance

    @property #getter method to return the royalties of the contract
    def royalties(self): #Get the royalties of the contract
        return self._royalties # update the royalties of the contract with the new royalties instance
    
    @royalties.setter #setter method to update the royalties of the contract with the new royalties instance
    def royalties(self, new_royalties): # Update the royalties of the contract with the new royalties instance
        if not isinstance(new_royalties, int): # Check if the new royalties is an instance of integer or not
            raise Exception("Royalties must be an integer") # Raise an exception if not 
        self._royalties = new_royalties # Update the royalties of the contract with the new royalties instance

    @classmethod #Class method to create a new contract
    def contracts_by_date(cls, date): # Class method to create a new contract
        results = [] # List of all contract instances
        for contract in cls.all: # Get all contract instances from the list of all contracts
            if contract.date == date: # Find contracst associated with this date 
                results.append(contract) # Create a new contract instance with the date associated 
        return results # Return a list of all contracts associated with this date
    def __repr__(self):
        return f"<Contract Author: {self.author.name}, Book: {self.book.title}, Date: {self.date}, Royalties: {self.royalties})>"
    
    

# auth_1 = Author("Seth")
# auth_2 = Author("Sammy")
# book_1 = Book("Pythons are Snakes")
# book_2 = Book("Just Say No to JSON")
# contract_1 = Contract(auth_1, book_1)

# print(contract_1)