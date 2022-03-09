import os

kk=[chr(97+i).upper() for i in range(26)]
print(kk)
for l in range(len(kk)):
    j = kk[l]+":\\"
    print(j)
    res=os.path.exists(j)
    #print(res)
    if res==True:
        print("The Local Disk Drives are"+" "+j)
        kkk=j

print("The final selected drive is:"+" "+kkk)
#format = os.path.join(kkk, "Drivers")
#os.mkdir(format)