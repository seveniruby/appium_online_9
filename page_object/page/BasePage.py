from selenium.webdriver.remote.webelement import WebElement

from page_object.driver.AndroidClient import AndroidClient


class BasePage(object):
    def __init__(self):
        self.driver=AndroidClient.driver

    def find(self, kv) -> WebElement:
        return self.driver.find_element(*kv)