import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_localisation_button(browser):
    browser.get(link)
    time.sleep(5)
    button = browser.find_element(by="css selector", value="button.btn.btn-lg.btn-primary")
    assert button, "button is not found"
