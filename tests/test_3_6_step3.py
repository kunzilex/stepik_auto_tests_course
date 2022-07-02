import pytest
import math
import time
from selenium import webdriver


@pytest.fixture(scope="class")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('link', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
class TestFindAnswer():
    def test_find_answer_from_each_link(self, browser, link):
        link = f"https://stepik.org/lesson/{link}/step/1"
        browser.get(link)
        browser.implicitly_wait(5)

        # answer = str(math.log(int(time.time())))
        input1 = browser.find_element(by="css selector", value=".ember-text-area")
        input1.send_keys(str(math.log(int(time.time()))))

        browser.implicitly_wait(5)

        button = browser.find_element(by="css selector", value=".submit-submission")
        button.click()

        optional_text = browser.find_element(by="css selector", value=".smart-hints__hint").text

        assert "Correct!" == optional_text


if __name__ == "__main__":
    pytest.main()

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


# ссылка на документацию по "scope"
# --> https://docs.pytest.org/en/6.2.x/fixture.html#scope-sharing-fixtures-across-classes-modules-packages-or-session
@pytest.fixture(scope="class")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    # ожидание 10 секунд, при поиске
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestPages:  # сделанно через класс, чтобы браузер один раз открылся и закрылся

    @pytest.mark.parametrize('numb', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
    def test_guest_should_see_login_link(self, browser, numb):
        link = f"https://stepik.org/lesson/{numb}/step/1"
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, 'textarea').send_keys(str(math.log(int(time.time() - 3.8))))
        browser.find_element(By.CSS_SELECTOR, '.submit-submission').click()
        answer = browser.find_element(By.CSS_SELECTOR, '.smart-hints__hint').text
        assert answer == 'Correct!', answer