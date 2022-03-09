import time
from POMDependencies import xpathclick

import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def test_node():
    global driver
    driver=webdriver.Chrome(executable_path="E:\KRN Files\Python\Selenium\Youtube\Browser Driver\chromedriver.exe")
    driver.maximize_window()
def test_get(test_node):
    driver.implicitly_wait(10)
    driver.get("http://192.168.0.199:9091/QuaLISWeb/#/login")
    time.sleep(6)
def test_login(test_node):
    #driver.find_element_by_xpath("//*[@id='sloginid']").send_keys("cdolman")
    xc=xpathclick(driver)
    xc.clickxpath("//*[text()='Login']")




