import time
import pytest
import allure


from PageObjects.login_page import LoginPage
from PageObjects.add_to_cart import AddToCart
from PageObjects.remove_from_cart import RemoveFromCart
from Utility.readConfiguration import ReadConfig
from Utility.logger import Loggen



class TestRemoveFromCart:
    base_url = ReadConfig.get_application_url()
    user_email = ReadConfig.get_user_email()
    user_password = ReadConfig.get_password()
    logger= Loggen.loggen()



    @pytest.mark.smoke
    def test_remove_from_cart(self,setup):
        driver = setup
        login = LoginPage(driver)
        add_to_cart = AddToCart(driver)
        remove_from_cart = RemoveFromCart(driver)

        self.logger.info("Remove from cart test started")

        with allure.step("Home page"):
            login.homepage(self.base_url)

        with allure.step("Set username"):
            login.set_username(self.user_email)

        with allure.step("Set password"):
            login.set_password(self.user_password)

        with allure.step("Login into the application"):
            login.login()
        actual_title = driver.title
        assert actual_title == "Swag Labs", "Tittle not matching"

        with allure.step("Add product to cart"):
            add_to_cart.click_on_add_to_cart_button()

        with allure.step("Open cart"):
            add_to_cart.click_on_add_to_cart_icon()

            time.sleep(3)

        with allure.step("Remove from  cart"):
            remove_from_cart.click_on_remove_button()

        with allure.step("Continue shopping"):
            remove_from_cart.click_on_continue_shopping_button()

        with allure.step("Logout from application"):
            login.logout()

        self.logger.info("Test remove from the cart is ended successfully")

