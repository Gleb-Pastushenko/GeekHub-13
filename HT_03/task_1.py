from text_decoration import singleLine, doubleLine, emptyLine
from tasks_data import task_1_data


def get_number():
    return input("Enter the value you want to replace with:  ")


if __name__ == "__main__":
    doubleLine()
    user_input = get_number()

    singleLine()
    new_list = [(*tuple_item[:-1], user_input) for tuple_item in task_1_data]

    print("Here are the initial tuples list:")
    emptyLine()

    for tuple_item in task_1_data:
        print(tuple_item)

    emptyLine()
    print("Here are the changed tuples list:")
    emptyLine()

    for tuple_item in new_list:
        print(tuple_item)

    doubleLine()
