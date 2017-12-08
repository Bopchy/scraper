# Gets pinned repos from GitHub homepage
from selenium import webdriver # launches browser
from selenium.webdriver.common.by import By # allows for searching via specific parameters
from selenium.webdriver.support.ui import WebDriverWait # waits for page to load
from selenium.webdriver.support import expected_conditions as EC # checks for specific conditions on loaded page
from selenium.common.exceptions import TimeoutException, NoSuchElementException # handles request timing out
# import logging
from bs4 import BeautifulSoup

option = webdriver.ChromeOptions()
option.add_argument("- incognito")

# new Chrome instance
browser = webdriver.Chrome(
    executable_path='/Users/bopchy/Downloads/chromedriver',  # points to where you donwloaded and saved your ChromeDriver
    chrome_options=option
    )

# passing in the desired website url
browser.get("https://github.com/TheDancerCodes")

# try/except timeout
timeout = 20
try:
    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="js-pjax-container"]/div/div[1]/a/img')))
    # Assumption is that if the avatar is loaded, then the whole page is loaded (since the avatar is the last to load)
    # find_elements_by_xpath returns an array of selenium objects.
    html_source = browser.page_source
    soup = BeautifulSoup(html_source, "html.parser")
    # repos = soup.find_all('nav', class_="UnderlineNav-item")
    try:
        # find all repos first
        all_repos = soup.find_all('li', class_='pinned-repo-item')
        # loop in list 
        for repo in all_repos:
            name = repo.find('span', class_='js-repo')
            language = repo.find('p', class_='f6')
            print((name.text, language.text.replace('\n', '').strip().split()[0]))
    except NoSuchElementException:
        print("NoSuchElementException")

except TimeoutException:
    print("Timed out waiting for page to load")

browser.quit()