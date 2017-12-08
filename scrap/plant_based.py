# Agenda: Go to https://www.plantbasedcooking.com/recipes/appetizers/, and pull out all of Appetizer dish names,
# then print them, followed by the recipes themselves and save them to a database.
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from browser_instance import chrome_instance
from get_page_data import wait_for_page_to_load, soupify
from user_navigation import click_button, hover
import json

class recipes:
    def __init__(self, food_group, image, prep_time, cook_time, servings, ingredients, instructions, nutrition_notes):
        self.food_group = food_group
        self.image = image
        self.prep_time = prep_time
        self.cook_time = cook_time
        self.servings = servings
        self.ingredients = ingredients
        self.instructions = instructions
        self.nutrition_notes = nutrition_notes

browser = chrome_instance('/Users/bopchy/Downloads/chromedriver')
# browser.get('https://www.plantbasedcooking.com/')
browser.get('https://www.plantbasedcooking.com/recipes/recipe-index/')
timeout = 25
try:
    wait_for_page_to_load(browser, '//*[@id="menu-plant-based-cooking-main-menu"]')
    page = soupify(browser) # contains the whole loaded page
    try:
        # # looking for the menu bar
        # menuBar = page.find('ul', _class='menu-primary')
        # # click on Recipes -> recipe index, wait for page to load
        # b = hover(browser, 'li #menu-item-2251', 'li #menu-item-3169')
        # wait_for_page_to_load(browser, '//*[@id="genesis-content"]/article/header/h1')

        # 1. create an object with the group as the key, and an array of recipe links as the value
        all_recipes = page.find('div', class_='wpurp-index-container') # grab all of the recipes on the page
        food_groups = all_recipes.find_all('a') # Appetizers, breakfast, etc.
        recipe_links = []
        for food in food_groups:
            recipe_links.append(food['href'])
        print(recipe_links)

        recipes_data = {}
        # {"recipe1":{}, "recipe2": {}}
        for url in recipe_links:
            browser.get(url)
            wait_for_page_to_load(browser, '//*[@id="menu-plant-based-cooking-main-menu"]')
            page = soupify(browser)
            data = {}
            try:
                data['title'] = (page.find('h1', class_='entry-title').text)
                data['recipe_image'] = page.find('img')['src']
                data['prep_time'] = page.find('span', class_='wpurp-recipe-prep-time').text
                # data['cook_time'] = page.find('span', class_='wpurp-recipe-cook-time').text ?? Can I put a default value??
                data['ingredients'] = page.find('ul', class_='wpurp-recipe-ingredient-container').text
                data['instructions'] = page.find('ol', class_='wpurp-recipe-instruction-container').text
            except NoSuchElementException:
                print('No such element found')
            recipes_data[data['title']] = data
        with open('recipes.json', 'w') as f:
            f.write(json.dumps(recipes_data))

        browser.quit()
    except NoSuchElementException:
        print('No such element found')
except TimeoutException:
    print('Timed out waiting for the page to load')
browser.quit()