# !/usr/bin/python3
# -*- encoding=utf8 -*-

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WebElement:

    def __init__(self, browser):
        self.browser = browser
        self.base_url = "https://google.com"

    def find_element(self, locator, wait=10):
        return WebDriverWait(self.browser, wait).until(EC.presence_of_element_located(locator),
                                                      message=f"Не найден элемент по локатору {locator}")

    def find_elements(self, locator, wait=10):
        return WebDriverWait(self.browser, wait).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Не найдены элементы по локатору {locator}")

    def send_keys(self, locator, wait=10):
        return WebDriverWait(self.browser, wait).until(EC.presence_of_element_located(locator),
                                                       message=f"Не найден элемент по локатору {locator}")

    def go_to_site(self, url):
        return self.browser.get(url)
