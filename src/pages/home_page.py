from .base_page import BasePage
from ..locators.search_locator import SearchGameLocator


class HomePage(BasePage):
    def __init__(self, driver) -> None:
        super().__init__(driver)
        driver.get("https://store.steampowered.com/?")

    def fill_search_field(self, game: str) -> None:
        self.enter_text(SearchGameLocator.search_field, game)

    def perform_search(self) -> None:
        self.click(SearchGameLocator.search_button)
