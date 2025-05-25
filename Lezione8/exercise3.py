
class Book:

    def __init__(self, title: str, author: str, isbn: str):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self) -> str:
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}"

    @classmethod
    def from_string(cls, book_str:str) -> str:
        book_str = book_str.split(",")
        
        title = book_str[0].strip()
        author = book_str[1].strip()
        isbn = book_str[2].strip()

        return cls(title, author, isbn)
    



if __name__ == "__main__":
    book_str: str = "La Divina Commedia, D. Alighieri, 999000666"
    divina_commedia = Book.from_string(book_str)

    print(divina_commedia.author)