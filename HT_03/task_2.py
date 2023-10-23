from text_decoration import doubleLine, singleLine, emptyLine
from tasks_data import task_2_data

if __name__ == "__main__":
    doubleLine()

    print("The initial list is:  ", end="")
    print(task_2_data)

    singleLine()

    print("The list with trimmed empties is:  ", end="")
    print([item for item in task_2_data if item])

    doubleLine()
