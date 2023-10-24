# Користувачем вводиться початковий і кінцевий рік.
# Створити цикл, який виведе всі високосні роки в цьому проміжку (границі включно).
# P.S. Рік є високосним, якщо він кратний 4, але не кратний 100, а також якщо він кратний 400.

from text_decoration import doubleLine, singleLine, emptyLine


def getLeaps(start, stop):
    return [year for year in range(start, stop + 1) if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0]


if __name__ == "__main__":
    # Intro and data prompting
    doubleLine()

    start_year = int(input("Enter the year you would like to start from:  "))
    emptyLine()
    stop_year = int(input("Enter the year you would like to stop on:  "))

    singleLine()

    # The task itself
    print("Here is the list of the leap years:  ", end="")

    # Printing out the result
    print(getLeaps(start_year, stop_year))

    doubleLine()
