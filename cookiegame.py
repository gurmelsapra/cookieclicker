from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def buy_upgrades(money):
    # List of tuples with element IDs and their corresponding cost thresholds
    upgrades = [
        ("buyMine", 2000),
        ("buyFactory", 500),
        ("buyGrandma", 119),
        ("buyCursor", 19)
    ]
    
    # Iterate over the upgrades in reverse order of importance
    for upgrade_id, cost in upgrades:
        if money > cost:
            try:
                upgrade = driver.find_element(By.ID, upgrade_id)
                upgrade.click()
                break  # Stop after buying the first affordable upgrade
            except:
                continue  # If element not found, skip to the next

# Set up Chrome options to keep the browser open after the script finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Initialize the WebDriver
driver = webdriver.Chrome(options=chrome_options)

# Open the Cookie Clicker game
driver.get("https://orteil.dashnet.org/experiments/cookie/")

# Find the cookie button element by its ID
cookie = driver.find_element(By.ID, "cookie")

# Record the start time
start_time = time.time()

# Run the game loop for 1 minute (can be adjusted as needed)
while time.time() - start_time < 60:
    # Click the cookie for 5 seconds
    end_time = time.time() + 5
    while time.time() < end_time:
        cookie.click()

    # Fetch the amount of money available
    money = driver.find_element(By.ID, "money").text
    money = int(money.replace(",", ""))  # Remove commas and convert to int

    # Buy upgrades if possible
    buy_upgrades(money)

    # Fetch and print cookies per second (CPS)
    cps = driver.find_element(By.ID, "cps").text
    print(f"Cookies per second: {cps}")

    time.sleep(1)  # Short sleep to avoid spamming too quickly

# Optionally, you can close the browser after the clicking is done
driver.quit()
