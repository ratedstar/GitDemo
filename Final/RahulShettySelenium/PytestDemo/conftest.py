import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will get executed first")
    yield
    print("I will get executed at the last")

@pytest.fixture()
def dataload():
    print("User profile data is being created")
    return["Kaamesh","indraganti","kaamesh.test@test.com"]

@pytest.fixture(params=[("chrome","kaamesh"),("firefox","MMA"),("IE","YogaTrainer")])
def crossBrowser(request):
    return request.param
