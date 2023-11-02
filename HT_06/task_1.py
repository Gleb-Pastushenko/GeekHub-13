# Написати функцію <square>, яка прийматиме один аргумент - сторону квадрата,\\
# вертатиме 3 значення у вигляді кортежа: периметр квадрата, площа квадрата та його діагональ.


def square(side_length):
    try:
        side_length = float(side_length)
        if side_length < 0:
            raise ValueError
            
        perimeter = side_length * 4
        area = side_length ** 2
        diagonal = (2 * side_length**2)**0.5

        return perimeter, area, diagonal
    
    except (ValueError, TypeError):
        print('The square side length shoul be positive int or float!')

    except Exception as error:
        print(type(error))
    

if __name__ == "__main__":
    square(input('Enter a square side lenght: '))