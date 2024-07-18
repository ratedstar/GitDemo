import pytest

@pytest.mark.run(order=2)
def test_methodA(oneTimeSetUp, setUp):
    print("Running demo1 method A")
@pytest.mark.run(order=4)
def test_methodB(oneTimeSetUp, setUp):
    print("Running demo1 method B")
@pytest.mark.run(order=3)
def test_methodC(oneTimeSetUp, setUp):
    print("Running demo1 method C")
@pytest.mark.run(order=1)
def test_methodD(oneTimeSetUp, setUp):
    print("Running demo1 method D")
@pytest.mark.run(order=5)
def test_methodE(oneTimeSetUp, setUp):
    print("Running demo1 method E")
@pytest.mark.run(order=6)
def test_methodF(oneTimeSetUp, setUp):
    print("Running demo1 method F")