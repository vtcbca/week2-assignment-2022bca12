import sqlite3 as sqlite
con=sqlite.connect("c:\\sqlite3\\ems.db")
b="select * from emp_01 where basic>6000"
cur=con.cursor()
cur.execute(b)
r=cur.fetchall()
for i in range(len(r)):
    print("emp id:",(r[i][0]))
    print("emp name:",(r[i][1]))
    print("emp dept:",(r[i][2]))
    print("emp basic:",(r[i][3]))
    print("emp branch:",(r[i][4]))
con.commit()
con.close()
