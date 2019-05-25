from page_object.driver.AndroidClient import AndroidClient
from page_object.page.MainPage import MainPage


class App(object):
    @classmethod
    def main(self):
        AndroidClient.restart_app()
        return MainPage()