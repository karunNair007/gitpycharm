import pypyodbc

databasecredentials="Driver={SQL Server};Server=192.168.0.199\SQLEXPRESS2019;Database=ctlims-sat;UID=sa;PWD=Krishna@007"
conn = pypyodbc.connect(databasecredentials)
print(conn)
cursor1 = conn.cursor()
selectscript="select sfirstname,slastname from users where sloginid='cdolman' "
script2=cursor1.execute(selectscript)

for i in script2:
    print(i)
    kk=[j for j in i]

un=kk[0]+" "+kk[1]
print("User name is",un)
