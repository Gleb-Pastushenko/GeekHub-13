# Написати функцію <bank> , яка працює за наступною логікою:
# користувач робить вклад у розмірі <a> одиниць строком на <years> років під <percents> відсотків
# (кожен рік сума вкладу збільшується на цей відсоток,
# ці гроші додаються до суми вкладу і в наступному році на них також нараховуються відсотки).
# Параметр <percents> є необов'язковим і має значення по замовчуванню <10> (10%).
# Функція повинна принтануть суму, яка буде на рахунку, а також її повернути (але округлену до копійок).

from functools import reduce


def bank(a, years, percents=10):    
    for _ in range(years):
        a += a * percents / 100

    a = round(a, 2)

    print(f'The amount on you account will be {a} in {years} years!')

    return a


if __name__ == "__main__":
    deposit = float(input('Input a deposit:  '))
    duration = int(input('Enter deposit duration in years:  '))
    percents = float(input('Enter a deposit rate:  '))

    bank(deposit, duration, percents)