# Write a script which accepts a <number> from user and generates dictionary in range <number>
# where key is <number> and value is <number>*<number> e.g. 3 --> {0: 0, 1: 1, 2: 4, 3: 9}

from text_decoration import doubleLine, singleLine, emptyLine

if __name__ == "__main__":
    # Intro and data prompting
    doubleLine()

    user_input = input("Enter a number:  ")

    singleLine()

    # The task itself
    result = {number: number ** 2 for number in range(int(user_input) + 1)}

    # Printing out the result
    print("Here is your squares dictionary:  ", end="")
    print(result)

    doubleLine()
