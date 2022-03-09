import time

from selenium import webdriver


driver=webdriver.Chrome(executable_path="E:\KRN Files\Python\Selenium\Youtube\Browser Driver\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://192.168.0.199:9091/QuaLISWeb/#/organisation")
driver.find_element_by_xpath("//input[@id='sloginid']").send_keys("cdolman")
driver.find_element_by_xpath("//input[@id='spassword']").send_keys("Admin@123")
driver.find_element_by_xpath("//button[text()='Login']").click()
driver.find_element_by_xpath("(//img[@alt='sidebar'])[2]").click()
driver.find_element_by_xpath("//*[text()='Registration']").click()
driver.find_element_by_xpath("//*[@nformcode='43']").click()
driver.find_element_by_xpath("(//*[@class='btn btn-primary'])[1]").click()
scroll=driver.find_element_by_xpath("//*[@name='add__file']")
scrollcheck=scroll.location_once_scrolled_into_view
print(scrollcheck)
driver.find_element_by_xpath("//*[@name='add__file']").click()
radio=driver.find_element_by_xpath("//*[@id='AddFiles']")
radioresult=radio.is_selected()
print(radioresult)
radio.click()
driver.find_element_by_xpath("//*[@class='dropzone']//*[@autocomplete='off']").send_keys("D:\Spirint 8 bugs.xls")
driver.find_element_by_xpath("//*[@id='sdescription']").send_keys("kk")
driver.find_element_by_xpath("//*[name()='svg']//*[name()='path' and @d='M433.941 129.941l-83.882-83.882A48 48 0 0 0 316.118 32H48C21.49 32 0 53.49 0 80v352c0 26.51 21.49 48 48 48h352c26.51 0 48-21.49 48-48V163.882a48 48 0 0 0-14.059-33.941zM272 80v80H144V80h128zm122 352H54a6 6 0 0 1-6-6V86a6 6 0 0 1 6-6h42v104c0 13.255 10.745 24 24 24h176c13.255 0 24-10.745 24-24V83.882l78.243 78.243a6 6 0 0 1 1.757 4.243V426a6 6 0 0 1-6 6zM224 232c-48.523 0-88 39.477-88 88s39.477 88 88 88 88-39.477 88-88-39.477-88-88-88zm0 128c-22.056 0-40-17.944-40-40s17.944-40 40-40 40 17.944 40 40-17.944 40-40 40z']").click()

