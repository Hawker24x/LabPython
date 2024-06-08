class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"

class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        return f"{self.name}: {self.sound}"

class Dog(Animal):
    def __init__(self, name, sound, breed):
        super().__init__(name, sound)
        self.breed = breed

class Bird:
    def fly(self):
        return None

class Sparrow(Bird):
    def fly(self):
        return "Sparrow flies high"

class Penguin(Bird):
    def fly(self):
        return "Penguin cannot fly"

class Encapsulation:
    def __init__(self, public, _private, __protected):
        self.public = public
        self._private = _private
        self.__protected = __protected

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)


class AverageCalculator:
    pass


class AverageCalculator:
    def __init__(self, numbers):
        self.numbers = numbers

    def calculate_average(self):
        return sum(self.numbers) / len(self.numbers)

    # Создаем экземпляр класса Student и выводим его свойства
    student1 = Student(name="Alice", age=20, grade="A")
    print(f"Student 1 - Name: {student1.name}, Age: {student1.age}, Grade: {student1.grade}")

    # Создаем экземпляр класса Student с методом display_info и выводим информацию
    student2 = Student(name="Bob", age=21, grade="B")
    print(student2.display_info())

    # Создаем экземпляр класса Animal и вызываем метод make_sound
    animal1 = Animal(name="Lion", sound="Roar")
    print(animal1.make_sound())

    # Создаем экземпляр класса Dog и выводим его свойства и метод make_sound
    dog1 = Dog(name="Buddy", sound="Bark", breed="Golden Retriever")
    print(f"Dog - Name: {dog1.name}, Sound: {dog1.sound}, Breed: {dog1.breed}")
    print(dog1.make_sound())

    # Создаем экземпляры класса Sparrow и Penguin и вызываем их методы fly
    sparrow1 = Sparrow()
    penguin1 = Penguin()
    print(sparrow1.fly())
    print(penguin1.fly())

    # Создаем экземпляр класса Encapsulation и выводим его свойства (публичное и защищенное)
    encapsulation1 = Encapsulation(public="public_value", _private="private_value", __protected="protected_value")
    print(f"Public: {encapsulation1.public}, Private: {encapsulation1._private}")

    # Создаем экземпляр класса Rectangle и выводим результат метода calculate_perimeter
    rectangle1 = Rectangle(width=5, height=10)
    print(f"Perimeter of Rectangle: {rectangle1.calculate_perimeter()}")

    # Создаем экземпляр класса AverageCalculator и выводим результат метода calculate_average
    average_calculator1 = AverageCalculator(numbers=[1, 2, 3, 4, 5])
    print(f"Average: {average_calculator1.calculate_average()}")
