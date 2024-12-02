from selenium.webdriver.common.by import By
from conftest import driver, login



def test_login_in_acc_btn(driver):
    driver.find_element(By.CSS_SELECTOR,'main button').click()
    login(driver)
    assert 'https://stellarburgers.nomoreparties.site/' == driver.current_url

def test_login_personal_cabinet_btn(driver):
    driver.find_element(By.CSS_SELECTOR,'[href="/account"] p').click()
    login(driver)
    assert 'https://stellarburgers.nomoreparties.site/' == driver.current_url

def test_login_on_registration_page(driver):
    driver.get('https://stellarburgers.nomoreparties.site/register')
    driver.find_element(By.CSS_SELECTOR,'[href="/login"]').click()
    login(driver)
    assert 'https://stellarburgers.nomoreparties.site/' == driver.current_url

def test_login_on_forgot_password_page(driver):
    driver.get('https://stellarburgers.nomoreparties.site/forgot-password')
    driver.find_element(By.CSS_SELECTOR,'[href="/login"]').click()
    login(driver)
    assert 'https://stellarburgers.nomoreparties.site/' == driver.current_url
