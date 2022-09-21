import mysql.connector as conn

mydb = conn.connect(host = "localhost" , user = "root", passwd = "HDj3xJJLwH678jCz")
cursor = mydb.cursor()

cursor.execute("select employee_id , emp_mailid  from italy.city4")

l= []

for i in cursor.fetchall():
    l.append(i)

print(l)

print(type(l[0]))


