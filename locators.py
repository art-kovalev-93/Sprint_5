from selenium.webdriver.common.by import By


class Locators:
    PERSONAL_ACCOUNT_BTN = (By.CSS_SELECTOR, '[href="/account"] p') #кнопка Личный кабинет в хидере
    PROFILE_TAB = (By.CSS_SELECTOR, ".text[href='/account/profile']") #вкладка Профайл в лк
    CONFIGURATOR_HEADER_BTN = (By.CSS_SELECTOR,"ul [href='/']") #кнопка Конструктор в хидере
    H1_MAIN_PAGE = (By.CSS_SELECTOR, 'h1') #заголовок h1 на главной странице
    LOGO_HEADER = (By.CSS_SELECTOR,".AppHeader_header__logo__2D0X2 [href='/']") #лого сайта в хидере
    LOGOUT_BTN = (By.CSS_SELECTOR,'nav button') #кнопка Выйти в лк
    LOGIN_H2 = (By.CSS_SELECTOR, 'h2') #заголовок на странице логина
    REGISTRATION_TEXTFIELDS = (By.CSS_SELECTOR,'.input__textfield') #поля для ввода данных в форме регистрации
    REGISTRATION_FORM_BTN = (By.CSS_SELECTOR,'form button') #кнопка Зарегистрироваться на форме регистрации
    REGISTRATION_ERR_MSG = (By.CSS_SELECTOR,'.input__error') #сообщение с ошибкой при регистрации
    PARTS_TABS = (By.CSS_SELECTOR, '.tab_tab__1SPyG .text') #список из трех вкладок
    LOGIN_BTN = (By.CSS_SELECTOR,'.mt-10 button') # кнопка Войти в аккаунт на главной странице
    REGISTRATION_LINK = (By.CSS_SELECTOR,"[href='/register']") #ссылка Зарегистрироваться на странице Логина
    LOGIN_URL = (By.CSS_SELECTOR,'[href="/login"]') #Ссылка Войти на странице регистриции и забыли пароль