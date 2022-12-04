import mysql.connector as mariadb
con=mariadb.connect(host='localhost',user='user1',password='abc@123',database='Employee')
print("Connection Established Successfully!")
cur=con.cursor()
cur.execute("delete from Department where dname = 'Sales'")
print("Number of rows deleted".cur.rowcount)
print("Data deleted Successfully!")
cur.close()
con.commit()
con.close()






