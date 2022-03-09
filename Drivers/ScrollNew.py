from datetime import datetime
from selenium import webdriver
from selenium.webdriver import Keys

driver=webdriver.Chrome(executable_path="../chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(15)
driver.get("http://192.168.0.199:9091/QuaLISWeb/#/login")
driver.find_element_by_xpath("//*[@name='sloginid']").send_keys("cdolman")
driver.find_element_by_xpath("//*[@name='spassword']").send_keys("123")
driver.find_element_by_xpath("//*[text()='Login']").click()
driver.find_element_by_xpath("//*[text()='Registration']").click()
driver.find_element_by_xpath("(//*[text()='Sample Registration'])[1]").click()
driver.find_element_by_xpath("(//*[name()='svg']//*[name()='path' and @d='M572.52 241.4C518.29 135.59 410.93 64 288 64S57.68 135.64 3.48 241.41a32.35 32.35 0 0 0 0 29.19C57.71 376.41 165.07 448 288 448s230.32-71.64 284.52-177.41a32.35 32.35 0 0 0 0-29.19zM288 400a144 144 0 1 1 144-144 143.93 143.93 0 0 1-144 144zm0-240a95.31 95.31 0 0 0-25.31 3.79 47.85 47.85 0 0 1-66.9 66.9A95.78 95.78 0 1 0 288 160z'])[1]").click()

scroll=driver.find_element_by_xpath("(//*[name()='svg']//*[name()='path' and @d='M416 208H272V64c0-17.67-14.33-32-32-32h-32c-17.67 0-32 14.33-32 32v144H32c-17.67 0-32 14.33-32 32v32c0 17.67 14.33 32 32 32h144v144c0 17.67 14.33 32 32 32h32c17.67 0 32-14.33 32-32V304h144c17.67 0 32-14.33 32-32v-32c0-17.67-14.33-32-32-32z'])[3]")
#scroll.location_once_scrolled_into_view
driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
driver.execute_script("arguments[0].scrollIntoView()",scroll)
scroll.click()