from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "https://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(by="css selector", value="img")
    x = x_element.get_attribute("valuex")
    y = calc(x)

    input1 = browser.find_element(by="id", value="answer")
    input1.send_keys(y)

    option1 = browser.find_element(by="id", value="robotCheckbox")
    option1.click()
    option2 = browser.find_element(by="id", value="robotsRule")
    option2.click()

    button1 = browser.find_element(by="css selector", value="button.btn")
    button1.click()

    time.sleep(1)

finally:
    time.sleep(5)
    browser.quit()
