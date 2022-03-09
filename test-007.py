import time

from  test_006 import kk
from selenium import webdriver
import threading

def b(orgid,usrnm,pswd,browserpath):
    browserdriver=webdriver.Chrome(executable_path=browserpath)
    x=kk(browserdriver)
    x.login("https://logilabelntesting.azurewebsites.net/",orgid,usrnm,pswd)
    x.xpathclick("(//*[text()='Orders'])[1]")
    time.sleep(100)





th1=threading.Thread(target=b,args=("agaramtech.onmicrosoft.com","arul","admin","E:\KRN Files\Python\Selenium\Youtube\Browser Driver\chromedriver.exe"))
th1.start()
th2=threading.Thread(target=b,args=("agaramtech.onmicrosoft.com","arul","admin","E:\KRN Files\Python\Selenium\Youtube\Browser Driver\chromedriver.exe"))
th2.start()


