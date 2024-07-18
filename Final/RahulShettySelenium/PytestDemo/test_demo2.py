import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_firstProgram():
    msg = "Hi"
    assert msg == "hello","Test failed becoz string doesn't match"

#for running multiple testcases in order
@pytest.mark.run(order=1)
def test_SecondPgmCreditCard():
    a =4
    b= 2
    assert a+2 ==6, "Addition didnot match"
