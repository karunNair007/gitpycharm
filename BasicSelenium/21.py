import time

from selenium import webdriver
driver = webdriver.Chrome (executable_path="E:\KRN Files\Python\Selenium\Youtube\Browser Driver\chromedriver.exe")
driver.maximize_window()
driver.get("http://192.168.0.199:9091/QuaLISWeb/#/login")
driver.find_element_by_xpath("//*[@name='sloginid']").send_keys("cdolman")
time.sleep(4)
driver.find_element_by_xpath("//*[@name='spassword']").click()
time.sleep(4)
s=driver.find_element_by_xpath("(//*[@class='react-select__control css-yk16xz-control'])[1]")
print(s.text)