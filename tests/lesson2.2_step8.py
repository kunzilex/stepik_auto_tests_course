
from selenium import webdriver
import time
import os

try:

    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")

    input1 = browser.find_element(by='tag name', value="input")
    input1.send_keys("Kalush")
    input2 = browser.find_element(by='name', value="lastname")
    input2.send_keys("Stefania")
    input3 = browser.find_element(by='name', value="email")
    input3.send_keys("Kyiv")

    choose_file = browser.find_element(by='id', value='file')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'test_txt.txt')
    choose_file.send_keys(file_path)

    button = browser.find_element(by="xpath", value='//button[@type="submit"]')
    button.click()

finally:
    time.sleep(5)
    browser.quit()
