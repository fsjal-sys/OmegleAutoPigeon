from utils import *

def getPage(driver):
    driver.get("https://proxyscrape.com/share/l5ty3b9")
    try:
        textArea = tryGetting(driver, "XPATH", '//*[@id="proxyshare"]').text
        print(textArea)
    except textArea == "Loading...":
        print("it's loading")

def main():
    driver = createDriver()
    getPage(driver)
    rest()

main()
