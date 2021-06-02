import pytest

from PythonTests.BaseClass import BaseClass


@pytest.mark.usefixtures("dataLoad")
class TestExample2(BaseClass):

    def test_editProfile(self, dataLoad):
        log = self.test_logging()
        log.info(dataLoad[0])
        log.info(dataLoad[2])