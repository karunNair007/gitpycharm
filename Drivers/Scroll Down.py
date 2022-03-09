import time

from selenium import webdriver


driver=webdriver.Chrome(executable_path="E:\KRN Files\Python\Selenium\Youtube\Browser Driver\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(3)
driver.get("http://192.168.0.199:9091/QuaLISWeb/#/organisation")
driver.find_element_by_xpath("//input[@id='sloginid']").send_keys("cdolman")
driver.find_element_by_xpath("//input[@id='spassword']").send_keys("Admin@123")
driver.find_element_by_xpath("//button[text()='Login']").click()
driver.find_element_by_xpath("(//img[@alt='sidebar'])[3]").click()
driver.find_element_by_xpath("//span[text()='Organisation']").click()
driver.find_element_by_xpath("//*[@nformcode='54']").click()
org=driver.find_element_by_xpath("//*[text()='Lab:IPV']")
var = org.location_once_scrolled_into_view
print(var)
driver.find_element_by_xpath("//*[text()='Lab:IPV']").click()

