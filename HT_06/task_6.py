#  Написати функцію, яка буде реалізувати логіку циклічного зсуву елементів в списку.
#  Тобто функція приймає два аргументи: список і величину зсуву (якщо ця величина додатня - пересуваємо з кінця на початок,
#  якщо від'ємна - навпаки - пересуваємо елементи з початку списку в його кінець).
#   Наприклад:
#   fnc([1, 2, 3, 4, 5], shift=1) --> [5, 1, 2, 3, 4]
#   fnc([1, 2, 3, 4, 5], shift=-2) --> [3, 4, 5, 1, 2]


def shift(lst, shift):
    if shift != 0:
        sign = int(abs(shift)/shift)
        shift_value = abs(shift) % len(lst) * sign

        return [*lst[-shift_value:], *lst[:-shift_value]]

    else:
        return lst

if __name__ == "__main__":    
    input_list = input('Enter a custom list (comma separated values):  ').strip(' []{}()').split(',')
    input_list = input_list or []    
    input_shift = int(input('Enter a shift value:  '))

    print(shift(input_list, input_shift))