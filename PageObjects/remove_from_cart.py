from selenium.webdriver.common.by import By

from PageObjects.add_to_cart import AddToCart
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RemoveFromCart(AddToCart):

    REMOVE_BUTTON = (By.ID, 'remove-sauce-labs-bike-light')
    CONTINUE_SHOPPING = (By.ID, 'continue-shopping')

    def __init__(self, driver):
        super().__init__(driver)

    def click_on_remove_button(self):
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.REMOVE_BUTTON)).click()

    def click_on_continue_shopping_button(self):
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.CONTINUE_SHOPPING)).click()


