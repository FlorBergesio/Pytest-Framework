from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_selenium_automated_input_value(chrome_browser):
    chrome_browser.get("https://techstepacademy.com/training-ground")
    input1Path = "input[id='ipt1']"
    input1Element = chrome_browser.find_element(By.CSS_SELECTOR, input1Path)
    input1Element.send_keys("Automated input content")
    time.sleep(1)
    assert input1Element.get_attribute("value") == "Automated input content"

def test_riddle_of_stone(chrome_browser):
    chrome_browser.get("https://techstepacademy.com/trial-of-the-stones")
    inputStonePath = "input[id='r1Input']"
    inputStoneElement = chrome_browser.find_element(By.CSS_SELECTOR, inputStonePath)
    inputStoneElement.send_keys("rock")
    time.sleep(1)
    buttonStonePath = "button[id='r1Btn']"
    buttonStoneElement = chrome_browser.find_element(By.CSS_SELECTOR, buttonStonePath)
    buttonStoneElement.click()
    time.sleep(1)
    passwordContainerStonePath = "div[id='passwordBanner']"
    passwordContainerStoneElement = chrome_browser.find_element(By.CSS_SELECTOR, passwordContainerStonePath)
    """ passwordStonePath = "//div[@id='passwordBanner']/h4"
    passwordStoneElement = chrome_browser.find_element(By.XPATH, passwordStonePath) """
    time.sleep(1)

    assert passwordContainerStoneElement.get_attribute("style") == "display: block;"
