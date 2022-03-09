import time

import pytest
from selenium import webdriver
4

@pytest.mark.login
def test_login1():
    driver=webdriver.Chrome(executable_path="E:\KRN Files\Python\Selenium\Youtube\Browser Driver\chromedriver.exe")
    driver.maximize_window()
    driver.get("http://192.168.0.199:9091/QuaLISWeb/#/login")
    time.sleep(4)
    driver.find_element_by_xpath("//*[@id='sloginid']").send_keys("cdolman")
    driver.find_element_by_xpath("//*[@id='spassword']").send_keys("123")
    time.sleep(4)
    driver.find_element_by_xpath("//*[text()='Login']").click()

@pytest.mark.login
def test_login2():
    driver=webdriver.Chrome(executable_path="E:\KRN Files\Python\Selenium\Youtube\Browser Driver\chromedriver.exe")
    driver.maximize_window()
    driver.get("http://192.168.0.199:9091/QuaLISWeb/#/login")
    time.sleep(4)
    driver.find_element_by_xpath("//*[@id='sloginid']").send_keys("cdolman")
    driver.find_element_by_xpath("//*[@id='spassword']").send_keys("123")
    time.sleep(4)
    driver.find_element_by_xpath("//*[text()='Login']").click()