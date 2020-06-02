from selenium import webdriver
from time import sleep
driver = webdriver.Firefox(executable_path='./geckodriver')

driver.get('http://35.225.243.133/admin/login/')

sleep(3)

mail_input = driver.find_element_by_css_selector('#id_username')
mail_input.send_keys('student')

password_input = driver.find_element_by_css_selector('#id_password')
password_input.send_keys('qatester')
sleep(2)
enter_btn = driver.find_element_by_css_selector('.submit-row > input:nth-child(2)')
enter_btn.click()
sleep(2)
driver.close()
