from selenium import webdriver
import time

try:
    link = "https://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(by="css selector", value="div.first_class input[required]")
    input1.send_keys("pika-pika")
    input2 = browser.find_element(by="css selector", value="div.second_class input[required]")
    input2.send_keys("pika-pika")
    input3 = browser.find_element(by="css selector", value="div.third_class input[required]")
    input3.send_keys("pika-pika")

    # Отправляем заполненную форму
    button = browser.find_element(by="css selector", value="button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(by="tag name", value="h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
