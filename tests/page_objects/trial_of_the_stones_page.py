from selenium.webdriver.common.by import By

from .base_page_object import BasePage
from .base_element import BaseElement
from .locator import Locator

class TrialStonesPage(BasePage):

    url = "https://techstepacademy.com/trial-of-the-stones"

    @property
    def stone_input(self):
        locator = Locator(by=By.CSS_SELECTOR, value="input[id='r1Input']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def stone_button(self):
        locator = Locator(by=By.CSS_SELECTOR, value="button[id='r1Btn']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def stone_password(self):
        locator = Locator(by=By.XPATH, value="//div[@id='passwordBanner']/h4")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def secrets_input(self):
        locator = Locator(by=By.CSS_SELECTOR, value="input[id='r2Input']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def secrets_button(self):
        locator = Locator(by=By.CSS_SELECTOR, value="button[id='r2Butn']")
        return BaseElement(driver=self.driver, locator=locator)