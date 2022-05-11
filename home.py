# from selenium import webdriver
# from selenium.webdriver.common.by import By

# driver = webdriver.Firefox()

# driver.get('http://automationpractice.com/')
# driver.find_element(By.LINK_TEXT,'Sign in').click()

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()

url = 'http://automationpractice.com/index.php'

driver.get(url)

add_buttons = driver.find_elements(By.CLASS_NAME, "product-container")

print(f'There are {len(add_buttons)} products displayed')

add_buttons[0].click()

driver.find_element(By.NAME, "Submit").click()

print('There is 1 item in your cart' in driver.page_source)