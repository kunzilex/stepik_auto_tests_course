from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements(by="css selector", value="input[type='text']")
    for element in elements:
        element.send_keys("xxx")

    button = browser.find_element(by="css selector", value="button.btn")
    button.click()

finally:

    time.sleep(30)

    browser.quit()

# не забываем оставить пустую строку в конце файла