
filepath='E:\Files\kk.txt'
open(filepath,'w')
lst=['1','2','3']
filewrite=open(filepath,'a').writelines(lst)
fileread=open(filepath,'r').readline()
print(fileread)