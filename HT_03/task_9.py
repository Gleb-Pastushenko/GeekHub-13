from text_decoration import doubleLine, singleLine, emptyLine


def getLeaps(start, stop):
    return [year for year in range(start, stop + 1) if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0]


if __name__ == "__main__":
    doubleLine()

    start_year = int(input("Enter the year you would like to start from:  "))
    emptyLine()
    stop_year = int(input("Enter the year you would like to stop on:  "))

    singleLine()

    print("Here is the list of the leap years:  ", end="")

    print(getLeaps(start_year, stop_year))

    doubleLine()
