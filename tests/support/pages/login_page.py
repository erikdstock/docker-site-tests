from base_page import *
from support.ui_maps import LoginPageMap
from selenium.webdriver.common.keys import Keys
import time

class LoginPage(BasePage):
    def is_login_page(self):
        """Verify we are on the login page"""
        return "Login with your Docker ID" in self.driver.page_source

    def log_in_as(self, user, password):
        """
        Fill out the login form, submit and give the page
        a chance to complete the login action
        """
        element = self.driver.find_element(*LoginPageMap.USERNAME_INPUT)
        element.send_keys(user)
        element = self.driver.find_element(*LoginPageMap.PASSWORD_INPUT)
        element.send_keys(password)
        element = self.driver.find_element(*LoginPageMap.SUBMIT_BUTTON)
        element.click()
        # Give search from time to happen since it is via react
        # TODO - look into a better way to implement this (if this were a real
        # test suite)
        time.sleep(2)

    def password_error_message(self):
        """ Password field error message"""
        element = self.driver.find_element(*LoginPageMap.PASSWORD_MESSAGE)
        return element.text

    def login_alert(self):
        """Login alert box"""
        return self.driver.find_element(*LoginPageMap.LOGIN_ALERT).text
