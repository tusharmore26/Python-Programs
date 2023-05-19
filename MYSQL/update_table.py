import mysql.connector as cn

db=cn.connect(
    host='localhost',
    username='root',
    password='root'
)

mycursor=db.cursor()

mycursor.execute("USE newdb")

sql="UPDATE  new SET age=20 WHERE name='Yash'"
mycursor.execute(sql)

db.commit()

print(mycursor.rowcount,"row updated!!")




