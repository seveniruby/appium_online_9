# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
import time

from appium import webdriver
import pytest
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import WebDriver


class TestXueqiuAndroid(object):
    driver=WebDriver
    @classmethod
    def setup_class(cls):
        print("setup class")

        #cls.driver =cls.init_appium()

    def setup_method(self):
        print("setup method")

        TestXueqiuAndroid.driver=self.restart_appium()
        self.driver = TestXueqiuAndroid.driver

    def test_login(self):
        el1 = TestXueqiuAndroid.driver.find_element_by_id("user_profile_icon")
        el1.click()
        el2 = TestXueqiuAndroid.driver.find_element_by_id("tv_login")
        el2.click()
        el3 = TestXueqiuAndroid.driver.find_element_by_id("tv_login_by_phone_or_others")
        el3.click()


    def test_基金(self):

        TestXueqiuAndroid.driver.find_element_by_xpath("//*[contains(@resource-id,'indicator')]//*[@text='基金']").click()


    def test_swipe(self):
        self.driver.find_element_by_xpath("//*[contains(@resource-id,'indicator')]//*[@text='基金']")
        for i in range(5):
            self.driver.swipe(1000, 1000, 200, 200)
            time.sleep(2)

    def test_action(self):
        self.driver.find_element_by_xpath("//*[contains(@resource-id,'indicator')]//*[@text='基金']")
        action=TouchAction(self.driver)
        for i in range(5):
            action.press(x=1000, y=1000).move_to(x=200, y=200).release().perform()
            time.sleep(2)

    def test_action_p(self):
        rect=self.driver.get_window_rect()
        self.driver.find_element_by_xpath("//*[contains(@resource-id,'indicator')]//*[@text='基金']")
        action = TouchAction(self.driver)
        for i in range(5):
            action\
                .press(x=rect['width']*0.8, y=rect['height']*0.8).move_to(x=rect['width']*0.2, y=rect['height']*0.2)\
                .release()\
                .perform()
            time.sleep(2)

    def test_window_size(self):
        print(self.driver.get_window_rect())

    def teardown_method(self):
        TestXueqiuAndroid.driver.quit()

    @classmethod
    def init_appium(cls) -> WebDriver:
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "hogwarts"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["autoGrantPermissions"] = "true"
        # caps['noReset']=True

        driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        driver.implicitly_wait(10)
        return driver

    @classmethod
    def restart_appium(cls) -> WebDriver:
        caps = {}
        #caps["app"]=''
        caps["platformName"] = "android"
        caps["deviceName"] = "hogwarts"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        #caps["autoGrantPermissions"] = "true"
        caps['noReset']=True

        driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        driver.implicitly_wait(10)
        return driver

