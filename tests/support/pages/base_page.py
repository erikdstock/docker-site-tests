
class BasePage(object):
    """
    Abstract page logic
    """

    def __init__(self, driver):
        self.driver = driver
