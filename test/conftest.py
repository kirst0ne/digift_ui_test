import pytest
from fixture.application import Application
import json
import os.path


fixture = None
target = None


def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as config_file:
            target = json.load(config_file)
    return target


@pytest.fixture(scope="session")
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    web_config = load_config(request.config.getoption("--target"))["web"]
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=web_config['baseUrl'])
    return fixture

#@pytest.fixture(scope="session")
#def app(request):
#    fixture = Application()
#    fixture.open_home_page()
#    request.addfinalizer(fixture.destroy)
#    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request, app):
    def fin():
        app.destroy()
    request.addfinalizer(fin)
    return app


@pytest.fixture
def check_ui(request):
    return request.config.getoption("--check_ui")


@pytest.fixture
def check_ui(request):
    return request.config.getoption("--check_ui")


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--target", action="store", default="target.json")
    parser.addoption("--check_ui", action="store_true")
