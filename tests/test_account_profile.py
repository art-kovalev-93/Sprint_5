from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from conftest import driver, login
from locators import Locators


def test_open_personal_cabinet_header_btn(driver):
    driver.find_element(*Locators.PERSONAL_ACCOUNT_BTN).click()
    login(driver)
    driver.find_element(*Locators.PERSONAL_ACCOUNT_BTN).click()
    WebDriverWait(driver, 3).until(expected_conditions.text_to_be_present_in_element(Locators.PROFILE_TAB, 'Профиль'))
    assert 'https://stellarburgers.nomoreparties.site/account/profile' == driver.current_url

def test_open_configurator_on_button(driver):
    driver.find_element(*Locators.PERSONAL_ACCOUNT_BTN).click()
    login(driver)
    driver.find_element(*Locators.PERSONAL_ACCOUNT_BTN).click()
    WebDriverWait(driver, 3).until(expected_conditions.text_to_be_present_in_element(Locators.PROFILE_TAB,'Профиль'))
    driver.find_element(*Locators.CONFIGURATOR_HEADER_BTN).click()
    WebDriverWait(driver, 3).until(expected_conditions.text_to_be_present_in_element(Locators.H1_MAIN_PAGE, 'Соберите бургер'))
    assert 'https://stellarburgers.nomoreparties.site/' == driver.current_url

def test_open_configurator_on_logo(driver):
    driver.find_element(*Locators.PERSONAL_ACCOUNT_BTN).click()
    login(driver)
    driver.find_element(*Locators.PERSONAL_ACCOUNT_BTN).click()
    WebDriverWait(driver, 3).until(expected_conditions.text_to_be_present_in_element(Locators.PROFILE_TAB,'Профиль'))
    driver.find_element(*Locators.LOGO_HEADER).click()
    WebDriverWait(driver, 3).until(expected_conditions.text_to_be_present_in_element(Locators.H1_MAIN_PAGE, 'Соберите бургер'))
    assert 'https://stellarburgers.nomoreparties.site/' == driver.current_url

def test_logout(driver):
    driver.find_element(*Locators.PERSONAL_ACCOUNT_BTN).click()
    login(driver)
    driver.find_element(*Locators.PERSONAL_ACCOUNT_BTN).click()
    WebDriverWait(driver, 3).until(expected_conditions.text_to_be_present_in_element(Locators.PROFILE_TAB,'Профиль'))
    driver.find_element(*Locators.LOGOUT_BTN).click()
    WebDriverWait(driver, 3).until(expected_conditions.text_to_be_present_in_element(Locators.LOGIN_H2, 'Вход'))
    assert 'https://stellarburgers.nomoreparties.site/login' == driver.current_url