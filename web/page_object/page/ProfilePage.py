from web.page_object.page.BasePage import BasePage
from web.page_object.page.SelectedPage import SelectedPage


class ProfilePage(BasePage):

    def login(self):
        print(self.driver.get_cookies())
        self.driver.add_cookie({"name": "device_id", "value": "XXXXXXX"})
        self.driver.add_cookie({"name": "Hm_lvt_1db88642e346389874251b5a1eded6e3", "value": "XXXXXXX"})
        self.driver.add_cookie({"name": "snbim_minify", "value": "true"})
        self.driver.add_cookie({"name": "bid", "value": "XXXX"})
        self.driver.add_cookie({"name": "utmcsr", "value": "(direct)|utmccn=(direct)|utmcmd=(none)"})
        self.driver.add_cookie({"name": "xq_is_login", "value": "1"})
        self.driver.add_cookie({"name": "u", "value": "XXXXX"})
        self.driver.add_cookie({"name": "Hm_lpvt_1db88642e346389874251b5a1eded6e3", "value": "XX"})
        self.driver.add_cookie({"name": "Hm_lpvt_1db88642e346389874251b5a1eded6e3", "value": "XX"})
        self.driver.add_cookie({"name": "xq_a_token", "value": "XXXXX"})
        self.driver.add_cookie({"name": "xq_a_token.sig", "value": "XXXXX"})
        self.driver.add_cookie({"name": "xq_r_token", "value": "XXXXxxxxx"})
        self.driver.add_cookie({"name": "xq_r_token.sig", "value": "--pmYDj5gI"})
        self.driver.add_cookie({"name": "xqat", "value": "XXXXXX"})

        print(self.driver.get_cookies())
        self.driver.refresh()
    def gotoSelected(self):
        return SelectedPage(self.driver)
