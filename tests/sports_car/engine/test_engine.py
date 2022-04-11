from pytest import mark

@mark.sports_car
@mark.engine
class EngineTests:

    @mark.smoke
    @mark.browser
    def test_engine_start(self, chrome_browser):
        chrome_browser.get('https://www.uala.com.co/')
        assert True

    @mark.smoke
    def test_engine_off(self):
        assert True

    def test_engine_self_destruct(self):
        assert True