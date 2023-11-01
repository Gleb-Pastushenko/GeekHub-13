# Написати функцию <is_prime>, яка прийматиме 1 аргумент - число від 0 до 1000,
# і яка вертатиме True, якщо це число просте і False - якщо ні.


def is_prime(number):
    deviders_number = 0
    
    for i in range(1, number // 2 + 1):
        if number % i == 0:
            deviders_number += 1
            
        if deviders_number > 1:
            return False
    
    return True