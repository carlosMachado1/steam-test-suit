from random import choice
from unittest import TestCase
from selenium.webdriver import Firefox
from src.pages.home_page import HomePage
from selenium.webdriver.firefox.service import Service
from src.locators.search_locator import SearchGameLocator


class TestHomePage(TestCase):
    def setUp(self) -> None:
        self.driver = Firefox()
        # self.service = Service(log_output=)
        self.home_page = HomePage(self.driver)
        self.locator = SearchGameLocator
        self.games = [
            "Dark Souls",
            "Remnant: From the Ashes",
            "Sekiro: Shadows Die Twice",
        ]

    def tearDown(self) -> None:
        self.driver.quit()

    def test_ct01(self):
        game = choice(self.games)
        self.home_page.fill_search_field(game)
        self.home_page.click(self.locator.search_button)
        result = self.home_page.find_element(self.locator.search_result)
        self.assertNotIn(
            "0 results match your search",
            result.text,
            f"Nenhum resultado encontrado para {game}",
        )

    def test_ct02(self):
        game = "anygame"
        self.home_page.fill_search_field(game)
        self.home_page.click(self.locator.search_button)
        result = self.home_page.find_element(self.locator.search_result)
        self.assertNotIn(
            "0 results match your search",
            result.text,
            f"Nenhum resultado encontrado para {game}",
        )

    def test_ct03(self):
        pass
