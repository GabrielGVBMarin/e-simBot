from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def openBrowser():
    return webdriver.Firefox(executable_path='./geckodriver')


def getLink(driver, link):
    driver.get(link)


def run(link):
    driver = openBrowser()
    getLink(driver, link)
