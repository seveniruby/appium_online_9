# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
import time

from appium import webdriver
import pytest
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import WebDriver


class TestXueqiuAndroid(object):
    @classmethod
    def setup_class(cls):
        print("setup class 在当前类下的所有用例执行之前只执行一次")
        #cls.install_app()

    def setup_method(self):
        print("setup method 在每个测试用例执行之前执行一次")
        #获取启动的appium的driver实例，用于后续每个case的driver
        self.driver=self.restart_app()
        self.driver.execute_script()

    def test_login(self):
        el1 = self.driver.find_element_by_id("user_profile_icon")
        el1.click()
        el2 = self.driver.find_element_by_id("tv_login")
        el2.click()
        el3 = self.driver.find_element_by_id("tv_login_by_phone_or_others")
        el3.click()


    def test_found(self):
        self.driver.find_element_by_xpath("//*[contains(@resource-id,'indicator')]//*[@text='基金']").click()

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
            self.driver.get_screenshot_as_file(str(i)+".png")

    def test_window_size(self):
        print(self.driver.get_window_rect())

    def teardown_method(self):
        #不加也没关系，如果不quit，启动appium会自动quit之前的session
        self.driver.quit()

    @classmethod
    def install_app(cls) -> WebDriver:
        caps = {}
        #如果有必要，进行第一次安装
        # caps["app"]=''
        caps["platformName"] = "android"
        caps["deviceName"] = "hogwarts"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        #解决第一次启动的问题
        caps["autoGrantPermissions"] = "true"
        # caps['noReset']=True

        driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        driver.implicitly_wait(10)
        return driver

    @classmethod
    def restart_app(cls) -> WebDriver:
        caps = {}

        caps["platformName"] = "android"
        caps["deviceName"] = "hogwarts"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        #为了更快的启动，并保留之前的数据，从而可以保存上一个case执行后的状态
        caps['noReset']=True
        caps['udid']='emulator-5554'

        driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        driver.implicitly_wait(10)
        return driver
