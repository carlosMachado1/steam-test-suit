from typing import List
from copy import deepcopy
from src.pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException
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

    def get_all_filters(self) -> List[str]:
        """Return all filters applied to the page"""
        filters = []
        try:
            filters_tag = self.find_elements(SearchGameLocator.search_filters_tag)
            for element in filters_tag:
                filters.append(element.text)
        except TimeoutException:
            pass
        except Exception as e:
            raise e
        return filters

    def set_filters(self, filters: List[str]) -> None:
        """Set all passed filters on the page"""
        filters_ = deepcopy(filters)
        while filters_:
            self.enter_text(SearchGameLocator.sugestion_filter, filters_[0])
            all_filters = self.find_elements(SearchGameLocator.all_filters)
            try:
                for element in all_filters:
                    if element.text == filters_[0]:
                        element.click()
                        filters_.pop(0)
                        self.clear_field(SearchGameLocator.sugestion_filter)
                        break

            except Exception as e:
                raise e

    def get_results(self) -> str:
        return self.find_element(SearchGameLocator.search_result).text

    def get_all_languages(self) -> List[str]:
        """Return all supported languages on the page"""
        all_languages = []
        self.click(SearchGameLocator.show_languages_button)
        languages = self.find_elements(SearchGameLocator.all_laguages)
        try:
            for element in languages:
                all_languages.append(element.text)
        except Exception as e:
            raise e
        finally:
            self.click(SearchGameLocator.show_languages_button)
        return all_languages

    def change_language(self, language: str) -> None:
        """Perform an change language"""
        self.click(SearchGameLocator.show_languages_button)
        languages = self.find_elements(SearchGameLocator.all_laguages)
        try:
            for element in languages:
                if element.text == language:
                    element.click()
                    break
        except Exception as e:
            raise e

    def change_sort(self, sort: str) -> None:
        """Change the sort type of the page if sort type exists on the page sort list"""
        self.click(SearchGameLocator.sort_button)
        sort_items = self.find_elements(SearchGameLocator.all_sorts)
        try:
            for element in sort_items:
                if element.text == sort:
                    element.click()
                    break
        except Exception as e:
            raise e

    def get_sort_type(self) -> str:
        """Return the selected sort type"""
        return self.find_element(SearchGameLocator.sort_button).text

    def add_game_to_cart(self, game: str) -> None:
        pass

    def remove_game_from_cart(self, game: str) -> None:
        pass
