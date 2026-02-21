#!/usr/bin/env python3

class Author:
    # Class attribute to store all Author instances
    all = []

    def __init__(self, name):
        # Initialize author with a name
        self.name = name

        # Store instance
        Author.all.append(self)

    # Return all contracts related to this author
    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    # Return all books related to this author through contracts
    def books(self):
        return [contract.book for contract in self.contracts()]

    # Create and return a new Contract object
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)

    # Return total royalties from all related contracts
    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())


class Book:
    # Class attribute to store all Book instances
    all = []

    def __init__(self, title):
        # Initialize book with title
        self.title = title

        # Store instance
        Book.all.append(self)

    # Return all contracts related to this book
    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]

    # Return all authors related to this book through contracts
    def authors(self):
        return [contract.author for contract in self.contracts()]


class Contract:
    # Class attribute to store all contracts
    all = []

    def __init__(self, author, book, date, royalties):
        # Validate author
        if not isinstance(author, Author):
            raise Exception("author must be an instance of Author")

        # Validate book
        if not isinstance(book, Book):
            raise Exception("book must be an instance of Book")

        # Validate date
        if not isinstance(date, str):
            raise Exception("date must be a string")

        # Validate royalties
        if not isinstance(royalties, int):
            raise Exception("royalties must be an integer")

        #This assigns attributes
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        #This is to store instance
        Contract.all.append(self)

    # Class method to filter contracts by date
    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]