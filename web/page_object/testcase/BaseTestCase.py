
import logging

class BaseTestCase(object):
    logging.basicConfig()
    _log=logging.getLogger("xueqiu")
    _log.setLevel(logging.DEBUG)

    @property
    def log(self):
        return self._log