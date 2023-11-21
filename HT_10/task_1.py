# Банкомат 2.0
#     - усі дані зберігаються тільки в sqlite3 базі даних. Більше ніяких файлів.
#       Якщо в попередньому завданні ви добре продумали структуру програми
#       то у вас не виникне проблем швидко адаптувати її до нових вимог.
#     - на старті додати можливість залогінитися або створити нового користувача
#       (при створенні нового користувача, перевіряється відповідність логіну і паролю мінімальним вимогам.
#       Для перевірки створіть окремі функції)
#     - в таблиці (базі) з користувачами має бути створений унікальний користувач-інкасатор,
#       який матиме розширені можливості (домовимось, що логін/пароль будуть admin/admin щоб нам було простіше перевіряти)
#     - банкомат має власний баланс
#     - кількість купюр в банкоматі обмежена. Номінали купюр - 10, 20, 50, 100, 200, 500, 1000
#     - змінювати вручну кількість купюр або подивитися їх залишок в банкоматі може лише інкасатор
#     - користувач через банкомат може покласти на рахунок лише сумму кратну мінімальному номіналу що підтримує банкомат.
#       В іншому випадку - повернути "здачу" (наприклад при поклажі 1005 --> повернути 5).
#       Але це не має впливати на баланс/кількість купюр банкомату, лише збільшуєтсья баланс користувача
#       (моделюємо наявність двох незалежних касет в банкоматі - одна на прийом, інша на видачу)
#     - зняти можна лише в межах власного балансу, але не більше ніж є всього в банкоматі.
#     - при неможливості виконання якоїсь операції - вивести повідомлення з причиною
#       (не вірний логін/пароль, недостатньо коштів на раунку, неможливо видати суму наявними купюрами тощо).

import sqlite3


con = sqlite3.connect("atm.db")
cursor = con.cursor()
ATM_DENOM = (10, 20, 50, 100, 200, 500, 1000)


def check_login(login):
    if len(login) >= 4 and login[0].isalpha():
        return True

    print("Login must have at least 4 characters and should start from letter!")
    return False


def check_password(password):
    if len(password) >= 5:
        return True

    print("Password must contain at least 5 characters")
    return False


def login():
    user_login = input("Login: ")
    user_password = input("Password: ")

    cursor.execute("""
        SELECT password
        FROM users
        WHERE login = ?
    """, (user_login,))

    password = cursor.fetchone()

    if not password:
        print("User with given login is not found!")
        return (False, user_login)

    if user_password == password[0]:
        return (True, user_login)
    else:
        print("Wrong Password!")
        return (False, user_login)


def signin():
    valid_login = False
    valid_password = False

    while not (valid_login and valid_password):
        login = input("Login: ")
        password = input("Password: ")

        valid_login = check_login(login)
        valid_password = check_password(password)

    cursor.execute("""
        SELECT login
        FROM users
        WHERE login = ?
    """, (login,))

    if cursor.fetchall():
        print("User with such login elready exists!")
        return (False, None)

    cursor.execute("""
        INSERT INTO users
        VALUES (?, ?, 'user')
    """, (login, password))

    cursor.execute(f"""
        CREATE TABLE {login}_account (
            balance numeric,
            transaction_type text,
            transaction_amount numeric
        )
    """)

    cursor.execute(f"""
        INSERT INTO {login}_account
        VALUES (0, null, null)
    """)

    con.commit()

    return (True, login)


def quit():
    print("Goodbye!")
    return ("quit", None)


def authorize():
    print("1. Log In")
    print("2. Sign In")
    print("3. Quit")
    print("")

    choice = input("Make choice: ")
    print("")

    if choice == "1":
        return login()
    elif choice == "2":
        return signin()
    elif choice == "3":
        return quit()


def check_balance(user):
    cursor.execute(f"""
        SELECT balance
        FROM {user}_account
    """)

    balance_list = cursor.fetchall()

    print(f"Current balance: {balance_list[-1][0]}")
    print("")

    return (True, user)


def top_up_balance(user):
    cursor.execute(f"""
        SELECT balance
        FROM {user}_account
    """)

    current_balance = cursor.fetchall()[-1][0]

    amount = float(
        input("Top up amount: "))
    print("")

    if amount < 0:
        print("Amount can't be negative!")
        print("")
        return (True, user)

    cursor.execute(f"""
        INSERT INTO {user}_account
        VALUES ({current_balance + amount}, 'top_up', {amount})
    """)

    con.commit()

    print(f"Your current balance is: {current_balance + amount}")

    return (True, user)


def atm_withdrawal(amount):

    cursor.execute("""
        SELECT *
        FROM atm_balance
    """)

    atm_banknotes = list(cursor.fetchone()[:-1])

    for i in range(6, -1, -1):
        cur_denom_banknote_number = amount // ATM_DENOM[i]

        if cur_denom_banknote_number <= atm_banknotes[i]:
            atm_banknotes[i] -= cur_denom_banknote_number
            amount -= cur_denom_banknote_number * ATM_DENOM[i]
        else:
            amount -= atm_banknotes[i] * ATM_DENOM[i]
            atm_banknotes[i] = 0

    if amount > 0:
        print("The ATM does not have the banknotes needed to dispense cash!")
        return False

    sql_banknotes = ' ,'.join(
        [f"'{ATM_DENOM[i]}' = {atm_banknotes[i]}" for i in range(7)])

    cursor.execute(f"""
        UPDATE atm_balance
        SET {sql_banknotes}
    """)

    con.commit()

    return True


def withdraw(user):
    cursor.execute(f"""
        SELECT balance
        FROM {user}_account
    """)

    current_balance = cursor.fetchall()[-1][0]

    cursor.execute(f"""
        SELECT *
        FROM atm_balance
    """)

    atm_balance = cursor.fetchone()
    current_atm_balance = sum(
        [ATM_DENOM[i] * atm_balance[i] for i in range(7)])

    amount = float(
        input("Withdraw amount: "))
    print("")

    if amount < 0:
        print("Amount can't be negative!")
        print("")
        return (True, user)

    if amount > current_balance:
        print("Withdraw amount exceeds your balance!")
        print("")
        return (True, user)

    if amount > current_atm_balance:
        print("Not enouth money in the ATM!")
        print("")
        return (True, user)

    if not atm_withdrawal(amount):
        return (True, user)

    cursor.execute(f"""
        INSERT INTO {user}_account
        VALUES ({current_balance - amount}, 'withdraw', {amount})
    """)

    print(f"Your current balance is: {current_balance - amount}")

    con.commit()

    return (True, user)


def check_atm_balance():
    cursor.execute(f"""
    SELECT *
    FROM atm_balance
    """)

    atm_balance = cursor.fetchone()

    print(f"Top up balance: {atm_balance[-1]}")
    print("")

    print("Withdraw balance:\n")
    print("-" * 25)
    print("|" + " Denomination " + "|" + " Number " + "|")
    print("-" * 25)
    for idx, denom in enumerate(ATM_DENOM):
        print("|" + f"{denom}".center(14) + "|" +
              f"{atm_balance[idx]}".center(8) + "|")
    print("-" * 25)
    print("")

    return (True, 'admin')


def refill_atm():
    banknote_denomination = None
    banknotes_number = None

    cursor.execute(f"""
        SELECT *
        FROM atm_balance
    """)

    atm_balance = list(cursor.fetchone())

    while True:
        banknote_denomination = int(input('Denomination: '))
        if banknote_denomination not in ATM_DENOM:
            print(
                f"Only the following denominations are available: {ATM_DENOM}")
            continue

        banknotes_number = int(input('Banknotes number: '))
        if banknotes_number < 0:
            print("The value must be positive!")
            continue

        break

    atm_balance[ATM_DENOM.index(banknote_denomination)] += banknotes_number

    cursor.execute(f"""
        UPDATE atm_balance
        SET '{str(banknote_denomination)}' = {atm_balance[ATM_DENOM.index(banknote_denomination)]}
    """, ())

    con.commit()

    check_atm_balance()

    return (True, 'admin')


def atm_collection():
    cursor.execute(f"""
        UPDATE atm_balance
        SET balance = 0
    """)
    con.commit()

    print("ATM collected!\n")
    check_atm_balance()

    return (True, 'admin')


def admin_menu():
    print("1. Check ATM balance")
    print("2. Refill ATM")
    print("3. ATM Collection")
    print("4. Quit")
    print("")

    choice = input("Enter choice: ")
    print("")

    if choice == '1':
        return check_atm_balance()
    elif choice == '2':
        return refill_atm()
    elif choice == '3':
        return atm_collection()
    elif choice == '4':
        return (False, None)
    else:
        print("Wrong choice!")
        return (True, 'admin')


def user_menu(user):
    print("1. Check balance")
    print("2. Top up balance")
    print("3. Withdraw")
    print("4. Quit")
    print("")

    choice = input("Enter choice: ")
    print("")

    if choice == '1':
        return check_balance(user)
    elif choice == '2':
        return top_up_balance(user)
    elif choice == '3':
        return withdraw(user)
    elif choice == '4':
        return (False, None)
    else:
        print("Wrong choice!")
        return (True, user)


def menu(user):
    if user == "admin":
        return admin_menu()
    else:
        return user_menu(user)


def start():
    logged = False
    user = None

    while not logged:
        logged, user = authorize()

        if logged == "quit":
            con.close()
            return

    while logged:
        logged, user = menu(user)


if __name__ == "__main__":
    start()
