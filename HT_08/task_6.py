# Напишіть функцію, яка прймає рядок з декількох слів і повертає довжину найкоротшого слова.
# Реалізуйте обчислення за допомогою генератора.

import re


def shortest_length(string):

    words = string.replace(',', ' ')
    words = re.split(r'\s+', words)

    return min((word for word in words), key=len)


if __name__ == "__main__":
    print(shortest_length(
        "I'm blue, da-bu-di da-bu-da, du-da-bu-di da-bu-da, da-bu-di da-bu-da"))
