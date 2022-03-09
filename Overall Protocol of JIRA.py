import os
import sys

import wget
from zipfile import ZipFile
import time
from selenium import webdriver

GettingAlphabets = [chr(97 + i).upper() for i in range(26)]
print(GettingAlphabets)
for j in range(len(GettingAlphabets)):
    driveformat = GettingAlphabets[j] + ":\\"
    print(driveformat)
    result = os.path.exists(driveformat)
    # print(result)
    if result == True:
        print("The Local Disk Drives are" + " " + driveformat)
        kkl = driveformat

print("the final selected drive are" + " " + kkl)
foldercheck = kkl + "Drivers" + "\\"
print(foldercheck)
result1 = os.path.isdir(foldercheck)
if result1 == True:
    print("Drivers folder present in" + " " + kkl)
else:
    format = os.path.join(kkl, "Drivers")
    os.mkdir(format)
filecheck = foldercheck + "chromedriver_win32.zip"
print(filecheck)
result2 = os.path.isfile(filecheck)
print(result2)
if result2 == True:
    print("Driver file is already exist" + " " + filecheck)

else:
    print("Downloading Path is" + " " + foldercheck)
    downloadurl = "https://chromedriver.storage.googleapis.com/97.0.4692.71/chromedriver_win32.zip"
    wget.download(downloadurl, foldercheck)

filecheck1 = foldercheck + "chromedriver.exe"
result3 = os.path.isfile(filecheck1)
if result3 == True:
    print("File is already Extracted")
else:
    zip = ZipFile(filecheck)
    zip.extractall(foldercheck)

driver = webdriver.Chrome(executable_path=filecheck1)
driver.maximize_window()
driver.get("http://10.10.10.4:8889/login.jsp")
driver.find_element_by_xpath("(//input[@class='text medium-field'])[1]").send_keys("ate145")
driver.find_element_by_xpath("(//input[@class='text medium-field'])[2]").send_keys("Krishna@007")
driver.find_element_by_xpath("//input[@value='Log In']").click()
time.sleep(3)
driver.find_element_by_xpath("//a[@id='greenhopper_menu']").click()
time.sleep(500)
