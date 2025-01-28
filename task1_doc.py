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

    """
        Класс Book представляет информацию о книге.
        Класс имеет следующие атрибуты:
         id : int - идентификатор книги.
         name : str - название книги.
        pages : int - количество страниц в книге.
        В классе содержатся методы:
        __str__() - возвращает строковое представление книги в формате: 'Книга "название книги"'.
        __repr__() - возвращает репрезентативное строковое представление книги,
        по которому можно инициализировать точно такой же экземпляр.
    """

    def __init__(self, id_: int,name: str, pages: int):

        """
              Инициализирует объект Book.
              Параметры:
              id_ : int - идентификатор книги.
              name : str - название книги.
              pages : int - количество страниц в книге.
        """

        self.id = id_
        self.name = name
        self.pages = pages
    def __str__(self) -> str:

        """
            Возвращает строковое представление книги.
            Возвращает:
            str - строка в формате: 'Книга "название книги"'.
        """

        #self.name = name
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:

        """
               Возвращает репрезентативное строковое представление книги.
               Возвращает:
               str - строка в формате: "Book(id_=идентификатор, name='название', pages=количество_страниц)".
        """
        
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
