import time
import allure
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from loguru import logger

from base.base_class import Base


class WashersPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # === Locators ===========================================================
    price_down = (By.XPATH, "(//div[contains(@class, 'filter__slider-bar')])[1]/span[1]")
    price_up = (By.XPATH, "(//div[contains(@class, 'filter__slider-bar')])[1]/span[2]")
    manufacturer = (By.XPATH, "(//div[contains(@class, 'filter__section filter__section--collapse')])[1]")
    made_samsung = (By.XPATH, "//input[@name='f[b][5]']//following-sibling::span")
    made_centlek = (By.XPATH, "//input[@name='f[b][804]']")
    type_loading = (By.XPATH, "(//div[contains(@class, 'filter__section filter__section--collapse')])[2]")
    loading_front = (By.XPATH, "//input[@name='f[123][фронтальная]']//following-sibling::span")
    button_submit = (By.XPATH, "//button[contains(@class, 'submit filter__submit')]")
    card_washer = (By.XPATH, "(//article[@class='product-card'])[1]//a")

    button_add_to_cart = (By.XPATH, "(//button[@data-id='129367'])[2]")
    button_cart = (By.XPATH, "//button[@class='toolbar__cart']")

    # === Getters =============================================================
    def get_price_down(self):
        return self.element_clickable(self.price_down, 30)

    def get_price_up(self):
        return self.element_clickable(self.price_up, 30)

    def get_manufacturer(self):
        return self.element_clickable(self.manufacturer, 30)

    def get_made_samsung(self):
        return self.element_clickable(self.made_samsung, 30)

    def get_made_centlek(self):
        return self.element_clickable(self.made_centlek, 30)

    def get_type_loading(self):
        return self.element_clickable(self.type_loading, 30)

    def get_loading_front(self):
        return self.element_clickable(self.loading_front, 30)

    def get_button_submit(self):
        return self.element_clickable(self.button_submit, 30)

    def get_button_add_to_cart(self):
        return self.element_clickable(self.button_add_to_cart, 30)

    def get_button_cart(self):
        return self.element_clickable(self.button_cart, 30)

    def get_card_washer(self):
        return self.element_clickable(self.card_washer, 30)

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
        # with allure.step("Select washing machine"):
        self.get_current_url()
        self.move_price_down()
        self.move_price_up()
        time.sleep(1)
        self.click_filter_manufacturer()
        time.sleep(1)
        self.click_made_samsung()
        time.sleep(1)
        self.click_filter_type_loading()
        time.sleep(1)
        self.click_type_loading_front()
        time.sleep(1)
        self.click_button_submit()
        time.sleep(1)
        self.get_screenshot()
        self.click_card_washer()
        time.sleep(1)
