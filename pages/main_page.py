import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from loguru import logger

from base.base_class import Base


class MainPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    url = "https://nk.ru"

    # === Locators ===========================================================
    catalog = "//div[contains(@class, 'toolbar wrapper')]/button"
    link_home_tech = "(//li[contains(@class, 'slidemenu__item slidemenu__item--topnav js-open-catalog-sm')]//following-sibling::li)[4]"
    link_washers = "//a[text()='Стиральные машины']"

    # === Getters =============================================================
    def get_button_catalog(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.catalog)))

    def get_link_home_tech(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.link_home_tech)))

    def get_link_washers(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.link_washers)))

    # === Actions ==============================================================
    def click_button_catalog(self):
        self.get_button_catalog().click()
        logger.info("Clicked button catalog")

    def click_link_home_tech(self):
        self.get_link_home_tech().click()
        logger.info("Clicked link home tech")

    def click_link_washers(self):
        self.get_link_washers().click()
        logger.info("Clicked link_washers")

    # === Methods ==============================================================
    def select_product(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_button_catalog()
        self.click_link_home_tech()
        self.click_link_washers()

