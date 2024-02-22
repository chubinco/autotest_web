import time
from datetime import datetime
from pathlib import Path
import allure
import pytest
from loguru import logger
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.basket_page import BasketPage
from pages.card_page import CardPage
from pages.main_page import MainPage
from pages.washers_page import WashersPage


# @allure.description("Test buy mashing machine")
def test_buy_mashing_machine():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    # driver = webdriver.Chrome()
    root = Path(__file__).resolve().parent.parent
    time_now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    logger.add(root.joinpath('logs', f'file_{time_now}.log'), rotation="1 week")

    mp = MainPage(driver)
    mp.select_product()

    wp = WashersPage(driver)
    wp.select_washing_machine()

    cp = CardPage(driver)
    cp.put_in_basket()

    bp = BasketPage(driver)
    bp.control_in_basket()
