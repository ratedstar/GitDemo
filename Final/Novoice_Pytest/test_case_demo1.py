import pytest


@pytest.yield_fixture()
def setUp():
    print("Once before every demo1  method")
    yield
    print("Once after every demo 1 method ")
def test_methodA(setUp):
    print("Running demo1 method A")
def test_methodB(setUp):
    print("Running demo1 method B")