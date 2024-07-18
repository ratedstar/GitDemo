import pytest

from RahulShettySelenium.PytestDemo.BaseClass import BaseClass


@pytest.mark.usefixtures("dataload")
class TestExample2(BaseClass):
    def test_editprofile(self,dataload):
        log = self.get_logger()
        log.info(dataload)
        log.info(dataload[0])
        log.info(dataload[1])
        log.info(dataload[2])

