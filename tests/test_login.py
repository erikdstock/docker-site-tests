import unittest
import os
import sys
from selenium import webdriver
from support.pages import HomePage, LoginPage

class LoginFlow(unittest.TestCase):
    """User login flow from homepage"""

    def setUp(self):
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)) + "/../bin/chromedriver")
        # use global chromedriver from PATH if specified
        self.driver = webdriver.Chrome() if (sys.argv[0] == "sys") else webdriver.Chrome(path)
        self.driver.get("https://hub.docker.com")

    def test_failed_login_no_password(self):
        """
        Login fails with no password & a helpful message appears
        """

        home_page = HomePage(self.driver)
        assert home_page.is_home_page(), "Docker tagline not found on home page"
        home_page.click_login_button()

        #Verifies that the login page loaded
        login_page = LoginPage(self.driver)
        assert login_page.is_login_page(), "Couldn't verify login page"
        login_page.log_in_as("test_user", "")
        assert(login_page.password_error_message() == "This field is required.",
            "couldn't find proper error message, found {0}".format(login_page.password_error_message()))

    def tearDown(self):
        self.driver.close()