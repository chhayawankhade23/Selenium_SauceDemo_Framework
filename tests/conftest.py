import tempfile

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def setup():


    chrome_options=ChromeOptions()
    chrome_options.add_experimental_option(
        "prefs", {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.default_content_setting_values.notifications": 2,
            "profile.default_content_setting_values.popups": 2
        }
    )
    chrome_options.add_argument("--incognito")

    # chrome_options.add_argument("--disable-save-password-bubble")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-infobars")
    # chrome_options.add_argument("--disable-features=PasswordManager")
    # chrome_options.add_argument("--disable-features=AutofillServerCommunication")

    profile_path = tempfile.mkdtemp()
    chrome_options.add_argument(f"--user-data-dir={profile_path}")

    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=chrome_options
    )




    driver.maximize_window()
    driver.implicitly_wait(5)

    yield driver
    driver.quit()