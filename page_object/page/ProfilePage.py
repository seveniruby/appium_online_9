from page_object.page.BasePage import BasePage
from page_object.page.LoginPage import LoginPage


class ProfilePage(BasePage):
    def gotoLogin(self):
        self.load("../data/ProfilePage.yaml", "gotoLogin")
        return LoginPage()