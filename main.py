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
'''
#6 Класс Point 
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

#13 Наследование: «Работник» и «Менеджер»:
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
manager.info() 