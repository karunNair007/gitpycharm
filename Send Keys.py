import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome(executable_path=".\Drivers\chromedriver.exe")
driver.maximize_window()
driver.get("http://10.10.10.4:8889/login.jsp")
driver.find_element_by_xpath("(//input[@class='text medium-field'])[1]").send_keys("ate145")
driver.find_element_by_xpath("(//input[@class='text medium-field'])[2]").send_keys("Krishna@007")
driver.find_element_by_xpath("//input[@value='Log In']").click()
kk=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@id='greenhopper_menu']")))
kk.click()

#driver.quit()