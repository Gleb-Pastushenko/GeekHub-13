# Write a script which accepts a <number> from a user
# and prints out a sum of the first <number> positive integers.

from text_decoration import doubleLine, singleLine, emptyLine


def getNumber():
    print('Enter an integer number:  ', end='')
    input_value = input()
    return (int(input_value))


def seriesSum(n):
    return int(n * (n + 1) / 2)


if __name__ == "__main__":
    doubleLine()
    number = getNumber()
    singleLine()
    print(f'The sum of series is:  {seriesSum(number)}')
    doubleLine()
