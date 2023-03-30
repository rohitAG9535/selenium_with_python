print("good evening")


import time
from selenium import webdriver

driver=webdriver.chrome()

driver.get("https://www.ecoders.com")

time.sleep(5)

print(driver.title)

print(driver.current_url)

print(driver.page_source)

driver.quit()