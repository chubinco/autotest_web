import pytest
from datetime import datetime
from selenium import webdriver
from loguru import logger


time_now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")


@pytest.fixture
def set_up():
    print(f"\nStart test: {time_now}")
    yield
    print(f"\nFinish test: {time_now}")


@pytest.fixture
def set_group(scope="module"):
    print(f"\nEnter system: {time_now}")
    yield
    print(f"\nExit system: {time_now}")
