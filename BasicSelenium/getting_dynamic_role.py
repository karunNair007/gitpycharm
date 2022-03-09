
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.maximize_window()
driver.get("http://192.168.0.199:9091/QuaLISWeb/#/login")
driver.find_element_by_xpath("//input[@id='sloginid']").send_keys("cdolman")
time.sleep(2)
driver.find_element_by_xpath("//input[@id='spassword']").send_keys("123")
time.sleep(2)
print(driver.find_element_by_xpath("(//*[@class='react-select__single-value css-1uccc91-singleValue'])[1]").text)