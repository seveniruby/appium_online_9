
import pytest

from page_object.page.App import App
from page_object.page.MainPage import MainPage


class TestSelected(object):
    def test_price(self):
        assert App.main().gotoSelected().getPriceByName("科大讯飞")==28.83

    def test_add_stock(self):
        pass