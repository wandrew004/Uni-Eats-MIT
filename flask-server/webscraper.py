import requests
from bs4 import BeautifulSoup

url = "https://www.bu.edu/dining/location/marciano/#menu"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the table element containing the menu items
    menu_table = soup.find("table", {"class": "menu-item-list"})

    if menu_table:
        # Find all the rows (tr elements) in the table
        menu_rows = menu_table.find_all("li")

        for row in menu_rows:
            # Find all the cells (td elements) in each row
            cells = row.find_all("td")

            # Extract and print the content of each cell
            for cell in cells:
                print(cell.text.strip())

            print("---")

    else:
        print("Menu table not found on the page.")

else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")