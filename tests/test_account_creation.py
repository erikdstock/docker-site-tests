import unittest
import os
import sys
from selenium import webdriver
from support.pages import HomePage, LoginPage

class AccountCreationFlow(unittest.TestCase):
    """User signs up for Docker Hub"""

    def setUp(self):
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)) + "/../bin/chromedriver")
        # use global chromedriver from PATH if specified
        self.driver = webdriver.Chrome() if (sys.argv[0] == "sys") else webdriver.Chrome(path)
        self.driver.get("https://hub.docker.com")

    def test_too_short_password(self):
        """
        Password must be at least 6 characters long. If it is shorter they 
        receive a helpful error message near the password field
        """

        home_page = HomePage(self.driver)
        assert home_page.is_home_page(), "Docker tagline not found on home page"

        home_page.create_account(
            username = "testuser",
            email = "test@test.test",
            password = "test")
        assert((home_page.password_error_message() == "Ensure this value has at least 6 characters (it has 4)."),
            "Could not find helpful password error message - found {0}".format(home_page.password_error_message()))

    def tearDown(self):
        self.driver.close()