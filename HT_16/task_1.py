# Автоматизувати процес замовлення робота за допомогою Selenium
# 1. Отримайте та прочитайте дані з "https://robotsparebinindustries.com/orders.csv".
#    Увага! Файл має бути прочитаний з сервера кожного разу при запускі скрипта, не зберігайте файл локально.
# 2. Зайдіть на сайт "https://robotsparebinindustries.com/"
# 3. Перейдіть у вкладку "Order your robot"
# 4. Для кожного замовлення з файлу реалізуйте наступне:
#     - закрийте pop-up, якщо він з'явився. Підказка: не кожна кнопка його закриває.
#     - оберіть/заповніть відповідні поля для замовлення
#     - натисніть кнопку Preview та збережіть зображення отриманого робота.
#       Увага! Зберігати треба тільки зображення робота, а не всієї сторінки сайту.
#     - натисніть кнопку Order та збережіть номер чеку. Увага! Інколи сервер тупить і видає помилку,
#       але повторне натискання кнопки частіше всього вирішує проблему. Дослідіть цей кейс.
#     - переіменуйте отримане зображення у формат <номер чеку>_robot (напр. 123456_robot.jpg).
#       Покладіть зображення в директорію output (яка має створюватися/очищатися під час запуску скрипта).
#     - замовте наступного робота (шляхом натискання відповідної кнопки)

# ** Додаткове завдання (необов'язково)
#     - окрім збереження номеру чеку отримайте також HTML-код всього чеку
#     - збережіть отриманий код в PDF файл
#     - додайте до цього файлу отримане зображення робота (бажано на одній сторінці, але не принципово)
#     - збережіть отриманий PDF файл у форматі <номер чеку>_robot в директорію output.
#       Окремо зображення робота зберігати не потрібно. Тобто замість зображень у вас будуть pdf файли які містять зображення з чеком.

import csv
from time import sleep

import requests
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OrderRobot:
    ORDERS_LIST_URL = "https://robotsparebinindustries.com/orders.csv"
    ORDER_SITE_URL = "https://robotsparebinindustries.com/"

    WAIT_DELAY = 5
    CLICK_DELAY = 2

    DEFAULT_SERVICE_ARGS = [
        "--no-sandbox",
        "--disable-application-cache",
        "--disable-web-security",
        "--allow-running-insecure-content",
        "--hide-scrollbars",
        "--disable-infobars",
        "--disable-notifications",
        "--disable-dev-shm-usage",
        "--disable-gpu",
        "--disable-setuid-sandbox",
    ]

    def __init__(self):
        chrome_options = ChromeOptions()

        for argument in self.DEFAULT_SERVICE_ARGS:
            chrome_options.add_argument(argument)

        chrome_options.add_experimental_option("excludeSwtitches", ["enable-automation"])
        chrome_options.add_experimental_option(
            "prefs",
            {
                "profile.default_content_setting_values.notifications": 2,
                "profile.default_content_settings.popups": 0,
            }
        )

        self._driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def _open_order_page(self):
        self._driver.get(self.ORDER_SITE_URL)
        self._wait_element((By.LINK_TEXT, "Order your robot!")).click()
        self._wait_element((By.CLASS_NAME, "btn-dark")).click()

    def _get_orders_list(self):    
        try:
            self.orders_list = requests.get(self.ORDERS_LIST_URL).text.split("\n")
            self.orders_list = list(csv.DictReader(self.orders_list[1:], fieldnames=self.orders_list[0].split(",")))
        except Exception:
            self.orders_list = None

    def _wait_element(self, select_by):
        wait_driver = WebDriverWait(self._driver, self.WAIT_DELAY)
        return wait_driver.until(EC.presence_of_element_located(select_by))
    
    def _find_by_id(self, id):
        return self._driver.find_element(By.ID, id)
    
    def _find_by_selector(self, selector):
        return self._driver.find_element(By.CSS_SELECTOR, selector)
    
    def _fill_order_form(self, order):
        # Get form fields
        head__selector = self._find_by_id("head")
        body__radio_btn = self._find_by_id(f"id-body-{order['Body']}")        
        legs__num_input = self._find_by_selector("input[type='number']")
        address__txt_input = self._find_by_id("address")

        # Fill form fields
        Select(head__selector).select_by_value(order['Head'])
        body__radio_btn.click()
        legs__num_input.send_keys(order['Legs'])
        address__txt_input.send_keys(order['Address'])
        sleep(10)

    def _make_order(self, order):
        self._fill_order_form(order)

    
    def _start_ordering(self):
        self._make_order(self.orders_list[0])  #Temp

    def start(self):
        self._get_orders_list()
        self._open_order_page()
        self._start_ordering()


if __name__ == "__main__":
    order_robot = OrderRobot()

    order_robot.start()













driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))