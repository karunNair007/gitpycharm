from selenium import webdriver
import os

path = "E:\KRN Files\Python\Selenium\Youtube\Browser Driver\chromedriver1.exe"
result = os.path.isfile(path)
print(result)
if result == True:
    driver = webdriver.Chrome(executable_path="E:\KRN Files\Python\Selenium\Youtube\Browser Driver\chromedriver.exe")
    driver.get("http://10.10.10.4:8889/login.jsp")
    driver.find_element_by_xpath("(//input[@class='text medium-field'])[1]").send_keys("ate145")
    driver.find_element_by_xpath("(//input[@class='text medium-field'])[2]").send_keys("Krishna@007")
    driver.find_element_by_xpath("//input[@value='Log In']").click()
    time.sleep(3)
    # driver.quit()
else:
    print("File  not found, kindly place the chrome driver in the respective path")
