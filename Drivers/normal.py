import time

import pytest
from selenium import webdriver

var1="E:\KRN Files\Python\Selenium\Youtube\Browser Driver\chromedriver.exe"
var2="http://192.168.0.199:9091/QuaLISWeb/#/batchCreation"
@pytest.fixture(scope="session")
def test_kk():
    driver = webdriver.Chrome(executable_path="E:\KRN Files\Python\Selenium\Youtube\Browser Driver\chromedriver.exe")
    driver.get("http://192.168.0.199:9091/QuaLISWeb/#/batchCreation")
    time.sleep(4)
    driver.find_element_by_xpath("//*[@name='sloginid']").send_keys("cdolman")
    time.sleep(4)
    driver.find_element_by_xpath("//*[@name='spassword']").send_keys("123")
    time.sleep(4)
    driver.find_element_by_xpath("//*[text()='Login']").click()
    time.sleep(100)