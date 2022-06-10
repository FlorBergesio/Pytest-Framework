from .page_object_model import TrainingGroundPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of, alert_is_present

def test_page_object_input_field(chrome_browser):
    test_text = "Testing Page Object input field"

    training_ground_page = TrainingGroundPage(driver=chrome_browser)
    training_ground_page.go()
    training_ground_page.type_inputElement_field(test_text)
    inputText = training_ground_page.get_inputElement_text()
    print(inputText)
    assert inputText == test_text
