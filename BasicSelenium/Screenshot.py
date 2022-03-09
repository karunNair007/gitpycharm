import pyscreenshot
from  selenium import webdriver
import  os
import wget
from zipfile import ZipFile
from datetime import datetime

scriptexecutiondateandtime=input("Enter the script execution date and time ")
sysname=os.getlogin()
alphabets=[chr(97+i).upper() for i in range(26)]
print(alphabets)
for j in range(len(alphabets)):
    driveformat = alphabets[j] + "://"
    print(driveformat)
    driveresult = os.path.exists(driveformat)
    if driveresult == True:
        print("The drives present in " + sysname + " system are " + driveformat)
        finalselecteddrive = driveformat


print(finalselecteddrive)
folderpath=finalselecteddrive+"Drivers"+'\\'
folderresult=os.path.isdir(folderpath)
if folderresult==True:
    print("Drivers folder already exist")

else:
    driversfoldercreation=os.path.join(finalselecteddrive,"Drivers")
    os.mkdir(driversfoldercreation)
    print("Drivers Folder is created")

zipfilepath=folderpath+"chromedriver_win32.zip"
zipfileresult=os.path.isfile(zipfilepath)
if zipfileresult==True:
    print("Driver zip file already exist")


else:
    wget.download("https://chromedriver.storage.googleapis.com/97.0.4692.71/chromedriver_win32.zip",folderpath)
    print("Driver zip file is downloaded in "+folderpath)                                                      



driverfilepath=folderpath+"\\chromedriver.exe"
driverfileresult=os.path.isfile(driverfilepath)
if driverfileresult==True:
    print("The driver file already extracted in "+folderpath)
else:
    syszippath=ZipFile(zipfilepath)
    syszippath.extractall(folderpath)
    print("Zip file is extracted in "+folderpath)

driver=webdriver.Chrome(executable_path=driverfilepath)
driver.maximize_window()
path="https://www.w3resource.com/python-exercises/python-basic-exercise-3.php"
driver.get(path)
a=1
while a>0:

    currentsysdateandtime=datetime.today()
    sysdateandtimeconversion=currentsysdateandtime.strftime('%m/%d/%Y %H:%M:%S')
    print("The Comparitive vales are "+scriptexecutiondateandtime+" and "+sysdateandtimeconversion)
    if scriptexecutiondateandtime==sysdateandtimeconversion:

        screenshotfolder=finalselecteddrive+"Screenshots"
        screenshotfolderresult=os.path.isdir(screenshotfolder)
        if screenshotfolderresult==True:
            print("The screenshot folder already present")
        else:
            screenshotfoldercreation=os.path.join(finalselecteddrive,"Screenshots")
            os.mkdir(screenshotfoldercreation)
            print("The screenshot folder is created in "+finalselecteddrive)

        screenshotfilepath=screenshotfolder+"\\test.png"
        print(screenshotfilepath)
        pyscreenshot.grab().save(screenshotfilepath)
        print("Screen shot is taken ")
        break


