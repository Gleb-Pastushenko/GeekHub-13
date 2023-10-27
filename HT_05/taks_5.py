# Ну і традиційно - калькулятор :slightly_smiling_face: Повинна бути 1 ф-цiя,
# яка б приймала 3 аргументи - один з яких операцiя, яку зробити!
# Аргументи брати від юзера (можна по одному - 2, окремо +, окремо 2; можна всі разом - типу 1 + 2).
# Операції що мають бути присутні: +, -, *, /, %, //, **. Не забудьте протестувати з різними значеннями на предмет помилок!


def inputAndDetermineType(prompt=''):
    value = None

    while value is None:
        input_value = input(prompt)
        try:
            value = int(input_value)
        except ValueError:
            try:
                value = float(input_value)
            except ValueError as error:
                print(f'{error}.  Try again!')

    return {'value': value, 'type': type(value)}


def calculate(val_1, val_2, operator):
    var_1 = val_1['value']
    var_2 = val_2['value']
    var_1_type = val_1['type']
    var_2_type = val_2['type']

    if operator in "%//" and (var_1_type == float or var_2_type == float):
        print('This operator requires both operands to be integer values!!!')
    elif operator == "+":
        print(f'Result:  {var_1 + var_2}')
    elif operator == "-":
        print(f'Result:  {var_1 - var_2}')
    elif operator == "*":
        print(f'Result:  {var_1 * var_2}')
    elif operator == "**" and var_1 == 0 and var_2 < 0:
        print(f'This will cause the "Zero division" error. Can\'t be done!')
    elif operator == "**":
        print(f'Result:  {var_1**var_2}')
    elif operator == "/" and var_2 == 0:
        print('This will cause "Zero division" error. Can\'t be done')
    elif operator == "/":
        print(f'Result:  {var_1 / var_2}')
    elif operator == "//":
        print(f'Result:  {var_1 // var_2}')
    elif operator == "%":
        print(f'Result:  {var_1 % var_2}')


if __name__ == "__main__":
    val_1 = inputAndDetermineType('Enter value 1:  ')
    val_2 = inputAndDetermineType('Enter value 2:  ')
    operator = input('Enter an operator:  ').strip()

    calculate(val_1, val_2, operator)
