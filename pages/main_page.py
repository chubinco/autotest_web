import time
import allure
from selenium.webdriver.common.by import By
from loguru import logger

from base.base_class import Base


class MainPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    url = "https://nk.ru"

    # === Locators ===========================================================
    catalog = (By.XPATH, "//div[contains(@class, 'toolbar wrapper')]/button")
    link_home_tech = (By.XPATH,
                      "(//li[contains(@class, 'slidemenu__item slidemenu__item--topnav js-open-catalog-sm')]//following-sibling::li)[4]")
    link_washers = (By.XPATH, "//a[text()='Стиральные машины']")

    # === Getters =============================================================
    def get_button_catalog(self):
        return self.element_clickable(self.catalog, 30)

    def get_link_home_tech(self):
        return self.element_clickable(self.link_home_tech, 30)

    def get_link_washers(self):
        return self.element_clickable(self.link_washers, 30)

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
        # with allure.step("Select product"):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_button_catalog()
        self.click_link_home_tech()
        self.click_link_washers()
