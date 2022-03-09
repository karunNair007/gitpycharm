import time

from selenium import webdriver
import os
import wget
from zipfile import ZipFile
import pyscreenshot
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from datetime import datetime
import threading
ourinput=input("Enter the date: ")
sysname=os.getlogin()
print(sysname)
alphabets=[chr(97+i).upper() for i in range(26)]
print(alphabets)
for j in range(len(alphabets)):
    driveformat=alphabets[j]+":/"
    print(driveformat)
    driveresult=os.path.exists(driveformat)
    if driveresult==True:
        print("The Driver present in "+sysname+" system is "+driveformat)
        selecteddrive=driveformat

print("The selected drive is " + selecteddrive)
folderpath=selecteddrive+"Drivers/"
folderresult=os.path.isdir(folderpath)
if folderresult==True:
    print("Drivers folder already exist")
else:
    foldercreation=os.path.join(selecteddrive,"Drivers")
    os.mkdir(foldercreation)
    print("Drivers folder is created")
filepath=folderpath+"chromedriver.exe"
fileresult=os.path.isfile(filepath)
if fileresult==True:
    print("Drivers exe already exist")
else:
    downloadurl = "https://chromedriver.storage.googleapis.com/97.0.4692.71/chromedriver_win32.zip"
    wget.download(downloadurl, folderpath)
    print("Drivers zip is downloaded in " + folderpath)
    zippath = folderpath + "chromedriver_win32.zip"
    zipformat=ZipFile(zippath)
    zipformat.extractall(folderpath)
    print("The Zip file is extracted in "+folderpath)


def a(driverpath,usrname,pswd):
    driver = webdriver.Chrome(executable_path=driverpath)
    driver.maximize_window()
    driver.implicitly_wait(4)
    driver.get("http://192.168.0.199:9091/QuaLISWeb/#/login")
    driver.find_element_by_xpath("//*[@id='sloginid']").send_keys(usrname)
    driver.find_element_by_xpath("//*[@id='spassword']").send_keys(pswd)
    driver.find_element_by_xpath("//*[text()='Login']").click()
    screenshotfolder = selecteddrive + "ScreenShot/"
    screenshotresult = os.path.isdir(screenshotfolder)
    if screenshotresult == True:
        print("Screenshot folder already exit")
    else:
        screenshotfolderjoin = os.path.join(selecteddrive, "ScreenShot")
        os.mkdir(screenshotfolderjoin)
        print("Screenshot folder is created")
    screenshotfilepath = screenshotfolder + "kk.png"
    pyscreenshot.grab().save(screenshotfilepath)
    print("Screenshot captured successfully")
    registrationtopmodule = driver.find_element_by_xpath("//*[text()='Registration']")
    # WebDriverWait(driver,10).until(EC.presence_of_element_located(registrationtopmodule))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[text()='Registration']")))
    registrationtopmodule.click()
    driver.find_element_by_xpath("//*[text()='Sample Registration']").click()
    driver.find_element_by_xpath(
        "(//*[name()='svg']//*[name()='path' and @d='M572.52 241.4C518.29 135.59 410.93 64 288 64S57.68 135.64 3.48 241.41a32.35 32.35 0 0 0 0 29.19C57.71 376.41 165.07 448 288 448s230.32-71.64 284.52-177.41a32.35 32.35 0 0 0 0-29.19zM288 400a144 144 0 1 1 144-144 143.93 143.93 0 0 1-144 144zm0-240a95.31 95.31 0 0 0-25.31 3.79 47.85 47.85 0 0 1-66.9 66.9A95.78 95.78 0 1 0 288 160z'])[1]").click()
    scroll = driver.find_element_by_xpath(
        "(//*[name()='svg']//*[name()='path' and @d='M416 208H272V64c0-17.67-14.33-32-32-32h-32c-17.67 0-32 14.33-32 32v144H32c-17.67 0-32 14.33-32 32v32c0 17.67 14.33 32 32 32h144v144c0 17.67 14.33 32 32 32h32c17.67 0 32-14.33 32-32V304h144c17.67 0 32-14.33 32-32v-32c0-17.67-14.33-32-32-32z'])[3]")
    objectaxis = scroll.location_once_scrolled_into_view
    print(objectaxis)
    # driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    scroll.click()
    FTPresult = driver.find_element_by_xpath("//*[@id='AddFiles']").is_selected()
    print(FTPresult)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='AddFiles']")))
    driver.find_element_by_xpath("//*[@id='AddFiles']").click()
    time.sleep(4)
    driver.find_element_by_xpath("//*[@class='dropzone']//*[@autocomplete='off']").send_keys("D:\Spirint 8 bugs.xls")
    driver.find_element_by_xpath("//*[@id='sdescription']").send_keys("kk")

    h = 1
    while h > 0:
        currentdt = datetime.today()
        currentdt1 = currentdt.strftime("%m/%d/%Y %H:%M:%S")
        print(ourinput)
        print(currentdt1)
        if currentdt1 == ourinput:
            driver.find_element_by_xpath(
                "//*[name()='svg']//*[name()='path' and @d='M433.941 129.941l-83.882-83.882A48 48 0 0 0 316.118 32H48C21.49 32 0 53.49 0 80v352c0 26.51 21.49 48 48 48h352c26.51 0 48-21.49 48-48V163.882a48 48 0 0 0-14.059-33.941zM272 80v80H144V80h128zm122 352H54a6 6 0 0 1-6-6V86a6 6 0 0 1 6-6h42v104c0 13.255 10.745 24 24 24h176c13.255 0 24-10.745 24-24V83.882l78.243 78.243a6 6 0 0 1 1.757 4.243V426a6 6 0 0 1-6 6zM224 232c-48.523 0-88 39.477-88 88s39.477 88 88 88 88-39.477 88-88-39.477-88-88-88zm0 128c-22.056 0-40-17.944-40-40s17.944-40 40-40 40 17.944 40 40-17.944 40-40 40z']").click()
            break

    print("all done")

#k1=threading.Thread(target=a(filepath,"cdolman","Admin@123"))
#k2=threading.Thread(target=a(filepath,"cdolman","Admin@123"))
k1=threading.Thread(target=a,args=(filepath,"cdolman","Admin@123"))
k2=threading.Thread(target=a,args=(filepath,"cdolman","Admin@123"))
k1.start()
k2.start()

time.sleep(500)

