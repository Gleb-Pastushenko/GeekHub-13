from text_decoration import doubleLine, singleLine, emptyLine
from tasks_data import task_3_data

if __name__ == "__main__":
    doubleLine()

    print("Here are three separate dicts:")
    emptyLine()

    for idx, dic in enumerate(task_3_data):
        print(f"dict_{idx + 1} = {dic}")

    for dic in task_3_data[1:]:
        task_3_data[0].update(dic)

    print("Here is updated dict_1:")
    emptyLine()
    print(task_3_data[0])

    doubleLine()
