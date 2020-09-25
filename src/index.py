from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.select import Select
from dotenv import load_dotenv
from pathlib import Path
import os


def openBrowser():
    return webdriver.Firefox(executable_path='./geckodriver')


def getLink(driver, link):
    driver.get(link)


def login(driver):
    driver.find_element_by_xpath("//input[@name='login']").send_keys(os.getenv("E-SIM-USER")
                                                                     )
    driver.find_element_by_xpath(
        "//input[@name='password']").send_keys(os.getenv("E-SIM-PASSWORD")
                                               )
    driver.find_element_by_xpath("//button[@type='submit']").click()


def run(link):
    browser = openBrowser()
    getLink(browser, link)
    login(browser)


def settings():
    env_path = Path('.') / '../.env'
    load_dotenv(dotenv_path=env_path)


settings()
