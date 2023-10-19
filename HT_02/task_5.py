# Write a script which accepts a decimal number from a user
# and converts it to a hexadecimal number.

from text_decoration import doubleLine, singleLine

from task_3 import getNumber

if __name__ == "__main__":
    doubleLine()
    number = getNumber()
    singleLine()
    print('The hexademical representation is:  ' + hex(number))
    doubleLine()
