
import pytest

from page_object.page.App import App
from page_object.page.MainPage import MainPage


class TestSelected(object):
    def test_price(self):
        assert App.main().gotoSelected().getPriceByName("科大讯飞")==28.83

    def test_is_selected_stock(self):
        searchPage=App.main().gotoSearch().search("alibaba")
        assert searchPage.isInSelected("BABA")==True
        assert searchPage.isInSelected("1688")==False

    def test_is_follow_user(self):
        #todo: 作业2
        pass