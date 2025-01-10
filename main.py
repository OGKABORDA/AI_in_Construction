class Table:
    """
    Класс описывает стол.
    """

    def __init__(self, material: str, height: int, width: int):
        """
        Создает объект стола.

        :param material: Материал, из которого сделан стол (например, "дерево").
        :param height: Высота стола в сантиметрах (должна быть > 0).
        :param width: Ширина стола в сантиметрах (должна быть > 0).

        :raises ValueError: Если высота или ширина некорректные.
        """
        if height <= 0 or width <= 0:
            raise ValueError("Высота и ширина стола должны быть положительными числами.")
        self.material = material
        self.height = height
        self.width = width

    def fold(self) -> None:
        """
        Складывает стол.

        :return: None

        >>> table = Table("металл", 75, 120)
        >>> table.fold()  # Заглушка для метода
        """
        ...

    def paint(self, color: str) -> None:
        """
        Красит стол в указанный цвет.

        :param color: Новый цвет стола.
        :return: None

        >>> table = Table("дерево", 75, 120)
        >>> table.paint("белый")  # Заглушка для метода
        """
        ...


class Tree:
    """
    Класс описывает дерево.
    """

    def __init__(self, species: str, age: int, height: int):
        """
        Создает объект дерева.

        :param species: Вид дерева (например, "дуб").
        :param age: Возраст дерева в годах (должен быть >= 0).
        :param height: Высота дерева в метрах (должна быть > 0).

        :raises ValueError: Если возраст или высота некорректные.
        """
        if age < 0 or height <= 0:
            raise ValueError("Возраст должен быть неотрицательным, а высота положительной.")
        self.species = species
        self.age = age
        self.height = height

    def grow(self, years: int) -> None:
        """
        Увеличивает возраст и высоту дерева.

        :param years: Количество лет роста (должно быть > 0).
        :return: None

        >>> tree = Tree("дуб", 10, 5)
        >>> tree.grow(3)  # Заглушка для метода
        """
        ...

    def shed_leaves(self) -> None:
        """
       Падение листвы.

        :return: None

        >>> tree = Tree("береза", 5, 3)
        >>> tree.shed_leaves()  # Заглушка для метода
        """
        ...


class Stack:
    """
    Класс описывает стек (абстрактную структуру данных).
    """

    def __init__(self):
        """
        Создает пустой стек.
        """
        self.stack: list[int] = []

    def push(self, value: int) -> None:
        """
        Добавляет элемент в стек.

        :param value: Значение, которое нужно добавить.
        :return: None

        >>> s = Stack()
        >>> s.push(10)  # Заглушка для метода
        """
        ...

    def pop(self) -> int:
        """
        Удаляет верхний элемент стека и возвращает его.

        :return: Верхний элемент стека.

        :raises IndexError: Если стек пуст.

        >>> s = Stack()
        >>> s.pop()  # Заглушка для метода
        """
        ...

    def peek(self) -> int:
        """
        Возвращает верхний элемент стека, не удаляя его.

        :return: Верхний элемент стека.

        :raises IndexError: Если стек пуст.

        >>> s = Stack()
        >>> s.peek()  # Заглушка для метода
        """
        ...


if __name__ == "__main__":
    import doctest

    doctest.testmod()