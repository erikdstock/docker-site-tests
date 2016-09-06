import unittest
import os
from selenium import webdriver
from support.pages import HomePage, LoginPage

class LoginFlow(unittest.TestCase):
    """User login flow from homepage"""

    def setUp(self):
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)) + "/../bin/chromedriver")
        self.driver = webdriver.Chrome(path)
        self.driver.get("https://hub.docker.com")
        home_page = HomePage(self.driver)
        assert home_page.is_home_page(), "Docker tagline not found on home page"
        home_page.click_login_button()

    def test_failed_login_no_password(self):
        """
        If the user doesn't enter a password
        Login fails with a helpful message
        around the password form field
        """
        login_page = LoginPage(self.driver)
        #Verifies that the login page loaded
        assert login_page.is_login_page(), "Couldn't verify login page"
        login_page.log_in_as("test_user", "")
        error_message = login_page.password_error_message()
        assert error_message == "This field is required.", \
            "couldn't find proper error message, found {0}".format(error_message)

    def test_failed_login_bad_password(self):
        """
        If a user enters a bad username/password combination
        they see an alert box
        """
        login_page = LoginPage(self.driver)
        #Verifies that the login page loaded
        assert login_page.is_login_page(), "Couldn't verify login page"
        login_page.log_in_as("test_user", "password123")
        login_alert = login_page.login_alert()
        assert login_alert == "Login Failed. The username or password may be incorrect.", \
            "couldn't find proper error message, found {0}".format(login_alert)


    def tearDown(self):
        self.driver.close()
