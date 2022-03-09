import time

import pytest
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver

class Testkk:

    @pytest.fixture(scope="class")
    @allure.severity(allure.severity_level)
    def test_begin(self):
        global driver
        driver = webdriver.Chrome(
            executable_path="E:\KRN Files\Python\Selenium\Youtube\Browser Driver\chromedriver.exe")
        driver.maximize_window()
        yield
        driver.close()

    def test_1(self,test_begin):
        driver.get("http://192.168.0.199:9091/QuaLISWeb/#/login")
        driver.find_element_by_xpath("//*[@id='sloginid']").send_keys("cdolman")
        driver.find_element_by_xpath("//*[@id='spassword']").send_keys("123")
        driver.find_element_by_xpath("//*[text()='Login']").click()
        time.sleep(6)

    def test_2(self,test_begin):
        allure.attach(driver.get_screenshot_as_png(), name="kk", attachment_type=AttachmentType.PNG)
        driver.find_element_by_xpath("//*[text()='Registration']").click()
        time.sleep(6)

