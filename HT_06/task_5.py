# Написати функцію <fibonacci>, яка приймає один аргумент і виводить всі числа Фібоначчі, що не перевищують його.


def fibonacci(number):
    fib_list = [0, 1]

    if number > 0:
        while sum(fib_list[-2:]) <= number:
            fib_list.append(sum(fib_list[-2:]))
        return fib_list
        
    else:
        print('Entered number should be positive!')
        return
    

if __name__ == "__main__":
    fibonacci_numbers = fibonacci(int(input("Enter a positive integer number:  ")))

    print(fibonacci_numbers)