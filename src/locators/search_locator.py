from selenium.webdriver.common.by import By


class SearchGameLocator:
    search_field = (By.ID, "store_nav_search_term")
    search_button = (
        By.XPATH,
        "/html/body/div[1]/div[7]/div[6]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/div[9]/div[1]/form/div/a/img",
    )
    search_filters = (
        By.ID,
        "searchtag_tmpl",
    )
    search_result = (
        By.XPATH,
        "/html/body/div[1]/div[7]/div[6]/form/div[1]/div/div[1]/div[3]/div[1]",
    )
    show_languages_button = (By.ID, "language_pulldown")
    all_laguages = (By.CLASS_NAME, "popup_menu_item")
    sort_button = (By.ID, "sort_by_trigger")
    all_sorts = (By.CLASS_NAME, "inactive_selection")
