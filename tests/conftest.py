from pytest import fixture
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@fixture(scope='function')
def chrome_browser():
    browser = webdriver.Chrome(ChromeDriverManager().install())
    return browser