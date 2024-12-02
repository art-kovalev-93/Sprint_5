from conftest import driver
from locators import Locators



def test_open_rolls_tab(driver):
    driver.find_element(*Locators.FILLING_TAB).click()
    driver.find_element(*Locators.ROLLS_TAB).click()
    assert driver.find_element(*Locators.ROLLS_TAB).is_displayed()

def test_open_souses_tab(driver):
    driver.find_element(*Locators.FILLING_TAB).click()
    driver.find_element(*Locators.SOUSES_TAB).click()
    assert driver.find_element(*Locators.SOUSES_TAB).is_displayed()

def test_open_filling_tab(driver):
    driver.find_element(*Locators.FILLING_TAB).click()
    assert driver.find_element(*Locators.FILLING_TAB).is_displayed()