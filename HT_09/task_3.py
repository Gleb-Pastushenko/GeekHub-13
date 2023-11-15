# Програма-банкомат.
#    Використувуючи функції створити програму з наступним функціоналом:
#       - підтримка 3-4 користувачів, які валідуються парою ім'я/пароль (файл <users.CSV>);
#       - кожен з користувачів має свій поточний баланс (файл <{username}_balance.TXT>)
#         та історію транзакцій (файл <{username_transactions.JSON>);
#       - є можливість як вносити гроші, так і знімати їх. Обов'язкова перевірка введених даних
#         (введено цифри; знімається не більше, ніж є на рахунку і т.д.).
#    Особливості реалізації:
#       - файл з балансом - оновлюється кожен раз при зміні балансу (містить просто цифру з балансом);
#       - файл - транзакціями - кожна транзакція у вигляді JSON рядка додається в кінець файла;
#       - файл з користувачами: тільки читається. Але якщо захочете реалізувати функціонал додавання нового користувача -
#         не стримуйте себе :)
#    Особливості функціонала:
#       - за кожен функціонал відповідає окрема функція;
#       - основна функція - <start()> - буде в собі містити весь workflow банкомата:
#       - на початку роботи - логін користувача (програма запитує ім'я/пароль).
#         Якщо вони неправильні - вивести повідомлення про це і закінчити роботу (хочете - зробіть 3 спроби,
#         а потім вже закінчити роботу - все на ентузіазмі :))
#       - потім - елементарне меню типу:
#         Введіть дію:
#            1. Продивитись баланс
#            2. Поповнити баланс
#            3. Вихід
#       - далі - фантазія і креатив, можете розширювати функціонал, але основне завдання має бути повністю реалізоване :)
#     P.S. Увага! Файли мають бути саме вказаних форматів (csv, txt, json відповідно)
#     P.S.S. Добре продумайте структуру програми та функцій (edited)

import csv
import os
import json


def log_in():
    login = input("Login: ")
    password = input("Password: ")

    with open(os.path.join("task_3_files", "users.csv"), "r") as users_csv:
        csv_reader = csv.reader(users_csv)

        for item in csv_reader:
            if item[0] == login:
                if password == item[1]:
                    return (True, login)
                else:
                    print("Wrong password!")
                    return (False, None)
        else:
            print(f"There is no user with name {login}")
            return (False, None)


def check_balance(user):
    balance = None

    with open(os.path.join("task_3_files", f"{user}_balance.txt"), "r") as balance_file:
        balance = balance_file.read()

    print(f"{user} balance: {balance}")


def top_up_account(user):
    balance = None
    transactions = None
    amount = float(input(f"Top up {user} account with:  "))

    if amount < 0:
        print("Amount should be positive!")
        return

    with open(os.path.join("task_3_files", f"{user}_balance.txt"), "r") as balance_file:
        balance = float(balance_file.read())

    with open(os.path.join("task_3_files", f"{user}_transactions.json"), "r") as transactions_file:
        transactions = json.load(transactions_file)

    balance += amount
    transactions.append({"transaction type": "top up", "amount": amount})

    with open(os.path.join("task_3_files", f"{user}_balance.txt"), "w") as balance_file:
        balance_file.write(str(balance))

    with open(os.path.join("task_3_files", f"{user}_transactions.json"), "w") as transactions_file:
        json.dump(transactions, transactions_file)

    print(f"{user} account replanished with {amount}")
    print(f"Current {user} account balance: {balance}")


def withdraw(user):
    balance = None
    transactions = None
    amount = float(input(f"Withdraw from {user} account:  "))

    if amount < 0:
        print("Amount should be positive!")
        return

    with open(os.path.join("task_3_files", f"{user}_balance.txt"), "r") as balance_file:
        balance = float(balance_file.read())

    if amount > balance:
        print("insufficient funds!")
        return

    with open(os.path.join("task_3_files", f"{user}_transactions.json"), "r") as transactions_file:
        transactions = json.load(transactions_file)

    balance -= amount
    transactions.append({"transaction type": "withdraw", "amount": amount})

    with open(os.path.join("task_3_files", f"{user}_balance.txt"), "w") as balance_file:
        balance_file.write(str(balance))

    with open(os.path.join("task_3_files", f"{user}_transactions.json"), "w") as transactions_file:
        json.dump(transactions, transactions_file)

    print(f"Debited from {user} account: {amount}")
    print(f"Current {user} account balance: {balance}")


def transactions(user):
    logged = True

    while logged:
        print("1. Check balance")
        print("2. Top up account")
        print("3. Withdraw")
        print("4. Log Out and exit")
        action = input("Choose action: ")

        if action == "1":
            check_balance(user)
        elif action == "2":
            top_up_account(user)
        elif action == "3":
            withdraw(user)
        elif action == "4":
            logged = False
        else:
            print("Wrong choice! Try again!")


def start():
    user = None
    logged = False
    login_tries = 0

    while not logged:

        if login_tries == 3:
            print("Login Failed! Try again later!")
            return

        print("1. Log In")
        print("2. Exit")
        action = input("Choose action: ")

        if action == "1":
            logged, user = log_in()
        elif action == "2":
            print("Goodbye!")
            return
        else:
            print("Wrong choice! Try again!")
            return

        login_tries += 1

    transactions(user)


if __name__ == "__main__":
    start()
