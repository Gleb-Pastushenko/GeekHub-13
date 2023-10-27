# Користувач вводить змiннi "x" та "y" з довiльними цифровими значеннями.
# Створiть просту умовну конструкцiю (звiсно вона повинна бути в тiлi ф-цiї),
# пiд час виконання якої буде перевiрятися рiвнiсть змiнних "x" та "y" та у випадку нервіності - виводити ще і різницю.
# Повиннi опрацювати такi умови (x, y, z заміність на відповідні числа):
#    x > y;       вiдповiдь - "х бiльше нiж у на z"
#    x < y;       вiдповiдь - "у бiльше нiж х на z"
#    x == y.      вiдповiдь - "х дорiвнює y"


def get_float(prompt='Enter custom value', *, min_val=None, max_val=None):
    float_val = None
    prompt = prompt.strip().strip(' :=')

    while float_val is None:
        try:
            float_val = float(input(f'{prompt}:  '))
            if min_val is not None and float_val < min_val:
                raise ValueError(f'The value can\'t be lower than {min_val}')
            if max_val is not None and float_val > max_val:
                raise ValueError(f'The value can\'t be higher than {max_val}')
        except ValueError as error:
            float_val = None
            print(f'{error}. Try again!')

    return float_val


def compare(x, y):
    if x > y:
        print(f'x more y by {x - y}')
    elif x < y:
        print(f'y more x by {y - x}')
    else:
        print('x is equal to y')


if __name__ == '__main__':
    x = get_float('Enter x')
    y = get_float('Enter y')

    compare(x, y)
