from .base_page import BasePage
from ..locators.search_locator import SearchGameLocator


class NewsPage(BasePage):
    def __init__(self, driver) -> None:
        super().__init__(driver)
        driver.get("https://store.steampowered.com/news/")
