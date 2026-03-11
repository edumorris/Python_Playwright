import pytest


@pytest.mark.smoke # Creating tags
def test_initial_check(preWork, tearDown):
    print("This is the first test")

@pytest.mark.skip # Skip test
def test_second_check(preWork, tearDown
                      ):
    print("This is the second test")