# Створити цикл від 0 до ... (вводиться користувачем).
# В циклі створити умову, яка буде виводити поточне значення, якщо остача від ділення на 17 дорівнює 0.

from text_decoration import doubleLine, singleLine, emptyLine


if __name__ == "__main__":
    # Intro and data prompting
    doubleLine()
    user_input = int(input("Enter a positive integer value:  "))
    singleLine()

    # Printing ou the result
    print("Here are the multiples of 17:  ")
    emptyLine()

    # The task itself
    for i in range(user_input + 1):
        if i % 17 == 0:
            print(i)

    doubleLine()
