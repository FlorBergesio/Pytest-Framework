from selenium import webdriver
from selenium.webdriver.common.by import By
from operator import attrgetter
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
    passwordStonePath = "//div[@id='passwordBanner']/h4"
    passwordStoneElement = chrome_browser.find_element(By.XPATH, passwordStonePath)
    time.sleep(1)
    if passwordContainerStoneElement.get_attribute("style") == "display: block;":
        inputSecretPath = "input[id='r2Input']"
        inputSecretElement = chrome_browser.find_element(By.CSS_SELECTOR, inputSecretPath)
        inputSecretElement.send_keys(passwordStoneElement.text)
        time.sleep(1)
        buttonSecretPath = "button[id='r2Butn']"
        buttonSecretElement = chrome_browser.find_element(By.CSS_SELECTOR, buttonSecretPath)
        buttonSecretElement.click()
        time.sleep(1)
        successContainerSecretPath = "div[id='successBanner1']"
        successContainerSecretElement = chrome_browser.find_element(By.CSS_SELECTOR, successContainerSecretPath)
        if successContainerSecretElement.get_attribute("style") == "display: block;":
            wealthListPath = "//label/../p"
            wealthList = chrome_browser.find_elements(By.XPATH, wealthListPath)
            maxWealth = 0
            for wealth in wealthList:
                if int(wealth.text) > maxWealth:
                    maxWealth = int(wealth.text)
            richestMerchantPath = "//label/../p[contains(text(),'" + str(maxWealth) + "')]/../span/b"
            richestMerchantElement = chrome_browser.find_element(By.XPATH, richestMerchantPath)
            inputMerchantPath = "input[id='r3Input']"
            inputMerchantElement = chrome_browser.find_element(By.CSS_SELECTOR, inputMerchantPath)
            inputMerchantElement.send_keys(richestMerchantElement.text)
            time.sleep(1)
            buttonMerchantPath = "button[id='r3Butn']"
            buttonMerchantElement = chrome_browser.find_element(By.CSS_SELECTOR, buttonMerchantPath)
            buttonMerchantElement.click()
            time.sleep(1)
            successContainerMerchantPath = "div[id='successBanner1']"
            successContainerMerchantElement = chrome_browser.find_element(By.CSS_SELECTOR, successContainerMerchantPath)
            if successContainerMerchantElement.get_attribute("style") == "display: block;":
                buttonFinalPath = "button[id='checkButn']"
                buttonFinalElement = chrome_browser.find_element(By.CSS_SELECTOR, buttonFinalPath)
                buttonFinalElement.click()
                time.sleep(1)
                successContainerFinalPath = "div[id='trialCompleteBanner']"
                successContainerFinalElement = chrome_browser.find_element(By.CSS_SELECTOR, successContainerFinalPath)
                if successContainerFinalElement.get_attribute("style") == "display: block;":
                    successTextPath = "//div[@id='trialCompleteBanner']/h4"
                    successTextElement = chrome_browser.find_element(By.XPATH, successTextPath)
                    assert successTextElement.text == "Trial Complete"
