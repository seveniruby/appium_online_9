from selenium.webdriver.common.by import By

from page_object.driver.AndroidClient import AndroidClient
from page_object.page.BasePage import BasePage
from page_object.page.SelectedPage import SelectedPage


class MainPage(BasePage):
    def gotoSelected(self):
        #调用全局的driver对象使用webdriver api操纵app

        #self.driver.find_element(By.xpath, "//*[@text='自选']")
        zixuan=(By.XPATH, "//*[@text='自选']")
        self.find(zixuan)
        #self.driver.find_element_by_xpath("//*[@text='自选']")

        self.find(zixuan).click()

        return SelectedPage()