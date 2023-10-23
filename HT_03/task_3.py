from text_decoration import doubleLine, singleLine, emptyLine
from tasks_data import task_3_data
from functools import reduce

if __name__ == "__main__":
    doubleLine()

    print("Here are three separate dicts:")
    emptyLine()

    for idx, dic in enumerate(task_3_data):
        print(f"dict_{idx + 1} = {dic}")

    singleLine()
    print("Here are concatenated dicts:")
    emptyLine()
    print(reduce(lambda acc, item: {**acc, **item}, task_3_data, {}))

    doubleLine()
