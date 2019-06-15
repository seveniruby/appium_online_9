from web.page_object.page.BasePage import BasePage


class SearchPage(BasePage):
    def follow(self, keyword):
        self.driver.find_element_by_xpath('//*[contains(text(), "%s")]/../../../..//*[@class="follow__control"]' % keyword).click()
        return self