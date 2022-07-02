
from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = str(math.ceil(math.pow(math.pi, math.e)*10000))
    l = browser.find_element(by='link text', value= x)
    l.click()

    input1 = browser.find_element(by='tag name', value="input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(by='name', value="last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(by='class name', value="form-control.city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(by='id', value="country")
    input4.send_keys("Russia")
    button = browser.find_element(by='css selector', value="button.btn")
    button.click()

finally:

    time.sleep(30)
    browser.quit()

    






