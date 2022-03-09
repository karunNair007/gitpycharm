import threading
import time
from datetime import datetime

from selenium import webdriver

#from samplefunction import click1,scroll,sendkeys,radiobutton,get

from samplefunction import kk
from samplefunction import d


#ourinput = input("Enter the date: ")


def a(driver,link,lock,USR):
    d(driver,link)
    kk(link, lock, USR)










k1 = threading.Thread(target=a,args=("webdriver.Chrome(executable_path='E:\KRN Files\Python\Selenium\Youtube\Browser Driver\chromedriver.exe')","http://192.168.0.199:9091/QuaLISWeb/#/login","//input[@id='sloginid']","cdolman"))
k1.start()
k2 = threading.Thread(target=a,args=("webdriver.Chrome(executable_path='E:\KRN Files\Python\Selenium\Youtube\Browser Driver\chromedriver.exe')","http://192.168.0.199:9091/QuaLISWeb/#/login","//input[@id='sloginid']","cdolman"))
k2.start()



