from selenium import webdriver
from time import sleep
driver = webdriver.Firefox(executable_path='./geckodriver')
driver.implicitly_wait(10)
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
add_blog_btn = driver.find_element_by_css_selector('.model-blog > td:nth-child(2) > a:nth-child(1)')
add_blog_btn.click()

add_title = driver.find_element_by_css_selector('#id_title')
add_title.send_keys('First blog')
sleep(1)
add_description = driver.find_element_by_css_selector('#id_short_description')
add_description.send_keys('My first blog')
sleep(1)
add_fullName = driver.find_element_by_css_selector('#id_blogger_full_name')
add_fullName.send_keys('Agil Mahmudov')
sleep(1)
add_content = driver.find_element_by_css_selector('#id_content')
add_content.send_keys('Lets finish this blog')

save_blog = driver.find_element_by_css_selector('.default')
save_blog.click()


sleep(3)
driver.close()
