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

    """ Find first trial's input and write the answer to the riddle """
    inputStonePath = "input[id='r1Input']"
    inputStoneElement = chrome_browser.find_element(By.CSS_SELECTOR, inputStonePath)
    inputStoneElement.send_keys("rock")

    """ Find first trial's button to check answer and click it """
    buttonStonePath = "button[id='r1Btn']"
    buttonStoneElement = chrome_browser.find_element(By.CSS_SELECTOR, buttonStonePath)
    buttonStoneElement.click()

    """ Check if first trial's answer is displayed """
    passwordContainerStonePath = "div[id='passwordBanner']"
    passwordContainerStoneElement = chrome_browser.find_element(By.CSS_SELECTOR, passwordContainerStonePath)
    WebDriverWait(chrome_browser, 10).until(visibility_of(passwordContainerStoneElement))

    """ Find first trial's password """
    passwordStonePath = "//div[@id='passwordBanner']/h4"
    passwordStoneElement = chrome_browser.find_element(By.XPATH, passwordStonePath)

    """ Find second trial's input and write the password """
    inputSecretPath = "input[id='r2Input']"
    inputSecretElement = chrome_browser.find_element(By.CSS_SELECTOR, inputSecretPath)
    inputSecretElement.send_keys(passwordStoneElement.text)

    """ Find second trial's button to check answer and click it """
    buttonSecretPath = "button[id='r2Butn']"
    buttonSecretElement = chrome_browser.find_element(By.CSS_SELECTOR, buttonSecretPath)
    buttonSecretElement.click()

    """ Check if second trial's answer is displayed """
    successContainerSecretPath = "div[id='successBanner1']"
    successContainerSecretElement = chrome_browser.find_element(By.CSS_SELECTOR, successContainerSecretPath)
    WebDriverWait(chrome_browser, 10).until(visibility_of(successContainerSecretElement))

    """ Get list of third trial's merchant's wealth and find max value """
    wealthListPath = "//label/../p"
    wealthList = chrome_browser.find_elements(By.XPATH, wealthListPath)
    maxWealth = 0
    for wealth in wealthList:
        if int(wealth.text) > maxWealth:
            maxWealth = int(wealth.text)

    """ Find richest merchant using max wealth value """
    richestMerchantPath = "//label/../p[contains(text(),'" + str(maxWealth) + "')]/../span/b"
    richestMerchantElement = chrome_browser.find_element(By.XPATH, richestMerchantPath)

    """ Find third trial's input and write the name of richest merchant """
    inputMerchantPath = "input[id='r3Input']"
    inputMerchantElement = chrome_browser.find_element(By.CSS_SELECTOR, inputMerchantPath)
    inputMerchantElement.send_keys(richestMerchantElement.text)

    """ Find third trial's button to check answer and click it """
    buttonMerchantPath = "button[id='r3Butn']"
    buttonMerchantElement = chrome_browser.find_element(By.CSS_SELECTOR, buttonMerchantPath)
    buttonMerchantElement.click()

    """ Check if third trial's answer is displayed """
    successContainerMerchantPath = "div[id='successBanner1']"
    successContainerMerchantElement = chrome_browser.find_element(By.CSS_SELECTOR, successContainerMerchantPath)
    WebDriverWait(chrome_browser, 10).until(visibility_of(successContainerMerchantElement))

    """ Find final button to check all trials and click it """
    buttonFinalPath = "button[id='checkButn']"
    buttonFinalElement = chrome_browser.find_element(By.CSS_SELECTOR, buttonFinalPath)
    buttonFinalElement.click()

    """ Check if final completion text is displayed """
    successContainerFinalPath = "div[id='trialCompleteBanner']"
    successContainerFinalElement = chrome_browser.find_element(By.CSS_SELECTOR, successContainerFinalPath)
    WebDriverWait(chrome_browser, 10).until(visibility_of(successContainerFinalElement))

    """ Find final completion text """
    successTextPath = "//div[@id='trialCompleteBanner']/h4"
    successTextElement = chrome_browser.find_element(By.XPATH, successTextPath)
    assert successTextElement.text == "Trial Complete"
