from support.pages.base_page import BasePage
from support.ui_maps import HomePageMap
from selenium.webdriver.common.keys import Keys
import time

class HomePage(BasePage):
    """
    The docker hub home page (https://hub.docker.com)
    as a medium-term goal look for ways to remove sleeps from functions-
    found one bug where the 'no results found' message appears for an instant when searching from
    the search page, but the method below would not be able to detect it
    """

    def is_home_page(self):
        return "Any App, Anywhere" in self.driver.page_source

    def click_login_button(self):
        """Click Login Button"""
        element = self.driver.find_element(*HomePageMap.LOGIN_BUTTON)
        element.click()
        self._wait_for_page_load()

    def search_for(self, string):
        """Fill out the search form and submit"""
        element = self.driver.find_element(*HomePageMap.SEARCH_BOX)
        element.send_keys(string)
        element.send_keys(Keys.RETURN)
        self._wait_for_page_load()

    def create_account(self, username, email, password):
        """Fill out the create account form and submit"""
        element = self.driver.find_element(*HomePageMap.CREATE_USERNAME_INPUT)
        element.send_keys(username)
        element = self.driver.find_element(*HomePageMap.CREATE_EMAIL_INPUT)
        element.send_keys(email)
        element = self.driver.find_element(*HomePageMap.CREATE_PASSWORD_INPUT)
        element.send_keys(password)
        element.send_keys(Keys.RETURN)
        self._wait_for_page_load()

    def password_error_message(self):
        """Get password field error message"""
        return self.driver.find_element(*HomePageMap.CREATE_PASSWORD_MESSAGE).text


    def _wait_for_page_load(self):
        """
        Sleep for 3 seconds to account for actions
        that do not trigger a page reload
        """
        time.sleep(3)

