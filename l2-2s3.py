from selenium import webdriver
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

x1_element = browser.find_element_by_css_selector("#num1")
x1 = x1_element.text
x2_element = browser.find_element_by_css_selector("#num2")
x2 = x2_element.text
y = str(int(x1) + int(x2))
input1 = browser.find_element_by_css_selector("#dropdown")
input1.click()
otvet_elt = browser.find_element_by_css_selector("[value=]")
otvet = otvet_elt.text
assert otvet == y
button = browser.find_element_by_css_selector("button.btn")
button.click()

set = Select(browser.find_element_by_css_selector("select"))
select.select_by_value(y)