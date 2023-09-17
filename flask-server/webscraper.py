import requests
from bs4 import BeautifulSoup
from food import food

url = "https://www.bu.edu/dining/location/marciano/#menu"

def import_food():
  response = requests.get(url)

  if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")

    menu_section = soup.find("li", id="2023-09-18-lunch")

    menu_item = menu_section.find_all("h4", class_="js-nutrition-open-alias menu-item-title")
    menu_item_cals = menu_section.find_all("li", class_="menu-nutrition-cals")
    menu_item_fat = menu_section.find_all("li", class_="menu-nutrition-saturated-fat")
    menu_item_carbs = menu_section.find_all("li", class_="menu-nutrition-carbs")
    menu_item_sugar = menu_section.find_all("li", class_="menu-nutrition-sugar")
    menu_item_protein = menu_section.find_all("li", class_="menu-nutrition-protein")
    foods = []
    for i in range(len(menu_item)):
        if(int(menu_item_cals[i].text.strip()[:-5]) > 80):
            f = food(menu_item[i].text.strip(), int(menu_item_cals[i].text.strip()[:-5]), 
            int(menu_item_fat[i].text.strip()[:-15]), int(menu_item_carbs[i].text.strip()[:-7]), 
            int(menu_item_sugar[i].text.strip()[:-8]), int(menu_item_protein[i].text.strip()[:-10]))
            foods.append(f) 
    return foods
  else:
    return []