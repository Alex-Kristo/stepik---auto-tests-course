from selenium import webdriver
import os


link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)
input1 = browser.find_element_by_name("firstname")
input1.send_keys("Alex")
input2 = browser.find_element_by_name("lastname")
input2.send_keys("Mas")
input3 = browser.find_element_by_name("email")
input3.send_keys("AlMas@gmail.com")
element = browser.find_element_by_id("file")
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'l2-2s8.txt')
element.send_keys(file_path)
button = browser.find_element_by_css_selector(".btn.btn-primary")
button.click()