# DB

To be known Knowledge of unix scripting and knowledge of RDBMS

1> Connect to the MariaDB Database

2> Insert data to the MariaDB

3> Fetch the data from the MariaDB database

4> Update data in the MariaDB Database

5> Delete data from the MariaDB Database

creating connect.py to establish the connection, 
insert.py to insert data into the table,
fetchdetails.py to fetch the data from table,
update.py to update the data to the table.

1>open the terminal

>>cd Desktop
>>Desktop>ls -ld pythonscripts
shows that python script date and time
>>Desktop> mkdir pythonscripts
>>Desktop>cd pythonscripts
>>Desktop/pythonscripts>mysql -u user1 -p
>>password:abc@123
>>show databases;
>>exit
>>
>>vi connect.py
>>press i


>>import mysql.connector as mariadb
>>con = mariadb.connect(host = 'localhost',user = 'user1',password = 'abc@123',database = 'Employee')
>>print("Connection is Established!")
>>con.close()
:wq = saves data

>>vi connect.py
>>python3 connect.py
Connection Establised Successfully!

Insert

>>use Employee;
>>show tables;
>>DESC Employee;
>>exit
>>>>vi connect.py
>>press i
>>
import mysql.connector as mariadb
con=mariadb.connect(host='localhost',user='user1',password='abc@123',database='Employee')
print("Connection Established Successfully!")
cur=con.cursor()
cur.execute("insert into Employee values(1007,'Rita','Developer',1001,'2021-90-30',50000,20)")
print("Data Added Successfully!")
cur.close()
con.commit()
con.close()




