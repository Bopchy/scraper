from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException


# Clicking on repository button
def click_button(browser, path):
    try:
        button = browser.find_element_by_xpath(path)
        return button.click()
    except NoSuchElementException:
        print('Element not found')


# Hovering over an element
def hover(browser, element_to_hover_over, element_to_click):
    try:
        hover = ActionChains(browser).move_to_element(element_to_hover_over).click(element_to_click).perfom()
        return hover
    except NoSuchElementException:
        print('Element not found')
