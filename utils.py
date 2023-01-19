from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import urllib
import pathlib

def rest():
    while True:
        pass

def tryGetting(driver, elementType, element):
    """
    Takes driver, element type, and the element path as arguments.
    The driver will look for that element and when it finds it,
    it will return the element object when it becomes accessible.
    """
    getting = True
    while getting:
        try:
            if (elementType == "CLASS_NAME"):
                element = driver.find_element(By.CLASS_NAME, element)
                getting = False
            elif (elementType == "XPATH"):
                element = driver.find_element(By.XPATH, element)
                getting = False
            return element
        except NoSuchElementException:
            continue

def createDriver():
    options = webdriver.ChromeOptions()
    options.binary_location = "/Applications/Chromium.app/Contents/MacOS/Chromium"
    driverPath = "/Users/farhan/Documents/Projects/textbook/chromedriver"
    driver = webdriver.Chrome(driverPath, chrome_options=options)
    return driver
