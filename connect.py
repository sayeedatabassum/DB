import mysql.connector as mariadb
con = mariadb.connect(host = 'localhost',user = 'user1',password ='abc@123',database = 'Employee')
print("Connection is Established!")
con.close()