from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get('http://automationpractice.com/')


try:
    element=WebDriverWait(driver,15).until(
        EC.presence_of_element_located((By.XPATH,"//a[text()='Contac us']"))
    )
except TimeoutException:
    print('Waited for 15 sec, could not locate the element')

else:
    element.click()
