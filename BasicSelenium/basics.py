


import win32serviceutil


kk=10
re={"name":"krn","initial":"v"}
print(type(kk))
print(isinstance(kk,int))
print(re)
print(5**2)#5 square of 2
import random
print(random.randrange(50,100))
print(random.choice("kk m t 32 23"))
print(5/2)
print(5//2)#for decimal value remove pani thanthudum
print(round(10.464,2))
mm="kljkjs"\
    "hsbaavsm"\
    "872812"

bb="\nkljkjs"\
    "\nhsbaavsm"\
    "\n872812"

cc="""
sdkjsd
dsjhsdsdhj
dskksd'kk'
"""
dd='''
jkdshjhdks"kk" 
hjdshds
1221
2121

'''


print(mm)
print(bb)
print(cc)
print(dd)
f=open("D:\check\jj.txt","w")
f.write(dd)
f.flush()

import os

#os.startfile("D:\check\servicestart.bat - Shortcut.lnk")

kk1='sjhksah \'sjkasjk\''

print(kk1)

ff='karune'

print(len(ff))
print(ff[0:5])#index first value zero la irundu start aagum but second iruku la athu 1 to 5 tan
print(ff[::])
print(ff[::2])
print(ff[0:6:4])
print(ff[::-1])#string reverse
ll=" karun "
print(ll)
print(ll.strip())
qq="123,345,455"
print(qq[0])
qq1=qq.split(",")
print(qq1)
s="this"
print(s.find("s"))#entha index la s word iruku nu solum
yy="karun"*4 #for repeatation
print(yy)
name="karun)"
place="chennai"
print(f"My name is {name},I lived in {place}")
print("My name is {},I lived in {}".format(name,place))
print("My name is %s,I lived in %s"%(name,place))
print("My name is",name+",I lived in",place)
print("My name is "+name+",I lived in "+place)
a=b=c=10
print(a,b,c)
a1="a"
print(ord(a1)) # ord method vechu ASCII valueget panikalam
b1="b"
print(ord(b1))
print(a1<b1)# character la compare pana character oda ASCII value vechu compare panum
print(')' in name)
v=')' in name
for i in "karun": # for loop ula ethume kudukalana error adikum so dummy uh null pass panuvom
    pass

w=('kk','jj')#tuple
w1=['k','kk']#list
w2={'k','k2'}#set
w3={"kk":"karun"}#dictionary
print(type(w))
print(type(w1))
print(type(w2))
print(type(w3))

def kk(age=28):# ethu tan default argument
    print("My present age is",age)

kk()

from selenium import webdriver
def kkk(*bp):
    # driver = webdriver.Chrome(executable_path="../chromedriver.exe")
    # driver.get(bp)
    print(bp)
kkk("http://192.168.0.199:9091/QuaLISWeb/#/login","http://192.168.0.199:9091/QuaLISWeb/#/login")


from OOPS import kk

a=kk()
a.k1("mon")
a.k2()



