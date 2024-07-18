import pytest

from Novoice_Pytest.Baseclass import BaseClass
import logging

@pytest.mark.usefixtures("dataLoad")
class TestDemoLog(BaseClass):
    def demoLog(self, dataLoad):
        log = self.getLogger()
        log.info(dataLoad[0])
        log.info(dataLoad[1])