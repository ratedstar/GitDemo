import pytest


@pytest.mark.usefixtures("setUp")
class TestExamples:

    def test_demo1(self):
        print("I am demo1")
    def test_demo2(self):
        print("I am demo2")
    def test_demo3(self):
        print("I am demo3")
    def test_demo4(self):
        print("I am demo4")