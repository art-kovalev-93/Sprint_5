import pytest
from selenium import webdriver
from urls import Url



@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(Url.MAIN_PAGE)
    yield driver
    driver.quit()
