# Write a script to check whether a value from a user's input
# is contained in a group of values.

from text_decoration import doubleLine, singleLine, emptyLine

from tasks_data import task_6_list


def getValue():
    input_value = input('Enter any value:  ')
    return input_value


def getConvertedValue(value):
    try:
        converted_value = int(value)
    except:
        converted_value = None

    if not converted_value:
        try:
            converted_value = float(value)
        except:
            pass

    if not converted_value:
        if value.strip().lower() == 'true':
            converted_value = True
        elif value.strip().lower() == 'false':
            converted_value = False

    if not converted_value:
        converted_value = value

    return converted_value


def printIsInList(val, list):
    print(f'The value is{" not" if val not in list else ""} in list')

    emptyLine()
    print(f'The list values are: {list}')


if __name__ == "__main__":
    doubleLine()
    value = getValue()

    singleLine()
    converted_value = getConvertedValue(value)
    printIsInList(converted_value, task_6_list)
    doubleLine()
