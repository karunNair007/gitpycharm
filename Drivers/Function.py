import time

from selenium import webdriver

def driverpath(DP,URL,xpath):
    driver=webdriver.Chrome(executable_path=DP)
    driver.maximize_window()
    driver.implicitly_wait(4)
    driver.get(URL)
    driver.find_element_by_xpath(xpath).click()
    time.sleep(500)

driverpath("E:\KRN Files\Python\Selenium\Youtube\Browser Driver\chromedriver.exe","https://www.facebook.com/","//button[@value='1']")
