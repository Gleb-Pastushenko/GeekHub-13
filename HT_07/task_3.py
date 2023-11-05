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


def validation(username, password):
    valid_name = 3 <= len(username) < 50
    valid_password = 8 <= len(password) and has_digit(password)
    pwd_includes_name = username.lower() in password.lower()

    if not valid_name:
        raise ValidationException(
            "User name can't be shorter than 3 or longer than 50 letter!")
    if not valid_password:
        raise ValidationException(
            "Password can't be shorter than 8 letters and should contain at least one digit!")
    if pwd_includes_name:
        raise ValidationException(
            "For security purposes the password shouldn't contain the user name!")


def validation_tester(validation_func, test_list):
    for item in test_list:
        print(f'Name:  {item[0]}')
        print(f'Password:  {item[1]}')

        try:
            validation_func(*item)
            print('Status:  OK')
        except Exception as error:
            print(f'Status:  {error}')


TEST_LIST = [
    ['user', 'password8'],
    ['Vu', 'Chang_pass1'],
    ['John', 'pass'],
    ['John', 'password'],
    ['David', 'pass15'],
    ['Tina', 'tina_password15']
]


if __name__ == "__main__":
    validation_tester(validation, TEST_LIST)
