from typing import Tuple
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import AnyDriver


class BasePage:
    def __init__(self, driver: AnyDriver) -> None:
        self.driver = driver

    def click(self, by_locator: Tuple[str, str]):
        """Performs click on web element whose locator is passed to it"""
        self.find_element(by_locator).click()

    def enter_text(self, by_locator: Tuple[str, str], *text: str):
        """Performs text entry of the passed in text, in a web element whose locator is passed to it"""
        return self.find_element(by_locator).send_keys(*text)

    def find_element(self, by_locator: Tuple[str, str]):
        """Returns a web element whose locator is passed to it"""
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(by_locator)
        )

    def find_elements(self, by_locator: Tuple[str, str]):
        """Returns all web elements whose locator is passed to it"""
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_elements_located(by_locator)
        )

    def get_title(self) -> str:
        """Returns the title of the page"""
        return self.driver.title

    def get_url(self) -> str:
        """Returns the URL of the page"""
        return self.driver.current_url
