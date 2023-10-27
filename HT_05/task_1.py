# Написати функцiю season, яка приймає один аргумент (номер мiсяця вiд 1 до 12)
# та яка буде повертати пору року, якiй цей мiсяць належить (зима, весна, лiто або осiнь).
# У випадку некоректного введеного значення - виводити відповідне повідомлення.


def season(month: int) -> str:
    match month:
        case 1 | 2 | 12:
            return 'winter'
        case 3 | 4 | 5:
            return 'spring'
        case 6 | 7 | 8:
            return 'summer'
        case 9 | 10 | 11:
            return 'autumn'

    print('There is no such month! Try Again!')


if __name__ == "__main__":
    user_input = None

    while not user_input:
        try:
            user_input = int(input('Enter month number:  '))
            current_season = season(user_input)
            if not current_season:
                user_input = None

        except ValueError as err:
            print('Month number should be an integer value! Try again!')

    print(f'Current season is:  {current_season}')
