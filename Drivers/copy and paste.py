import shutil
from shutil import copyfile

srcfilepath = "E:\\KRN Files\\Python\\Copy and Paste\\notes.txt"
targetpath="E:\KRN Files\Python\Copy and Paste\Test"


try:
    #shutil.copy(srcfilepath+"/notes.txt", targetpath)
    #print("File copied successfully.")
    shutil.move(srcfilepath,targetpath)




except PermissionError:
    print("Permission denied.")

