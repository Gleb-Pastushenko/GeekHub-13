# Write a script which accepts a <number> from user and then <number> times asks user for string input.
# At the end script must print out result of concatenating all <number> strings.

from text_decoration import doubleLine, singleLine, emptyLine
from task_3 import getNumber


def promptValue():
    emptyLine()
    print('Input any string:  ', end='')
    input_value = input()
    return input_value if input_value.isnumeric() else None


if __name__ == "__main__":
    doubleLine()
    number = getNumber()

    input_list = [item for i in range(number) if (item := promptValue())]

    singleLine()
    stringified = [str(item) for item in input_list]
    joined = ''.join(stringified)
    print('Here is concatenated numeric strings:  ' + joined)

    doubleLine()
