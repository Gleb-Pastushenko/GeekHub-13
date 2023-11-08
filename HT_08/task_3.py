# Всі ви знаєте таку функцію як <range>.
# Напишіть свою реалізацію цієї функції. Тобто щоб її можна було використати у вигляді:
#     for i in my_range(1, 10, 2):
#         print(i)
#     1
#     3
#     5
#     7
#     9
#    P.S. Повинен вертатись генератор.
#    P.P.S. Для повного розуміння цієї функції - можна почитати документацію по ній:
#        https://docs.python.org/3/library/stdtypes.html#range
#    P.P.P.S Не забудьте обробляти невалідні ситуації (аналог range(1, -10, 5)).
#        Подивіться як веде себе стандартний range в таких випадках.


def my_range(*args):
    if len(args) == 1:
        start = 0
        stop = args[0]
        step = 1
    elif len(args) == 2:
        start = args[0]
        stop = args[1]
        step = 1
    elif len(args) == 3:
        start = args[0]
        stop = args[1]
        step = args[2]
    elif len(args) > 3:
        raise TypeError(
            f'my_range expected at most 3 arguments, got {len(args)}')
    else:
        raise TypeError('my_range expected at least 1 argument, got 0')

    if (type(start), type(stop), type(step)) != (int, int, int):
        raise TypeError('my_range accepts only integer values')

    while (stop - start) / step > 0:
        yield start
        start += step


if __name__ == "__main__":
    for i in my_range(1, 10, 2):
        print(i)
