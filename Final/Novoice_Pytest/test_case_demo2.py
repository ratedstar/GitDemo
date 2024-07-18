import pytest


@pytest.yield_fixture()
def setUp():
    print("Once before demo2 every method")
    yield
    print("Once after every demo2 method ")
def test_methodA(setUp):
    print("Running demo2 method A")
def test_methodB(setUp):
    print("Running demo2 method B")