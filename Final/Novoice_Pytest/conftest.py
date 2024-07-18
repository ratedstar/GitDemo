import pytest

@pytest.yield_fixture(scope="class")
def setUp():
    print("Running method level setup")
    yield
    print("Running method level teardown")

@pytest.fixture(scope='class')
def setup():
    print("I will be executed first")
    yield
    print("I will be executed last")

@pytest.yield_fixture(scope='module')
def oneTimeSetUp():
    print("Running one time setup")
    yield
    print("Running one time teardown ")
@pytest.fixture()
def dataLoad():
    print("User profile data is being created")
    return["Rahul","Shetty","rahulshetty@gmail.com"]

@pytest.fixture(params=[('chrome',"Rahul","teacher"),('firefox',"Shetty"),('IE',"ss")])
def crossBrowser(request):
    return request.param