
import time

from selenium import webdriver


driver=webdriver.Chrome(executable_path="E:\KRN Files\Python\Selenium\Youtube\Browser Driver\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(3)
driver.get("https://stackoverflow.com/questions/20986631/how-can-i-scroll-a-web-page-using-selenium-webdriver-in-python")
driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")


