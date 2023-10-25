# Write a script to get the maximum and minimum value in a dictionary

from text_decoration import doubleLine, singleLine, emptyLine

NUMS = (int, float, bool)
ITERS = (list, tuple, set, frozenset, dict)


def getVals(type, vals):
    return list(filter(lambda val: isinstance(val, type), vals))


def showMinMax(type_name, values):
    if isinstance(values[0], ITERS):
        print(
            f'{type_name} values:\n    min: {min(values, key=len)}, max: {max(values, key=len)}')
    else:
        print(f'{type_name} values:\n    min: {min(values)}, max: {max(values)}')


# TASK DATA
task_6_data = {1: '23', 'two': [1, 3, 3], 3: 1.5, 'four': '4.4', "dic": {
    'a': 'a', 'b': 'b', 'c': 'c', 'd': 'c'}, 'empty': ()}

if __name__ == "__main__":
    # Intro and data prompting
    doubleLine()

    print('Here is the initial dict:')
    emptyLine()
    print(task_6_data)

    singleLine()

    # The task itself
    values = task_6_data.values()

    num_vals = getVals(NUMS, values)
    str_vals = getVals(str, values)
    iter_vals = getVals(ITERS, values)

    # Printing out the result
    if num_vals:
        showMinMax('Number', num_vals)

    if str_vals:
        showMinMax('String', str_vals)

    if iter_vals:
        showMinMax('Iterable', iter_vals)

    doubleLine()
