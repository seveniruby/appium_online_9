# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
import time

from appium import webdriver
import pytest
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestXueqiuAndroidLogin(object):
    driver = WebDriver
    @classmethod
    def setup_class(cls):
        print("setup class 在当前类下的所有用例执行之前只执行一次")
        #cls.driver=cls.install_app()
        cls.driver=cls.restart_app()
        WebDriverWait(cls.driver, 20).until(EC.presence_of_element_located((MobileBy.XPATH, "//*[@text='交易']")))
        cls.driver.find_element_by_xpath("//*[@text='交易']").click()

        #进入我的页面
        #el1 = cls.driver.find_element_by_id("user_profile_icon")
        #el1.click()


    def setup_method(self):
        print("setup method 在每个测试用例执行之前执行一次")
        #获取启动的appium的driver实例，用于后续每个case的driver
        self.driver=TestXueqiuAndroidLogin.driver

        #每次都会执行一次进入登录页的点击
        self.driver.find_element_by_xpath("//*[@text='交易']").click()


    def test_webview_simulator_A(self):
        self.driver.find_element_by_accessibility_id("A股开户").click()
        self.driver.find_element_by_accessibility_id("立即开户")
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID, "立即开户")))


    def teardown_method(self):
        #不加也没关系，如果不quit，启动appium会自动quit之前的session
        self.driver.back()
        self.driver.back()

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
        caps["udid"]="emulator-5554"

        driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        driver.implicitly_wait(10)
        return driver
