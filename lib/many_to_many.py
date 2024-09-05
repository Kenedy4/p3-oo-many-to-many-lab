

# lib/book.py

# lib/book.py

class Book:
    all = []  # Class variable to store all Book instances

    def __init__(self, title):
        self.title = title
        Book.all.append(self)  # Add this book to the list of all books

    def contracts(self):
        """Return a list of all contracts related to this book"""
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        """Return a list of all authors related to this book using contracts"""
        return [contract.author for contract in self.contracts()]




class Author:
    all = []  # Class variable to store all Author instances

    def __init__(self, name):
        self.name = name
        Author.all.append(self)  # Add this author to the list of all authors

    def contracts(self):
        """Return a list of all contracts related to this author"""
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        """Return a list of books related to this author using contracts"""
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        """Create and return a new contract between the author and book"""
        if not isinstance(book, Book):
            raise Exception("Invalid book instance")
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        """Return the total royalties earned by the author from all contracts"""
        return sum(contract.royalties for contract in self.contracts())


class Contract:
    all = []  # Class variable to store all Contract instances

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("Invalid author instance")
        if not isinstance(book, Book):
            raise Exception("Invalid book instance")
        if not isinstance(royalties, int):
            raise Exception("Royalties must be an integer")
        if not isinstance(date, str):
            raise Exception("Date must be a string")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        Contract.all.append(self)  # Add this contract to the list of all contracts

    @classmethod
    def contracts_by_date(cls, date):
        """Return all contracts that have the same date as the given date"""
        return [contract for contract in cls.all if contract.date == date]

