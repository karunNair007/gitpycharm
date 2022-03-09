import time
import pyscreenshot


from selenium import webdriver
#from selenium.webdriver.common.keys import keys

driver=webdriver.Chrome(executable_path="E:\KRN Files\Python\Selenium\Youtube\Browser Driver\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.facebook.com/")
emailtextbox=driver.find_element_by_xpath("//input[@type='text']")
print(emailtextbox.is_displayed())
print(emailtextbox.is_enabled())
driver.find_element_by_xpath("(//a[@role='button'])[2]").click()
time.sleep(2)
radiobutton=driver.find_element_by_xpath("(//input[@type='radio'])[2]")
screeshotfilename="E:\ScreenShots\\ test.png"
pyscreenshot.grab().save(screeshotfilename)
print(radiobutton.is_selected())
driver.quit()
