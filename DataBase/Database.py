import pypyodbc

databasecredentials="Driver={SQL Server};Server=192.168.0.199\SQLEXPRESS2019;Database=ctlims-sat;UID=sa;PWD=Krishna@007"
conn = pypyodbc.connect(databasecredentials)
print(conn)
cursor1 = conn.cursor()
updatescript="update manufacturercontactinfo set semail='xxxx1@agaramtech.com'"
script=cursor1.execute(updatescript)
selectscript="select * from manufacturercontactinfo "
script2=cursor1.execute(selectscript)

kk=[ i for i in script2]
print(kk)
