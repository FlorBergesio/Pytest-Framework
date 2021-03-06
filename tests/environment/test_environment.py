from pytest import mark

def test_environment_is_qa(env):
    assert env == 'qa'

def test_environment_is_dev(env):
    assert env == 'dev'

@mark.skip(reason="Staging environment not yet created")
def test_environment_is_staging(env):
    assert env == 'staging'

@mark.xfail(reason="Expected to fail when wrong environment is used")
def test_environment_is_env_wrong(env):
    SUPPORTED_ENVS: list
    SUPPORTED_ENVS = ['dev', 'qa']

    assert ( env.lower() in SUPPORTED_ENVS )

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
