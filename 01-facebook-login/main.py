from selenium import webdriver
from time import sleep
driver = webdriver.Firefox(executable_path='./geckodriver')

driver.get('https://www.fb.com/')

sleep(3)

mail_input = driver.find_element_by_css_selector('#email')
mail_input.send_keys('example')

password_input = driver.find_element_by_css_selector('#pass')
password_input.send_keys('example')
sleep(2)
enter_btn = driver.find_element_by_css_selector('#u_0_b')
enter_btn.click()
sleep(2)
driver.close()
