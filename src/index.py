from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


# caps = DesiredCapabilities.FIREFOX.copy()
# caps['marionette'] = False
# webdriver.Firefox(capabilities=caps, executable_path='./geckodriver')
webdriver.Chrome(executable_path='~/Desktop/projects/e-simBot/chromedriver')
webdriver.get('www.google.com')


def main():
    print("SUCCESS")
    print(sys.path)


main()
