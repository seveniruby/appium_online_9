from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from web.page_object.page.BasePage import BasePage


class SelectedPage(BasePage):
    def __init__(self, driver):
        super(self, driver)
        #super().__init__(driver)
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".optional_stocks .iconfont")))
    def select(self, keyword, market):
        self.driver.find_element_by_css_selector(".optional .search__dropdown input").send_keys(keyword)
        self.driver.find_element_by_xpath("//*[@class='search__dropdown__list']//li[contains(text(), '%s')]" % market).click()

    def getCurrentPrice(self, keyword):
        pass

