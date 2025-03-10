import time
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

bot = driver.find_element(By.ID, 'cookie')

strips = ["Cursor -","Grandma -", "Factory -", "Mine -", "Shipment -","Alchemy lab -","Portal -","Time machine -"]

money = driver.find_element(By.ID, "money")

while True:
    # Continuously click the cookie
    bot.click()

    # Every 5 seconds, check which item can be bought
    if int(time.time()) % 15 == 0:
        items = driver.find_elements(By.CSS_SELECTOR, '#store b')
        affordable_items = []

        for smth in range(len(items)):
            try:
                # Parse the price of each item
                item_price = int(items[smth].text.strip(strips[smth]).replace(",", "").replace(" ", ""))
                current_money = int(money.text)

                # Check if the item is affordable
                if current_money >= item_price:
                    affordable_items.append((item_price, items[smth]))  # Store price and element
            except (IndexError, ValueError):
                continue

        # If there are affordable items, click the most expensive one
        if affordable_items:
            # Sort by price in descending order and select the first item
            most_expensive_item = max(affordable_items, key=lambda x: x[0])[1]
            most_expensive_item.click()

        # Short sleep to prevent multiple evaluations in the same second
        time.sleep(1)
