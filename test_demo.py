import pytest
import yaml

class TestDemo(object):

    @pytest.mark.parametrize("x,y",
                             [
                                 (1, 2),
                                 (3, 4)
                             ]
                             )
    def test_one(self, x, y):
        print("%s %s" % (x, y))
        pass
