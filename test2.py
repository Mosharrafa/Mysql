import mysql.connector as conn

mydb = conn.connect(host = "localhost" , user = "root", passwd = "HDj3xJJLwH678jCz")
print(mydb)

cursor = mydb.cursor()
s = "insert into italy.city4 values(101 , 'David d' , 'david@hotmail.ca' , 1000 , 30 )"

cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)

mydb.commit()

cursor.execute("select * from italy.city4")
for i in cursor.fetchall():
    print(i)