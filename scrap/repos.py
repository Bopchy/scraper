# Gets all repos of a user
from browser_instance import chrome_instance as chrome
from get_page_data import wait_for_page_to_load as loaded, soupify
from user_navigation import click_button

# new Chrome instance
browser = chrome('/Users/bopchy/Downloads/chromedriver')

# passing in the desired website url
browser.get("https://github.com/TheDancerCodes")
# clicking on repositories tab
click_button(browser, '//*[@id="js-pjax-container"]/div/div[2]/div[2]/nav/a[2]')
# ensure page loaded, after button click
loaded(browser, '//*[@id="your-repos-filter"]', 30)

page = soupify(browser).find('div', class_='pagination')
last_page = int(page.text.split()[-2])
all_projects = []

with open('repos.txt', 'w') as outfile:
    while last_page > 0:
        last_page = last_page - 1
        all_repos = soupify(browser).find_all('li', class_='d-block')
        for repo in all_repos:
            name = repo.find('div', class_='mb-1')
            pname = name.find('a').text
            language = repo.find('div', class_='mt-2')
            color = language.find('span', class_='repo-language-color')
            if color is not None:
                outfile.write(pname.split()[-1] + ' ' + language.text.replace('\n', '').strip().split()[0] + '\n')
            else:
                outfile.write(pname.split()[-1] + ' ' + '-' + '\n')
        next = browser.find_element_by_xpath('//*[@id="user-repositories-list"]/div/div/a[3]')
        next.click()
        loaded(browser, '//*[@id="your-repos-filter"]', 30)
        soupify(browser)

browser.quit()
