from selenium.webdriver.common.by import By


class Locators:
    PERSONAL_ACCOUNT_BTN = (By.CSS_SELECTOR, '[href="/account"] p') #кнопка Личный кабинет в хидере
    PROFILE_TAB = (By.CSS_SELECTOR, ".text[href='/account/profile']") #вкладка Профайл в лк
    CONFIGURATOR_HEADER_BTN = (By.CSS_SELECTOR,"ul [href='/']") #кнопка Конструктор в хидере
    H1_MAIN_PAGE = (By.CSS_SELECTOR, 'h1') #заголовок h1 на главной странице
    LOGO_HEADER = (By.CSS_SELECTOR,".AppHeader_header__logo__2D0X2 [href='/']") #лого сайта в хидере
    LOGOUT_BTN = (By.XPATH,'//*[@id="root"]/div/main/div/nav/ul/li[3]/button') #кнопка Выйти в лк
    LOGIN_H2 = (By.CSS_SELECTOR, 'h2') #заголовок на странице логина
    REGISTRATION_TEXTFIELDS = (By.CSS_SELECTOR,'.input__textfield') #поля для ввода данных в форме регистрации
    REGISTRATION_FORM_BTN = (By.CSS_SELECTOR,'form button') #кнопка Зарегистрироваться на форме регистрации
    REGISTRATION_ERR_MSG = (By.CSS_SELECTOR,'.input__error') #сообщение с ошибкой при регистрации
    ROLLS_TAB = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[1]/span') #вкладка Булки
    SOUSES_TAB = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[2]/span') #вкладка Соусы
    FILLING_TAB = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[3]/span') #вкладка Начинки