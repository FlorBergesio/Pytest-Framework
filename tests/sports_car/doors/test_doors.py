from pytest import mark

@mark.sports_car
@mark.doors
class DoorTests:

    @mark.smoke
    @mark.browser
    def test_all_doors_locked(self, chrome_browser):
        chrome_browser.get('https://www.uala.com.ar/')
        assert True