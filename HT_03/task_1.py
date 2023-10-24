# Write a script that will run through a list of tuples and replace the last value for each tuple.
# The list of tuples can be hardcoded. The "replacement" value is entered by user.
# The number of elements in the tuples must be different.

from text_decoration import singleLine, doubleLine, emptyLine


def get_value():
    return input("Enter the value you want to replace with:  ")


# TASK DATA
task_1_data = [
    (1, 2, 3, 4, 5, 6, 7),
    ('who', 'lets', 'the', 'dogs', 'out'),
    (),
    ('I', 'came', 'in', 'right', 'a', 'wrecking', 'ball'),
    ('',),
    (['what', 'if', 'God', 'was'], 1, ['of', 'us']),
]

if __name__ == "__main__":
    # Intro and data prompting
    doubleLine()
    user_input = get_value()
    singleLine()

    # The task itself
    changed_tuples = [(*tup[:-1], user_input) if tup else ()
                      for tup in task_1_data]

    # Printing out the result
    print("Here are the initial tuples:")
    emptyLine()

    for tup in task_1_data:
        print(tup)

    emptyLine()
    print("Here are the changed tuples:")
    emptyLine()

    for tup in changed_tuples:
        print(tup)

    doubleLine()
