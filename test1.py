import time

from selenium import webdriver


driver = webdriver.Firefox(executable_path="E:\KRN Files\Python\Selenium\Youtube\Browser Driver\geckodriver.exe")
driver.get("https://www.facebook.com/")
driver.implicitly_wait(5)
driver.find_element_by_xpath("(//a[@role='button'])[2]").click()
driver.execute_script("window.open('https://github.com/mozilla/geckodriver/releases','new window')")
#driver.get("https://github.com/mozilla/geckodriver/releases")

driver.title
driver.back()
driver.forward()
driver.quit()

