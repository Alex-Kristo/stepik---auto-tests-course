from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

opt = webdriver.ChromeOptions()
opt.add_experimental_option('w3c', False)
browser = webdriver.Chrome(chrome_options=opt)
browser.get("http://suninjuly.github.io/explicit_wait2.html")
browser.implicitly_wait(5)

button = browser.find_element_by_css_selector("#book")
WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element((By.ID, "price"), "10000 RUR"))
button.click()

x_element = browser.find_element_by_css_selector("#input_value")
x = x_element.text
y = calc(x)
input1 = browser.find_element_by_css_selector("#answer")
input1.send_keys(y)
button2 = browser.find_element_by_css_selector("#solve")
button2.click()