# Написати функцію <prime_list>, яка прийматиме 2 аргументи - початок і кінець діапазона,
# і вертатиме список простих чисел всередині цього діапазона.
# Не забудьте про перевірку на валідність введених даних та у випадку невідповідності - виведіть повідомлення.

from task_3 import is_prime


def prime_list(lower_limit, upper_limit):
    primes = []
    if lower_limit <= upper_limit:
        for i in range(lower_limit, upper_limit):
            if is_prime(i):
                primes.append(i)
    else:
        print("Lower limit can't be bigger than upper limit!!!")
        return
    
    return primes if primes else "There are no any primes in the given range!"