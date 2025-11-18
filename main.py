'''
#Класс Книга
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
'''
#Класс Студент
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

#Переопределения методов (Транспорт)
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
    vehicle.move()