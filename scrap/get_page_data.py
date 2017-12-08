# Get page data
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup


# To check if page loaded
def wait_for_page_to_load(browser, xpath, timeout=20):
    page_loaded = WebDriverWait(browser, timeout).until(
        EC.visibility_of_element_located((By.XPATH, xpath)))
    return page_loaded


# Create the soup
def soupify(browser):
    html_source = browser.page_source
    soup = BeautifulSoup(html_source, "html.parser")
    return soup
