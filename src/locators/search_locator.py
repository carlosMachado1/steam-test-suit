from selenium.webdriver.common.by import By


class SearchGameLocator:
    search_field = (By.ID, "store_nav_search_term")
    search_button = (By.XPATH, "//*[@id='store_search_link']")
    search_filters = (
        By.ID,
        "searchtag_tmpl",
    )
