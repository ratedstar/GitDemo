#Any file should start with test_ or end with _test
#Code should should be wrapped in a method and method name should start with test
# 2 Methods should not have same name
# Method names should have sense
#-k stands for method name execution, -s logs in out put, -v stands for more info metadata
# we can run specfic file with py.test <filename.py>
# We can run Tag tests using @pytest.mark.<tagname> terminal -m
# We can skip tests using @pytest.mark.skip
# @pytest.mark.xfail these will run the test put if it fails logs will not be printed out
# fixtures are used for setup and tear down methods
# conftest file is used for generalize fixtures and make it available to all the test files


import pytest

from Novoice_Pytest.Baseclass import BaseClass


class TestLog:

    def test_thirdPgm(setup):
        print("I will be executed after setup")

    def test_crossBrowser(crossBrowser):
        print(crossBrowser[1])
