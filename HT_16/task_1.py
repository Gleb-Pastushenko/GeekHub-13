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
from pathlib import Path
from shutil import rmtree

import requests
import selenium
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from xhtml2pdf import pisa


class OrderRobot:
    OUTPUT_PATH = Path('output')

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
        self._driver.maximize_window()

    def _create_output_dir(self):
        if self.OUTPUT_PATH.exists():
            rmtree(self.OUTPUT_PATH)

        self.OUTPUT_PATH.mkdir(parents=True, exist_ok=True)

    def _open_order_page(self):
        self._driver.get(self.ORDER_SITE_URL)
        self._wait_element((By.LINK_TEXT, "Order your robot!")).click()

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

    def _get_preview_images_urls(self):
        # Click preview button    
        self._wait_element((By.ID, "preview"))   
        self._driver.execute_script("preview.click()") 

        # Get images urls
        preview_images = self._wait_element((By.ID, "robot-preview-image"))
        self._driver.execute_script("window['robot-preview-image'].scrollIntoView()")

        return [img.get_attribute("src") for img in preview_images.find_elements(By.TAG_NAME, 'img')]        
    
    def _get_receipt(self):
        receipt = None
        # Click "ORDER" until get the receipt
        while receipt is None:
            try:
                self._wait_element((By.ID, "order"))   
                self._driver.execute_script("order.click()")
                receipt = self._wait_element((By.ID, "receipt"))
            except selenium.common.exceptions.TimeoutException as error:
                receipt = None
        
        return receipt
        
    def _save_preview(self, images_container, image_file_path):

        self._driver.execute_script("""
            window.document.documentElement.style = 'scroll-behavior: auto !important';
            window['robot-preview-image'].scrollIntoView({behavior: 'instant'});                        
        """)
           
        images_container.screenshot(str(image_file_path))

    def _save_pdf(self, receipt, receipt_number, pdf_file_path):
        image_file_path = self.OUTPUT_PATH.joinpath(f"{receipt_number}_robot.png")
        html_content = (
            f"<table>"
            f"<td style='margin-right: 20px'>{receipt.get_attribute('outerHTML')}</td>"
            f"<td><img src='{image_file_path}' /></td>"
            f"</table>"
        )

        with open(pdf_file_path, "w+b") as pdf_file:
            pisa.CreatePDF(html_content, pdf_file)

    def _make_order(self, order):
        self._wait_element((By.CLASS_NAME, "btn-dark")).click()

        # Fill the order form
        self._fill_order_form(order)

        # Get order details
        receipt = self._get_receipt()
        receipt_number = receipt.find_element(By.CSS_SELECTOR, "p.badge-success")
        receipt_number = receipt_number.text.split("-")[-1]
        images_container = self._wait_element((By.ID, "robot-preview-image"))
        
        # Save order details
        image_file_path = self.OUTPUT_PATH.joinpath(f"{receipt_number}_robot.png")  # _robot.jpg -> _robot.png
        pdf_file_path = self.OUTPUT_PATH.joinpath(f"{receipt_number}_robot.pdf")        
        self._save_preview(images_container, image_file_path)
        self._save_pdf(receipt, receipt_number, pdf_file_path)
        
    def _next_order(self):
        self._wait_element((By.ID, "order-another"))
        self._driver.execute_script("window['order-another'].click()")
    
    def _start_ordering(self):
        for order in self.orders_list:
            self._make_order(order)
            self._next_order()

    def start(self):
        self._create_output_dir()
        self._get_orders_list()
        self._open_order_page()
        self._start_ordering()
        self._driver.close()


if __name__ == "__main__":
    order_robot = OrderRobot()
    order_robot.start()
