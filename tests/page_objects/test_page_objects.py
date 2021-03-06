from .trial_of_the_stones_page import TrialStonesPage
from .training_ground_page import TrainingGroundPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import alert_is_present
from selenium.webdriver.common.alert import Alert

from pytest import mark

@mark.skip(reason="Original code has been commented out. New code not yet created")
def test_page_object_input_field(chrome_browser):
    test_text = "Testing Page Object input field"

    training_ground_page = TrainingGroundPage(driver=chrome_browser)
    training_ground_page.go()
    training_ground_page.type_inputElement_field(test_text)
    inputText = training_ground_page.get_inputElement_text()
    print(inputText)
    assert inputText == test_text
    chrome_browser.quit()

def test_page_object_base_element_button_click(chrome_browser):
    training_ground_page = TrainingGroundPage(driver=chrome_browser)
    training_ground_page.go()
    training_ground_page.button1.click()
    WebDriverWait(chrome_browser, 10).until(alert_is_present())
    alertElement = Alert(chrome_browser)
    assert alertElement.text == "You clickedButton1."
    chrome_browser.quit()

def test_page_object_base_element_button_text(chrome_browser):
    training_ground_page = TrainingGroundPage(driver=chrome_browser)
    training_ground_page.go()
    assert training_ground_page.button1.text == 'Button1'
    chrome_browser.quit()

def test_page_object_trial_of_the_stones(chrome_browser):
    trial_page = TrialStonesPage(driver=chrome_browser)
    trial_page.go()
    trial_page.stone_input.input_text("rock")
    trial_page.stone_button.click()
    assert trial_page.stone_password.text == "bamboo"
    chrome_browser.quit()
