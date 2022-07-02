from selenium import webdriver
import time


link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(by='tag name', value="input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(by='name', value="last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(by='class name', value="form-control.city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(by='id', value="country")
    input4.send_keys("Russia")
    button = browser.find_element(by="xpath", value='//button[@type="submit"]')
    button.click()

finally:

    time.sleep(30)
    browser.quit()

