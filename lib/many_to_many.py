class Author:
    all = []
    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("Author name must be a string")
        self.name = name
        Author.all.append(self)
    pass

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
    pass

    def books(self):
        return list(set([contract.book for contract in self.contracts()]))
    pass

    def sign_contract(self, book, date, royalties):
        contract = Contract(self, book, date, royalties)
        return contract
    pass
    
    def total_royalties(self):
        return sum([contract.royalties for contract in self.contracts()])
    pass

class Book:
    all = []
    def __init__(self, title):
        if not isinstance(title, str):
            raise Exception("Book title must be a string")
        self.title = title
        Book.all.append(self)
    pass

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]
    pass

    def authors(self):
        return list(set([contract.author for contract in self.contracts()]))
    pass


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("Author must be an instance of Author")
        if not isinstance(book, Book):
            raise Exception("Book must be an instance of Book")
        if not isinstance(date, str):
            raise Exception("Date must be a string")
        if not isinstance(royalties, int):
            raise Exception("Royalties must be an int")
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)
    pass

    @staticmethod
    def contracts_by_date(date):
        return [contract for contract in Contract.all if contract.date == date]
    
    