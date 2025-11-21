'''#15 Задача 15. Класс "Автомобиль"
class Car :
    def __init__(self,brand,model,mileage):
        self.brand=brand
        self.model=model
        self.mileage=mileage
    def drive(self,distance):
        self.mileage+=distance
        
    def info(self):
         return f"Автомобиль {self.brand}{self.model}, пробег {self.mileage} км"

car = Car("Toyota", "Camry", 10000)
car.drive(150)
car.drive(200)
print(car.info())'''

class Book:
    def __init__(self, title, author, year):
        self.title = title.strip()
        self.author = author.strip()
        self.year = year.strip()

class Library:
    def __init__(self):
        self.list_of_books = {}

    def add_book(self, book):
        key = (book.title, book.author, book.year)
        if key in self.list_of_books:
            print("Книга с таким названием, автором и годом уже есть в библиотеке")
        else:
            self.list_of_books[key] = book
            print(f"Книга {book.title} добавлена")

    def list_books(self):
        print("Список книг в библиотеке:")
        for book in self.list_of_books.values():
            print(f"{book.title}, {book.author}, {book.year}")

    def load_books(self, filename):
        books = []
        try:
            with open(filename, encoding='utf-8') as file:
                for line in file:
                    parts = line.strip().split(';')
                    if len(parts) == 3 and parts[0] != "Название":  # Пропуск заголовка
                        title, author, year = parts
                        books.append({"title": title, "author": author, "year": year})
        except FileNotFoundError:
            print("Файл не найден!")
        return books

books = []
filename = "books.csv"

library1 = Library()
book_dicts = library1.load_books(filename)

for b in book_dicts:
    book = Book(b["title"], b["author"], b["year"])
    library1.add_book(book)

print()
library1.list_books()
