BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]

class Book:
    def __init__(self, id_: int,name: str, pages: int): #передаем ссылку на экземпляр (self) и атрибуты.
        self.id = id_  #инициализируем id книги
        self.name = name # инициализируем имя книги
        self.pages = pages #инициализриуем страницы в книге
    def __str__(self) -> str:
        #self.name = name
        return f'Книга "{self.name}"' # возращаем  в формате строки

    def __repr__(self) -> str:
        return f"Book(id_={self.id!r}, name={self.name!r}, pages={self.pages!r})" # ИЛИ name='{self.name}'
# TODO написать класс Book


if __name__ == '__main__':
    # Инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]

    for book in list_books:
        print(book)  # Проверяем метод __str__

    print(list_books)  # Проверяем метод __repr__
