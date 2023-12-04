# 2. Створіть програму для отримання курсу валют за певний період.
# - отримати від користувача дату (це може бути як один день так і інтервал - початкова і кінцева дати,
#   продумайте механізм реалізації) і назву валюти
# - вивести курс по відношенню до гривні на момент вказаної дати (або за кожен день у вказаному інтервалі)
# - не забудьте перевірку на валідність введених даних

from datetime import datetime
from dateutil.relativedelta import relativedelta
import requests


# Output funcitons

def show_day_rate(date, date_str):
    REQUEST_URL = "https://api.privatbank.ua/p24api/exchange_rates?date="

    if not check_range(date):
        return

    response = requests.get(REQUEST_URL + date_str)
    rates = filter(
        lambda rate: rate["currency"] in ("USD", "EUR", "PLN"),
        response.json()["exchangeRate"]
    )

    for rate in rates:
        print(f"{rate['currency']}:")
        print(f"sale: {rate['saleRate']}")
        print(f"purchase: {rate['purchaseRate']}")
        print("")


def show_period_rates(start_date, end_date):
    for days in range((end_date[0] - start_date[0]).days + 1):
        cur_date = start_date[0] + relativedelta(days=days)
        cur_date_str = cur_date.strftime("%d.%m.%Y")
        print(cur_date_str)

        show_day_rate(cur_date, cur_date_str)


def rates_for_date():
    show_day_rate(*input_date())

    return True


def rates_for_period():
    start_date = None
    end_date = None

    while not (start_date and end_date):
        if not start_date:
            start_date = input_date("start")

        if not check_range(start_date[0]):
            start_date = None

        if start_date:
            end_date = input_date("end")

            if not check_range(end_date[0]):
                end_date = None

    show_period_rates(start_date, end_date)
    return True


# Input/validate functions

def check_range(date):
    min_date_range_timestamp = (
        datetime.now() - relativedelta(years=4)).timestamp()
    max_date_range_timestamp = datetime.now().timestamp()

    if date.timestamp() < min_date_range_timestamp or date.timestamp() > max_date_range_timestamp:
        print("Date is out of range! Only four last years are available!")
        return False

    return True


def input_date(date_name=""):
    date = None

    while not date:
        input_date = input(f"Enter {date_name} date in format dd.mm.yyyy: ")
        print("")
        format = "%d.%m.%Y"

        try:
            date = datetime.strptime(input_date, format)
            return (date, input_date)
        except Exception as error:
            print(error)
            print("")


def quit():
    return False


def start():
    show_menu = True

    while show_menu:
        print("Note that exchange rates are available for the last four years!")
        print("")
        print("1. Rates for date")
        print("2. Rates for period")
        print("3. Quit")
        print("")

        choice = input("Enter choice: ")

        if choice == "1":
            show_menu = rates_for_date()
        elif choice == "2":
            show_menu = rates_for_period()
        elif choice == "3":
            show_menu = quit()
        else:
            print("Wrong choice!")


if __name__ == "__main__":
    start()
