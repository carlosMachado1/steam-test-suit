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
        return self.find_elements(SearchGameLocator.search_filters)
