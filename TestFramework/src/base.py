from selenium import webdriver
import time


class Browser:
    def __init__(self):
        self.driver = None

    def start(self):
        if self.driver is None:
            self.driver = webdriver.Chrome()

    def quit(self):
        if self.driver is not None:
            self.driver.quit()
            self.driver = None

    def get_driver(self):
        return self.driver


browser = Browser()


def makeTest(testFunc):
    browser.start()
    try:
        testFunc()
    finally:
        browser.quit()


from .func.others.goToUrl import goToUrl
