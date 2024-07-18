import pytest

from Novoice_Pytest.Baseclass import BaseClass


@pytest.mark.usefixtures("dataLoad")
class TestLoad(BaseClass):
    def test_EditProfile(self,dataLoad):
        print(dataLoad)
        print(dataLoad[0])
        print(dataLoad[1])
        log = self.getLogger()
        log.info(dataLoad[0])
        log.warning(dataLoad[1])
        log.debug("This message is for debug")
        log.info("This is for info")
        log.warning("This is for warnings")
        log.error("This is for error")
        log.critical("This is for critical")
