def test_switch_between_tabs(chrome_browser):
    chrome_browser.get("https://techstepacademy.com/training-ground")
    chrome_browser.execute_script('window.open("http://techstepacademy.com/trial-of-the-stones","_blank");')
    handles = chrome_browser.window_handles
    chrome_browser.switch_to.window(handles[0])
    chrome_browser.switch_to.window(handles[-1])
    assert True