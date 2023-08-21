from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver) -> None:
        self.driver = driver

    def click(self, by_locator):
        """Performs click on web element whose locator is passed to it"""
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(by_locator)
        ).click()

    def enter_text(self, by_locator, text):
        """Performs text entry of the passed in text, in a web element whose locator is passed to it"""
        return (
            WebDriverWait(self.driver, 10)
            .until(EC.visibility_of_element_located(by_locator))
            .send_keys(text)
        )

    def get_title(self) -> str:
        """Returns the title of the page"""
        return self.driver.title

    def get_url(self) -> str:
        """Returns the URL of the page"""
        return self.driver.current_url
