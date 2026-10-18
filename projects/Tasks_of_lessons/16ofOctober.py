# Книги
# class Book:
#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year
#
#     def info(self):
#         return f"книга - {self.title}, автор - {self.author}, год - {self.year}"
# class Ebook(Book):
#     def __init__(self, title, author, year, format):
#         # self.title = title
#         # self.author = author
#         # self.year = year
#         # self.format = format
#         super().__init__(title, author, year)
#         self.format = format
#     def info(self):
#         return f"книга - {self.title}, автор - {self.author}, год - {self.year}, формат - {self.format}"
# book_cats = Book("Путешествия котов", " Лорд_кот", 2000)
# ebook_dogs = Ebook("путешествие собак", "барон догвиль", 2003, "электронная")
# print(ebook_dogs.info())
# print(book_cats.info())
#------------------
#Менеджеры
# class Employee:
#     def __init__(self, id, name, base_money):
#         self.id = id
#         self.name = name
#         self.base_money = base_money
#
#     def calculate_salaries(self):
#         return self.base_money
#
#
# class Manager(Employee):
#     def __init__(self, id, name, base_money, bonus):
#         super().__init__(id, name, base_money)
#         self.bonus = bonus
#
#     def calculate_salaries(self):
#         return self.base_money + self.bonus
#
#
# class Developer(Employee):
#     def __init__(self, id, name, base_money, project_sum):
#         super().__init__(id, name, base_money)
#         self.project_sum = project_sum
#
#     def calculate_salaries(self):
#         return self.base_money + self.project_sum * 10_000
#
#
# emp_alex = Employee(0, 'Alex', 50_000)
# manager_ivan = Manager(1, 'Ivan', 50_000, 10_000)
# dev_eva = Developer(2, 'Eva', 50_000, 5)
#
# print(emp_alex.calculate_salaries())
# print(manager_ivan.calculate_salaries())
# print(dev_eva.calculate_salaries())
#---------------------
#Машины
# class Transport:
#     def __init__(self, name):
#         self.name = name
#
#     def description(self):
#         return f'Транспорт - {self.name}'
#
#
# class Car(Transport):
#     def __init__(self, name, power):
#         super().__init__(name)
#         self.power = power
#
#     def description(self):
#         return f'Транспорт - {self.name} Мощность - {self.power}'
#
#
# class Plane(Transport):
#     def __init__(self, name, size):
#         super().__init__(name)
#         self.size = size
#
#     def description(self):
#         return f'Транспорт - {self.name}, Размах крыльев - {self.size}'
#
#
# class Bike(Transport):
#     def __init__(self, name, tank):
#             super().__init__(name)
#             self.tank = tank
#
#
#
#     def description(self):
#         return f'Транспорт - {self.name}, объем бака - {self.tank}'
#
# #Данные выдуманы и не соответствуют реальности, гуглить времени не было
# bike = Bike("Honda", '3 куб.м.')
# car = Car('Maclaren', '800 лс')
# plane = Plane('СУ - 134', '20 м')
#
# print(bike.description())
# print(car.description())
# print(plane.description())