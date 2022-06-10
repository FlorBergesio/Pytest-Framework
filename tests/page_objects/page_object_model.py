from selenium.webdriver.common.by import By
from selenium import webdriver

class TrainingGroundPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://techstepacademy.com/training-ground"

    def go(self):
        self.driver.get(self.url)

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
