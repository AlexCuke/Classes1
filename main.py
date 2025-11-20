
'''#Класс Книга
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def get_info(self):
        return f"{self.title} {self.author} {self.year}"
book = Book("1984", "Джордж Оруэлл",1949)
print(book.get_info()) 
'''

'''#Класс Студент
class Student: #класс студент
    def __init__(self, name,age,grades):
        self.name = name
        self.age = age
        self.grades = grades
    def add_grade(self,grade): #добавление оценки
        if grade<=5 and grade>0:
            self.grades.append(grade)
    def get_average(self):      #средняя оценка
        if len(self.grades)>0:
            return sum(self.grades)/len(self.grades)
        else:
            return 0
    def get_info(self): #информация о студенте
        return f"{self.name} {self.age} {self.grades}"
student = Student("Иван", 20, [4, 5, 3])
student.add_grade(5)
print(student.get_average()) 
'''

'''#Класс Банковский счет
class BankAccount: #класс Банковский счет
    def __init__(self, account_number,balance):
        self.account_number = account_number
        self.balance = balance
    def deposit(self,amount): #добавление денег
        self.balance=self.balance + amount
    def withdraw(self, amount): #снятие денег
        if self.balance >= amount:
            self.balance=self.balance - amount 
    def get_balance(self): #информация о балансе
        return self.balance
account = BankAccount("123456789", 1000)
account.deposit(500)
account.withdraw(200)
print(account.get_balance()) '''

'''#Класс Фигура
class Shape: #класс Фигура
    def __init__(self):
        pass
    def area(self): #площадь
        return 0    # по умолчанию 0
class Rectangle(Shape) : #класс Прямогульник
    def __init__(self,leight,height):
        self.leight=leight
        self.height=height
    def area(self): #площадь
        return self.leight*self.height  # длина*высота
class Circle(Shape) : #класс Прямогульник
    def __init__(self,radius):
        self.radius=radius
    def area(self): #площадь
        return self.radius**2*3.14  # площадь
    
rect = Rectangle(5, 3)
print(rect.area())  # Выведет: 15
circle = Circle(4)
print(circle.area())'''

'''#Класс Автомобиль
class Car: #класс Автомобиль
    def __init__(self,brand,model,year,speed):
        self.brand=brand
        self.model=model
        self.year=year
        self.speed=speed
    def accelerate(self): #ускорение
        self.speed+=10
    def brake(self): #торможение
        self.speed=max(0,self.speed-10)
    def get_info(self): #инфо
        print(f"{self.brand} {self.model} {self.year} {self.speed}")
car = Car("Toyota", "Camry", 2020, 50)
car.accelerate()
car.brake()
car.get_info()  '''

'''#Переопределения методов (животные)
class Animal:
    def __init__(self):
        pass
    def make_sound(self):
        print("Some sound")
class Dog(Animal):
    def __init__(self):
        pass
    def make_sound(self):
        print("Woof!")
class Cat (Animal):
    def __init__(self):
        pass
    def make_sound(self):
        print("Meow!")
class Bird  (Animal):
    def __init__(self):
        pass
    def make_sound(self):
        print("Tweet!")
        
animals = [Dog(), Cat(), Bird()]
for animal in animals:
    animal.make_sound()   '''  

'''#Переопределения методов (Фигуры)
class Shape :
    def __init__(self):
        pass
    def area(self):
        return 0
class Rectangle (Shape ): # прямоугольник
    def __init__(self,height,length ):
        self.height=height
        self.length =length 
    def area(self):
        return self.height*self.length 
class Circle  (Shape): #круг
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius**2
class Triangle  (Shape): #треугольник
    def __init__(self,height,base ):
        self.height=height
        self.base=base 
    def area(self):
        return self.height*self.base /2
shapes = [Rectangle(5, 3), Circle(4), Triangle(6, 4)]
for shape in shapes:
    print(shape.area())'''

'''#Переопределение методов Банковский счет
class BankAccount: #класс Банковский счет
    def __init__(self, account_number,balance):
        self.account_number = account_number
        self.balance = balance
    def deposit(self,amount): #добавление денег
        self.balance=self.balance + amount
    def withdraw(self, amount): #снятие денег
        if self.balance >= amount:
            self.balance=self.balance - amount 
    def get_balance(self): #информация о балансе
        return self.balance
class SavingsAccount (BankAccount):
    def __init__(self, account_number,balance,interest_rate):
        super().__init__(account_number,balance)
        self.interest_rate=interest_rate
    def add_interest(self):
        self.balance=self.balance*(1+self.interest_rate/100)
class CheckingAccount  (BankAccount):
    def __init__(self, account_number, balance, fee_rate):
        super().__init__(account_number, balance)
        self.fee_rate = fee_rate

    def apply_fee(self, amount):
        fee = amount * self.fee_rate / 100
        if self.balance >= amount + fee:
            self.balance = self.balance - amount - fee
        else:
            print("Недостаточно средств для снятия и комиссии")

savings = SavingsAccount("12345", 1000, 5)
savings.add_interest()
print(savings.get_balance())  # Выведет: 1050.0

checking = CheckingAccount("67890", 1000, 2)
checking.apply_fee(100)
print(checking.get_balance())  # Выведет: 898.0'''

'''#Переопределения методов (Транспорт)
class Vehicle:
    def move(self):
        print("Vehicle is moving")
class Car (Vehicle):
    def __init__(self):
        pass
    def move(self):
        print("Car is driving")
class Bicycle   (Vehicle):
    def __init__(self):
        pass
    def move(self):
        print("Bicycle is riding")
        
class Boat  (Vehicle):
    def __init__(self):
        pass
    def move(self):
        print("Boat is sailing")
vehicles = [Car(), Bicycle(), Boat()]
for vehicle in vehicles:
    vehicle.move()'''

'''#1 Класс кот 
class Cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def meow(self):
        print(f"Мяу! Я кот {self.name}. Мне {self.age} года")
cat1 = Cat("Вася",  5)
cat2=Cat("Снежок",  3)
cat1.meow()
cat2.meow()'''

'''#2 Класс Круг 
class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        print(self.radius**2*3.14)  # площадь
circle = Circle(5)
circle.area()'''

'''#3 Класс Счетчик 
class Counter:
    def __init__(self,value):
        self.value=value
        value=0
    def inc(self):
        self.value+=1
    def reset(self):
        self.value=0

counter = Counter(0)
counter.inc()
counter.inc()
print(counter.value)

counter.reset()
print(counter.value)'''

'''#6 Класс Point 
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        return f"Point(x={self.x}, y={self.y})"
point1=Point(1,2)
point2=Point(5,7)

print(point1)
print(point2)'''

'''#7 Класс Rectangle 
class Rectangle:
    def __init__(self, width, height):
        self.width=width
        self.height=height
    def area(self):
        print(self.height*self.width)
    def perimeter(self):
        print((self.height+self.width)*2)
Rectangle1=Rectangle(1,2)
Rectangle2=Rectangle(5,7)

Rectangle1.area()
Rectangle1.perimeter()
Rectangle2.area()
Rectangle2.perimeter()'''

'''#11 Класс Temperature 
class Temperature:
    def __init__(self, celsius):
        self.celsius=celsius
    def to_fahrenheit(self):
        print( self.celsius*9/5+32) 
    def is_freezing(self):
        if self.celsius>0:
            return True
        else:
            return False

temperature=Temperature(25)
temperature.to_fahrenheit()
print(temperature.is_freezing())'''

'''#11 Класс Vector2D 
class Vector2D :
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def add(self,other):
        # возвращаем НОВЫЙ вектор — сумму текущего и другого
        return Vector2D(self.x + other.x, self.y + other.y)
    def length(self):
        return   (self.x**2+self.y**2)**0.5

v1 = Vector2D(5, 7)
v2 = Vector2D(2, 3)

v3 = v1.add(v2)          # новый вектор (7, 10)
print(v3.x, v3.y)        # 7 10
print(v3.length())       # длина вектора'''

'''#13 Наследование: «Работник» и «Менеджер»:
class Employee ():
    def __init__(self, name, salary):
        self.name=name
        self.salary=salary
    def info(self):
        print(f"Имя: {self.name}. зарплата: {self.salary} ")
class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size=team_size
    def info(self):
        print(f"Имя: {self.name}. зарплата: {self.salary} , размер команды: {self.team_size} человек")
employee=Employee("Alex",50)    
manager =Manager ("Ivan",70,5)      
employee.info()
manager.info() 

#14 Класс с общим счётчиком объектов»:
class Employee ():
    def __init__(self, name, salary):
        self.name=name
        self.salary=salary
    def info(self):
        print(f"Имя: {self.name}. зарплата: {self.salary} ")
class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size=team_size
    def info(self):
        print(f"Имя: {self.name}. зарплата: {self.salary} , размер команды: {self.team_size} человек")
employee=Employee("Alex",50)    
manager =Manager ("Ivan",70,5)      
employee.info()
manager.info() '''

'''#1  Склад товаров (композиция + классы)
class Product ():
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
    def as_row(self, index):
        """Вернёт одну строку таблицы с данными товара."""
        return f"{index:2} | {self.name:11} | {self.price:4} | {self.quantity:9}"

class Warehouse:
    def __init__ (self):
        self.products={}
    def add_product(self,product):
        name = product.name
        if name in self.products:
            self.products[name].quantity+=product.quantity

        else:
            self.products[name] = product
    def remove_product(self, name, quantity):
        if name not in self.products:
            raise ValueError("Товара с таким именем нет на складе")
        if self.products[name].quantity < quantity:
            raise ValueError("Недостаточно товара на складе")
        self.products[name].quantity -= quantity      
    def total_value(self):
        total = 0
        for product in self.products.values():
            total += product.price * product.quantity
        return total
    def print_table(self):
        print("№ | Наименование | Цена | Количество")
        print("--+-------------+------+-----------")
        count = 1
        for product in self.products.values():
            print(product.as_row(count))
            count += 1
    def find_product(self,name):
        return self.products.get(name)


warehouse = Warehouse()

p1 = Product("Яблоки", 10, 5)   # 5 штук по 10
p2 = Product("Груши", 15, 3)    # 3 штуки по 15
p3 = Product("Яблоки", 10, 2)   # ещё 2 яблока

warehouse.add_product(p1)
warehouse.add_product(p2)
warehouse.add_product(p3)       # количество яблок станет 7
warehouse.print_table() 
product = warehouse.find_product("Яблоки")
if product is not None:
    print(product.name, product.price, product.quantity)
else:
    print("Такого товара на складе нет")
print(warehouse.total_value())  # 7*10 + 3*15 = 115
warehouse.remove_product("Яблоки", 4)  # останется 3 яблока
print(warehouse.total_value())'''

'''#2  Библиотека книг (композиция + поиск)
class Book ():
    def __init__(self,title,author,year,is_available=True):
        self.title=title
        self.author=author
        self.year=year
        self.is_available=is_available  #можно указвать достцупность книги

class Library:
    def __init__(self):
        self.list_of_books={}
    def add_book(self,book):
        key = (book.title,book.author, book.year)
        if key in self.list_of_books:
            print("Книга с таким названием и годом издания уже есть в библиотеке")
        else:
            self.list_of_books[key] = book
            print(f"Книга {book.title}  добавлена")
    def find_by_author(self, author):
        found = []
        for book in self.list_of_books.values():
            if book.author == author:
                found.append(book)

        if found:
            print(f"Книги автора {author}:")
            for book in found:
                print(f"- {book.title} ({book.year})")
        else:
            print(f"Книг автора {author} в библиотеке нет")  
    def borrow(self, title):
        # ищем книгу по названию
        for book in self.list_of_books.values():
            if book.title == title:
                if book.is_available:
                    book.is_available = False
                    print(f"Книга '{title}' выдана посетителю.")
                else:
                    print(f"Книга '{title}' сейчас уже выдана.")
                return  # выходим из метода после нахождения книги
        # если цикл завершился без return
        print(f"Книги '{title}' в библиотеке нет")

    def return_book(self, title):
        for book in self.list_of_books.values():
            if book.title == title:
                if not book.is_available:
                    book.is_available = True
                    print(f"Книга '{title}' возвращена.")
                else:
                    print(f"Книга '{title}' и так числится как доступная.")
                return
        print(f"Книги '{title}' в библиотеке нет")

lib = Library()

b1 = Book("Война и мир", "Толстой", 1869)          # is_available=True по умолчанию
b2 = Book("Преступление и наказание", "Достоевский", 1866, False)  # явно указываем
b3 = Book("Война и мир", "Толстой", 1869)  # такая же, как b1

lib.add_book(b1)  # добавится
lib.add_book(b2)  # добавится
lib.add_book(b3)  # выведет сообщение, что такая книга уже есть

a1=("Толстой")
lib.find_by_author("Толстой")
lib.find_by_author("Пушкин")
lib.borrow("Война и мир")          # выдаст книгу
lib.borrow("Война и мир")          # скажет, что уже выдана
lib.return_book("Война и мир")     # вернёт
lib.return_book("Война и мир")     # скажет, что и так доступна
lib.borrow("Идиот")                # книги нет в библиотеке'''

'''#3 Фигуры: площадь и периметр (наследование + полиморфизм)
class Shape :
    def __init__(self):
        pass
    def area(self):
        return 0
    def perimeter(self):
        return 0
class Rectangle (Shape ): # прямоугольник
    def __init__(self,height,length ):
        self.height=height
        self.length =length 
    def area(self):
        return self.height*self.length
    def perimeter(self):
        return (self.height+self.length)*2
class Circle  (Shape): #круг
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius**2
    def perimeter(self):
        return 2*3.14*self.radius
class Triangle  (Shape): #треугольник
    def __init__(self,height,base ):
        self.height=height
        self.base=base 
    def area(self):
        return self.height*self.base /2
    def perimeter(self):
        return self.base+2*(((self.base/2))**2+self.height**2)**(1/2)   
class Square(Rectangle):
    def __init__(self,side ):
        self.side=side    
        super().__init__(side, side)

shapes = [Rectangle(5, 3), Circle(4), Triangle(6, 4),Square(6)]
for shape in shapes:
    print(shape.area(),' ',shape.perimeter())'''

'''#Переопределение методов Банковский счет
class Account: #класс Банковский счет
    interest_rate=0.03
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
    def deposit(self,amount): #добавление денег
        self.balance+=amount
    def withdraw(self, amount): #снятие денег
        if self.balance >= amount:
            self.balance-=amount
        else:
            print("Недостаточно средств") 
    def get_balance(self): #информация о балансе
        return self.balance  
    def add_interest(self): #информация о балансе
        self.balance=self.balance*(1+self.interest_rate)   
        return self.balance    
class SavingsAccount(Account): #класс Банковский счет
    interest_rate=0.05
    def add_interest(self): #информация о балансе
        self.balance=self.balance*(1+self.interest_rate)
        return self.balance
class CheckingAccount (Account):
    def __init__(self,owner, balance,commission):
        super().__init__(owner, balance)
        self.commission = commission
    def withdraw(self, amount):
        total = amount + self.commission
        if self.balance >= total:
            self.balance -= total
        else:
            print("Недостаточно средств") 


# Пример использования
acc = Account("Иван", 1000)
sav = SavingsAccount("Мария", 1000)
chk = CheckingAccount("Алексей", 1000, 1)

acc.deposit(500)
acc.withdraw(200)
acc.add_interest()

sav.deposit(300)
sav.withdraw(100)
sav.add_interest()

chk.deposit(400)
chk.withdraw(200)

print("Обычный счёт:", acc.get_balance())
print("Накопительный счёт:", sav.get_balance())
print("Расчетный счёт:", chk.get_balance())'''

'''#Задача 5. Меню ресторана и заказ (композиция + магические методы)
class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price
class Order:
    def __init__(self):
        self.items = {}  # словарь: название блюда -> количество
        self.menu = {}   # словарь: название блюда -> объект MenuItem
    def add_item(self, item, quantity):
        if item.name in self.items:
            self.items[item.name] += quantity
        else:
            self.items[item.name] = quantity
        self.menu[item.name] = item  # сохраняем объект MenuItem
    def total(self):
        total_price = 0
        for item_name, quantity in self.items.items():
            price = self.menu[item_name].price
            total_price += quantity * price
        return total_price
    def __str__(self):
        lines = []
        for item_name, quantity in self.items.items():
            price = self.menu[item_name].price
            lines.append(f"{item_name} — {quantity} — {quantity * price}")
        lines.append(f"Итого: {self.total()}")
        return "\n".join(lines)
    def __len__(self):
        return len(self.items)

# Пример использования
pizza = MenuItem("Пицца", 500)
salad = MenuItem("Салат", 200)
drink = MenuItem("Напиток", 100)

order = Order()
order.add_item(pizza, 2)
order.add_item(salad, 1)
order.add_item(drink, 3)

print(order)
print("Количество разных позиций:", len(order))'''

#Задача 6. Система задач (ToDo) с приоритетами (инкапсуляция + сортировка)
class Task:
    def __init__(self, title, priority):
        self.__title = title
        self.__priority = priority

    @property
    def priority(self):
        return self.__priority

    @priority.setter
    def priority(self, value):
        if 1 <= value <= 3:
            self.__priority = value
        else:
            raise ValueError("Приоритет должен быть от 1 до 3")

    def __str__(self):
        return f"Задача: {self.__title}, приоритет: {self.__priority}"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def get_tasks_by_priority(self, priority):
        return [task for task in self.tasks if task.priority == priority]

    def remove_task(self, title):
        for task in self.tasks:
            if task._Task__title == title:
                self.tasks.remove(task)
                return
        print(f"Задача '{title}' не найдена")

    def __len__(self):
        return len(self.tasks)


# Тестовые данные
task1 = Task("Сделать домашку", 1)
task2 = Task("Купить продукты", 2)
task3 = Task("Сходить на пробежку", 3)
task4 = Task("Позвонить маме", 1)
task5 = Task("Проверить почту", 2)

# Создаём менеджер задач
manager = TaskManager()

# Добавляем тестовые задачи
manager.add_task(task1)
manager.add_task(task2)
manager.add_task(task3)
manager.add_task(task4)
manager.add_task(task5)

# Выводим отсортированный список задач по приоритету
for priority in [1, 2, 3]:
    print(f"Приоритет {priority}:")
    for task in manager.get_tasks_by_priority(priority):
        print(task)

# Удаляем одну задачу
manager.remove_task("Проверить почту")

# Выводим количество задач
print(f"Всего задач: {len(manager)}")