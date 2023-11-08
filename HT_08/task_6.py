# Напишіть функцію, яка прймає рядок з декількох слів і повертає довжину найкоротшого слова.
# Реалізуйте обчислення за допомогою генератора.

import re


def shortest_length(string):

    def getWord(string):
        words = string.replace(',', ' ')
        words = re.split(r'\s+', words)

        for word in words:
            yield word

    words = getWord(string)

    shortest = len(next(words))

    while True:
        try:
            shortest = min(len(next(words)), shortest)
        except:
            return shortest


if __name__ == "__main__":
    print(shortest_length(
        "I'm blue, da-bu-di da-bu-da, du-da-bu-di da-bu-da, da-bu-di da-bu-da"))
