class Book:
    all_books = []

    def __init__(self, title):
        self.title = title
        Book.all_books.append(self)

class Author:
    all_authors = []

    def __init__(self, name):
        self.name = name
        self.contracts_list = []
        Author.all_authors.append(self)

    def contracts(self):
        return self.contracts_list

    def books(self):
        return [contract.book for contract in self.contracts_list]

    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book):
            raise Exception("Invalid book object")
        if not isinstance(date, str):
            raise Exception("Invalid date format")
        if not isinstance(royalties, int):
            raise Exception("Royalties must be an integer")
        contract = Contract(self, book, date, royalties)
        self.contracts_list.append(contract)
        return contract

    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts_list)

class Contract:
    all_contracts = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all_contracts.append(self)

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        if not isinstance(author, Author):
            raise Exception("Author must be an instance of the Author class")
        self._author = author

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all_contracts if contract.date == date]

