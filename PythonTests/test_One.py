import pytest


@pytest.mark.usefixtures("setup")
class TestOne:

    def test_m1(self):
        assert 1 < 2

    # @pytest.mark.xfail
    def test_s1(self):
        assert "john" == "michael"

    @pytest.mark.smoke
    def test_s2(self):
        assert "peter" == "peter"

    @pytest.mark.skip
    def test_s3(self):
        assert "me" == "I"

    def test_crossBrowser(self, crossBrowser):
        print(crossBrowser)