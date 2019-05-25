from inspect import stack

from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from page_object.driver.AndroidClient import AndroidClient
import yaml

class BasePage(object):
    driver:WebDriver
    def __init__(self):
        self.driver=self.getDriver()

    @classmethod
    def getDriver(cls):
        cls.driver=cls.getClient().driver
        return cls.driver

    @classmethod
    def getClient(cls):
        return AndroidClient

    def find(self, kv) -> WebElement:
        #todo: 处理各类弹框
        return self.driver.find_element(*kv)
    def findByText(self, text) -> WebElement:
        return self.find((By.XPATH, "//*[@text='%s']" %text))

    def load(self, path, method, **params):
        print(stack()[1][3])
        steps=[]
        with open(path) as f:
            steps=yaml.safe_load(f)
        for step in steps[method]:

            if(dict(step).keys().__contains__("action")==False):
                if(step['by']=="text"):
                    self.findByText(step['value']).click()
                else:
                    self.driver.find_element(by=step['by'], value=step['value']).click()
            else:
                action=str(step['action'])
                for k, v in params.items():
                    action = action.replace("$%s" % k, v)
                self.driver.find_element(by=step['by'], value=step['value']).send_keys(action)


