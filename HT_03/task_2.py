# Write a script to remove an empty elements from a list.
# Test list: [(), ('hey'), ('',), ('ma', 'ke', 'my'), [''], {}, ['d', 'a', 'y'], '', []]

from text_decoration import doubleLine, singleLine, emptyLine

# TASK DATA
task_2_data = [(), ('hey'), ('',), ('ma', 'ke', 'my'),
               [''], {}, ['d', 'a', 'y'], '', []]

if __name__ == "__main__":
    # Intro and data prompting
    doubleLine()

    print("The initial list is:  ", end="")
    print(task_2_data)

    singleLine()

    # The task itself
    cleared_list = [item for item in task_2_data if item]

    # Printing out the result
    print("The list with trimmed empties is:  ", end="")
    print(cleared_list)

    doubleLine()
