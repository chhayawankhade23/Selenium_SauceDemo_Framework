
from selenium.common import NoAlertPresentException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    USERNAME_TEXT = (By.ID,"user-name")
    PASSWORD_TEXT = (By.ID,"password")
    LOGIN_BUTTON =(By.ID,"login-button")
    MENU_BUTTON = (By.ID,"react-burger-menu-btn")
    LOGOUT_BUTTON =(By.XPATH,"//a[@id='logout_sidebar_link']")



    def __init__(self,driver):
        self.driver=driver

    def homepage(self,base_url):
        self.driver.get(base_url)

    def set_username(self,username):
        self.driver.find_element(*self.USERNAME_TEXT).clear()
        self.driver.find_element(*self.USERNAME_TEXT).send_keys(username)

    def set_password(self,password):
        self.driver.find_element(*self.PASSWORD_TEXT).clear()
        self.driver.find_element(*self.PASSWORD_TEXT).send_keys(password)

    def login(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def logout(self):
        act=ActionChains(self.driver)
        self.driver.find_element(*self.MENU_BUTTON).click()
        logout_element=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.LOGOUT_BUTTON))
        act.move_to_element(logout_element).click().perform()