from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep 


driver = webdriver.Firefox()

driver.get('http://www.seleniumframework.com/Practiceform/')

driver.find_element(By.XPATH,"//button[text()='New Browser Tab']")
new_tab_button=driver.find_element(By.XPATH,"//button[text()='New Browser Tab']")

sleep(10)

new_tab_button.click()

print(driver.window_handles)
first_tab=driver.window_handles [0]
second_tab=driver.window_handles [1]

driver.switch_to.window(second_tab)
sleep(5)
driver.close()
sleep(5)
driver.switch_to.window(first_tab)
driver.close()