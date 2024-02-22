import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from loguru import logger

from base.base_class import Base


class CardPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    product_name = ""
    product_price = ""

    # === Locators ===========================================================
    name_washer = "//h2[@class='product__name']"
    price_washer = "//span[@class='product__cost-val']"
    button_to_cart = "//div[contains(@class, 'product__button product__button_inbag')]"
    modal_button_order = "//div[@class='goods-info']//following-sibling::a[1]"
    button_cart = "//button[@class='toolbar__cart']"

    # === Getters =============================================================
    def get_name_washer(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.name_washer)))

    def get_price_washer(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_washer)))

    def get_button_to_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_to_cart)))

    def get_button_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_cart)))

    def get_modal_button_order(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.modal_button_order)))

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
        with allure.step("Put in basket"):
            self.get_current_url()
            self.check_name_washer()
            self.check_price_washer()
            self.get_screenshot()
            self.click_button_to_cart()
            time.sleep(2)
            self.click_modal_button_order()
