import os
import time

import wget
from zipfile import ZipFile
from selenium import webdriver

alphabets=[chr(97+i).upper() for i in range(26)]
print(alphabets)
for j in range(len(alphabets)):
    driveformat=alphabets[j]+":\\"
    print(driveformat)
    driveresult=os.path.exists(driveformat)
    if driveresult==True:
        sysname=os.getlogin()
        print("The Drive present in"+" "+ sysname+" "+"system is"+" "+driveformat)
        finaldrive=driveformat
print("The final selected drive is"+" "+finaldrive)
folderpath=finaldrive+"Drivers"+"\\"
print(folderpath)
resultoffolder=os.path.isdir(folderpath)
if resultoffolder==True:
    print("The Drivers folder already exist in"+" "+finaldrive)
else:
    createdfolder=os.path.join(finaldrive,"Drivers")
    os.mkdir(createdfolder)
    print("Created folder is"+" "+createdfolder)

filepath=folderpath+"chromedriver.exe"
print(filepath)
fileresult=os.path.isfile(filepath)
if fileresult==True:
    print("Drivers file already exist")
else:
    wget.download("https://chromedriver.storage.googleapis.com/97.0.4692.71/chromedriver_win32.zip", folderpath)

zippath=folderpath+"chromedriver_win32.zip"
zip=ZipFile(zippath)
zip.extractall(folderpath)

driver=webdriver.Chrome(executable_path=filepath)
driver.maximize_window()
driver.get("https://fitgirl-repacks.site/")
time.sleep(4)
driver.execute_script("window.open('https://www.skidrowreloaded.com/','new window')")
#driver.get("https://www.skidrowreloaded.com/")
time.sleep(500)