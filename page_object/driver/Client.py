from appium import webdriver
from appium.webdriver.webdriver import WebDriver
import yaml

class AndroidClient(object):

    driver:WebDriver
    platform="android"
    @classmethod
    def install_app(cls) -> WebDriver:

        # caps = {}
        # #如果有必要，进行第一次安装
        # # caps["app"]=''
        # caps["platformName"] = "android"
        # caps["deviceName"] = "hogwarts"
        # caps["appPackage"] = "com.xueqiu.android"
        # caps["appActivity"] = ".view.WelcomeActivityAlias"
        # #解决第一次启动的问题
        # caps["autoGrantPermissions"] = "true"
        # # caps['noReset']=True
        #
        # cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        # cls.driver.implicitly_wait(10)
        # return cls.driver

        cls.initDriver("install_app")

    @classmethod
    def restart_app(cls) -> WebDriver:
        # caps = {}
        #
        # caps["platformName"] = "android"
        # caps["deviceName"] = "hogwarts"
        # caps["appPackage"] = "com.xueqiu.android"
        # caps["appActivity"] = ".view.WelcomeActivityAlias"
        # #为了更快的启动，并保留之前的数据，从而可以保存上一个case执行后的状态
        # caps['noReset']=True
        # caps['chromedriverExecutableDir']="/Users/seveniruby/projects/chromedriver/2.20"
        # caps['unicodeKeyboard']=True
        # caps['resetKeyboard']=True
        # #caps["udid"]="emulator-5554"
        #
        # cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        # cls.driver.implicitly_wait(10)
        # return cls.driver

        return cls.initDriver("restart_app")

    @classmethod
    def initDriver(cls, key):
        driver_data=yaml.load(open("../data/driver.yaml"))
        platform=str(driver_data['platform'])
        cls.platform=platform
        server = driver_data[key]['server']
        implicitly_wait = driver_data[key]['implicitly_wait']
        caps=driver_data[key]['caps'][platform]
        cls.driver = webdriver.Remote(server, caps)
        cls.driver.implicitly_wait(implicitly_wait)
        return cls.driver