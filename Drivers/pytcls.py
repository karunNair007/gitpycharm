import time

import pytest
from selenium import webdriver


class Testkkm():
    @pytest.fixture(scope="class")
    def test_node(self):
        global driver
        driver=webdriver.Chrome(executable_path="E:\KRN Files\Python\Selenium\Youtube\Browser Driver\chromedriver.exe")
        driver.maximize_window()
        time.sleep(5)

    def test_first(self,test_node):
        driver.get("http://192.168.0.199:9091/QuaLISWeb/#/login")
        driver.find_element_by_xpath("//*[@id='sloginid']").send_keys("cdolman")
        driver.find_element_by_xpath("//*[@id='spassword']").send_keys("123")
        time.sleep(5)

    def test_second(self,test_node):
        driver.find_element_by_xpath("//*[text()='Login']").click()
        time.sleep(5)

    def test_third(self,test_node):
        driver.find_element_by_xpath("//*[text()='Registration']").click()
        time.sleep(5)