import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import _thread

from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="E:\KRN Files\Python\Selenium\Youtube\Browser Driver\chromedriver.exe")
driver1 = webdriver.Chrome(executable_path="E:\KRN Files\Python\Selenium\Youtube\Browser Driver\chromedriver.exe")
driver3 = webdriver.Chrome(executable_path="E:\KRN Files\Python\Selenium\Youtube\Browser Driver\chromedriver.exe")

def a(link1,USR1,PSWD1):
    driver.maximize_window()
    driver.implicitly_wait(2)
    driver.get(link1)
    driver.find_element_by_xpath("//input[@id='sloginid']").send_keys(USR1)
    driver.find_element_by_xpath("//input[@id='spassword']").send_keys(PSWD1)
    driver.find_element_by_xpath("//button[text()='Login']").click()
    driver.find_element_by_xpath("(//img[@alt='sidebar'])[2]").click()
    driver.find_element_by_xpath("//*[text()='Registration']").click()
    driver.find_element_by_xpath("//*[@nformcode='43']").click()
    driver.find_element_by_xpath("(//*[@class='btn btn-primary'])[1]").click()
    scroll = driver.find_element_by_xpath("//*[@name='add__file']")
    scrollcheck = scroll.location_once_scrolled_into_view
    print(scrollcheck)
    driver.find_element_by_xpath("//*[@name='add__file']").click()
    radio = driver.find_element_by_xpath("//*[@id='AddFiles']")
    radioresult = radio.is_selected()
    print(radioresult)
    WebDriverWait(driver,10).until(presence_of_element_located((By.XPATH,"//*[@id='AddFiles']")))
    radio.click()
    driver.find_element_by_xpath("//*[@class='dropzone']//*[@autocomplete='off']").send_keys("D:\Spirint 8 bugs.xls")
    driver.find_element_by_xpath("//*[@id='sdescription']").send_keys("kk")
    driver.find_element_by_xpath(
        "//*[name()='svg']//*[name()='path' and @d='M433.941 129.941l-83.882-83.882A48 48 0 0 0 316.118 32H48C21.49 32 0 53.49 0 80v352c0 26.51 21.49 48 48 48h352c26.51 0 48-21.49 48-48V163.882a48 48 0 0 0-14.059-33.941zM272 80v80H144V80h128zm122 352H54a6 6 0 0 1-6-6V86a6 6 0 0 1 6-6h42v104c0 13.255 10.745 24 24 24h176c13.255 0 24-10.745 24-24V83.882l78.243 78.243a6 6 0 0 1 1.757 4.243V426a6 6 0 0 1-6 6zM224 232c-48.523 0-88 39.477-88 88s39.477 88 88 88 88-39.477 88-88-39.477-88-88-88zm0 128c-22.056 0-40-17.944-40-40s17.944-40 40-40 40 17.944 40 40-17.944 40-40 40z']").click()


def b(link2,USR2,PSWD2):
    # driver.get("https://www.facebook.com/")

    driver1.maximize_window()
    driver1.implicitly_wait(2)
    driver1.get(link2)
    driver1.find_element_by_xpath("//input[@id='sloginid']").send_keys(USR2)
    driver1.find_element_by_xpath("//input[@id='spassword']").send_keys(PSWD2)
    driver1.find_element_by_xpath("//button[text()='Login']").click()
    driver1.find_element_by_xpath("(//img[@alt='sidebar'])[2]").click()
    driver1.find_element_by_xpath("//*[text()='Registration']").click()
    driver1.find_element_by_xpath("//*[@nformcode='43']").click()
    driver1.find_element_by_xpath("(//*[@class='btn btn-primary'])[1]").click()
    scroll = driver1.find_element_by_xpath("//*[@name='add__file']")
    scrollcheck = scroll.location_once_scrolled_into_view
    print(scrollcheck)
    driver1.find_element_by_xpath("//*[@name='add__file']").click()
    radio = driver1.find_element_by_xpath("//*[@id='AddFiles']")
    radioresult = radio.is_selected()
    print(radioresult)
    WebDriverWait(driver,10).until(presence_of_element_located((By.XPATH,"//*[@id='AddFiles']")))
    radio.click()
    driver1.find_element_by_xpath("//*[@class='dropzone']//*[@autocomplete='off']").send_keys("D:\Spirint 8 bugs.xls")
    driver1.find_element_by_xpath("//*[@id='sdescription']").send_keys("kk")
    driver1.find_element_by_xpath(
        "//*[name()='svg']//*[name()='path' and @d='M433.941 129.941l-83.882-83.882A48 48 0 0 0 316.118 32H48C21.49 32 0 53.49 0 80v352c0 26.51 21.49 48 48 48h352c26.51 0 48-21.49 48-48V163.882a48 48 0 0 0-14.059-33.941zM272 80v80H144V80h128zm122 352H54a6 6 0 0 1-6-6V86a6 6 0 0 1 6-6h42v104c0 13.255 10.745 24 24 24h176c13.255 0 24-10.745 24-24V83.882l78.243 78.243a6 6 0 0 1 1.757 4.243V426a6 6 0 0 1-6 6zM224 232c-48.523 0-88 39.477-88 88s39.477 88 88 88 88-39.477 88-88-39.477-88-88-88zm0 128c-22.056 0-40-17.944-40-40s17.944-40 40-40 40 17.944 40 40-17.944 40-40 40z']").click()

def c(link3,USR3,PSWD3):
    # driver.get("https://www.facebook.com/")

    driver3.maximize_window()
    driver3.implicitly_wait(2)
    driver3.get(link3)
    driver3.find_element_by_xpath("//input[@id='sloginid']").send_keys(USR3)
    driver3.find_element_by_xpath("//input[@id='spassword']").send_keys(PSWD3)
    driver3.find_element_by_xpath("//button[text()='Login']").click()
    driver3.find_element_by_xpath("(//img[@alt='sidebar'])[2]").click()
    driver3.find_element_by_xpath("//*[text()='Registration']").click()
    driver3.find_element_by_xpath("//*[@nformcode='43']").click()
    driver3.find_element_by_xpath("(//*[@class='btn btn-primary'])[1]").click()
    scroll = driver3.find_element_by_xpath("//*[@name='add__file']")
    scrollcheck = scroll.location_once_scrolled_into_view
    print(scrollcheck)
    driver3.find_element_by_xpath("//*[@name='add__file']").click()
    radio = driver3.find_element_by_xpath("//*[@id='AddFiles']")
    radioresult = radio.is_selected()
    print(radioresult)
    WebDriverWait(driver,10).until(presence_of_element_located((By.XPATH,"//*[@id='AddFiles']")))
    radio.click()
    driver3.find_element_by_xpath("//*[@class='dropzone']//*[@autocomplete='off']").send_keys("D:\Spirint 8 bugs.xls")
    driver3.find_element_by_xpath("//*[@id='sdescription']").send_keys("kk")
    driver3.find_element_by_xpath(
        "//*[name()='svg']//*[name()='path' and @d='M433.941 129.941l-83.882-83.882A48 48 0 0 0 316.118 32H48C21.49 32 0 53.49 0 80v352c0 26.51 21.49 48 48 48h352c26.51 0 48-21.49 48-48V163.882a48 48 0 0 0-14.059-33.941zM272 80v80H144V80h128zm122 352H54a6 6 0 0 1-6-6V86a6 6 0 0 1 6-6h42v104c0 13.255 10.745 24 24 24h176c13.255 0 24-10.745 24-24V83.882l78.243 78.243a6 6 0 0 1 1.757 4.243V426a6 6 0 0 1-6 6zM224 232c-48.523 0-88 39.477-88 88s39.477 88 88 88 88-39.477 88-88-39.477-88-88-88zm0 128c-22.056 0-40-17.944-40-40s17.944-40 40-40 40 17.944 40 40-17.944 40-40 40z']").click()

try:
    _thread.start_new_thread(a, ("http://192.168.0.199:9091/QuaLISWeb/#/login","admin1","Admin@123"))
    _thread.start_new_thread(b, ("http://192.168.0.199:9091/QuaLISWeb/#/login","cdolman","Admin@123"))
    _thread.start_new_thread(c, ("http://192.168.0.199:9091/QuaLISWeb/#/login", "admin1", "Admin@123"))
except:
    print("Error")

#while True:pass

