import allure
import pytest

from Utility.readConfiguration import ReadConfig
from PageObjects.login_page import LoginPage
from PageObjects.add_to_cart import AddToCart
import time
from Utility.logger import Loggen

class TestAddToCart:
    logger = Loggen.loggen()

    @pytest.mark.regression
    @pytest.mark.smoke
    def test_add_to_cart(self,setup):
            driver = setup
            login =LoginPage(driver)
            add_to_cart=AddToCart(driver)

            self.logger.info("Add to cart test started")
            with allure.step("Home page"):
                login.homepage(ReadConfig.get_application_url())
            actual_title = driver.title
            assert actual_title == "Swag Labs", "Tittle not matching"

            with allure.step("Set username"):
                login.set_username(ReadConfig.get_user_email())

            with allure.step("Set password"):
                login.set_password(ReadConfig.get_password())

            with allure.step("Login into the application"):
                login.login()
            actual_title = driver.title
            assert actual_title == "Swag Labs", "Tittle not matching"


            with allure.step("Product added to cart"):
                add_to_cart.click_on_add_to_cart_button()
            with allure.step("Cart page") :
                add_to_cart.click_on_add_to_cart_icon()
            with allure.step("Checkout the product"):
                add_to_cart.click_on_checkout()

            with allure.step("Add user information"):
                add_to_cart.enter_firstname()
                add_to_cart.enter_lastname()
                add_to_cart.enter_postalcode()
                time.sleep(2)
                add_to_cart.click_on_continue_button()
                add_to_cart.click_on_finish_button()


            with allure.step("Logout from application"):
                login.logout()

            self.logger.info("Add to cart test successfully completed")








