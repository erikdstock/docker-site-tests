from support.pages.base_page import BasePage
from support.ui_maps import SearchPageMap
from selenium.webdriver.common.keys import Keys
import time

class SearchResultsPage(BasePage):
    """
    The page for displaying search results
    """

    def no_results_found(self):
        """No results are found"""
        return "We couldn't find any results for this search." in self.driver.page_source

    def search_results(self):
        """List of search results (repo names)"""
        results = self.driver.find_elements(*SearchPageMap.SEARCH_RESULTS)
        found_repos = [result.text for result in results]
        return found_repos
