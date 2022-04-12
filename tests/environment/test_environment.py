def test_environment_is_qa(env):
    assert env == 'qa'

def test_environment_is_dev(env):
    assert env == 'dev'

def test_base_url_in_dev_env(app_config, chrome_browser):
    url = app_config.base_url
    port = app_config.app_port
    chrome_browser.get(url)
    assert url == 'https://www.uala.com.ar/'
    assert port == 8080

def test_base_url_in_qa_env(app_config, chrome_browser):
    url = app_config.base_url
    port = app_config.app_port
    chrome_browser.get(url)
    assert url == 'https://www.uala.com.co/'
    assert port == 80
