import time
from configparser import ConfigParser

from selenium import webdriver
class Global():
    # init nale constructor tan
    def __init__(self, browser):
        self.browser=browser
        if self.browser=="chrome":
            self.kk=webdriver.Chrome(executable_path="E:\KRN Files\Python\Selenium\Youtube\Browser Driver\chromedriver.exe")
            self.kk.maximize_window()

        elif self.browser=="firefox":
            self.kk=webdriver.Firefox(executable_path="E:\KRN Files\Python\Selenium\Youtube\Browser Driver\geckodriver.exe")


    def clickxpath(self,loc1):

        self.kk.implicitly_wait(20)
        self.kk.find_element_by_xpath(loc1).click()

    def sendxpath(self,loc2,send):
        self.kk.implicitly_wait(20)
        self.kk.find_element_by_xpath(loc2).send_keys(send)

    def login(self):
        config=ConfigParser()
        config.read("C:\\Users\\Karun\\PycharmProjects\\Sel;enium with Python\\Drivers\\configuration.ini")
        UN=config.get("login credentials","un")
        PWD=config.get("login credentials","pswd")
        LINK=config.get("login credentials","link")
        UNXPATH = config.get("locator", "unxpath")
        PWDXPATH = config.get("locator", "pswdxpath")
        LOGINXPATH = config.get("locator", "loginxpath")
        self.kk.get(LINK)
        time.sleep(4)
        self.sendxpath(UNXPATH,UN)
        self.sendxpath(PWDXPATH, PWD)
        time.sleep(4)
        self.clickxpath(LOGINXPATH)
        time.sleep(8)

    def get(self,link):
        self.kk.implicitly_wait(20)
        self.kk.get(link)

    def getattribute(self,tag,attribute):
        self.kk.implicitly_wait(20)
        t=self.kk.find_elements_by_tag_name(tag)
        print("kk",t)
        # print(t.get_attribute(attribute))
        for i in t:
            print(i.get_attribute(attribute))
            print(i.text)

    def global_screen_open(self,menuloc,screenloc):
        self.kk.implicitly_wait(20)
        time.sleep(5)
        self.clickxpath(menuloc)
        self.clickxpath(screenloc)

    def scrolled_dowm(self, scrollloc):
        self.kk.implicitly_wait(20)
        org = self.kk.find_element_by_xpath(scrollloc)
        var = org.location_once_scrolled_into_view
        time.sleep(3)
        org.click()
        print(var)











