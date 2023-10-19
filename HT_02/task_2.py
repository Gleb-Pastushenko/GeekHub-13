# Write a script which accepts two sequences of comma-separated
# colors from a user, then prints out a set containing all the colors
# from the color_list_1 which are not present in the color_list_2

from text_decoration import doubleLine, singleLine, emptyLine


def createWordsSet(string):
    stripped_words = map(lambda word: word.strip().lower(), string.split(','))
    return set(stripped_words)


if __name__ == "__main__":
    doubleLine()
    color_list_1 = createWordsSet(
        input('Enter the first colors set separaterd by commas:  '))

    emptyLine()
    color_list_2 = createWordsSet(
        input('Enter the second colors set separaterd by commas:  '))

    singleLine()
    uniques_for_list_1 = list(color_list_1.difference(color_list_2))
    uniqies_str = ', '.join(uniques_for_list_1)

    print('Here are unique values for the first colors set:  ' + uniqies_str)
    doubleLine()
