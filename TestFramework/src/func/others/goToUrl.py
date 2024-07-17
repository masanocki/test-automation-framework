from TestFramework.src.base import browser


def goToUrl(url):
    driver = browser.get_driver()
    driver.get(url)
