from datetime import datetime
from selenium import webdriver

executiondateandtime=input("The Enter the script execution date and time ")
a=1
while a>0:
    currentdateandtime = datetime.today()
    conversionofcurrentdateandtime = currentdateandtime.strftime('%m/%d/%Y %H:%M:%S')
    print(executiondateandtime)
    print(conversionofcurrentdateandtime)
    if executiondateandtime==conversionofcurrentdateandtime:
        driver=webdriver.Chrome(executable_path="E:\Drivers\chromedriver.exe")
        driver.maximize_window()
        driver.get("https://www.w3resource.com/python-exercises/python-basic-exercise-3.php")
        driver.execute_script("window.open('https://www.w3resource.com/python-exercises/python-basic-exercise-3.php','new window')")
        break


