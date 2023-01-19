from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import pathlib

class Bot:
    def __init__(self):
        self.driverPath = str(pathlib.Path("chromedriver").parent.resolve())+"/chromedriver"
        self.chromeOptions = webdriver.ChromeOptions()
        self.chromeOptions.binary_location = "/Applications/Chromium.app/Contents/MacOS/Chromium"

    def setDriver(self):
        self.driver = webdriver.Chrome(service=Service(self.driverPath), options=self.chromeOptions)

    def tryGetting(self, elementXPATH):
        getting = True
        while getting:
            try:
                element = self.driver.find_element(By.XPATH, elementXPATH)
                getting = False
                return element
            except NoSuchElementException:
                continue

    def rest(self):
        print("Resting...")
        while True:
            continue

class ProxyRetrieverBot(Bot):
    def __init__(self):
        Bot.__init__(self)
        self.chromeOptions.add_argument("--headless")

    def getPage(self):
        self.driver.get("https://proxyscrape.com/share/l5ty3b9")

    def getProxies(self):
        proxies = self.tryGetting('//*[@id="proxyshare"]')
        self.rest()

