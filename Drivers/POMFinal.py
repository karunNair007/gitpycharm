import threading
import time

from selenium import webdriver
from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable
from selenium.webdriver.support.wait import WebDriverWait
from Drivers.POMDependencies  import xpathclick


def a(Driverpath,Link,USR1,PSWD1):
    driver = webdriver.Chrome(executable_path=Driverpath)
    driver.maximize_window()
    driver.get(Link)
    x=xpathclick(driver)
    x.sendxpath("//input[@id='sloginid']",USR1)
    x.sendxpath("//input[@id='spassword']", PSWD1)
    x.clickxpath("//button[text()='Login']")
    x.clickxpath("(//img[@alt='sidebar'])[2]")
    x.clickxpath("//*[text()='Registration']")
    x.clickxpath("//*[@nformcode='43']")
    x.clickxpath("(//*[@class='btn btn-primary'])[1]")
    scroll = driver.find_element_by_xpath("//*[@name='add__file']")
    scrollcheck = scroll.location_once_scrolled_into_view
    print(scrollcheck)
    x.clickxpath("//*[@name='add__file']")
    radio = driver.find_element_by_xpath("//*[@id='AddFiles']")
    radioresult = radio.is_selected()
    print(radioresult)
    x.clickxpath("//*[@id='AddFiles']")
    x.sendxpath("//*[@class='dropzone']//*[@autocomplete='off']", "D:\Spirint 8 bugs.xls")
    x.sendxpath("//*[@id='sdescription']", "kk")
    x.clickxpath("//*[name()='svg']//*[name()='path' and @d='M433.941 129.941l-83.882-83.882A48 48 0 0 0 316.118 32H48C21.49 32 0 53.49 0 80v352c0 26.51 21.49 48 48 48h352c26.51 0 48-21.49 48-48V163.882a48 48 0 0 0-14.059-33.941zM272 80v80H144V80h128zm122 352H54a6 6 0 0 1-6-6V86a6 6 0 0 1 6-6h42v104c0 13.255 10.745 24 24 24h176c13.255 0 24-10.745 24-24V83.882l78.243 78.243a6 6 0 0 1 1.757 4.243V426a6 6 0 0 1-6 6zM224 232c-48.523 0-88 39.477-88 88s39.477 88 88 88 88-39.477 88-88-39.477-88-88-88zm0 128c-22.056 0-40-17.944-40-40s17.944-40 40-40 40 17.944 40 40-17.944 40-40 40z']")
    time.sleep(500)




k1=threading.Thread(target=a,args=("E:\KRN Files\Python\Selenium\Youtube\Browser Driver\chromedriver.exe","http://192.168.0.199:9091/QuaLISWeb/#/login","cdolman","123"))
k2=threading.Thread(target=a,args=("E:\KRN Files\Python\Selenium\Youtube\Browser Driver\chromedriver.exe","http://192.168.0.199:9091/QuaLISWeb/#/login","cdolman","123"))
k3=threading.Thread(target=a,args=("E:\KRN Files\Python\Selenium\Youtube\Browser Driver\chromedriver.exe","http://192.168.0.199:9091/QuaLISWeb/#/login","cdolman","123"))
k4=threading.Thread(target=a,args=("E:\KRN Files\Python\Selenium\Youtube\Browser Driver\chromedriver.exe","http://192.168.0.199:9091/QuaLISWeb/#/login","cdolman","123"))
k1.start()
k2.start()
k3.start()
k4.start()