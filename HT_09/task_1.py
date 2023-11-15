# Програма-світлофор.
# Створити програму-емулятор світлофора для авто і пішоходів.
# Після запуска програми на екран виводиться в лівій половині - колір автомобільного, а в правій - пішохідного світлофора.
# Кожну 1 секунду виводиться поточні кольори.
# Через декілька ітерацій - відбувається зміна кольорів - логіка така сама як і в звичайних світлофорах
# (пішоходам зелений тільки коли автомобілям червоний).
#  Приблизний результат роботи наступний:
#       Red        Green
#       Red        Green
#       Red        Green
#       Red        Green
#       Yellow     Red
#       Yellow     Red
#       Green      Red
#       Green      Red
#       Green      Red
#       Green      Red
#       Yellow     Red
#       Yellow     Red
#       Red        Green

import time


def create_traffic_light_program(red, yellow, green):
    return ['Red'] * red + ['Yellow'] * yellow + ['Green'] * green + ['Yellow'] * yellow


def traffic_light_operation(program):
    program_iterator = iter(program)

    while True:

        try:
            cars_light = next(program_iterator)
            pedestrians_light = 'Green' if cars_light == 'Red' else 'Red'
            print(cars_light.center(10) + pedestrians_light.center(10))
            time.sleep(1)

        except StopIteration:
            program_iterator = iter(program)


if __name__ == "__main__":
    program = create_traffic_light_program(4, 2, 4)
    traffic_light_operation(program)
