import logging as log
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
        self.games = [
            "Dark Souls",
            "Remnant: From the Ashes",
            "Sekiro: Shadows Die Twice",
            "Remnant II",
        ]

    def tearDown(self) -> None:
        self.driver.quit()

    # def test_ct01(self):
    #     """Pass a random game in the search field"""
    #     game = choice(self.games)
    #     log.info(f"Search for any game: {game}")
    #     self.home_page.fill_search_field(game)
    #     self.home_page.click(SearchGameLocator.search_button)
    #     result = self.home_page.get_results()
    #     self.assertNotIn(
    #         "0 results match your search",
    #         result,
    #         f"Nenhum resultado encontrado para {game}",
    #     )

    # def test_ct02(self):
    #     """Pass a invalid game in the search field"""
    #     game = "anygame"
    #     log.info(f"Search for any invalid game: {game}")
    #     self.home_page.fill_search_field(game)
    #     self.home_page.click(SearchGameLocator.search_button)
    #     result = self.home_page.get_results()
    #     # while 1:
    #     #     pass
    #     self.assertIn(
    #         "0 results match your search",
    #         result,
    #         f"Jogos foram encontrados para uma pesquisa inválida: jogo {game}",
    #     )

    # def test_ct03(self):
    #     """Pass a blank string in the search field"""
    #     game = ""
    #     log.info(f"Search nothing (blank string)")
    #     self.home_page.fill_search_field("")
    #     self.home_page.click(SearchGameLocator.search_button)
    #     result = self.home_page.get_results()
    #     self.assertIn(
    #         "0 results match your search",
    #         result,
    #         f"Jogos foram encontrados para uma pesquisa inválida: jogo {game}",
    #     )

    # def test_ct04(self):
    #     game = choice(self.games)
    #     log.info(f"Search for any game: {game}")
    #     self.home_page.fill_search_field(game)
    #     self.home_page.click(SearchGameLocator.search_button)
    #     sort_types = [
    #         "Release date",
    #         "Name",
    #         "Lowest Price",
    #         "Highest Price",
    #         "Steam Deck Compatibility Review Date",
    #     ]
    #     sort_type = choice(sort_types)
    #     log.debug(f"Change page sort type to {sort_type}")
    #     self.home_page.change_sort(sort_type)
    #     page_sort_type = self.home_page.get_sort_type()
    #     self.assertEqual(sort_type, page_sort_type, "Sort type is not matching")

    def test_ct05(self):
        """Targeted test to verify filter tool function"""
        pass

    # def test_ct06(self):
    #     pass

    # def test_ct07(self):
    #     pass

    # def test_ct08(self):
    #     """Assert change page language"""
    #     languages = [
    #         "Deutsch (German)",
    #         "Español - Latinoamérica (Spanish - Latin America)",
    #         "Português (Portuguese - Portugal)",
    #         "Português - Brasil (Portuguese - Brazil)",
    #     ]
    #     language = choice(languages)
    #     log.info(f"Change page language to {language}")
    #     assert self.home_page.change_language(
    #         language
    #     ), "Couldn't change languague from page"
