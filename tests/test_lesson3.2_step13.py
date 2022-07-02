from selenium import webdriver
import time
import unittest




class TestAbs(unittest.TestCase):
    def test_abs1(self):
        link = "http://suninjuly.github.io/registration1.html"
        self.browser = webdriver.Chrome()
        browser = self.browser
        browser.get(link)

        input1 = browser.find_element(by="css selector", value="div input.form-control.first")
        input1.send_keys("pika-pika")
        input2 = browser.find_element(by="css selector", value="div input.form-control.second")
        input2.send_keys("pika-pika")
        input3 = browser.find_element(by="css selector", value="div input.form-control.third")
        input3.send_keys("pika-pika")

        button = browser.find_element(by="css selector", value="button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element(by="tag name", value="h1")

        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Should be equal")

    def test_abs2(self):
        link = "https://suninjuly.github.io/registration2.html"
        self.browser = webdriver.Chrome()
        browser = self.browser
        browser.get(link)

        input1 = browser.find_element(by="css selector", value="div.first_class input[required]")
        input1.send_keys("pika-pika")
        input2 = browser.find_element(by="css selector", value="div.second_class input[required]")
        input2.send_keys("pika-pika")
        input3 = browser.find_element(by="css selector", value="div.third_class input[required]")
        input3.send_keys("pika-pika")

        button = browser.find_element(by="css selector", value="button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element(by="tag name", value="h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)


if __name__ == "__main__":
    unittest.main()
