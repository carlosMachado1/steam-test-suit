from typing import List
from src.pages.base_page import BasePage
from src.locators.search_locator import SearchGameLocator
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.expected_conditions import AnyDriver


class HomePage(BasePage):
    def __init__(self, driver: AnyDriver) -> None:
        super().__init__(driver)
        driver.get("https://store.steampowered.com/?")

    def fill_search_field(self, game: str) -> None:
        """Fill the search field with game parameter"""
        self.enter_text(SearchGameLocator.search_field, game)

    def perform_search(self) -> None:
        """Perform a click to start the search"""
        self.click(SearchGameLocator.search_button)

    def get_all_filters(self) -> List[WebElement]:
        """Return all filters applied to the page"""
        filters = []
        filters_tag = self.find_elements(SearchGameLocator.search_filters)
        return filters

    def get_results(self) -> str:
        return self.find_element(SearchGameLocator.search_result).text

    def change_language(self, language: str) -> bool:
        """Perform an change language"""
        self.click(SearchGameLocator.show_languages_button)
        languages = self.find_elements(SearchGameLocator.all_laguages)
        try:
            for element in languages:
                if element.text == language:
                    element.click()
                    return True
        except Exception as e:
            raise e
        return False

    def change_sort(self, sort: str) -> bool:
        self.click(SearchGameLocator.sort_button)
        sort_items = self.find_elements(SearchGameLocator.all_sorts)
        try:
            for element in sort_items:
                if element.text == sort:
                    element.click()
                    return True
        except Exception as e:
            raise e
        return False

    def get_sort_type(self) -> str:
        return self.find_element(SearchGameLocator.sort_button).text
