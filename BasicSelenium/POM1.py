import time
from configparser import ConfigParser
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
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
        WebDriverWait(self.kk,20).until(EC.element_to_be_clickable((By.XPATH,loc1)))
        self.kk.find_element_by_xpath(loc1).click()

    def sendxpath(self,loc2,send):
        self.kk.implicitly_wait(20)
        WebDriverWait(self.kk, 20).until(EC.element_to_be_clickable((By.XPATH, loc2)))
        self.kk.find_element_by_xpath(loc2).send_keys(send)

    def login(self,datasection,link,undatakey,pswddatakey,locsection,unloc,pswdloc,loginloc):
        config=ConfigParser()
        config.read("C:\\Users\\Karun\\PycharmProjects\\Sel;enium with Python\\Drivers\\configuration.ini")
        UN=config.get(datasection,undatakey)
        PWD=config.get(datasection,pswddatakey)
        LINK=config.get(datasection,link)
        UNXPATH = config.get(locsection, unloc)
        PWDXPATH = config.get(locsection, pswdloc)
        LOGINXPATH = config.get(locsection, loginloc)
        self.kk.get(LINK)
        time.sleep(4)
        self.sendxpath(UNXPATH,UN)
        self.sendxpath(PWDXPATH, PWD)
        time.sleep(4)
        self.clickxpath(LOGINXPATH)


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

    def open_screen(self,section,menukey,screenkey):
        self.kk.implicitly_wait(20)
        config=ConfigParser()
        config.read("E:\\KRN Files\\Python\\Pycharm files\\Configuration\\configuration.ini")
        menu = config.get(section, menukey)
        screen = config.get(section, screenkey)
        self.clickxpath(menu)
        self.clickxpath(screen)

    def scrolled_down_locate_element(self, scrollloc):
        self.kk.implicitly_wait(20)
        org = self.kk.find_element_by_xpath(scrollloc)
        var = org.location_once_scrolled_into_view
        org.click()
        print(var)

    def scroll_up(self,loc):
        time.sleep(3)
        self.clickxpath(loc)
        self.kk.find_element_by_tag_name('body').send_keys(Keys.HOME)
        #self.kk.execute_script("window.scroll(0, -300)")

    def config(self,key,section):
        config=ConfigParser()
        config.read("E:\\KRN Files\\Python\\Pycharm files\\Configuration\\configuration.ini")
        value=config.get(key,section)
        return value

    def config_click(self,key,section):

        value=self.config(key,section)
        self.clickxpath(value)











