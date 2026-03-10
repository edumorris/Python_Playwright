import pytest

# function will run for every test in the file.
# "module/class" will run once.
# "Session" will run once for whole execution
@pytest.fixture(scope="function")
def preWork():
    print("Setup  browser instance")