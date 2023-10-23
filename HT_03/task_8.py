from text_decoration import doubleLine, singleLine, emptyLine


def getMultipliesList(number):
    return ", ".join([str(i) for i in range(1, user_input + 1) if i % number == 0])


if __name__ == "__main__":
    doubleLine()
    user_input = int(input("Enter a positive integer value:  "))
    singleLine()

    print("Here are the multiples of 17:  ", end="")
    print(getMultipliesList(17))

    doubleLine()
