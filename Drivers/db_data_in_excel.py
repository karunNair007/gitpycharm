import pypyodbc
import openpyxl

databasecredentials="Driver={SQL Server};Server=192.168.0.199\SQLEXPRESS2019;Database=NIBSCNEW-01-02-2022;UID=sa;PWD=Krishna@007"
conn = pypyodbc.connect(databasecredentials)
print(conn)
cursor1 = conn.cursor()
updatescript="update manufacturercontactinfo set semail='xxxx1@agaramtech.com'"
script=cursor1.execute(updatescript)
selectscript="select * from client "
script2=cursor1.execute(selectscript)
excel_path="D:\check\Excel\kk.xlsx"

open_workbook=openpyxl.load_workbook(excel_path)
open_worksheet=open_workbook["Test Case"]
row=1
column=1


kk=[ i for i in script2]
print(kk)
kk_len=len(kk)
u=str(kk)
print(kk_len)
for j in range(kk_len):
    ll1 = kk[j]
    ll2 = str(ll1)
    print(ll2)
    ll = ll2.split(",")
    print(ll)
    for k in range(len(ll)):
        print(ll[k].strip())
        ll3=ll[k].strip()
        ll4=str(ll3)
        print("next begins")
        open_worksheet.cell(row, column).value=ll4
        column+=1
        v=')' in ll4
        if v==True:
            print(") is present")
            row+=1
            column=1
        open_workbook.save(excel_path)
        open_workbook.close()




