from selenium.webdriver.common.by import By

from .base_page_object import BasePage
from .base_element import BaseElement

class TrainingGroundPage(BasePage):

    url = "https://techstepacademy.com/training-ground"

    """ 
    First iteration of code, prior to cleanup with abstraction of BaseElement

    def type_inputElement_field(self, text):
        inputElement = self.driver.find_element(By.CSS_SELECTOR, "input[id='ipt1']")
        inputElement.clear()
        inputElement.send_keys(text)
        return None

    def get_inputElement_text(self):
        inputElement = self.driver.find_element(By.CSS_SELECTOR, "input[id='ipt1']")
        inputElement_text = inputElement.get_attribute("value")
        return inputElement_text

    def click_buttonElement_1(self):
        buttonElement = self.driver.find_element(By.CSS_SELECTOR, "button#b1")
        buttonElement.click()
        return None
    """

    @property
    def button1(self):
        return BaseElement(driver=self.driver, by=By.ID, value='b1')