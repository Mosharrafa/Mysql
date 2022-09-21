import mysql.connector as conn

mydb = conn.connect(host = "localhost" , user = "root", passwd = "HDj3xJJLwH678jCz")
print(mydb)

cursor = mydb.cursor()
#cursor.execute("create database Italy")

#cursor.execute("show databases")
#s= "create table italy.city4(employee_id int(10) , emp_name varchar(8) , emp_mailid varchar(20) , emp_salary int(6) , emp_attendence int(9))"

#q1 = cursor.execute(s)

q2 = cursor.execute("select * from italy.city4")

print(q2)

#print()

#print(cursor.fetchall())
