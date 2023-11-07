# На основі попередньої функції (скопіюйте кусок коду) створити наступний скрипт:
#   а) створити список із парами ім'я/пароль різноманітних видів
#       (орієнтуйтесь по правилам своєї функції) - як валідні, так і ні;
#   б) створити цикл, який пройдеться по цьому циклу і, користуючись валідатором,
#       перевірить ці дані і надрукує для кожної пари значень відповідне повідомлення, наприклад:
#       Name: vasya
#       Password: wasd
#       Status: password must have at least one digit
#       -----
#       Name: vasya
#       Password: vasyapupkin2000
#       Status: OK
#    P.S. Не забудьте використати блок try/except ;)


class ValidationException(Exception):
    pass


def has_digit(string):
    for char in string:
        if char.isdecimal():
            return True

    return False


def validation(login, password):
    if not (3 <= len(login) < 50):
        raise ValidationException(
            "User name can't be shorter than 3 or longer than 50 letter!")
    if not (8 <= len(password) and has_digit(password)):
        raise ValidationException(
            "Password can't be shorter than 8 letters and should contain at least one digit!")
    if login.lower() in password.lower():
        raise ValidationException(
            "For security purposes the password shouldn't contain the user name!")


def validation_tester(validation_func, test_list):
    for item in test_list:
        print(f'Name:  {item["login"]}')
        print(f'Password:  {item["password"]}')

        try:
            validation_func(**item)
            print('Status:  OK')
        except Exception as error:
            print(f'Status:  {error}')


TEST_LIST = [
    {'login': 'user', 'password': 'password8'},
    {'login': 'Vu', 'password': 'Chang_pass1'},
    {'login': 'John', 'password': 'pass'},
    {'login': 'John', 'password': 'password'},
    {'login': 'David', 'password': 'pass15'},
    {'login': 'Tina', 'password': 'tina_password15'}
]


if __name__ == "__main__":
    validation_tester(validation, TEST_LIST)
