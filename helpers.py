import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators



def login(driver):
    login_data = {'email': 'test_user_007@ya.ru', 'password': 'Qwerty12345'}
    text_fields = driver.find_elements(*Locators.REGISTRATION_TEXTFIELDS)
    text_fields[0].send_keys(login_data.get('email'))
    text_fields[1].send_keys(login_data.get('password'))
    driver.find_element(By.CSS_SELECTOR, 'form button').click()
    WebDriverWait(driver, 3).until(
        expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, 'h1'), 'Соберите бургер'))
    return driver

def create_name():
    names = ['Ann', 'Kate', 'Bob', 'John']
    name = random.choice(names)
    return name

def create_email():
    second_name=['Smith', 'Konnar', 'Wick', 'Stark']
    domens=['ya.ru','mail.ru','gmail.com']
    email = create_name()+'_'+random.choice(second_name)+'_'+ str(random.choice(range(1960,2010)))+'@'+random.choice(domens)
    return email

def create_password():
    symbols = ['A','b','L','#','1','8','5','K','0','O','!','J','s']
    password=''
    for i in range(1,13):
        password+=random.choice(symbols)
    return password

def open_registration_form(driver):
    driver.find_element(*Locators.LOGIN_BTN).click()
    driver.find_element(*Locators.REGISTRATION_LINK).click()
    return driver