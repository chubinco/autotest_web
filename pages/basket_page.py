import time
import allure
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
    total__sum = ""

    # === Locators ===========================================================
    name_washer_basket = (By.XPATH, "//div[@class='title']//a")
    price_washer_basket = (By.XPATH, "//span[@class='cost_sum']//b")
    total_sum = (By.XPATH, "//span[@id='im_bag_total']")
    input_name = (By.XPATH, "//input[@name='name']")
    input_phone = (By.XPATH, "//input[@name='phone']")
    input_email = (By.XPATH, "//input[@name='email']")
    radio_button_shop = (By.XPATH, "//label[@for='radiobut_0_2']")
    radio_button_payment = (By.XPATH, "//label[@for='im_bag_card']")
    button_send_order = (By.XPATH, "//button[contains(@class, 'submit btcart__submit')]")

    # === Getters =============================================================
    def get_basket_name_washer(self):
        return self.element_clickable(self.name_washer_basket, 30)

    def get_basket_price_washer(self):
        return self.element_clickable(self.price_washer_basket, 30)

    def get_total_sum(self):
        return self.element_clickable(self.total_sum, 30)

    def get_input_name(self):
        return self.element_clickable(self.input_name, 30)

    def get_input_phone(self):
        return self.element_clickable(self.input_phone, 30)

    def get_input_email(self):
        return self.element_clickable(self.input_email, 30)

    def get_radio_button_shop(self):
        return self.element_clickable(self.radio_button_shop, 30)

    def get_radio_button_payment(self):
        return self.element_clickable(self.radio_button_payment, 30)

    def get_button_send_order(self):
        return self.element_clickable(self.button_send_order, 30)

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
        BasketPage.total__sum = int(self.get_total_sum().text.replace(" ", ""))
        logger.info(f"Общая сумма заказа: {BasketPage.total__sum}")
        return BasketPage.total__sum

    def check_name(self):
        assert BasketPage.product_name_basket == CardPage.product_name, \
            f"Name product from catalog is not equal to name in basket"
        logger.info(f"Name product from catalog is equal to name in basket")

    def check_price(self):
        assert BasketPage.product_price_basket == CardPage.product_price, \
            f"Price product from catalog is not equal to price in basket "
        logger.info(f"Price product from catalog is equal to price in basket")

    def check_order(self):
        assert BasketPage.total__sum == CardPage.product_price, \
            f"Sum of order no match with product price in catalog"
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
        # with allure.step("Control in basket"):
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
        time.sleep(1)

