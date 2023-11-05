# Написати функцію <square>, яка прийматиме один аргумент - сторону квадрата,\\
# вертатиме 3 значення у вигляді кортежа: периметр квадрата, площа квадрата та його діагональ.


def square(side_length):   
    side_length = float(side_length)

    perimeter = side_length * 4
    area = side_length ** 2
    diagonal = (2 * side_length**2)**0.5

    return perimeter, area, diagonal


if __name__ == "__main__":
    square_params = square(input('Enter a square side lenght: '))
    print(square_params)

    