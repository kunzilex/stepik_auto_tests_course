import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

try:
    browser = webdriver.Chrome()

    browser.get(" http://suninjuly.github.io/explicit_wait2.html")

    text = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
        )
    button = browser.find_element(by="id", value="book")
    button.click()

    x = browser.find_element(by="id", value="input_value").text
    y = math.log(abs(12 * math.sin(int(x))))

    input1 = browser.find_element(by="id", value="answer")
    input1.send_keys(y)

    button = browser.find_element(by="id", value="solve")
    button.click()

    time.sleep(5)


finally:
    time.sleep(2)
    browser.quit()
