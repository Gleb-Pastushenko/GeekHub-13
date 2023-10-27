# Створiть 3 рiзних функцiї (на ваш вибiр).
# Кожна з цих функцiй повинна повертати якийсь результат (напр. інпут від юзера, результат математичної операції тощо).
# Також створiть четверту ф-цiю, яка всередині викликає 3 попереднi, обробляє їх результат та також повертає результат своєї роботи.
# Таким чином ми будемо викликати одну (четверту) функцiю, а вона в своєму тiлi - ще 3.


def get_integer(prompt='Enter int value', *, min_val=None, max_val=None):
    integer = None
    prompt = prompt.strip().strip(' :=')

    while integer is None:
        try:
            integer = int(input(f'{prompt}:  '))
            if min_val is not None and integer < min_val:
                raise ValueError(f'The value can\'t be lower than {min_val}')
            if max_val is not None and integer > max_val:
                raise ValueError(f'The value can\'t be higher than {max_val}')
        except ValueError as error:
            integer = None
            print(f'{error}. Try again!')

    return integer


def input_income_by_months(months_number):
    income_list = [get_integer(f'month {i + 1} income', min_val=0)
                   for i in range(months_number)]

    return income_list


def mean_median(values):
    list_len = len(values)
    sorted_list = sorted(values)
    mean = round(sum(values)/len(values), 2)
    median = sorted_list[list_len // 2] if list_len % 2 else sum(
        sorted_list[list_len // 2 - 1: list_len // 2 + 1])/2

    return mean, median


def get_incomes_statistics():
    months_number = get_integer('Enter the number of income months', min_val=2)
    income_list = input_income_by_months(months_number)
    mean, median = mean_median(income_list)
    return {'mean': mean, 'median': median}


if __name__ == "__main__":
    statistics = get_incomes_statistics()

    for stat_name, stat_value in statistics.items():
        print(f'{stat_name}: {stat_value}')
