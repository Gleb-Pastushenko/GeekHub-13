from text_decoration import doubleLine, singleLine, emptyLine
from tasks_data import task_5_data


def removeDuplicates(dictionary):
    items = list(dictionary.items())
    values = [value for key, value in items]
    unique_values = set(values)
    uniques = [items[values.index(value)] for value in unique_values]
    return dict(uniques)


if __name__ == "__main__":
    doubleLine()

    print("The initial dictionary is:  ", end="")
    print(task_5_data)

    singleLine()

    print("The dict with duplicates removed:  ", end="")
    print(removeDuplicates(task_5_data))

    doubleLine()
