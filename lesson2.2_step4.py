from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

# def calc(x, y):
# return int(math(x + y))

try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(by="id", value="num1").text
    num1 = int(x)
    y = browser.find_element(by="id", value="num2").text
    num2 = int(y)
    sum_el = num1 + num2

    select = Select(browser.find_element(by="id", value="dropdown"))
    select.select_by_value(value=str(sum_el))

    button1 = browser.find_element(by="css selector", value="button.btn")
    button1.click()

    time.sleep(1)

finally:
    time.sleep(5)
    browser.quit()
