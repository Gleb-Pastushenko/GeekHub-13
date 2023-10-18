# Write a script which accepts a sequence of comma-separated numbers
# from a user and generates a list and a tuple with those numbers

from text_decoration import doubleLine, singleLine, emptyLine


def toIntsList(raw_list):
    mapped = map(lambda x: int(x), raw_list)
    return list(mapped)


def toIntsTuple(raw_list):
    mapped = map(lambda x: int(x), raw_list)
    return tuple(mapped)


if __name__ == "__main__":
    doubleLine()
    print('Enter comma separated integer numbers:', end='  ')
    user_input_raw = input().split(',')
    singleLine()

    user_list = toIntsList(user_input_raw)
    user_tuple = toIntsTuple(user_input_raw)

    print(f'list: {user_list}')
    emptyLine()
    print(f'tuple: {user_tuple}')
    doubleLine()
