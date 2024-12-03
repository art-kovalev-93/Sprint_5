from conftest import driver
from locators import Locators



def test_open_rolls_tab(driver):
    driver.find_elements(*Locators.PARTS_TABS)[2].click()
    driver.find_elements(*Locators.PARTS_TABS)[0].click()
    assert driver.find_elements(*Locators.PARTS_TABS)[0].is_displayed()

def test_open_souses_tab(driver):
    driver.find_elements(*Locators.PARTS_TABS)[2].click()
    driver.find_elements(*Locators.PARTS_TABS)[1].click()
    assert  driver.find_elements(*Locators.PARTS_TABS)[1].is_displayed()

def test_open_filling_tab(driver):
    driver.find_elements(*Locators.PARTS_TABS)[2].click()
    assert driver.find_elements(*Locators.PARTS_TABS)[2].is_displayed()