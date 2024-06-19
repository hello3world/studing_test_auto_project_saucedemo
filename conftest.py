import pytest


@pytest.fixture()
def set_up():
    print("Start test")

    yield

    print("Finish test")


@pytest.fixture(scope="module")
def set_group():
    print("Enter to System")

    yield

    print("Exit from system")