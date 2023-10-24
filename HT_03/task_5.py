# Write a script to remove values duplicates from dictionary. Feel free to hardcode your dictionary.

from text_decoration import doubleLine, singleLine, emptyLine


def removeDuplicates(dictionary):
    items = list(dictionary.items())
    values = [value for key, value in items]
    unique_values = set(values)
    uniques = [items[values.index(value)] for value in unique_values]
    return dict(uniques)


# TASK DATA
task_5_data = {1: "one", 2: "two", 3: "three",
               "3": "three", "four": "four", 4: "four"}


if __name__ == "__main__":
    # Intro and data prompting
    doubleLine()

    print("The initial dictionary is:  ", end="")
    print(task_5_data)

    singleLine()

    # The task itself
    cleared_dict = removeDuplicates(task_5_data)

    # Printing out the result
    print("The dict with duplicates removed:  ", end="")
    print(removeDuplicates(task_5_data))

    doubleLine()
