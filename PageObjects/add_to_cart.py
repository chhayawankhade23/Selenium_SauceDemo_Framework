from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class AddToCart:

    ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    ADD_TO_CART_ICON = (By.ID,'shopping_cart_container')
    CHECKOUT_BUTTON = (By.XPATH,'//button[@data-test="checkout"]')
    REMOVE_BUTTON = (By.ID,'remove-sauce-labs-bike-light')
    CONTINUE_SHOPPING =(By.ID,'continue-shopping')
    FIRST_NAME = (By.ID,'first-name')
    LAST_NAME = (By.ID,'last-name')
    POSTAL_CODE = (By.ID,'postal-code')
    CONTINUE_BUTTON = (By.ID,'continue')
    FINISH_BUTTON = (By.ID,'finish')

    def __init__(self,driver):
        self.driver =driver



    def click_on_add_to_cart_button(self):
        self.driver.find_element(*self.ADD_TO_CART_BUTTON).click()

    def click_on_add_to_cart_icon(self):
        self.driver.find_element(*self.ADD_TO_CART_ICON).click()
        try:
            WebDriverWait(self.driver, 10).until(EC.url_contains("cart"))
        except:
            print("URL after click:", self.driver.current_url)
            raise

    def click_on_checkout(self):
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()

    def enter_firstname(self):
        self.driver.find_element(*self.FIRST_NAME).clear()
        self.driver.find_element(*self.FIRST_NAME).send_keys("abcd")

    def enter_lastname(self):
        self.driver.find_element(*self.LAST_NAME).clear()
        self.driver.find_element(*self.LAST_NAME).send_keys("xyz")

    def enter_postalcode(self):
        self.driver.find_element(*self.POSTAL_CODE).clear()
        self.driver.find_element(*self.POSTAL_CODE).send_keys(567858)

    def click_on_continue_button(self):
        self.driver.find_element(*self.CONTINUE_BUTTON).click()

    def click_on_finish_button(self):
        self.driver.find_element(*self.FINISH_BUTTON).click()




