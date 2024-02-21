import time

import pytest
from selenium import webdriver

from pages.basket_page import BasketPage
from pages.card_page import CardPage
from pages.main_page import MainPage
from pages.washers_page import WashersPage


def test_buy_mashing_machine():
    driver = webdriver.Chrome()

    mp = MainPage(driver)
    mp.select_product()

    wp = WashersPage(driver)
    wp.select_washing_machine()

    cp = CardPage(driver)
    cp.put_in_basket()

    bp = BasketPage(driver)
    bp.control_in_basket()
