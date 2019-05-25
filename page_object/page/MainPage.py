from selenium.webdriver.common.by import By

from page_object.driver.AndroidClient import AndroidClient
from page_object.page.BasePage import BasePage
from page_object.page.SearchPage import SearchPage
from page_object.page.SelectedPage import SelectedPage


class MainPage(BasePage):
    def gotoSelected(self):
        #调用全局的driver对象使用webdriver api操纵app

        #self.driver.find_element(By.xpath, "//*[@text='自选']")
        zixuan="自选"
        self.findByText(zixuan)
        #self.driver.find_element_by_xpath("//*[@text='自选']")
        self.findByText(zixuan).click()

        return SelectedPage()

    def gotoSearch(self):
        search_button=(By.ID, "home_search")
        self.find(search_button).click()
        return SearchPage()