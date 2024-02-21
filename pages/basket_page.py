import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from loguru import logger

from base.base_class import Base
from pages.card_page import CardPage


class BasketPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    product_name_basket = ""
    product_price_basket = ""
    total_sum = ""

    # === Locators ===========================================================
    name_washer_basket = "//div[@class='title']//a"
    price_washer_basket = "//span[@class='cost_sum']//b"
    total_sum = "//span[@id='im_bag_total']"
    input_name = "//input[@name='name']"
    input_phone = "//input[@name='phone']"
    input_email = "//input[@name='email']"
    radio_button_shop = "//label[@for='radiobut_0_2']"
    radio_button_payment = "//label[@for='im_bag_card']"
    button_send_order = "//button[contains(@class, 'submit btcart__submit')]"

    # === Getters =============================================================
    def get_basket_name_washer(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.name_washer_basket)))

    def get_basket_price_washer(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_washer_basket)))

    def get_total_sum(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.total_sum)))

    def get_input_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_name)))

    def get_input_phone(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_phone)))

    def get_input_email(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_email)))

    def get_radio_button_shop(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.radio_button_shop)))

    def get_radio_button_payment(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.radio_button_payment)))

    def get_button_send_order(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_send_order)))

    # === Actions ==============================================================
    def check_basket_name_washer(self):
        BasketPage.product_name_basket = self.get_basket_name_washer().text.replace(" ", "")
        logger.info(f"Название: {BasketPage.product_name_basket}")
        return BasketPage.product_name_basket

    def check_basket_price_washer(self):
        BasketPage.product_price_basket = int(self.get_basket_price_washer().text.replace(" ", ""))
        logger.info(f"Цена: {BasketPage.product_price_basket}")
        return BasketPage.product_price_basket

    def check_total_sum(self):
        BasketPage.total_sum = int(self.get_total_sum().text.replace(" ", ""))
        logger.info(f"Общая сумма заказа: {BasketPage.total_sum}")
        return BasketPage.total_sum

    def check_name(self):
        assert BasketPage.product_name_basket == CardPage.product_name, f"Name product from catalog is not equal to name in basket"
        logger.info(f"Name product from catalog is equal to name in basket")

    def check_price(self):
        assert BasketPage.product_price_basket == CardPage.product_price, f"Price product from catalog is not equal to price in basket "
        logger.info(f"Price product from catalog is equal to price in basket")

    def check_order(self):
        assert BasketPage.total_sum == CardPage.product_price, f"Sum of order no match with product price in catalog"
        logger.info(f"Sum of order match with product price in catalog")

    def input__name(self, name):
        self.get_input_name().send_keys(name)
        logger.info(f"Input first name is {name}")

    def input__phone(self, phone):
        self.get_input_phone().send_keys(phone)
        logger.info(f"Input phone is {phone}")

    def input__email(self, email):
        self.get_input_email().send_keys(email)
        logger.info(f"Input email is {email}")

    def how_delivery_order(self):
        self.get_radio_button_shop().click()
        logger.info(f"Method delivery order is shop")

    def how_payment_order(self):
        self.hover_element(self.get_radio_button_payment())
        self.get_radio_button_payment().click()
        logger.info(f"Method payment order by bank card")

    # === Methods ==============================================================

    def control_in_basket(self):
        self.get_current_url()
        self.check_basket_name_washer()
        self.check_basket_price_washer()
        self.check_total_sum()
        self.check_name()
        self.check_price()
        self.check_order()
        time.sleep(1)
        self.input__name("Михалыч")
        time.sleep(1)
        self.input__phone("4212333451")
        time.sleep(1)
        self.input__email("michael@samoha.com")
        time.sleep(1)
        self.how_delivery_order()
        time.sleep(1)
        self.how_payment_order()
        time.sleep(1)
        self.get_screenshot()
        time.sleep(3)
