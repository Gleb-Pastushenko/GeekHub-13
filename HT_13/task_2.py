# 2. Створіть за допомогою класів та продемонструйте свою реалізацію шкільної бібліотеки (включіть фантазію).
# Наприклад вона може містити класи Person, Teacher, Student, Book, Shelf, Author, Category і.т.д.


class Person:
    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.books = []

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def __repr__(self):
        return self.__str__()


class Shelf:
    def __init__(self, number):
        self.number = number
        self.books = []
        self.library = library

    def __str__(self):
        return str(self.number)

    def __repr__(self):
        return f'shelf #{self}'

    def add_book(self, book):
        self.books.append(book)
        book.shelf = self.number
        self.library.books.append(book)


class Book:
    def __init__(self, id, book_name, author, shelf):
        self.id = id
        self.book_name = book_name
        self.author = author
        self.shelf = None
        self.is_taken = False
        self.taken_by = None

    def take(self, person):
        self.is_taken = True
        self.taken_by = person
        person.books.append(self)

    def return_book(self):
        index = self.taken_by.index(self)
        del self.taken_by[index]
        self.taken_by = None
        self.is_taken = False

    def find(self):
        if self.is_taken is True:
            return f'The book is taken by {self.taken_by}'
        else:
            return f'The book is on the shelf {self.shelf}'

    def __str__(self):
        return f'{self.book_name} - {self.author}'

    def __repr__(self):
        return self.__str__()


class Library:
    def __init__(self):
        self.members = []
        self.books = []
        self.shelves = []

    def new_member(self, person):
        self.members.append(person)

    def add_shelf(self, shelf):
        self.shelves.append(shelf)
        self.books.extend(shelf.books)
        self.library = self

    def take_book(self, person, book):
        print(book.find())

        if book.is_taken:
            return
        else:
            book.take(person)

    def return_book(self, book):
        book.return_book()


if __name__ == "__main__":
    library = Library()

    library.add_shelf(Shelf(1))
    library.add_shelf(Shelf(2))

    print(library.shelves)

    library.shelves[0].add_book(Book(1, 'Invincible', 'Stanislav Lem', None))
    library.shelves[0].add_book(Book(2, 'Solaris', 'Stanislav Lem', None))

    library.new_member(Person(1, 'Ivan', 'Ivanov'))
    library.new_member(Person(2, 'Mykola', 'Mykolaenko'))

    print(library.members)

    print(library.books)

    library.take_book(library.members[0], library.books[1])

    print(library.books[1].find())
