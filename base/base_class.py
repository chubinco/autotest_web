import pathlib
from datetime import datetime
from loguru import logger
from pathlib import Path

from selenium.webdriver import ActionChains, Keys


class Base:
    """ Base class for all test cases """

    def __init__(self, driver):
        self.driver = driver


    def get_current_url(self):
        """ Method get current url """
        get_url = self.driver.current_url
        logger.info(f"Current url: {get_url}")

    def compare_words(self, way, result):
        """ Method compare text with result """
        value_text = way.text
        assert value_text == result
        logger.info(f"Text so match: {value_text}")

    def get_screenshot(self):
        """ Method screenshot """
        self.driver.implicitly_wait(10)
        root = Path(__file__).resolve().parent.parent
        time_now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        self.driver.save_screenshot(root.joinpath('screen', f'{time_now}.png'))
        logger.info(f"Screenshot ready {f'{time_now}.png'}")

    def assert_url(self, result):
        """ Method compare url with result """
        get_url = self.driver.current_url
        assert get_url == result
        logger.info(f"URL so match: {get_url}")

    def hover_element(self, get_element):
        """ Method hover element by mouse """
        ActionChains(self.driver).move_to_element(get_element).perform()
        logger.info(f"Hover element")


