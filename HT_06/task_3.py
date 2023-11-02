# Написати функцию <is_prime>, яка прийматиме 1 аргумент - число від 0 до 1000,
# і яка вертатиме True, якщо це число просте і False - якщо ні.


def is_prime(number):
    if number < 1:
        print(f'{number} in not a natural number!')
        return None
    
    deviders_number = 0
    
    for i in range(1, number // 2 + 1):
        if number % i == 0:
            deviders_number += 1
            
        if deviders_number > 1:
            return False
    
    if deviders_number == 0:
        return False
    
    return True


if __name__ == "__main__":
    result = is_prime(int(input('Enter a natural number:  ')))

    print(result)