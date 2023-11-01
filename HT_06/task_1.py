# Написати функцію <square>, яка прийматиме один аргумент - сторону квадрата,\\
# вертатиме 3 значення у вигляді кортежа: периметр квадрата, площа квадрата та його діагональ.


def square(side_length):
    if type(side_length) in (int, float) and side_length >= 0:
        perimeter = side_length * 4
        area = side_length ** 2
        diagonal = (2 * side_length**2)**0.5

        return (perimeter, area, diagonal)
    else: print('The square side length shoul be positive int or float')