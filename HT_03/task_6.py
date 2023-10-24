# Write a script to get the maximum and minimum value in a dictionary

from text_decoration import doubleLine, singleLine, emptyLine
from tasks_data import task_6_data


def isNumberValue(val):
    try:
        float(val)
        return True
    except:
        pass


# TASK DATA
task_6_data = {1: '23', 'two': [1, 3, 3], 3: 1.5, 'four': '4.4'}

if __name__ == "__main__":
    doubleLine()

    print('Here is the initial dict:')
    emptyLine()
    print(task_6_data)

    singleLine()

    number_values = filter(isNumberValue, task_6_data.values())
    values = [float(value) if float(value) % 1 != 0 else int(value)
              for value in number_values]

    print("The min value is:  " + str(min(values)))
    emptyLine()
    print("The max value is:  " + str(max(values)))

    doubleLine()
