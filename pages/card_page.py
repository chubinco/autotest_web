import time
import allure
from selenium.webdriver.common.by import By
from loguru import logger

from base.base_class import Base


class CardPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    product_name = ""
    product_price = ""

    # === Locators ===========================================================
    name_washer = (By.XPATH, "//h1[contains(@class, 'page-title product__title')]")
    price_washer = (By.XPATH, "//div[@class='product__currentprice']")
    button_to_cart = (By.XPATH, "//button[contains(@class, 'submit product__tocart')]")
    modal_button_order = (By.XPATH, "//div[@class='goods-info']//following-sibling::a[1]")
    button_cart = (By.XPATH, "//button[@class='toolbar__cart']")

    # === Getters =============================================================
    def get_name_washer(self):
        return self.element_clickable(self.name_washer, 30)

    def get_price_washer(self):
        return self.element_clickable(self.price_washer, 30)

    def get_button_to_cart(self):
        return self.element_clickable(self.button_to_cart, 30)

    def get_button_cart(self):
        return self.element_clickable(self.button_cart, 30)

    def get_modal_button_order(self):
        return self.element_clickable(self.modal_button_order, 30)

    # === Actions ==============================================================
    def check_name_washer(self):
        CardPage.product_name = self.get_name_washer().text.replace(" ", "")
        logger.info(f"Название: {CardPage.product_name}")
        return CardPage.product_name

    def check_price_washer(self):
        price = self.get_price_washer().text.split()
        logger.info(f"{price}")
        CardPage.product_price = int("".join([price[0], price[1]]))
        logger.info(f"Цена: {CardPage.product_price}")
        return CardPage.product_price

    def click_button_to_cart(self):
        self.get_button_to_cart().click()
        logger.info("Clicked button to cart")

    def click_button_cart(self):
        self.get_button_cart().click()
        logger.info("Clicked button_cart. Go to basket page")

    def click_modal_button_order(self):
        self.get_modal_button_order().click()
        logger.info("Clicked modal button order. Go to basket page")

    # === Methods ==============================================================
    def put_in_basket(self):
        # with allure.step("Put in basket"):
        self.get_current_url()
        self.check_name_washer()
        self.check_price_washer()
        self.get_screenshot()
        self.click_button_to_cart()
        time.sleep(1)
        self.click_button_cart()
