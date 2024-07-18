#Any file should start with test_ or end with _test
#Code should should be wrapped in a method and method name should start with test
# 2 Methods should not have same name
# Method names should have sense
#-k stands for method name execution, -s logs in out put, -v stands for more info metadata
# we can run specfic file with py.test <filename.py>
# We can run Tag tests using @pytest.mark.<tagname> terminal -m
# We can skip tests using @pytest.mark.skip
# @pytest.mark.xfail these will run the test put if it fails logs will not be printed out
# we use scope='class' when we want to run setup and teardown once before class and after class
# datadrivenpy.test and parameterization can be done with return statements

import pytest
@pytest.mark.skip
def test_firstPgm():
    print("Hello")

@pytest.mark.smoke
def test_2ndPgm():
    print("HI")

