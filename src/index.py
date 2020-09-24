from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver = webdriver.Firefox(executable_path='./geckodriver')


def main():
    print("SUCCESS")


main()
