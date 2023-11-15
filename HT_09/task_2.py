# Написати функцію, яка приймає два параметри: ім'я (шлях) файлу та кількість символів.
# Файл також додайте в репозиторій. На екран повинен вивестись список із трьома блоками -
# символи з початку, із середини та з кінця файлу. Кількість символів в блоках - та, яка введена в другому параметрі.
# Придумайте самі, як обробляти помилку, наприклад, коли кількість символів більша, ніж є в файлі або, наприклад,
# файл із двох символів і треба вивести по одному символу, то що виводити на місці середнього блоку символів?).
# Не забудьте додати перевірку чи файл існує.


def show_summary(filename, string_length):

    with open(filename, "r") as file:
        file_length = file.seek(0, 2)

        if file_length < string_length:
            print('The file length is less than the given summary length!')
            print(f'File content is: {file.read()}')
        else:
            # show ... after the first part if there are any symbols after
            file.seek(0)
            first_part = file.read(string_length) + \
                ('...' if string_length < file_length else '')

            # show ... before and after the middle part is there are any symbols before and after the middle part accordingly
            middle_index = (file_length - string_length) // 2
            file.seek(middle_index)
            middle_part = ('...' if middle_index > 0 else '') + file.read(
                string_length) + ('...' if middle_index + string_length < file_length else '')

            # show ... before the last part if there are any symbols before
            file.seek(file_length - string_length)
            last_part = ('...' if string_length <
                         file_length else '') + file.read(string_length)

            print([first_part, middle_part, last_part])


if __name__ == "__main__":
    show_summary("task_2.txt", 1)
    show_summary("task_2.txt", 2)
    show_summary("task_2.txt", 3)
    show_summary("task_2.txt", 4)
