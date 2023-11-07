# Створіть функцію для валідації пари ім'я/пароль за наступними правилами:
#    - ім'я повинно бути не меншим за 3 символа і не більшим за 50;
#    - пароль повинен бути не меншим за 8 символів і повинен мати хоча б одну
#    цифру;
#    - якесь власне додаткове правило :)
#    Якщо якийсь із параментів не відповідає вимогам - породити виключення із відповідним текстом.


class ValidationException(Exception):
    pass


def has_digit(string):
    for char in string:
        if char.isdecimal():
            return True

    return False


def validation(username, password):
    if not (3 <= len(username) < 50):
        raise ValidationException(
            "User name can't be shorter than 3 or longer than 50 letter!")
    if not (8 <= len(password) and has_digit(password)):
        raise ValidationException(
            "Password can't be shorter than 8 letters and should contain at least one digit!")
    if username.lower() in password.lower():
        raise ValidationException(
            "For security purposes the password shouldn't contain the user name!")


if __name__ == "__main__":
    validation('user', 'pas5word')
    # validation('Wu', 'Chang438')
    # validation('Jim', 'my_password')
    validation('John', 'my_pwd')
