from selenium.webdriver.common.by import By
from conftest import driver
from helpers import login
from locators import Locators
from urls import Url



def test_login_in_acc_btn(driver):
    driver.find_element(*Locators.LOGIN_BTN).click()
    login(driver)
    assert Url.MAIN_PAGE == driver.current_url

def test_login_personal_cabinet_btn(driver):
    driver.find_element(*Locators.PERSONAL_ACCOUNT_BTN).click()
    login(driver)
    assert Url.MAIN_PAGE == driver.current_url

def test_login_on_registration_page(driver):
    driver.get(Url.REGISTRATION_PAGE)
    driver.find_element(*Locators.LOGIN_URL).click()
    login(driver)
    assert Url.MAIN_PAGE == driver.current_url

def test_login_on_forgot_password_page(driver):
    driver.get(Url.FORGOT_PSW_PAGE)
    driver.find_element(*Locators.LOGIN_URL).click()
    login(driver)
    assert Url.MAIN_PAGE == driver.current_url
