import time

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

driver=webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.get("http://192.168.0.199:9091/QuaLISWeb/#/login")
driver.maximize_window()
print(driver.title)
time.sleep(6)