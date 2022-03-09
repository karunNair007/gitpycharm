import time

from selenium import webdriver


driver=webdriver.Chrome(executable_path="chromedriver.exe")
driver.maximize_window()

# Assign URL
url = "https://www.geeksforgeeks.org/"

# New Url
new_url = "https://www.facebook.com/"

# Opening first url
driver.get(url)

# Open a new window
#driver.execute_script("window.open('')")
driver.execute_script("window.open('https://www.facebook.com/','new window')")

# Switch to the new window and open new URL
handle=driver.window_handles[1]
driver.switch_to.window(handle)
print(driver.current_url)
handle2=driver.window_handles[0]
driver.switch_to.window(handle2)
print(driver.current_url)