from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(x))))


try:
    link = "https://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(by="id", value="input_value")
    x = x_element.text
    y = calc(int(x))

    input1 = browser.find_element(by="id", value="answer")
    input1.send_keys(y)

    option1 = browser.find_element(by="id", value="robotCheckbox")
    option1.click()
    button = browser.find_element(by="css selector", value="button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    # browser.execute_script("window.scrollBy(0, 100);")

    option2 = browser.find_element(by="id", value="robotsRule")
    option2.click()

    button.click()

    time.sleep(5)

finally:
    time.sleep(5)
    browser.quit()

from selenium import webdriver
from math import log, sin

link = "https://SunInJuly.github.io/execute_script.html"
with webdriver.Chrome() as browser:
    browser.get(link)
    x = int(browser.find_element_by_id('input_value').text)
    y = log(abs(12 * sin(x)))
    ans = browser.find_element_by_tag_name('input')
    ans.send_keys(str(y))
    browser.execute_script("return arguments[0].scrollIntoView(true);", ans)

    for n in ['robotCheckbox', 'robotsRule']:
        browser.find_element_by_id(n).click()
    browser.find_element_by_tag_name("button").click()

    code = browser.switch_to.alert.text
    print(code.split()[-1])