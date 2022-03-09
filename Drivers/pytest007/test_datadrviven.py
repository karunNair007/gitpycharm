import time
from configparser import ConfigParser

import pytest
from selenium import webdriver


def confg2(section,key1,key2):
    config = ConfigParser()
    config.read("C:\\Users\\Karun\\PycharmProjects\\Sel;enium with Python\\Drivers\\configuration.ini")
    k1=config.get(section, key1)
    k2 = config.get(section, key2)
    k3 = config.get(section, key1)
    k4 = config.get(section, key2)
    kk = []
    kkk=[]
    mm=[]
    kk.insert(0, k1)
    kk.insert(1, k2)
    kkk.insert(1,kk)
    kkk.insert(2, kk)
    return [kk]

@pytest.mark.parametrize("var1,var2",confg2("login credentials","un","pswd"))
def test_login(var1,var2):
    driver=webdriver.Chrome(executable_path="E:\KRN Files\Python\Selenium\Youtube\Browser Driver\chromedriver.exe")
    driver.maximize_window()
    driver.get("http://192.168.0.199:9091/QuaLISWeb/#/login")
    time.sleep(4)
    driver.find_element_by_xpath("//*[@id='sloginid']").send_keys(var1)
    driver.find_element_by_xpath("//*[@id='spassword']").send_keys(var2)
    time.sleep(4)
    driver.find_element_by_xpath("//*[text()='Login']").click()
    time.sleep(4)