from selenium.webdriver.common.by import By

class HomePageMap(object):
    """Selenium element selection strategies"""
    SEARCH_BOX = (By.CSS_SELECTOR, 'input[placeholder~="Search"]')
    LOGIN_BUTTON = (By.LINK_TEXT, 'Log In')
    CREATE_USERNAME_INPUT = (By.CSS_SELECTOR, "input[placeholder='Choose a Docker Hub ID']")
    CREATE_EMAIL_INPUT = (By.CSS_SELECTOR, "input[type=email]")
    CREATE_PASSWORD_INPUT = (By.CSS_SELECTOR, "input[type=password]")
    # CREATE_USERNAME_MESSAGE = 
    # CREATE_EMAIL_MESSAGE = 
    CREATE_PASSWORD_MESSAGE = (By.CSS_SELECTOR, "input[type=password] ~ div[class^=FancyInput__error]")

class LoginPageMap(object):
    """Selenium element selection strategies"""
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[type=submit]')
    USERNAME_INPUT = (By.CSS_SELECTOR, 'input[placeholder=Username]')
    PASSWORD_INPUT = (By.CSS_SELECTOR, 'input[type=password]')
    PASSWORD_MESSAGE = (By.CSS_SELECTOR, 'input[type=password] ~ div[class^=FancyInput__error]')
    LOGIN_ALERT = (By.CSS_SELECTOR, "form p.alert-box")

class SearchPageMap(object):
    """Selenium element selection strategies"""
    NO_RESULTS_MESSAGE = (By.CSS_SELECTOR, 'h2 span')
    SEARCH_RESULTS = (By.CSS_SELECTOR, 'div[class^=RepositoryListItem__repoName]')