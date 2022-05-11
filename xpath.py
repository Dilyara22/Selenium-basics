from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Firefox()

driver.get('http://automationpractice.com/')

driver.find_element(By.XPATH,"//a[text()='Contact us']").click()

select = Select(driver.find_element(By.NAME,'id_contact'))
select.select_by_index(1)


driver.find_element(By.CSS_SELECTOR,'#email').send_keys('team@skillrill.com')

driver.find_element(By.CSS_SELECTOR,'#id_order').send_keys('1')

driver.find_element(By.XPATH,"//input[@name='fileUpload']").send_keys(r'C:\AUTOMATION\Selenium-basics\test.txt')

driver.find_element(By.CSS_SELECTOR,'#message').send_keys('test')

driver.find_element(By.XPATH,"//button[@name='submitMessage']").click()

print('Your message has been successfully sent to our team.' in driver.page_source)

