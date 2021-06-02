import pytest


@pytest.fixture()
def setup():
    print("I will be executed first")
    yield
    print("I will be executed last")


@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return ("Rahul", "Shetty", "rahulshettyacademy.com")


@pytest.fixture(params=["Chrome", "Firefox", "IE"])
def crossBrowser(request):
    return request.param
