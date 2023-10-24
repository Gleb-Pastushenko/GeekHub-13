# Write a script that combines three dictionaries by updating the first one.

from text_decoration import doubleLine, singleLine, emptyLine

# TASK DATA
dict_1 = {'foo': 'bar', 'bar': 'buz'}
dict_2 = {'dou': 'jones', 'USD': 36}
dict_3 = {'AUD': 19.2, 'name': 'Tom'}

if __name__ == "__main__":
    # Intro and data prompting
    doubleLine()

    print("Here are three separate dicts:")
    emptyLine()
    print(dict_1)
    print(dict_2)
    print(dict_3)

    # The task itself
    dict_1.update(dict_2)
    dict_1.update(dict_3)

    # Printing out the result
    singleLine()
    print("Here is updated dict_1:")
    emptyLine()
    print(dict_1)

    doubleLine()
