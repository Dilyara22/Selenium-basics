from selenium import webdriver

driver = webdriver.Firefox()

driver.get('https://www.saucedemo.com/')

print(f'Title of the website {driver.title}')
print(f'Name of the browser {driver.name}')
print(driver.current_url)
print('Accepted usernames' in driver.page_source)
