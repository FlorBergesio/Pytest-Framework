from selenium.webdriver.common.by import By

def test_iframe(chrome_browser):
    chrome_browser.get("https://techstepacademy.com/iframe-training")
    iframeElement = chrome_browser.find_element(By.CSS_SELECTOR, "iframe")
    chrome_browser.switch_to.frame(iframeElement)
    textElementIframe = chrome_browser.find_element(By.CSS_SELECTOR, "div#block-ec928cee802cf918d26c div p")
    chrome_browser.switch_to.default_content()
    textElement = chrome_browser.find_element(By.CSS_SELECTOR, "div#block-5d3de848045889000188d389 div p")
    assert textElement.text == " Training Ground for IFrames and traditional frames"