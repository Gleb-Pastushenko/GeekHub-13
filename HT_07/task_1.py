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
    users_list = [
        {'login': 'Vasya', 'password': 'Vasya'},
        {'login': 'Petya', 'password': 'petya_pass'},
        {'login': 'Kolya', 'password': 'kolya_pass'},
        {'login': 'Ivan', 'password': 'ivan_pass'},
        {'login': 'Sasha', 'password': 'sasha_pass'}
    ]

    match_list = list(filter(
        lambda user: user['login'] == username and user['password'] == password, users_list))

    if match_list:
        return True
    else:
        if silent:
            return False
        else:
            raise LoginException


if __name__ == "__main__":
    # print(login('Vasya', 'vasya_pass'))

    print(login('Yura', 'youra_pass', silent=True))

    print(login('Petya', 'petya_pass'))
