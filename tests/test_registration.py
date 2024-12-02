from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from conftest import create_name, create_email, create_password, open_registration_form, login, driver
from locators import Locators


def test_registration_success(driver):
    open_registration_form(driver)
    text_fields=driver.find_elements(*Locators.REGISTRATION_TEXTFIELDS)
    text_fields[0].send_keys(create_name())
    text_fields[1].send_keys(create_email())
    text_fields[2].send_keys(create_password())
    driver.find_element(*Locators.REGISTRATION_FORM_BTN).click()
    WebDriverWait(driver,3).until(expected_conditions.text_to_be_present_in_element(Locators.LOGIN_H2,'Вход'))
    assert '/login' in driver.current_url

def test_registration_empty_name_error(driver):
    open_registration_form(driver)
    text_fields=driver.find_elements(*Locators.REGISTRATION_TEXTFIELDS)
    text_fields[1].send_keys(create_email())
    text_fields[2].send_keys(create_password())
    driver.find_element(*Locators.REGISTRATION_FORM_BTN).click()
    assert '/register' in driver.current_url

def test_registration_wrong_email_error(driver):
    open_registration_form(driver)
    text_fields=driver.find_elements(*Locators.REGISTRATION_TEXTFIELDS)
    text_fields[0].send_keys(create_name())
    text_fields[1].send_keys('wrong@email')
    text_fields[2].send_keys(create_password())
    driver.find_element(*Locators.REGISTRATION_FORM_BTN).click()
    error_message = (WebDriverWait(driver,3).until(expected_conditions.visibility_of_element_located(Locators.REGISTRATION_ERR_MSG))).text
    assert error_message == 'Такой пользователь уже существует'

def test_registration_short_password_error(driver):
    open_registration_form(driver)
    text_fields=driver.find_elements(*Locators.REGISTRATION_TEXTFIELDS)
    text_fields[0].send_keys(create_name())
    text_fields[1].send_keys(create_email())
    text_fields[2].send_keys('12345')
    driver.find_element(*Locators.REGISTRATION_FORM_BTN).click()
    error_message = (WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.REGISTRATION_ERR_MSG))).text
    assert error_message == 'Некорректный пароль'
