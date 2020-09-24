from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def openBrowser():
    driver = webdriver.Firefox(executable_path='./geckodriver')
