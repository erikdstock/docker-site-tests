import unittest
import os
import sys
from selenium import webdriver
from support.pages import HomePage, LoginPage

class AccountCreationFlow(unittest.TestCase):
    """User signs up for Docker Hub"""

    def setUp(self):
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)) + "/../bin/chromedriver")
        self.driver = webdriver.Chrome(path)
        self.driver.get("https://hub.docker.com")

    def test_too_short_password(self):
        """
        If the password is not at least 6 characters long,
        they receive a helpful error message in the password field
        """
        home_page = HomePage(self.driver)
        assert home_page.is_home_page(), "Docker tagline not found on home page"
        home_page.create_account(
            username="testuser",
            email="test@test.test",
            password="test")
        error_message = home_page.password_error_message()
        assert error_message == "Ensure this value has at least 6 characters (it has 4).", "Could not find helpful password error message - found {0}".format(error_message)

    def tearDown(self):
        self.driver.close()