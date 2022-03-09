import time

import pyscreenshot
from selenium import webdriver
import os
import wget
from zipfile import ZipFile

from datetime import datetime

userdefineddatetime=input("Type date time you want to execute the scripts ")
alphabets=[chr(97+i).upper() for i in range(26)]
print(alphabets)
sysname=os.getlogin()
for j in range(len(alphabets)):
    driveformat=alphabets[j]+":/"
    print(driveformat)
    driveresult=os.path.exists(driveformat)
    if driveresult==True:
        print("The Local drives present in "+sysname+"  system is "+driveformat)
        selecteddrive=driveformat


print("The final selected drive is "+selecteddrive)


folderpath=selecteddrive+"Drivers"
print(folderpath)
folderresult=os.path.isdir(folderpath)
if folderresult==True:
    print("The Drivers folder already exist")
else:
    mkdir=os.path.join(selecteddrive,"Drivers")
    os.mkdir(mkdir)
    print("The Drivers folder is created")
downloadurl="https://chromedriver.storage.googleapis.com/97.0.4692.71/chromedriver_win32.zip"
filepath=folderpath+"/chromedriver.exe"
fileresult=os.path.isfile(filepath)
if fileresult==True:
    print("chrome driver already exist")
else:
    wget.download(downloadurl,folderpath)
    print("driver file downloaded in the drivers folder")
zippath=folderpath+"/chromedriver_win32.zip"
zip=ZipFile(zippath)
zip.extractall(folderpath)
driver=webdriver.Chrome(executable_path=filepath)
driver.maximize_window()
driver.implicitly_wait(5)
url="https://www.facebook.com/"

screeshotfilename="E:\ScreenShots\\ test.png"
pyscreenshot.grab().save(screeshotfilename)
driver.get(url)
currenturl=driver.current_url
pagesourcecode=driver.page_source
title=driver.title
print(currenturl)
print(pagesourcecode)
print(title)
driver.find_element_by_xpath("//input[@type='text']").send_keys("karun@agaramtech.com")
driver.find_element_by_xpath("//input[@type='password']").send_keys("Krishna@007")
screenshotpath=selecteddrive+"/ScreenShots"
screenshotresult=os.path.isdir(screenshotpath)
if screenshotresult==True:
    print("screenshot folder already present")
else:
    screenshotmkdir=os.path.join(selecteddrive,"ScreenShots")
    os.mkdir(screenshotmkdir)


l=1
while l>0:
    currentdatetime = datetime.today()
    print(currentdatetime)
    conversiondatetime = currentdatetime.strftime("%m/%d/%Y %H:%M:%S")
    print(conversiondatetime)
    print(userdefineddatetime)
    if conversiondatetime == userdefineddatetime:
        driver.find_element_by_xpath("//button[@value='1']").click()
        break

txtfolderpath=selecteddrive+"/notepad"
txtresult=os.path.isdir(txtfolderpath)
if txtresult==True:
    print("Notepad folder already exist")
else:
    notepad=os.path.join(selecteddrive,"notepad")
    os.mkdir(notepad)
    print("Notepad folder is created")
txtpath=txtfolderpath+"/notes.txt"
txt1=open(txtpath,'a')
txt1.write("All set, Everything looks fine")
txt1.flush()
time.sleep(500)
