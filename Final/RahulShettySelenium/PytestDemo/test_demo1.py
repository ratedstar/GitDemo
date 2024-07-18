# Any test file should start with test_ or end with _test
# pytest method name should start with test
#Any code should be wrapped in method and every method is treated as test case
# Method name should have sense
# -k stands for method name execution, -s logs in output -v stands for more info metadata
# we can run specific file with py.test <filename>
# we can mark (tag) tests @pytest.mark.smoke and run with -m
# we can skip test with @pytest.mark.skip
# fixtures are used for setuo and teardown methods conftest file is to genralize
# fixutures and make it available for all test cases
# when we define fixture pyscope to class level, it will get executed before and after class
# datadriven and parameterisation can be done with return statements using tuple format

import pytest


@pytest.mark.smoke
def test_firstPgm():
    print("Hello")

#@pytest.mark.xfail
def test_secondPgmCreditCard(setup):
    print("hey")

def test_crossbrower(crossBrowser):
    print(crossBrowser)
    print(crossBrowser[1])