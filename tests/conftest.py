from pytest import fixture
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from config import Config

@fixture(scope='function')
def chrome_browser():
    browser = webdriver.Chrome(ChromeDriverManager().install())
    yield browser

    #Teardown
    print('Chrome browser teardown')

def pytest_addoption(parser):
    parser.addoption(
        "--env", 
        action="store",
        default="no-env",
        help="Environment to run the tests in"
    )

@fixture(scope='session')
def env(request):

    #Tomamos el parametro env de: pytest --env='XX' / pytest --env=XX / pytest --env XX

    return request.config.getoption("--env")

@fixture(scope='session')
def app_config(env):
    cfg = Config(env)
    return cfg