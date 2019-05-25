from page_object.driver.AndroidClient import AndroidClient
from page_object.page.SelectedPage import SelectedPage


class MainPage(object):

    #调用appium启动app
    def __init__(self):
        AndroidClient.restart_app()


    def gotoSelected(self):
        #调用全局的driver对象使用webdriver api操纵app
        AndroidClient.driver.find_element_by_xpath("//*[@text='自选']")
        AndroidClient.driver.find_element_by_xpath("//*[@text='自选']").click()

        return SelectedPage()