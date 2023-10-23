from text_decoration import doubleLine, singleLine, emptyLine

if __name__ == "__main__":
    doubleLine()

    user_input = input("Enter a number:  ")

    singleLine()

    print("Here is your squares dictionary:  ", end="")
    print({number: number**2 for number in range(int(user_input) + 1)})

    doubleLine()
