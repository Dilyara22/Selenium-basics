from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep 

driver = webdriver.Firefox()


driver.get('http://www.seleniumframework.com/Practiceform/')


driver.find_element(By.CSS_SELECTOR,'#alert')


alert_button = driver.find_element(By.CSS_SELECTOR,'#alert').click()

alert=driver.switch_to.alert

sleep(5)

alert.accept()