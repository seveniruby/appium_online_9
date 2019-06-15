import json
from time import sleep

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities


class TestTesterHome(object):
    def setup(self):
        #self.driver=webdriver.Firefox()

        options=webdriver.ChromeOptions()
        #options.binary_location="chrome path"
        #self.driver = webdriver.Chrome(options=options)
        self.driver=webdriver.Remote(desired_capabilities=DesiredCapabilities.CHROME)
        self.driver.implicitly_wait(10)
        self.driver.get("https://testerhome.com")

    def test_mtsc2019(self):
        self.driver.find_element_by_partial_link_text("MTSC2019").click()
        #self.driver.find_element_by_xpath('//*[@data-toggle="dropdown" and @class="btn btn-default"]').click()
        self.driver.find_element_by_css_selector(".toc-container .btn").click()
        import time
        time.sleep(2)
        self.driver.find_element_by_partial_link_text("金数据").click()
        self.driver.find_element_by_partial_link_text("http://2019.test-china.org/").click()

    def test_basic(self):
        self.driver.maximize_window()
        self.driver.fullscreen_window()

    def test_execute_script(self):
        raw=self.driver.execute_script("return JSON.stringify(window.performance.timing)")
        print(raw)
        print(json.dumps(json.loads(raw), indent=4))

    def test_execute(self):
        self.driver.execute("getXXX", params={"x": 1, "y": 2})


    def teardown(self):
        sleep(10)
        #self.driver.quit()

    def test_cookie(self):
        print(self.driver.get_cookies())
        self.driver.add_cookie({"name": "a", "value":"b"})
        self.driver.add_cookie({"name": "name", "value": "name demo"})
        print(self.driver.get_cookies())




