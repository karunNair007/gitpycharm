from selenium import webdriver

import pytest
def test_kk():
    driver = webdriver.Chrome(executable_path="E:\KRN Files\Python\Selenium\Youtube\Browser Driver\chromedriver.exe")

    driver.get("https://www.facebook.com/")

    print(driver.title)
    print(driver.current_url)
    print(driver.page_source)
    driver.close()


