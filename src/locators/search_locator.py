from selenium.webdriver.common.by import By


class SearchGameLocator:
    search_field = (By.ID, "store_nav_search_term")
    search_button = (By.ID, "store_search_link")
    # news_search_field = (By., "store_search_link")
