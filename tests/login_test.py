import pytest

from PageObjects.login_page import LoginPage
import allure
from Utility.readConfiguration import ReadConfig
from Utility.logger import Loggen



class TestLogin:
    base_url = ReadConfig.get_application_url()
    user_email = ReadConfig.get_user_email()
    user_password = ReadConfig.get_password()
    logger= Loggen.loggen()



    @pytest.mark.smoke
    def test_homepage(self,setup):
        self.logger.info("Home page is loading")
        driver=setup
        login = LoginPage(driver)

        with allure.step("Homepage"):
            login.homepage(self.base_url)

    @pytest.mark.regression
    @pytest.mark.smoke
    def test_login(self,setup):

        self.logger.info("Test login started")
        driver=setup
        login=LoginPage(driver)

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

        driver.close()

        self.logger.info("Test login ended")

    @pytest.mark.regression
    @pytest.mark.smoke
    def test_logout(self,setup):
        self.logger.info("Test logout started")

        driver= setup
        login = LoginPage(driver)

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

        with allure.step("Logout from application"):
            login.logout()

        self.logger.info("Test logout ended")
