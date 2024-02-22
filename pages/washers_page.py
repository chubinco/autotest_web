import time
import allure
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from loguru import logger

from base.base_class import Base


class WashersPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # === Locators ===========================================================
    price_down = "(//div[contains(@class, 'filter__slider-bar')])[1]/span[1]"
    price_up = "(//div[contains(@class, 'filter__slider-bar')])[1]/span[2]"
    manufacturer = "(//div[contains(@class, 'filter__section filter__section--collapse')])[1]"
    made_samsung = "//input[@name='f[b][5]']//following-sibling::span"
    made_centlek = "//input[@name='f[b][804]']"
    type_loading = "(//div[contains(@class, 'filter__section filter__section--collapse')])[2]"
    loading_front = "//input[@name='f[123][фронтальная]']//following-sibling::span"
    button_submit = "//button[contains(@class, 'submit filter__submit')]"
    card_washer = "(//article[@class='product-card'])[1]//a"

    button_add_to_cart = "(//button[@data-id='129367'])[2]"
    button_cart = "//button[@class='toolbar__cart']"

    # === Getters =============================================================
    def get_price_down(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_down)))

    def get_price_up(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_up)))

    def get_manufacturer(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.manufacturer)))

    def get_made_samsung(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.made_samsung)))

    def get_made_centlek(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.made_centlek)))

    def get_type_loading(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.type_loading)))

    def get_loading_front(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.loading_front)))

    def get_button_submit(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_submit)))

    def get_button_add_to_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_add_to_cart)))

    def get_button_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_cart)))

    def get_card_washer(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.card_washer)))

    # === Actions ==============================================================
    def move_price_down(self):
        action = ActionChains(self.driver)
        action.click_and_hold(self.get_price_down()).move_by_offset(40, 0).release().perform()
        logger.info("Moved priceDown -> up")

    def move_price_up(self):
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(self.get_price_up(), -88, 0).release().perform()
        logger.info("Moved priceUp -> down")

    def click_filter_manufacturer(self):
        self.get_manufacturer().click()
        logger.info("Clicked filter manufacturer")

    def click_made_samsung(self):
        self.hover_element(self.get_made_centlek())
        self.hover_element(self.get_made_samsung())
        self.get_made_samsung().click()
        logger.info("Clicked manufacturer - Samsung")

    def click_filter_type_loading(self):
        self.get_type_loading().click()
        logger.info("Clicked filter type_loading")

    def click_type_loading_front(self):
        self.get_loading_front().click()
        logger.info("Clicked type_loading - front")

    def click_button_submit(self):
        self.hover_element(self.get_button_submit())
        self.get_button_submit().click()
        logger.info("Clicked button submit")

    def click_card_washer(self):
        self.get_card_washer().click()
        logger.info("Clicked card washing machine")

    def click_button_add_to_cart(self):
        self.get_button_add_to_cart().click()
        logger.info("Clicked button add to cart")

    def click_button_cart(self):
        self.get_button_cart().click()
        logger.info("Clicked button cart. Go to basket page")

    # === Methods ==============================================================
    def select_washing_machine(self):
        with allure.step("Select washing machine"):
            self.get_current_url()
            self.move_price_down()
            self.move_price_up()
            time.sleep(1)
            self.click_filter_manufacturer()
            time.sleep(1)
            self.click_made_samsung()
            time.sleep(2)
            self.click_filter_type_loading()
            time.sleep(1)
            self.click_type_loading_front()
            time.sleep(1)
            self.click_button_submit()
            time.sleep(5)
            self.get_screenshot()
            self.click_card_washer()
            time.sleep(1)
