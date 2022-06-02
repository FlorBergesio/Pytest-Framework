from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of

def test_selenium_automated_input_value(chrome_browser):
    chrome_browser.get("https://techstepacademy.com/training-ground")
    input1Path = "input[id='ipt1']"
    input1Element = chrome_browser.find_element(By.CSS_SELECTOR, input1Path)
    input1Element.send_keys("Automated input content")
    assert input1Element.get_attribute("value") == "Automated input content"

def test_riddle_of_stone(chrome_browser):
    chrome_browser.get("https://techstepacademy.com/trial-of-the-stones")
    inputStonePath = "input[id='r1Input']"
    inputStoneElement = chrome_browser.find_element(By.CSS_SELECTOR, inputStonePath)
    inputStoneElement.send_keys("rock")
    buttonStonePath = "button[id='r1Btn']"
    buttonStoneElement = chrome_browser.find_element(By.CSS_SELECTOR, buttonStonePath)
    buttonStoneElement.click()
    passwordContainerStonePath = "div[id='passwordBanner']"
    passwordContainerStoneElement = chrome_browser.find_element(By.CSS_SELECTOR, passwordContainerStonePath)
    passwordStonePath = "//div[@id='passwordBanner']/h4"
    passwordStoneElement = chrome_browser.find_element(By.XPATH, passwordStonePath)
    WebDriverWait(chrome_browser, 10).until(visibility_of(passwordContainerStoneElement))
    inputSecretPath = "input[id='r2Input']"
    inputSecretElement = chrome_browser.find_element(By.CSS_SELECTOR, inputSecretPath)
    inputSecretElement.send_keys(passwordStoneElement.text)
    buttonSecretPath = "button[id='r2Butn']"
    buttonSecretElement = chrome_browser.find_element(By.CSS_SELECTOR, buttonSecretPath)
    buttonSecretElement.click()
    successContainerSecretPath = "div[id='successBanner1']"
    successContainerSecretElement = chrome_browser.find_element(By.CSS_SELECTOR, successContainerSecretPath)
    WebDriverWait(chrome_browser, 10).until(visibility_of(successContainerSecretElement))
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
    buttonMerchantPath = "button[id='r3Butn']"
    buttonMerchantElement = chrome_browser.find_element(By.CSS_SELECTOR, buttonMerchantPath)
    buttonMerchantElement.click()
    successContainerMerchantPath = "div[id='successBanner1']"
    successContainerMerchantElement = chrome_browser.find_element(By.CSS_SELECTOR, successContainerMerchantPath)
    WebDriverWait(chrome_browser, 10).until(visibility_of(successContainerMerchantElement))
    buttonFinalPath = "button[id='checkButn']"
    buttonFinalElement = chrome_browser.find_element(By.CSS_SELECTOR, buttonFinalPath)
    buttonFinalElement.click()
    successContainerFinalPath = "div[id='trialCompleteBanner']"
    successContainerFinalElement = chrome_browser.find_element(By.CSS_SELECTOR, successContainerFinalPath)
    WebDriverWait(chrome_browser, 10).until(visibility_of(successContainerFinalElement))
    successTextPath = "//div[@id='trialCompleteBanner']/h4"
    successTextElement = chrome_browser.find_element(By.XPATH, successTextPath)
    assert successTextElement.text == "Trial Complete"
