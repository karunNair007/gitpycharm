import os
from zipfile import ZipFile


kk=os.getlogin()
print(kk)
path="C:\\Users\\"+kk+"\\Downloads\\IEDriverServer_x64_4.0.0.zip"
print(path)
zip = ZipFile(path)
zip.extractall("E:\\Drivers")
