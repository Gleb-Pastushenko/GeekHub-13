# Банкомат 2.0: переробіть программу з функціонального підходу програмування на використання класів.
# Додайте шанс 10% отримати бонус на баланс при створенні нового користувача.

import sqlite3
import random


class ATM():
    ATM_DENOM = (10, 20, 50, 100, 200, 500, 1000)

    def __init__(self):
        self.logged = False
        self.user = None
        self.connection = sqlite3.connect("atm.db")
        self.cursor = self.connection.cursor()

    # Validation methods

    @staticmethod
    def check_login(login):
        if len(login) >= 4 and login[0].isalpha():
            return True

        print("Login must have at least 4 characters and should start from letter!")
        return False

    @staticmethod
    def check_password(password):
        if len(password) >= 5:
            return True

        print("Password must contain at least 5 characters")
        return False

    # Authorizing methods

    def login(self):
        user_login = input("Login: ")
        user_password = input("Password: ")

        self.cursor.execute("""
            SELECT password
            FROM users
            WHERE login = ?
        """, (user_login,))

        password = self.cursor.fetchone()

        if not password:
            print("User with given login is not found!")
            return

        if user_password == password[0]:
            self.logged = True
            self.user = user_login
        else:
            print("Wrong Password!")
            return

    def signin(self):
        valid_login = False
        valid_password = False

        while not (valid_login and valid_password):
            login = input("Login: ")
            password = input("Password: ")

            valid_login = self.check_login(login)
            valid_password = self.check_password(password)

        self.cursor.execute("""
            SELECT login
            FROM users
            WHERE login = ?
        """, (login,))

        if self.cursor.fetchall():
            print("User with such login elready exists!")
            return

        self.cursor.execute("""
            INSERT INTO users
            VALUES (?, ?, 'user')
        """, (login, password))

        self.cursor.execute(f"""
            CREATE TABLE {login}_account (
                balance numeric,
                transaction_type text,
                transaction_amount numeric
            )
        """)

        bonus = 50 if random.random() < 0.1 else 0

        self.cursor.execute(f"""
            INSERT INTO {login}_account
            VALUES ({bonus}, null, null)
        """)
        self.connection.commit()

        self.logged = True
        self.user = login

    def authorize(self):
        print("1. Log In")
        print("2. Sign In")
        print("3. Quit")
        print("")

        choice = input("Make choice: ")
        print("")

        if choice == "1":
            self.login()
        elif choice == "2":
            self.signin()
        elif choice == "3":
            self.quit()
        else:
            print("Wrong choice!")

    # Workflow methods

    def menu(self):
        if self.user == "admin":
            self.admin_menu()
        else:
            self.user_menu()

    def quit(self):
        print("Goodbye!")
        self.connection.close()
        self.logged = "quit"

    def user_menu(self):
        print("1. Check balance")
        print("2. Top up balance")
        print("3. Withdraw")
        print("4. Quit")
        print("")

        choice = input("Enter choice: ")
        print("")

        if choice == '1':
            self.check_balance()
        elif choice == '2':
            self.top_up_balance()
        elif choice == '3':
            self.withdraw()
        elif choice == '4':
            self.quit()
        else:
            print("Wrong choice!")
            return

    def admin_menu(self):
        print("1. Check ATM balance")
        print("2. Refill ATM")
        print("3. ATM Collection")
        print("4. Quit")
        print("")

        choice = input("Enter choice: ")
        print("")

        if choice == '1':
            self.check_atm_balance()
        elif choice == '2':
            self.refill_atm()
        elif choice == '3':
            self.atm_collection()
        elif choice == '4':
            self.quit()
        else:
            print("Wrong choice!")

    # Transactions methods

    def check_balance(self):
        self.cursor.execute(f"""
            SELECT balance
            FROM {self.user}_account
        """)

        balance_list = self.cursor.fetchall()

        print(f"Current balance: {balance_list[-1][0]}")
        print("")

    def top_up_balance(self):
        self.cursor.execute(f"""
            SELECT balance
            FROM {self.user}_account
        """)

        current_balance = self.cursor.fetchall()[-1][0]

        amount = float(
            input("Top up amount: "))
        print("")

        if amount < 0:
            print("Amount can't be negative!")
            print("")
            return

        self.cursor.execute(f"""
            INSERT INTO {self.user}_account
            VALUES ({current_balance + amount}, 'top_up', {amount})
        """)

        self.cursor.execute(f"""
            UPDATE atm_balance
            SET balance = ?
        """, (amount,))

        self.connection.commit()
        print(f"Your current balance is: {current_balance + amount}")

    def withdraw(self):
        self.cursor.execute(f"""
            SELECT balance
            FROM {self.user}_account
        """)

        current_balance = self.cursor.fetchall()[-1][0]

        self.cursor.execute(f"""
            SELECT *
            FROM atm_balance
        """)

        atm_balance = self.cursor.fetchone()
        current_atm_balance = sum(
            [self.ATM_DENOM[i] * atm_balance[i] for i in range(7)])

        amount = float(
            input("Withdraw amount: "))
        print("")

        if amount < 0:
            print("Amount can't be negative!")
            print("")
            return

        if amount > current_balance:
            print("Withdraw amount exceeds your balance!")
            print("")
            return

        if amount > current_atm_balance:
            print("Not enouth money in the ATM!")
            print("")
            return

        if not self.atm_withdrawal(amount):
            return

        self.cursor.execute(f"""
            INSERT INTO {self.user}_account
            VALUES ({current_balance - amount}, 'withdraw', {amount})
        """)
        self.connection.commit()
        print(f"Your current balance is: {current_balance - amount}")

    def atm_withdrawal(self, amount):
        self.cursor.execute("""
            SELECT *
            FROM atm_balance
        """)

        atm_banknotes = list(self.cursor.fetchone()[:-1])

        for i in range(6, -1, -1):
            cur_denom_banknote_number = amount // self.ATM_DENOM[i]

            if cur_denom_banknote_number <= atm_banknotes[i]:
                atm_banknotes[i] -= cur_denom_banknote_number
                amount -= cur_denom_banknote_number * self.ATM_DENOM[i]
            else:
                amount -= atm_banknotes[i] * self.ATM_DENOM[i]
                atm_banknotes[i] = 0

        if amount > 0:
            print("The ATM does not have the banknotes needed to dispense cash!")
            return False

        sql_banknotes = ' ,'.join(
            [f"'{self.ATM_DENOM[i]}' = {atm_banknotes[i]}" for i in range(7)])

        self.cursor.execute(f"""
            UPDATE atm_balance
            SET {sql_banknotes}
        """)
        self.connection.commit()

        return True

    # Admin operations methods

    def check_atm_balance(self):
        self.cursor.execute(f"""
        SELECT *
        FROM atm_balance
        """)

        atm_balance = self.cursor.fetchone()

        print(f"Top up balance: {atm_balance[-1]}")
        print("")

        print("Withdraw balance:\n")
        print("-" * 25)
        print("|" + " Denomination " + "|" + " Number " + "|")
        print("-" * 25)
        for idx, denom in enumerate(self.ATM_DENOM):
            print("|" + f"{denom}".center(14) + "|" +
                  f"{atm_balance[idx]}".center(8) + "|")
        print("-" * 25)
        print("")

    def refill_atm(self):
        banknote_denomination = None
        banknotes_number = None

        self.cursor.execute(f"""
            SELECT *
            FROM atm_balance
        """)

        atm_balance = list(self.cursor.fetchone())

        while True:
            banknote_denomination = int(input('Denomination: '))
            if banknote_denomination not in self.ATM_DENOM:
                print(
                    f"Only the following denominations are available: {self.ATM_DENOM}")
                continue

            banknotes_number = int(input('Banknotes number: '))
            if banknotes_number < 0:
                print("The value must be positive!")
                continue

            break

        atm_balance[self.ATM_DENOM.index(
            banknote_denomination)] += banknotes_number

        self.cursor.execute(f"""
            UPDATE atm_balance
            SET '{str(banknote_denomination)}' = {atm_balance[self.ATM_DENOM.index(banknote_denomination)]}
        """, ())
        self.connection.commit()

        self.check_atm_balance()

    def atm_collection(self):
        self.cursor.execute(f"""
            UPDATE atm_balance
            SET balance = 0
        """)
        self.connection.commit()

        print("ATM collected!\n")
        self.check_atm_balance()


def start(atm):
    while atm.logged is not True:
        atm.authorize()

        if atm.logged == "quit":
            return

    while atm.logged is True:
        atm.menu()


if __name__ == "__main__":
    atm = ATM()
    start(atm)
