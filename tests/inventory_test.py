
import allure
import pytest


from PageObjects.login_page import LoginPage
from PageObjects.inventory_page import InventoryPage
from Utility.logger import Loggen
from Utility.readConfiguration import ReadConfig

class TestInventoryPage:

    base_url = ReadConfig.get_application_url()
    user_email = ReadConfig.get_user_email()
    user_password = ReadConfig.get_password()
    logger =Loggen.loggen()

    @pytest.mark.regression
    @pytest.mark.smoke
    def test_inventory(self,setup):

        self.logger.info("Inventory test started")
        driver=setup
        login =LoginPage(driver)

        inventory= InventoryPage(driver)

        with allure.step("Home Page"):
            login.homepage(self.base_url)

        with allure.step("Set username"):
            login.set_username(self.user_email)

        with allure.step("Set password"):
            login.set_password(self.user_password)

        with allure.step("Login into the application"):
            login.login()

        actual_title = driver.title
        assert actual_title == "Swag Labs", "Tittle not matching"

        with allure.step("Verifying inventory page"):
            inventory.is_inventory_page_loaded()

        with allure.step("Inventory Page"):
            inventory.select_sort_by_name_az()

        with allure.step("Inventory Page"):
            inventory.select_sort_by_name_za()

        with allure.step("Inventory Page"):
            inventory.select_sort_by_price_lh()

        with allure.step("Inventory Page"):
            inventory.select_sort_by_price_hl()

        with allure.step("Logout from application"):
            login.logout()

        self.logger.info("Inventory test is ended successfully")