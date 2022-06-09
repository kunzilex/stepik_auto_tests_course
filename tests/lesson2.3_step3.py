from selenium import webdriver
import time
import math

#def calc(x):
#    return math.log(abs(12 * math.sin(x)))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")

    button = browser.find_element(by="css selector", value="button.btn")
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x = browser.find_element(by="id", value="input_value").text
    #x = x_element.text
    y = math.log(abs(12 * math.sin(int(x))))

    input1 = browser.find_element(by="id", value="answer")
    input1.send_keys(y)

    button = browser.find_element(by="css selector", value="button.btn")
    button.click()


    time.sleep(2)

finally:
    time.sleep(5)
    browser.quit()

