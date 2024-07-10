import pytest


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--hub_host")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture()
def hub_host(request):
    return request.config.getoption("--hub_host")
