if __name__ == "__main__":
    # Write your solution here
    from typing import List


    class Employee:
        """
        Базовый класс, представляющий сотрудника.
        """

        def __init__(self, name: str, age: int, salary: float) -> None:
            """
            Конструктор для инициализации сотрудника.
            где name: Имя сотрудника
            age: Возраст сотрудника
            salary: Зарплата сотрудника
            """
            self._name = name  # Инкапсуляция имени, так как оно не должно изменяться напрямую
            self.age = age
            self.salary = salary

        def __str__(self) -> str:
            """
             Возвращает строковое представление объекта для пользователя, со всеми данными.
            """
            return f"Employee: {self._name}, Age: {self.age}, Salary: {self.salary}"

        def __repr__(self) -> str:
            """
            Возвращает строковое представление объекта для разработчика.
            """
            return f"Employee(name={self._name}, age={self.age}, salary={self.salary})"

        def work(self) -> str:
            """
            Метод-имитация работы сотрудника.
            """
            return f"{self._name} is working..."


    class Manager(Employee):
        """
        Класс, представляющий менеджера, наследованный от Employee.
        """

        def __init__(self, name: str, age: int, salary: float, employees: List[Employee]) -> None:
            """
            Конструктор расширяет базовый класс добавлением списка подчиненных
            employees: Список сотрудников, которыми управляет менеджер.
            """
            super().__init__(name, age, salary)
            self.employees = employees

        def manage(self) -> str:
            """
            Метод, который демонстрирует управление командой.
            """
            return f"{self._name} is managing {len(self.employees)} employees."

        def __str__(self) -> str:
            """
            Перегрузка метода __str__, чтобы добавить информацию о количестве подчиненных.
            """
            return f"Manager: {self._name}, Age: {self.age}, Salary: {self.salary}, Employees: {len(self.employees)}"


    class Developer(Employee):
        """
        Класс, представляющий разработчика.
        """

        def __init__(self, name: str, age: int, salary: float, programming_language: str) -> None:
            """
            Конструктор расширяет базовый класс добавлением информации о языке программирования.

            :param programming_language: Основной язык программирования разработчика.
            """
            super().__init__(name, age, salary)
            self.programming_language = programming_language

        def code(self) -> str:
            """
            Метод, имитирующий процесс написания кода разработчиком.
            """
            return f"{self._name} is coding in {self.programming_language}."

        def work(self) -> str:
            """
            Перегруженный метод work.
            В отличие от обычного сотрудника, разработчик не просто работает, а пишет код.
            """
            return self.code()

        def __str__(self) -> str:
            """
            Перегрузка метода __str__, чтобы добавить информацию о языке программирования.
            """
            return f"Developer: {self._name}, Age: {self.age}, Salary: {self.salary}, Language: {self.programming_language}"


    pass
