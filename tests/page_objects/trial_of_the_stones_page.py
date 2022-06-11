from selenium.webdriver.common.by import By

from .base_page_object import BasePage
from .base_element import BaseElement

class TrialStonesPage(BasePage):

    url = "https://techstepacademy.com/trial-of-the-stones"

    @property
    def stone_input(self):
        return BaseElement(driver=self.driver, by=By.CSS_SELECTOR, value="input[id='r1Input']")

    @property
    def stone_button(self):
        return BaseElement(driver=self.driver, by=By.CSS_SELECTOR, value="button[id='r1Btn']")

    @property
    def stone_password(self):
        return BaseElement(driver=self.driver, by=By.XPATH, value="//div[@id='passwordBanner']/h4")

    @property
    def secrets_input(self):
        return BaseElement(driver=self.driver, by=By.CSS_SELECTOR, value="input[id='r2Input']")

    @property
    def secrets_button(self):
        return BaseElement(driver=self.driver, by=By.CSS_SELECTOR, value="button[id='r2Butn']")