# Write a script to concatenate all elements in a list into a string and print it.
# List must include both strings and integers and must be hardcoded.

from text_decoration import doubleLine, singleLine, emptyLine

from tasks_data import task_7_list

if __name__ == "__main__":
    doubleLine()
    print('The given list is hardcoded and looks like this:  ', end='')
    print(task_7_list)

    singleLine()
    stringified = [str(item) for item in task_7_list]
    joined = ''.join(stringified)
    print('The concatenated list looks like this:  ' + joined)

    doubleLine()
