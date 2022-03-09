import time

import pytest

from selenium import webdriver


bp = "E:\KRN Files\Python\Selenium\Youtube\Browser Driver\chromedriver.exe"
link = "http://192.168.0.199:9091/QuaLISWeb/#/login"


@pytest.mark.parametrize("test_input,expected", [(bp, link), (bp, link), (bp, link)])
def test_eval1(test_input, expected):
    driver = webdriver.Chrome(executable_path=test_input)
    driver.get(expected)
    time.sleep(4)
    driver.find_element_by_xpath("//*[@name='sloginid']").send_keys("cdolman")
    time.sleep(4)
    driver.find_element_by_xpath("//*[@name='spassword']").send_keys("123")
    time.sleep(4)
    driver.find_element_by_xpath("//*[text()='Login']").click()
    time.sleep(100)
