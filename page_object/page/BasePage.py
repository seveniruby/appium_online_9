from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from page_object.driver.AndroidClient import AndroidClient
import yaml

class BasePage(object):
    def __init__(self):
        self.driver: WebDriver=self.getDriver()

    @classmethod
    def getDriver(cls):
        cls.driver=AndroidClient.driver
        return cls.driver

    @classmethod
    def getClient(cls):
        return AndroidClient

    def find(self, kv) -> WebElement:
        #todo: 处理各类弹框
        return self.driver.find_element(*kv)
    def findByText(self, text) -> WebElement:
        return self.find((By.XPATH, "//*[@text='%s']" %text))

    def loadSteps(self, po_path, key, **kwargs):
        file=open(po_path, 'r')
        po_data=yaml.load(file)
        po_method=po_data[key]
        for step in po_method:
            step: dict
            element: WebElement=self.driver.find_element(by=step['by'], value=step['locator'])
            action=str(step['action']).lower()

            #todo: 定位失败，多数是弹框，try catch后进入一个弹框处理 元素智能等待
            if action=="click":
                element.click()
            elif action=="sendkeys":
                text=str(step['text'])
                for k,v in kwargs.items():
                    text=text.replace("$%s" %k, v)
                    print("update text: %s" % (text))
                element.send_keys(text)
            else:
                print("UNKNOW COMMAND %s" % step)

