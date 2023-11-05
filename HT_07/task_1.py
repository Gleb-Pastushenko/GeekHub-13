# Створіть функцію, всередині якої будуть записано список із п'яти користувачів (ім'я та пароль).
# Функція повинна приймати три аргументи: два - обов'язкових (<username> та <password>)
# і третій - необов'язковий параметр <silent> (значення за замовчуванням - <False>).
# Логіка наступна:
#     якщо введено коректну пару ім'я/пароль - вертається True;
#     якщо введено неправильну пару ім'я/пароль:
#         якщо silent == True - функція вертає False
#         якщо silent == False -породжується виключення LoginException (його також треба створити =))


class LoginException(Exception):
    pass


def login(username, password, silent=False):
    users_list = {
        'Vasya': 'vasya_pass',
        'Petya': 'petya_pass',
        'Kolya': 'kolya_pass',
        'Ivan': 'ivan_pass',
        'Sasha': 'sasha_pass',
    }

    if username in users_list and password == users_list[username]:
        return True
    else:
        if silent:
            return False
        else:
            raise LoginException


if __name__ == "__main__":
    print(login('Vasya', 'vasya_pass'))

    print(login('Yura', 'youra_pass', silent=True))

    print(login('Petya', 'petya pass'))
