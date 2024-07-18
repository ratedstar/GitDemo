#Any file should start with test_ or end with _test
#Code should should be wrapped in a method and method name should start with test
# 2 Methods should not have same name


import pytest


@pytest.mark.smoke
def test_firstPgm():
    msg = "Hey"
    assert msg == "Hey","This test is failed"
@pytest.mark.xfail
def test_SecondPgm():
    a=4
    b= 6
    assert a+2 == 8, "Addition doesnot match"
