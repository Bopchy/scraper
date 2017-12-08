# Creates browser instances (because you might have different browsers)
from selenium import webdriver

option = webdriver.ChromeOptions()
option.add_argument("- incognito")

# Creating a Chrome instance
def chrome_instance(path, options=option):
    browser = webdriver.Chrome(executable_path=path, chrome_options=options)
    return browser