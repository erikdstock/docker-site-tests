import unittest
import os
import sys
from selenium import webdriver
from support.pages import HomePage, SearchResultsPage

class RepoSearchFlow(unittest.TestCase):
    """Searching provides relevant results"""

    def setUp(self):
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)) + "/../bin/chromedriver")
        self.driver = webdriver.Chrome(path)
        self.driver.get("https://hub.docker.com")

    def test_search_flow(self):
        """
        When the user searches, they see relevant results
        """

        home_page = HomePage(self.driver)
        assert home_page.is_home_page(), "Docker tagline not found on home page"
        #Search for something that will exist
        home_page.search_for("ubuntu trusty")
        # home_page.search_for("aaaaaaaaazzzzzzzz") # 0 results
        search_results_page = SearchResultsPage(self.driver)
        #Verifies that the relevant result is found
        search_results = search_results_page.search_results()
        assert "pacur/ubuntu-trusty" in search_results, "Did not find relevant repo in {0}".format(search_results)

    def test_no_results_search_flow(self):
        """
        When a search doesn't find anything
        the user sees a helpful error message.
        """

        #Load the main page. In this case the home page of Python.org.
        home_page = HomePage(self.driver)
        #Checks if the word "Python" is in title
        assert home_page.is_home_page(), "Docker tagline not found on home page"
        #Search for something that will not exist
        home_page.search_for("aaaaaaaaazzzzzzzz") # 0 results
        search_results_page = SearchResultsPage(self.driver)
        #Verify a helpful message and no results
        assert search_results_page.no_results_found(), "Couldn't find no results message"
        assert len(search_results_page.search_results()) == 0, "search found something"


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()