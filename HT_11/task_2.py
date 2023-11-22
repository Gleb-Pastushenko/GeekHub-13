# 2. Створити клас Person, в якому буде присутнім метод __init__ який буде приймати якісь аргументи,
#   які зберігатиме в відповідні змінні.
# - Методи, які повинні бути в класі Person - show_age, print_name, show_all_information.
# - Створіть 2 екземпляри класу Person та в кожному з екземплярів створіть атребут profession
#   (його не має інсувати під час ініціалізації).


class Person:
    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender

    def show_age(self):
        print(f"I'm {self.age} years old")

    def print_name(self):
        print(f"I'm {self.first_name} {self.last_name}")

    def show_all_information(self):
        self.print_name()
        self.show_age()

        print("And here is a summary about me:")

        for key, value in self.__dict__.items():
            print(f"{key}: {value}")


if __name__ == "__main__":
    person_1 = Person("Albert", "Einstein", "30", "man")
    person_2 = Person("Niels", "Bohr", "33", "man")

    person_1.profession = "physicist"
    person_2.profession = "physicist"

    person_1.show_all_information()
    person_2.show_all_information()
